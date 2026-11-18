# Final adapted methodology and deviation register

Date: 15 November 2026. Scope: Pathway B controlled comparison of citation-support credit on archived observations. This amendment was authorized by the user's master instruction to implement a defensible, explicitly documented adaptation if exact B0 reconstruction was unavailable. The saved pre-score configuration is configs/protocol.json (SHA256 in protocol.sha256 and first clean run manifest). It was created before C0/C1 scores were calculated. The prior 357-query screen was known but was not adopted as the final cohort.

## What was and was not reproduced

The original rule uses P0=(T_fs+T_ps)/N_paper. Conditional partial units count only if collective support is full and there is no individually full-supporting citation for that statement. This rule is not half-credit. The source rule and documented label normalization are implemented and behaviorally checked. Original-cohort occurrence propagation, repeated-record selection and zero-citation aggregation remain UNKNOWN. Faithful B0 is NOT REPRODUCED. The original_b0 entrypoint raises NotImplementedError to prevent an accidental claim.

C0 and C1 are separately named adaptations. Neither denominator nor averaging is represented as the authors' recovered convention.

## Primary contract

1. Validate exact input size/hash; parse every row; preserve line order and raw data.
2. Exclude all repeated response IDs, including identical records, from primary eligibility. Require one raw row per exact query/system cell.
3. Validate half-open citation offsets against unchanged response text. A cited statement must have exactly one exact substring span. Its marker multiset must equal its judgment marker multiset. Each statement-marker judgment must link to exactly one citation object inside that span, and every object must be used exactly once. Equal counts alone do not pass.
4. Zero citation count means undefined precision, not zero support. Null/unknown required judgments or unresolved mapping exclude the response from both controls; retain reasons. All recorded raw exceptional labels retain their original category; documented no-support mapping is applied.
5. Retain only exact queries eligible for all four historical systems. No paraphrase merging, query sampling or label-conditioned threshold selection. Observed final cohort: 353 queries, 1,412 records, 4,382 mapped citation units. These are independently reconstructed, not assumed from the prior screen.
6. C0=(full+conditional_partial)/N and C1=full/N with the same positive mapped-occurrence denominator. Cited units, labels, records and weights are identical; only partial credit changes.
7. Macro-average response ratios with equal query weights. Use exact fractions for values and tie comparisons. Compute all six pairs in fixed system order bing_chat, neeva, perplexity, you. D_ab=(P_a1-P_b1)-(P_a0-P_b0)=L_b-L_a. Report precision percent and differences in percentage points.
8. No stochastic processing, bootstrap, p values, confidence intervals or practical-effect threshold. This is finite-archive description conditional on labels. No train/validation/test split because no model is fitted or tuned.

## Declared sensitivity analyses

- Collapse identical: keep one representative of full-object-identical records, exclude groups with differing records. The earliest line represents identical content for provenance only; it does not select one conflicting annotation. Final common cohort 363 queries.
- Distinct-record mean: retain one copy of each structurally distinct record and equally average their scores within each response/query; require identical response text and valid mappings for every retained record. This is not an assumption of independent annotators. Final common cohort 369 queries and 1,482 record instances. Equal query weights remain.
- Pooled aggregation: use sum of credited units / sum of denominators on the unchanged 353-query primary cohort. This changes response weights, not policy unit definitions. It is not original AGG-01 recovery.
- Failure analysis: all exclusions retained; nonbijective markers, nonunique spans, nulls, zero citations and duplicate records reported. Reason counts overlap.

The duplicate variants change cohort coverage as well as handling; they do not isolate a causal annotation-selection effect. Primary results were not switched to the variant yielding the largest effect. Repeated citation propagation and zero-as-zero alternatives were not added after viewing results; excluded ambiguity is a limitation, not silently resolved.

## Source-to-code bridge

| Evidence | Operational use | Implemented file | Validation |
|---|---|---|---|
| Liu §2.4, conditional support definition | Qualifying partial-credit predicate | src/scoring.py | Synthetic edge cases and exhaustive small label combinations |
| Authors' README, category mapping | Full/partial/other normalization, raw category retained | src/annotation_parser.py | Exceptional-label tests |
| Archive position objects and mappings | Conservative bijection, explicit adaptation | src/annotation_parser.py | Wrong offsets/repeated markers tests; independent full archive bridge audit |
| Unresolved original record/aggregation convention | Primary exclusion plus declared variants, no original fidelity claim | src/cohort.py; src/metrics.py | Raw-data reconstruction and exact fractions |
| Fixed archived-label study question | Six pairwise gap changes | scripts/run_experiment.py | Independent raw-label recalculation |

No model-generation source code was reused. Algorithms were written for this study with AI assistance. The original source definitions are credited, but no source-content correctness or human-annotation agreement claim is added.
