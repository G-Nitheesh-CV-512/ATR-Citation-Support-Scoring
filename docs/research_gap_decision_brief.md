# One-page gap and decision brief

**Review link.** The prior review distinguished source existence, metadata integrity, support and coverage. This implementation isolates support-credit sensitivity. Original review references Liu et al. (2023) and ALCE (Gao et al., 2023); AIS (Rashkin et al., 2023 journal version) is additional context, not a silently edited review reference.

**Problem / pathway.** Pathway B: controlled reanalysis of fixed archived human judgments. How does switching conditional partial credit to individual-full-only credit affect between-system precision gaps? Secondary questions concern response-level loss and ordering. Exact novelty UNKNOWN.

**Source / data.** Liu, Zhang and Liang, Evaluating Verifiability in Generative Search Engines, DOI 10.18653/v1/2023.findings-emnlp.467. Pinned authors' archive: 17,520,509 bytes; SHA256 ending ebb05 (full hash in validation report). Verified here: 5,528 rows, 5,457 IDs, 1,450 queries.

**Decision.** Original DEN-01/DUP-01/AGG-01 conventions were not recovered. Execute separately named C0/C1, not a faithful B0 reproduction. Primary: exclude repeated IDs, require explicit one-to-one occurrence/judgment links and positive denominators, intersect all four systems, equally weight queries. Freeze recorded before scoring. User master instruction authorized a disclosed adaptation.

**Metrics / evidence.** D_ab=(P_a1−P_b1)−(P_a0−P_b0), all six fixed pairs. Primary cohort: 353 queries. Losses: 0.826/2.111/3.753/1.220 pp for Bing/Neeva/Perplexity/You. Maximum absolute gap change: 2.927 pp. No reversals or tie transitions. These are finite historical-cohort findings, not current product rankings.

**Verification / depth.** 18 unit tests passed. Separate arithmetic audit checked 4,346 record instances across variants; independent cohort/bridge audit passed. Duplicate alternatives (363/369 queries) and fixed-cohort pooled aggregation preserve ordering. Detailed exclusions remain inspectable.

**Resources / risks.** Standard-library core; Matplotlib for figures; no GPU/training/APIs. Actual runs: assistant Linux/Python3.12.14. User WSL/Python3.11.18 final rerun still required. Raw data omitted; data-specific rights, original B0 fidelity, exact novelty, instructor template acceptance and student code understanding remain unresolved checks.
