# Baseline validation record

Initialized: 2026-11-14, Prompt 04. This is a status register, NOT the completed Prompt 10 validation report.
Candidate baseline: Liu et al. (2023), original citation-verifiability scoring procedure, B0.
Overall status: NOT IMPLEMENTED / NOT VALIDATED. Formal Gate G2 not reached.

| Check | Evidence status | Validation status | Next stage |
| --- | --- | --- | --- |
| Original method source | VERIFIED inspected | Definition available; implementation not checked | 06, 09, 10 |
| Published collective partial-support rule | VERIFIED in original method | B0 must preserve it; B1 differs deliberately | 07, 09, 10 |
| Data artifact | VERIFIED prior parse/hash | Semantic validity not established by file access | 06 |
| Duplicates/null annotations | VERIFIED observed in Prompt 03 | NEEDS CORRECTION if silently discarded or treated as independent generations | 06, 07 |
| Counting/denominators/aggregation | UNKNOWN exact implementation mapping | UNCERTAIN until documented | 06, 07, 10 |
| User environment | UNKNOWN | No console output or installed-version evidence | 08 |
| Baseline source code | UNKNOWN / not created | Not executed | 09 |
| Unit/sanity tests | UNKNOWN / not created | Not run | 09, 10 |
| Measured baseline output | UNKNOWN / absent | No result or reproduction claim | 10 |
| Comparison authorization | Pending baseline validation | No extension execution allowed yet | 12 |

Prompt 10 requires VERIFIED / UNCERTAIN / NEEDS CORRECTION validation items. These will coexist with the evidence ledger's VERIFIED / INFERRED / UNKNOWN labels; the labels serve different purposes.

No weights or GPU are required by the proposed archived-label calculation. No measured resource claim is made. No baseline, testing, or experiment code was written in Prompt 04.


## Prompt 04 approved - documentation clarification (2026-11-14)
The user approved Prompt 04 with these corrections. Earlier entries above are historical and preserved.
- Prompt 05 remains NOT STARTED; wait for the user's next explicit instruction. No coding, dataset modification or experiments authorized.
- The four-day estimate assumes approximately six focused hours per day; this is a planning assumption, not confirmed user availability.
- Dataset hash verification occurred in the inspected assistant working environment. Successful access/hash checking from the user's WSL environment remains UNKNOWN and pending Prompt 08.
- Scope remains citation-support scoring sensitivity only: no source-existence audit, bibliographic metadata evaluation, full four-dimensional benchmark or current-system rankings.
- B0 is the faithful original scoring procedure; B1 is strict full-support-only; optional B2 is removed first if time becomes insufficient.
- Exact novelty remains UNKNOWN until the targeted literature screening is sufficiently completed. Feasibility approval does not establish novelty or baseline validity.


## Prompt 05 documentation update (2026-11-14)
B0 remains NOT IMPLEMENTED / NOT VALIDATED. Paper-level formula verified; exact label mapping, denominator, aggregation and original code remain unresolved. New planning reference: docs/prompt05_research_questions.md. The proposed common-query comparison is separate from original-cohort reproduction. B1 is individual-full-support-only; B2 excluded. No score, sanity test, execution or baseline acceptance is claimed. User WSL access is still pending Prompt 08.


## Prompt 05 denominator clarification (2026-11-14)
User approval is in principle, subject to clarification now documented. VERIFIED: paper defines total response citations; schema separates occurrence-offset objects from statement-to-marker-text associations. INFERRED: their counts are equivalent only under a verified complete one-to-one mapping and matching eligibility/counting conventions. UNKNOWN / DEN-01: exact original mapping. Earlier association-denominator wording is superseded, not evidence of reproduction. B0 formula is preserved; association-based adaptation is not authorized. Limited read-only schema/example inspection and document correction only; no experimental code or execution. Prompt 06 not started. See docs/prompt05_research_questions.md, denominator clarification.


## Prompt 06 verification completion (2026-11-15)
Current status: NOT IMPLEMENTED / NOT VALIDATED; verification report complete but fidelity BLOCKED. Historical entries above remain unchanged.

