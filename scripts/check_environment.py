#!/usr/bin/env python3
"""Prompt 08 environment check only; no scoring, downloads or data modification.

Use Python 3.11 in citation_eval. JSON report goes to stdout. --output creates
a NEW report only (exclusive write); existing files are never overwritten.
An explicit --dataset is opened only in binary read mode. No path search occurs.
"""
import argparse
import hashlib
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import sys
import tempfile
from datetime import datetime, timezone

EXPECTED_SIZE = 17520509
EXPECTED_SHA256 = "51c66d4dcec9b6bc035d9a08e51d4a7b750615b6fc469be1d666e5d5693ebb05"
COMMIT = "2c6b485ae1c2bd296ad7d5e0eee4da4065535e57"
SOURCE = ("https://raw.githubusercontent.com/nelson-liu/"
          "evaluating-verifiability-in-generative-search-engines/" + COMMIT
          + "/human_evaluation_annotations.jsonl")
REQUIRED_IMPORTS = ("json", "hashlib", "pathlib", "platform", "sys", "csv",
                    "statistics", "argparse", "logging", "collections")


def read_text_if_possible(path):
    try:
        return Path(path).read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError):
        return None


def memory_info():
    result = {"source": "/proc/meminfo", "total_bytes": None,
              "available_bytes": None, "cgroup_memory_max": None}
    text = read_text_if_possible("/proc/meminfo")
    if text:
        for line in text.splitlines():
            if line.startswith(("MemTotal:", "MemAvailable:")):
                key = "total_bytes" if line.startswith("MemTotal:") else "available_bytes"
                result[key] = int(line.split()[1]) * 1024
    result["cgroup_memory_max"] = read_text_if_possible("/sys/fs/cgroup/memory.max")
    return result


def reject_nonfinite(value):
    raise ValueError("Non-standard JSON constant: " + value)


