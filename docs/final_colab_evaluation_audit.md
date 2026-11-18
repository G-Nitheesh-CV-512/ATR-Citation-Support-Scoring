# Final Colab integration and evaluation audit

Date: 18 November 2026. Sources: uploaded earlier final package, uploaded Colab evidence ZIP and assignment screenshots (sections 7–12). The inputs are hashed in colab_integration_audit_logs/uploaded_input_identities.json. This is a review and packaging stage; no new experiment or literature expansion was performed.

| Check | Status | Evidence / limitation |
|---|---|---|
| Colab archive integrity | VERIFIED | CRC passes; all 56 supplied evidence file hashes match |
| Earlier source archive | VERIFIED | CRC and supplied package content manifest checked |
| Colab code/config identity | VERIFIED | 20 code/script/test hashes plus frozen configuration match |
| Numerical reproduction | VERIFIED | All 28 primary/sensitivity CSVs match prior canonical outputs byte for byte |
| Figure reproduction | VERIFIED | Four PNG files match exactly; PDF generation metadata may differ |
| Tests | VERIFIED | 18 tests in uploaded Colab log; 18 tests rerun in each prepared evaluation/GitHub copy |
| Independent audits | VERIFIED | Uploaded raw-arithmetic and cohort/bridge audit reports PASS; this review did not rerun raw-data scoring |
| Manuscript numbers | VERIFIED | Exact fraction relationships and all six pair gaps match Colab CSVs; display fragments and sensitivity losses checked |
| Scientific preservation | VERIFIED | All prior source/test/configuration/result files unchanged; all 57 uploaded Colab files preserved exactly in evaluation copy |
| Final paper | VERIFIED | 8 scientific pages + 2 references; all 10 pages rendered and inspected |
| Bibliography | VERIFIED / prior source verification reused | All 22 entries unchanged and cited; no new literature search, unused keys or missing references |
| Clean LaTeX build | VERIFIED | Fresh build directory; no warnings or overflow in final log |
| Assignment A–E files | VERIFIED present with qualifications | See assignment_compliance.md; original executed notebook and actual oral demonstration remain student actions |
| GitHub upload copy | VERIFIED file preparation | Allowlist contains source, paper, aggregate evidence and selected docs; no raw/per-record exports or common credential signatures detected |
| Original B0 | NOT REPRODUCED | C0/C1 remain declared adaptations; conventions unresolved |
| Dataset-specific rights | UNKNOWN | Access/hash evidence is not a reuse/redistribution license |
| Full assignment/template compliance | UNKNOWN beyond supplied screenshots | No complete PDF/current Classroom settings; existing article layout retained |
| Original executed notebook | NOT SUPPLIED | New launcher is unexecuted; syntax checked, no fabricated cell outputs |
| Local WSL run | UNKNOWN | Actual user reproduction occurred in Colab |
| GitHub publication / sharing | NOT PERFORMED | User must create/upload repository and set instructor access |
| Novelty / human annotation truth | UNKNOWN / not established | Reproduction does not validate novelty or original human source judgments |

## Results retained

Primary: 353 common queries, 1412 responses, 4382 mapped citation units. Losses remain Bing Chat 0.826, Neeva 2.111, Perplexity 3.753 and You 1.220 percentage points. Maximum absolute pairwise gap change is 2.927 points. All six pairwise orderings remain unchanged. Alternative duplicate cohorts retain 363 and 369 queries; pooled aggregation uses the unchanged primary cohort. The repeated-record variants also alter coverage, so they do not isolate a causal annotation effect.

## Corrections and boundaries

The paper's execution paragraph and data-provenance limitation were updated to recognize the supplied Colab evidence. Code, scoring definitions, cohort, references and experimental outputs were not changed. The inherited hardcoded assistant-environment label remains in the unchanged runner/manifest, with the actual Colab context preserved separately. Detailed evidence is kept in the instructor package; the GitHub copy omits per-record exports and private histories. This is a prudent release scope, not an assertion of legal clearance. Keep the repository private pending instructor/institution approval for public release.

The complete earlier manuscript and bibliography are backed up. Root historical records remain preserved with appended current evidence. Old audits report earlier states and are not silently rewritten as if Colab had run then. The new unexecuted launcher is provided for rerunning; it must not be presented as the missing original executed notebook.

## What must be done by the student

Confirm enrollment number, template and Classroom instructions; download the original executed .ipynb with outputs; review and understand the source and limitations; resolve dataset handling terms; create the repository and provide actual access/link; prepare the five-minute demonstration. See evaluation_steps.md for exact placement and commands. No institutional acceptance, oral defense, GitHub publication or laptop execution is claimed by this audit.

## Package integrity

Both prepared ZIPs opened successfully, every entry CRC passed and every manifest content hash matched. All required implementation/paper paths were present. GitHub allowlist inspection found no raw archive or per-record exports. A final packaging pass includes this record; final ZIPs are checked again. Full manifest and inventory record included paths rather than asserting all unseen assignment conditions are satisfied.

## Package integrity

Both prepared ZIPs opened successfully, every entry CRC passed and every manifest content hash matched. All required implementation/paper paths were present. GitHub allowlist inspection found no raw archive or per-record exports. A final packaging pass includes this record; final ZIPs are checked again. Full manifest and inventory record included paths rather than asserting all unseen assignment conditions are satisfied.
