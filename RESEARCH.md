# User brief and comparison

## Intended user and painful task

Notebook reviewers handing analysis to another engineer. A saved notebook can contain repeated/decreasing counts, orphaned outputs and saved errors; reviewers need precise cell evidence without rerunning code.

Current alternatives: Notebook clearing, nbstripout/nb-clean and semantic nbdime review.

Evidence and limits: nbstripout issue 180 requests handling error outputs; it supports interest in notebook hygiene, not a request for this project. Execution-state demand is inferred. No fabricated customers, requests, adoption, testimonials or growth promise.

## Smallest useful capability and acceptance criteria

Detect duplicate/decreasing execution counts, orphaned outputs, mismatched result counts and saved errors; reject invalid counters; preserve the notebook.

Runnable acceptance fixtures are `test_notebook_state_check.py` and `demo.py`. Invalid inputs must return an explicit failure, and diagnostics must preserve source files where the contract is read-only. See README for supported subsets and bounds. Plausible discovery path: python, jupyter and notebook topics; a synthetic count-anomaly example linked from the project index.

## Live leader research on 5 October 2026

Queries `notebook clean outputs`; `notebook diff in:name,description` were requested from live GitHub sorted by stars descending. Search receipts include exact query URLs, observation times and top-ten metadata in [research-evidence.json](research-evidence.json). Irrelevant broad matches were rejected: map fonts/geospatial tools are not JavaScript source-map comparables, browser redirect extensions are not site migration analysis, and unrelated notebook/diffusion matches are not notebook hygiene tools.

Highest-star relevant comparable found among the researched set: [jupyter/nbdime](https://github.com/jupyter/nbdime) with 2843 stars. Some established comparables were added outside the narrow search query. This is bounded search coverage, not an exhaustive global ranking. Stars are a discovery signal, not a performance/reliability result.

| Comparable | Stars | Last observed push UTC | License metadata | Workflow, install, docs and tradeoff |
| --- | ---: | --- | --- | --- |
| [jupyter/nbconvert](https://github.com/jupyter/nbconvert) | 1939 | 2026-09-14T15:30:42Z | BSD-3-Clause | Notebook conversion and execution workflows; broader runtime/template tooling. Docs provide conversion commands; not installed or timed here. |
| [kynan/nbstripout](https://github.com/kynan/nbstripout) | 1485 | 2026-04-11T18:16:00Z | unresolved metadata; inspect license before reuse | Clears output/metadata through pip and Git filters. Issue 180 discusses error-output hygiene. Clearing and diagnostics are different actions; no missing-feature claim. |
| [jupyter/nbdime](https://github.com/jupyter/nbdime) | 2843 | 2026-06-10T10:12:19Z | unresolved metadata; inspect license before reuse | Notebook-aware semantic diff and merge; pip install, command/UI documentation and tests. Broader comparison workflow; not installed or timed. |
| [srstevenson/nb-clean](https://github.com/srstevenson/nb-clean) | 202 | 2026-09-01T18:04:35Z | ISC | Notebook metadata/output cleaning with Git and pre-commit support. Preserving selected metadata is documented; this MVP is read-only diagnostics. |

Current READMEs and the returned recent issue/PR samples were inspected. Samples may be maintainer PRs, not genuine user requests. Support channels and examples are visible; support responsiveness, actual installation reliability and time to first useful result of comparables were not measured. License metadata marked unresolved/unavailable is not a permission to reuse. No competitor code or prose is incorporated.

## Distinctness and rejected directions

Compared with all 133 owned repository names, descriptions/READMEs for overlapping tools and yesterday's five launch briefs. The five new products handle saved notebook state, planned redirect graphs, exported LFS bytes, content-bound JSONL record references, and generated-code source positions respectively. They share packaging, not one subdivided product.

Existing json-differ/log-parser/traceweave analyze different JSON or agent-trace semantics; urlnorm normalizes URLs; syncplan plans filesystem synchronization; wheel-sentinel validates Python wheel archives; portable-tree audits names. This candidate's user contract is separate. Environment checking was rejected because envdiff/env-vault/dotenv-mini already cover it; another archive checker was rejected as overlapping Wheel Sentinel.

## Fairness and limitations

Saved counts do not prove reproducibility, freshness, causality or correctness. No kernel execution or secret detection. nbformat 4 subset, maximum 10 MB / 10,000 cells; cell positions are zero based.

There is no measured competitor benchmark or superiority claim. Local examples establish our behavior only. No claim is made that a competitor lacks this capability. Broader established tools can be better choices when their workflow/dependencies fit. Evidence dates, installed behavior and untested limits remain separate.