def inspect_dataset(supplied_path, acquisition_note):
    if supplied_path is None:
        return {"status": "NOT_CHECKED", "reason": "No explicit dataset path supplied"}
    path = Path(supplied_path).expanduser().resolve()
    result = {"status": "FAIL", "supplied_path": supplied_path,
              "resolved_path": str(path), "expected_size_bytes": EXPECTED_SIZE,
              "expected_sha256": EXPECTED_SHA256, "official_source_reference": SOURCE,
              "source_commit": COMMIT,
              "actual_acquisition_note": acquisition_note or "UNKNOWN",
              "dataset_license_scope": "UNRESOLVED LIC-01",
              "jsonl_status": "NOT_CHECKED"}
    try:
        if not path.is_file():
            result["error"] = "Dataset path does not exist or is not a regular file"
            return result
        digest = hashlib.sha256()
        lines = 0
        first_error = None
        # Hash and parse the SAME byte stream. Never open the dataset for writing.
        with path.open("rb") as stream:
            before = os.fstat(stream.fileno())
            for lines, raw_line in enumerate(stream, start=1):
                digest.update(raw_line)
                if first_error is not None:
                    continue  # Finish checksum without manufacturing further parse results.
                try:
                    text = raw_line.decode("utf-8")
                    if not text.strip():
                        raise ValueError("Blank JSONL line")
                    record = json.loads(text, parse_constant=reject_nonfinite)
                    if not isinstance(record, dict):
                        raise ValueError("Expected a JSON object on each archive line")
                except (ValueError, UnicodeError, RecursionError) as exc:
                    first_error = {"line": lines, "type": type(exc).__name__,
                                   "message": str(exc)}
            after = os.fstat(stream.fileno())
        current = path.stat()
        signature = lambda stat: (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns)
        stable = signature(before) == signature(after) == signature(current)
        result.update(size_bytes=after.st_size, sha256=digest.hexdigest(),
                      lines_read=lines, unchanged_during_read=stable,
                      size_matches=(after.st_size == EXPECTED_SIZE),
                      sha256_matches=(digest.hexdigest() == EXPECTED_SHA256))
        if lines == 0:
            first_error = {"line": 0, "type": "ValueError", "message": "Empty file"}
        result["jsonl_status"] = "PASS" if first_error is None else "FAIL"
        if first_error:
            result["jsonl_error"] = first_error
        if not stable:
            result["error"] = "File changed or was replaced while being read; stop"
        if not result["sha256_matches"]:
            result["integrity_action"] = "STOP: investigate provenance; do not accept or overwrite file"
        if stable and result["size_matches"] and result["sha256_matches"] and first_error is None:
            result["status"] = "PASS"
        result["scope"] = "Byte identity and JSON-object readability only; no methodological validation"
    except (OSError, ValueError) as exc:
        result["error"] = type(exc).__name__ + ": " + str(exc)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-dir", required=True, help="Existing project workspace")
    parser.add_argument("--dataset", help="Explicit path to an EXISTING archive; never downloaded")
    parser.add_argument("--dataset-provenance", help="How this local file was actually obtained")
    parser.add_argument("--output", help="NEW JSON report path; parent directory must exist")
    args = parser.parse_args()
    project = Path(args.project_dir).expanduser().resolve()
    dataset_path = Path(args.dataset).expanduser().resolve() if args.dataset else None
    output = Path(args.output).expanduser().resolve() if args.output else None
    if output is not None and (output.exists() or output == dataset_path):
        parser.error("Output exists or equals dataset path; choose a new report filename")
    checks = []

    def check(name, status, detail):
        checks.append({"name": name, "status": status, "detail": detail})

    check("python_target", "PASS" if sys.version_info[:2] == (3, 11) else "FAIL",
          {"required_series": "3.11", "actual": platform.python_version()})
    check("linux_platform", "PASS" if platform.system() == "Linux" else "FAIL",
          {"system": platform.system(), "wsl_evidence": "microsoft" in platform.release().lower(),
           "note": "Confirm distribution and WSL version using the manual diagnostics"})
    conda_name = os.environ.get("CONDA_DEFAULT_ENV")
    conda_prefix = os.environ.get("CONDA_PREFIX")
    prefix_matches = bool(conda_prefix) and Path(conda_prefix).resolve() == Path(sys.prefix).resolve()
    check("dedicated_conda_environment",
          "PASS" if conda_name == "citation_eval" and prefix_matches else "FAIL",
          {"CONDA_DEFAULT_ENV": conda_name, "CONDA_PREFIX": conda_prefix,
           "sys_prefix": sys.prefix, "prefix_matches": prefix_matches,
           "expected_environment": "citation_eval"})
    for name in REQUIRED_IMPORTS:
        try:
            importlib.import_module(name)
            check("import_" + name, "PASS", "Imported from this interpreter")
        except Exception as exc:
            check("import_" + name, "FAIL", type(exc).__name__ + ": " + str(exc))
    try:
        if not project.is_dir():
            raise NotADirectoryError("Project directory must already exist: " + str(project))
        # Only a unique temporary directory within the workspace is created/removed.
        with tempfile.TemporaryDirectory(prefix=".envcheck-", dir=project) as temporary:
            probe = Path(temporary) / "probe.txt"
            probe.write_text("environment-read-write-check\n", encoding="utf-8")
            if probe.read_text(encoding="utf-8") != "environment-read-write-check\n":
                raise OSError("Read-back mismatch")
        check("workspace_read_write", "PASS", str(project))
    except OSError as exc:
        check("workspace_read_write", "FAIL", type(exc).__name__ + ": " + str(exc))
    try:
        usage = shutil.disk_usage(project)
        disk = {"path": str(project), "total_bytes": usage.total,
                "used_bytes": usage.used, "free_bytes": usage.free}
    except OSError as exc:
        disk = {"status": "UNKNOWN", "error": str(exc)}
    optional = {}
    for name in ("pandas", "numpy", "matplotlib"):
        try:
            metadata = importlib.metadata.metadata(name)
            optional[name] = {"status": "INSTALLED_METADATA_ONLY",
                              "version": importlib.metadata.version(name),
                              "requires_python": metadata.get("Requires-Python"),
                              "import_tested": False}
        except importlib.metadata.PackageNotFoundError:
            optional[name] = {"status": "NOT_INSTALLED_OPTIONAL", "import_tested": False}
        except Exception as exc:
            optional[name] = {"status": "UNKNOWN", "error": str(exc), "import_tested": False}
    dataset = inspect_dataset(args.dataset, args.dataset_provenance)
    environment_ok = all(item["status"] != "FAIL" for item in checks)
    report = {
        "stage": "Prompt 08 environment check ONLY",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "environment_status": "PASS" if environment_ok else "FAIL",
        "interpreter": sys.executable, "python": sys.version,
        "platform": platform.platform(), "kernel": platform.release(),
        "os_release": read_text_if_possible("/etc/os-release"),
        "logical_cpus": os.cpu_count(), "memory": memory_info(), "disk": disk,
        "checks": checks, "optional_packages": optional, "dataset": dataset,
        "gpu_required": False, "baseline_status": "NOT IMPLEMENTED / NOT VALIDATED",
        "methodological_blockers": ["DEN-01", "DUP-01", "AGG-01"],
        "random_seed": "NOT APPLICABLE: deterministic inspection",
        "scope_note": "A PASS does not validate B0/B1, eligibility, license or reproduction."
    }
    failed = not environment_ok or dataset["status"] == "FAIL"
    report["exit_code"] = 1 if failed else 0
    if output is not None:
        try:
            with output.open("x", encoding="utf-8") as stream:
                json.dump(report, stream, indent=2, ensure_ascii=True)
                stream.write("\n")
        except OSError as exc:
            report["report_write_error"] = type(exc).__name__ + ": " + str(exc)
            report["exit_code"] = 1
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return report["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
