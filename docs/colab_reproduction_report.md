# Colab reproduction verified from uploaded evidence

Date: 18 November 2026. Input: ATR_Colab_Evidence_colab_run_20261118_050741_235632.zip, user-uploaded. No experimental pipeline was rerun for this integration.

## VERIFIED

- All 57 archive entries pass CRC; all 56 file hashes in the supplied evidence manifest match.
- All 28 CSV exports match the prior canonical run byte for byte, including primary, pooled aggregation and both duplicate variants.
- All four PNGs match the original figure files byte for byte. PDF metadata can differ across generation times; PDF byte identity is not the scientific reproduction criterion.
- All 20 source/script/test hashes recorded in the Colab manifest match the uploaded project; the frozen configuration hash also matches.
- Colab Python 3.13.18, Linux, two logical CPUs; all six runner subprocesses exit 0, 18 tests pass, both independent audits PASS.
- Primary cohort: 353 queries, 1412 responses, 4382 mapped units. Alternative cohorts: 363 and 369 queries. Arithmetic audit: 4346 record instances. All six pooled pair checks pass.
- Core scoring, tests and audits: 12.764311302 seconds, max child RSS 108288 KiB. Figure generation and plotting installation are separate and excluded from this timing. Matplotlib 3.10.8 is present in the supplied installation record and package inventory.
- Input acquisition provenance and validation both record 17520509 bytes and SHA256 51c66d4dcec9b6bc035d9a08e51d4a7b750615b6fc469be1d666e5d5693ebb05.

## Preserved discrepancy

The original runner writes a hardcoded `environment` description saying assistant workspace. This is not automatic environment detection. Its original log and code are preserved unchanged. `colab_execution_context.json`, Colab paths, interpreter/platform and user-supplied execution evidence document the actual Colab run. No claim of WSL execution follows. Future invocations of this runner need an explicit supplemental context record, as provided by the new launcher notebook.

## Limitations / missing files

The original executed .ipynb was not attached. This does not negate the supplied code/output/log evidence, but prevents inspection of the original notebook cell order and complete interactive session. `notebooks/reproduce_colab.ipynb` is a newly generated launcher with no executed outputs; do not present it as the executed original. Save and supply the original notebook separately if required by the instructor.

The dataset's access and identity are evidenced, but dataset-specific licensing and third-party redistribution terms remain UNKNOWN. Original B0 is NOT REPRODUCED. C0/C1 implement the documented adaptation; exact novelty remains UNKNOWN. A Colab reproduction is not independent human source-support validation or a laptop hardware benchmark.
