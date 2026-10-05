# notebook-state-check

Read-only notebook execution-state diagnostics with precise cell evidence.

## Install and first useful result

```bash
git clone https://github.com/nripankadas07/notebook-state-check
cd notebook-state-check
python -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/python demo.py
.venv/bin/notebook-state-check --help
```

Python 3.10 or newer. The example creates synthetic inputs; it needs no account, service, token or downloaded dataset. Runtime uses only the standard library. Building requires setuptools from the package registry. POSIX commands above; Windows/macOS installation has not been tested.

## Useful contract

Detect duplicate/decreasing execution counts, orphaned outputs, mismatched result counts and saved errors; reject invalid counters; preserve the notebook.

Import `notebook_state_check` for the function used by `demo.py`, or use the installed CLI described by `--help`. JSON reports print to stdout. Exit 0 means the documented success condition, 1 means diagnostic findings or an unmapped source position where applicable, and 2 means invalid input or I/O failure. JSONL indexing uses 0/2 only; LFS returns 2 when no pointers were found.

## Limits

Saved counts do not prove reproducibility, freshness, causality or correctness. No kernel execution or secret detection. nbformat 4 subset, maximum 10 MB / 10,000 cells; cell positions are zero based.

No performance or superiority claim. Demand is inferred. See [research and acceptance criteria](RESEARCH.md), [validation](VALIDATION.md) and [support and security](SUPPORT.md). MIT license; implementation and synthetic fixtures are original. Comparables inform scope; no competitor code or prose is incorporated.

## Development

```bash
python -m unittest -v
python -m compileall -q notebook_state_check.py
python demo.py
```

## CLI input

`notebook-state-check analysis.ipynb` reads a saved nbformat 4 file; cell indices in diagnostics are zero based. It does not execute notebook code.
