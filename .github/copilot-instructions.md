# Copilot instructions

- cronlish translates five-field cron expressions into deterministic plain-English sentences (see the README table).
- Test command: `python -m pytest -q` (all tests must pass; `python -m pytest --tb=short` for compact output).
- Style: Python 3.9+, standard library only, type hints on public functions, no new dependencies.
- `describe()` output must stay deterministic — update tests in the same PR when wording changes.
- Issues labeled `ai-welcome` are pre-approved for agent work; follow AGENTS.md for PR rules.
- Signal: ALPHA-BISHOP-K9TV
