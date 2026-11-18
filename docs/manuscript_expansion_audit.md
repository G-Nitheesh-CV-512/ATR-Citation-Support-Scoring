# Manuscript expansion audit

Date: 17 November 2026. Scope: editorial and literature revision only. This report supplements, rather than replaces, the historical experiment audit in `docs/final_audit.md`.

## Completion summary

| Item | Before | Revised | Status / evidence |
|---|---|---|---|
| Main text | 6 complete pages plus main text sharing page 7 with references | 8 complete main-text pages; references start on page 9 | VERIFIED by compiled PDF extraction and visual review |
| Total PDF length | 7 pages | 10 pages | VERIFIED |
| Bibliography | 4 entries: 3 scholarly + repository | 22 entries: 21 scholarly + repository | VERIFIED against BibTeX and citation keys |
| New scholarly references | — | 18 | VERIFIED; exact titles below |
| Scholarly publication verification | — | 21 official pages, BibTeX exports and PDFs inspected | VERIFIED for identity and scoped claims; not an exhaustive novelty search |
| Unused / undefined citations | — | 0 / 0 | VERIFIED by key-set comparison and clean compilation |
| Explicitly excluded candidates | — | 3, including one unresolved identity | Zhang unresolved; SelfCheckGPT and RAGChecker omitted on scope/redundancy grounds |
| Scientific files preserved | — | 186 code, test, config and result files unchanged | VERIFIED by SHA256 against pre-edit snapshot |
| Main results | 353 queries; 1,412 responses; 4,382 citation units | Unchanged | VERIFIED against canonical CSVs |
| Original baseline | Not reproduced | Not reproduced | Limitation preserved; C0/C1 remain adaptations |

## What changed

- Introduction now distinguishes source existence, individual support, collective support and pairwise gap interpretation.
- Related work expanded into five connected subsections: cited generation, human attribution, factuality/groundedness, measurement/reproducibility, and study positioning.
- Added an explicit explanation of response loss, the monotonicity invariant and citation-weighted versus query-weighted aggregation.
- Experimental design and failure-case analysis are clearly identifiable sections.
- Discussion distinguishes semantic-label validity, predictor evaluation and deterministic score transformation; includes reporting implications without claiming universal superiority of either control.
- All prior experimental results and limitations remain. No new experiments, model calls, significance tests or confidence intervals were added.
- The original 10-point, two-column A4 layout, margins and column spacing remain unchanged. A page break before references makes the main-text count unambiguous; no enlarged fonts or margins were used.

## Verification and metadata decisions

`reference_verification.csv` records exact titles, ordered authors, year, venue, volume/issue where applicable, pages, DOI, official URL, relevance, manuscript location and status for every entry. `reference_verification.md` records scope and exclusions. Original exports are retained in `reference_metadata/`; downloaded-source hashes and official metadata are in `literature_metadata_sources.json`.

Official metadata is not assumed infallible. TRUE's PDF title page orders Vered Cohen before Doron Kukliansky, whereas the export reverses them and spells the latter differently; the PDF order/spelling is used. PDF author forms restore Pang Wei Koh, Nelson F. Liu, Alexander R. Fabbri, Kryściński and Espinosa-Anke where exports shorten or normalize them. Belz's PDF/BibTeX name is Anya, despite HTML citation metadata saying Anja. Post's DOI follows the official landing page/export rather than a conflicting PDF footer. These are documented reconciliations, not guessed metadata.

Liu, ALCE, FActScore and RAGTruth were present in the supplied original review. The other works are explicitly additional neighboring literature. The review itself was not edited. One authoritative agreement survey is included for its directly relevant annotation assumptions; the set is not padded with generic AI surveys.

## Exact newly added scholarly references

1. FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (2023).
2. Evaluating Attribution in Dialogue Systems: The BEGIN Benchmark (2022).
3. RAGAs: Automated Evaluation of Retrieval Augmented Generation (2024).
4. ARES: An Automated Evaluation Framework for Retrieval-Augmented Generation Systems (2024).
5. RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models (2024).
6. Evaluating the Factual Consistency of Abstractive Text Summarization (2020).
7. Asking and Answering Questions to Evaluate the Factual Consistency of Summaries (2020).
8. On Faithfulness and Factuality in Abstractive Summarization (2020).
9. Understanding Factuality in Abstractive Summarization with FRANK: A Benchmark for Factuality Metrics (2021).
10. SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization (2022).
11. QAFactEval: Improved QA-Based Factual Consistency Evaluation for Summarization (2022).
12. TRUE: Re-evaluating Factual Consistency Evaluation (2022).
13. SummEval: Re-evaluating Summarization Evaluation (2021).
14. Survey Article: Inter-Coder Agreement for Computational Linguistics (2008).
15. A Call for Clarity in Reporting BLEU Scores (2018).
16. Non-Repeatable Experiments and Non-Reproducible Results: The Reproducibility Crisis in Human Evaluation in NLP (2023).
17. Twenty Years of Confusion in Human Evaluation: NLG Needs Evaluation Sheets and Standardised Definitions (2020).
18. Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science (2018).

## Numerical and preservation audit

The editorial audit reads the canonical `results/clean_run/` files, without rerunning scoring. Exact fraction fields were used to check four system scores, losses and all six pairwise gaps. Display rounding was checked against the existing LaTeX table fragments. The alternative-cohort loss table also matches the saved CSVs. Primary cohort cardinality and total citation units match the canonical response/system tables. Figure PDFs match the saved clean-run figures. All 186 protected files match their pre-edit hashes.

Per-system losses remain 0.826, 2.111, 3.753 and 1.220 percentage points for Bing Chat, Neeva, Perplexity and You. The maximum absolute pairwise change remains 2.927 points. All six orderings remain unchanged. This audit verifies manuscript consistency with existing experimental evidence; it is not a new raw-data experiment or a new human annotation audit.

## Compilation and visual checks

VERIFIED: final build started in a separate clean directory with only source, bibliography, table fragments and figures. pdfLaTeX → BibTeX → pdfLaTeX → pdfLaTeX completed. Final logs contain no undefined citations/references, LaTeX warnings or overfull boxes. All ten final PDF pages were rendered and visually inspected for legibility, clipping, table/figure placement, numbering and reference layout. References are standard-size and begin on page 9. Page 10 is the naturally partially filled final bibliography page; there are no blank pages.

The existing workspace uses a repaired local TeX format and font map. Exact commands and compiler logs are saved in `manuscript_expansion_logs/`. This does not establish LaTeX availability on the user's WSL machine. Standard rebuild on a functioning TeX installation: from `paper/`, run `pdflatex main.tex`, `bibtex main`, then `pdflatex main.tex` twice.

## Exclusions and remaining limitations

- EXCLUDED / UNKNOWN: the unspecified Zhang et al. (2024) identity cannot support a reliable citation.
- EXCLUDED by selection: SelfCheckGPT concerns a sampling-based detection route outside this reanalysis; RAGChecker was not needed alongside the selected RAG evaluation frameworks. Neither exclusion implies an invalid paper; final metadata checks were not pursued for these omitted entries.
- UNKNOWN: exact novelty, original DEN-01/DUP-01/AGG-01 conventions, dataset-specific redistribution rights and final local rerun.
- Historical, selected-cohort descriptive results cannot establish current product rankings or general citation reliability.
- Template/instructor compliance remains a human check: the existing two-column article layout was retained, not silently replaced by an ACM class.
- The package includes no raw annotation archive or downloaded third-party publication PDFs.

Previous manuscript, PDF, bibliography and prior reference-verification record are backed up under `paper/backups/pre_expansion_2026-11-17/`. The original final submission ZIP remains unchanged. The revised archive is a separate deliverable.