| Item | Evidence status | Validation consequence |
| --- | --- | --- |
| Archive identity | VERIFIED assistant-local hash and Git blob | Not user WSL verification; pending Prompt 08. |
| Core B0 rule and named exceptional labels | VERIFIED paper/README | Executable fidelity still untested. |
| DEN-01 denominator | UNKNOWN original convention; VERIFIED 335 list/mapping count mismatches | Block faithful reproduction; require original normalization and numerator propagation. |
| DUP-01 repeated records | VERIFIED observed; original selection UNKNOWN | No silent deduplication/averaging or independent-generation assumption. |
| AGG-01 aggregation and N=0 | UNKNOWN executable conventions | Cannot claim Table 8 reproduction. |
| Scorer availability | No precision scorer in inspected main snapshot | Paper-based implementation would need independent verification; code not written. |
| COHORT-01 | Preliminary screens VERIFIED; final eligible cohort UNKNOWN | No global ranking until common semantic cohort established. |
| Licensing | MIT software notice VERIFIED; data-specific scope UNKNOWN | Keep data redistribution unclaimed. |

See docs/prompt06_dataset_comparator_verification.md for exact source links, examples, counts and minimum clarification packet. Prompt 07 not started. No experimental output or baseline gate passed.


## Prompt 07 conditional blueprint (2026-11-15)
Overall status remains NOT IMPLEMENTED / NOT VALIDATED. Prompt 07 is a conditional blueprint, not a passed baseline gate. Original B0 formula retained; operational DEN-01, DUP-01, AGG-01 remain blocking. No denominator/zero-citation/weighting defaults introduced. Published-cohort reproduction is distinct from matched-cohort sensitivity.

Planned validation: independent worked cases and original count propagation, exact shared units/denominators, raw label branches, repeated-record rules, N=0 conventions, provenance coverage and published-cohort reconciliation. Reference values/tolerances require evidence before scoring. No checks have been executed. User WSL/environment remains pending Prompt 08. See blueprint sections N–O for freeze and correction gates.


## Prompt 08 — environment materials prepared, local evidence pending (2026-11-15)
- VERIFIED — user authorized environment instructions and one inspection script only. The script and guide now exist; syntax was statically parsed, but the script was NOT executed here and no package installation was performed as local-user evidence.
- INFERRED — separate `citation_eval` with Python 3.11 and standard library is a suitable initial setup. `polegeo` must remain untouched. requirements.txt has no external dependencies; environment.yml is proposed, not an actual export.
- VERIFIED — optional release metadata: pandas 2.2.3 >=Python3.9, NumPy 2.1.3 >=Python3.10, Matplotlib 3.9.2 >=Python3.9; all list Python3.11. These pins are deferred candidates, not tested local compatibility or latest-release claims. Sources and conditional checks are in docs/prompt08_environment_setup.md.
- UNKNOWN — current WSL/Conda/Python installation, user hardware diagnostics, local dataset access/hash and every optional package's actual compatibility. Await actual console output and JSON reports.
- VERIFIED — new GitHub metadata request failed with a transport error; it provides no new archive-access evidence. Prior inspected archive identity is retained without claiming user-side verification.
- Decision P08-D01: environment-only checks may complete without a dataset; report dataset NOT_CHECKED. No download without separate confirmation; no raw-data redistribution while LIC-01 is unresolved.
- Decision P08-D02: B0/B1 remain NOT IMPLEMENTED / NOT VALIDATED; DEN-01, DUP-01 and AGG-01 stay blocking. Environment success cannot resolve methodological fidelity. Novelty remains UNKNOWN. Prompt 09 not started.
- Decision P08-D03: deterministic inspection/scoring has no seed; stochastic analysis remains separately conditional. Preserve original errors and rerun outputs rather than inventing debugging evidence.
- Next action: user runs the staged WSL commands and supplies actual output; inspect it before marking Prompt 08 complete. Docs copies of historical root records are synchronized; earlier entries and corrections are retained.


