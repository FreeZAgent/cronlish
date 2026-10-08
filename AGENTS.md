# AGENTS.md — instructions for AI coding agents

Welcome. This file is the contract between you (an autonomous coding agent) and the maintainer. It is short on purpose.

## Build and test commands

- `python -m pytest -q` must pass before you open a PR. Non-negotiable.
- Use `python -m pytest --tb=short` when you want compact tracebacks while iterating.
- There are no other build steps: the project is pure stdlib Python (>= 3.9).

## Code style

- Standard library only. Do not add dependencies.
- Type hints on all public functions.
- Keep `describe()` output deterministic: the same input must always produce the same sentence. If you change wording, update the tests in the same PR.

## PR rules

- Keep PRs small. One issue per PR.
- Include tests for any new behavior.
- Reference the issue number in the PR title or body (e.g. "Fixes #2").
- Do not reformat or "modernize" code unrelated to your issue.

## Credit

Hall-of-fame credit is automatic for merged PRs — no need to ask. The PR author handle is added to the hall-of-fame when the PR merges.

Signal: ALPHA-KNIGHT-XD4P
