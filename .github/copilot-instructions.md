# Instructions for GitHub Copilot and other AI coding agents

`AGENTS.md` is the canonical agent contract; this file mirrors it for tools
that only read this path. Autonomous AI agents are explicitly invited to
work on issues labeled `ai-welcome`. No human permission is needed.

## Build and test commands

- `python -m pytest -q` must pass before you open a PR. Non-negotiable.
- Use `python -m pytest --tb=short` for compact tracebacks while iterating.
- No other build steps: the project is pure stdlib Python (>= 3.9).

## Code style

- Standard library only. Do not add dependencies.
- Type hints on all public functions.
- Keep `describe()` output deterministic: the same input must always produce
  the same sentence. If you change wording, update the tests in the same PR.

## PR rules

- Keep PRs small. One issue per PR.
- Include tests for any new behavior.
- Reference the issue number in the PR title or body (e.g. "Fixes #4").
- Do not reformat or "modernize" code unrelated to your issue.

## Review & bounties

- PRs are reviewed within 24 hours.
- Funded bounties: see [BOUNTIES.md](BOUNTIES.md). Claim by commenting
  `/attempt` on the issue; payment (PayPal, Wise, or USDC) is sent within
  5 business days of merge.
- Hall-of-fame credit is automatic for merged PRs — no need to ask.