## 15 November 2026 — executed adapted study and current status

This current entry supersedes earlier stage-stop statuses; earlier history remains intact. The actual master execution and continuation prompts authorized a defensible named adaptation and completion in the accessible workspace. The laptop path was inaccessible; no local-machine modification or execution is claimed.

VERIFIED: existing archive size/hash and structural counts rechecked; C0/C1 implemented; 18 unit tests passed; original_b0 intentionally raises NotImplementedError. Primary cohort: 353 queries, 1,412 records, 4,382 occurrence links. Separate raw-label audit checked 4,346 record instances across primary and two duplicate variants; separate cohort audit verified memberships, bridges, duplicate policies, weights and all six pooled gaps. Five key tables from two genuine runs were byte-identical.

Measured primary losses (pp): bing_chat 0.826251180358829; neeva 2.111156077161743; perplexity 3.7528665857277757; you 1.2197041233868429. Largest absolute gap change 2.9266154053689464 pp. No reversal or tie transition. Duplicate variants use 363 and 369 queries and preserve ordering. These are adapted finite-cohort results, not original published or current-product rankings.

FINAL-D01: use C0/C1 under configs/protocol.json, frozen before scoring. Conservative unique-ID, bijective positive-citation eligibility and equal-query macro weights are explicit adaptations. User authorized adaptation; instructor acceptance is unobserved.
FINAL-D02: zero citations remain undefined; nulls are not unsupported; exclusions apply identically. Unknown original propagation is not guessed.
FINAL-D03: original B0 NOT REPRODUCED; DEN-01/DUP-01/AGG-01 stay UNKNOWN for original fidelity. COHORT-01 is resolved only for this adaptation. LIC-01 and exact novelty remain UNKNOWN.
FINAL-D04: no raw archive or source excerpts distributed; detailed derived judgment exports require rights review before public release. No GitHub publication.
FINAL-D05: actual Linux/Python3.12.14 workspace execution; user reports WSL/Python3.11.18 success but actual final local run is TEST REQUIRED. Matplotlib3.10.8 was used here; metadata supports Python>=3.10, local compatibility remains untested.
FINAL-D06: actual TeX and metadata-report errors are preserved in error_log.md. Table formatting repair changes no scientific values. No invented research-code failure or human correction.

Evidence: docs/methodology_final.md; results/clean_run/logs; tests; master_execution_prompt.md; resume_prompt.md. Next actions: student reviews adaptation, rights, template, code understanding and local reproducibility. Full earlier verbatim chats and instructor gate approvals remain unverified.

### Adapted validation verdict
VERIFIED: credit rules, suppression, contradiction, exceptional labels, null rejection, positive aligned denominators, repeated markers/IDs and exact arithmetic under the adaptation. Exhaustive small label cases supplement hand-constructed examples. Separate auditors do not import scorer/parser/cohort functions. NOT COMPLETED: full published Figure2 example reconstruction and Table8 reproduction under recovered original conventions. Synthetic tests are not mislabeled published examples.


## 18 November 2026 — User Colab reproduction verified from uploaded evidence

VERIFIED: supplied Colab run colab_run_20261118_050741_235632 has the expected input hash, matching code/configuration hashes, 18 passing tests, all six orchestration subprocesses exit 0, and both independent audits PASS. All 28 CSV exports match results/clean_run/ byte for byte. Core scoring/audits: 12.764 seconds, 108288 KiB maximum child RSS; separately generated figures use Matplotlib 3.10.8. Notebook file not supplied; full WSL execution remains UNKNOWN. The runner's hardcoded environment label is preserved and explained by colab_execution_context.json. No source/configuration or experimental-output values were changed. Manuscript execution/provenance paragraphs updated to reflect this evidence. Original B0 NOT REPRODUCED; C0/C1 remain adaptations. Dataset-specific rights and exact novelty remain UNKNOWN.


The Colab reproduction confirms the documented adaptation and arithmetic, not original-cohort B0 fidelity or correctness of human support labels.
