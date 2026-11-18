# Citation-support scoring sensitivity

A controlled reanalysis of fixed historical responses and human support annotations from Liu, Zhang and Liang (2023), *Evaluating Verifiability in Generative Search Engines*. This is the repository upload copy for an AI Tools for Research assignment.

## Research question and result

Primary: how does removing conditional collective partial-support credit affect between-system citation-precision gaps? Supporting questions concern per-system loss and ordering. C0 and C1 are explicitly adapted controls. Original Liu B0 was **not faithfully reproduced** because occurrence, repeated-annotation and aggregation conventions remain unresolved.

The common cohort contains 353 queries, 1412 responses and 4382 mapped units. C0-to-C1 losses are 0.826/2.111/3.753/1.220 percentage points for Bing Chat/Neeva/Perplexity/You. The largest absolute gap change is 2.927 points, with no pairwise ordering reversal or tie transition. Results are historical, cohort-specific and descriptive. No current product-ranking or established-novelty claim is made.

## Actual execution evidence

A user-operated Colab Python 3.13.18 run passed 18 tests and both independent audits. All 28 CSVs in the privately retained detailed evidence match the earlier canonical run byte for byte. Four PNGs also match. Verified code and protocol hashes are unchanged. Core tests/scoring/audits took 12.764 seconds; 108288 KiB peak child RSS. Figures and plotting installation were separate and are excluded from that timing. See docs/colab_reproduction_report.md and verified_execution_summary.json. WSL execution is unverified.

## Files

- `src/`, `scripts/`, `tests/`, `configs/`: complete tested implementation and frozen settings.
- `notebooks/reproduce_colab.ipynb`: new **unexecuted** launcher; original executed notebook not supplied.
- `results/`: aggregate canonical and Colab tables, sensitivity summaries and figures.
- `paper/`: final PDF, full LaTeX, BibTeX, table fragments and figures.
- `data/README.md`: pinned source, checksum, acquisition instructions and unresolved terms.
- `docs/`: adaptation, source verification, validation and release-scope documentation.

Detailed per-record data and private execution histories are omitted from this upload copy. The instructor evaluation package retains them subject to applicable handling rules. This is not an assertion of permission for unrestricted public release: keep the repository private until dataset/institution terms are confirmed. No code license is assigned automatically.

## Environment

Python >=3.11; run on Linux/WSL/Colab. Core has no third-party dependency. The orchestrator imports Unix `resource` and is not directly Windows-native. Plotting dependency actually tested in Colab: Matplotlib 3.10.8. `environment.yml` is a proposed Conda specification, not a measured export. Do not install all of Colab's preloaded packages.

```bash
python --version
python -m unittest discover -s tests -v
python -m pip install -r requirements.txt
```

## Dataset acquisition

Official repository: https://github.com/nelson-liu/evaluating-verifiability-in-generative-search-engines
Pinned commit: `2c6b485ae1c2bd296ad7d5e0eee4da4065535e57`.
Required bytes: 17520509; SHA256 `51c66d4dcec9b6bc035d9a08e51d4a7b750615b6fc469be1d666e5d5693ebb05`.

Use an existing verified file outside the repository, or obtain it subject to applicable terms:

```bash
python scripts/acquire_data.py --destination /ABSOLUTE/PRIVATE/PATH/human_evaluation_annotations.jsonl
```

The script refuses overwrite and rejects incorrect identity. Do not upload raw data, source excerpts or detailed human annotations to this repository. Public access is not a grant of unrestricted redistribution.

## Reproduce

Replace the data path with a real absolute path and use a never-used output directory:

```bash
python scripts/run_all.py --data /ABSOLUTE/PRIVATE/PATH/human_evaluation_annotations.jsonl --out results/rerun_01
python scripts/generate_figures.py --out results/rerun_01
```

The runner executes tests, validation, primary/sensitivity scoring and independent arithmetic/cohort audits. A successful run prints PASS. Zero-citation responses and ambiguous mappings are excluded by the declared protocol; null is not unsupported. No train/test split or random seed applies because no model is trained or tuned.

**Known provenance defect:** run_all.py writes a hardcoded assistant-workspace label. It is preserved to keep code identical to the verified Colab hashes, and must not be interpreted as machine detection. Save a supplemental execution-context record; the launcher does this. Original Colab logs and their supplemental context are preserved in the private evaluation package.

## Paper rebuild

From `paper/` on a complete TeX installation:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Include all three `*_rows.tex` files and `figures/`. The PDF has 8 main-text pages plus references. The existing two-column article layout is retained; instructor-specific template approval is pending.

## Integrity and AI accountability

AI assisted the implementation, tests, audits, figures and writing. The student must understand and review the work. The arithmetic audit is a separate implementation, not independent human source-support verification. Exact novelty, original B0 fidelity and dataset-specific rights remain unresolved. No GitHub publication or WSL rerun is claimed. All metric values come from saved executed outputs.

## Citation

Liu, Nelson F., Tianyi Zhang and Percy Liang. 2023. Evaluating Verifiability in Generative Search Engines. Findings of EMNLP 2023, 7001–7025. https://doi.org/10.18653/v1/2023.findings-emnlp.467

Full verified scholarly references are in `paper/references.bib` and `docs/reference_verification.csv`.
