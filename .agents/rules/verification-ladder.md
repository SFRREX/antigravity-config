---
trigger: model_decision
description: Enforces the mandatory 6-step verification ladder before declaring any task, bugfix, or feature complete. Applies whenever concluding work or asserting tests pass.
---

# The 6-Step Verification Ladder (Evidence Before Assertions)

Under Antigravity rules, **a plan is not execution; a tool call is not proof of success; and a passing test is not proof of every requirement**. Never claim work is done without empirical verification.

```
[Level 6] Explicit User Confirmation
    ▲     (Mandatory for Level 3 high-impact / irreversible actions: db drops, secret rotations)
    │
[Level 5] Independent Review & Spec Verification
    ▲     (Syntax & logic verification against all initial constraints and edge cases)
    │
[Level 4] Integration & Live State Verification
    ▲     (Dev server invocation, live HTTP response check, or browser E2E test)
    │
[Level 3] Targeted Unit & Regression Test Suite
    ▲     (Execute pytest / vitest / jest / dart test; inspect exit code 0)
    │
[Level 2] Deterministic Invariants & Schema Assertions
    ▲     (Confirm output files exist on disk, non-empty, valid JSON/YAML/AST syntax)
    │
[Level 1] Syntax & Type Validation
          (Compiler check, linter pass, typechecker: tsc / flake8 / dart analyze)
```

## Mandatory Verification Protocol
1. **Never Assume Exit Code 0**: Inspect the exact command output and exit status of test runners before declaring tests pass.
2. **Deterministic File Verification**: Use `Test-Path` or file inspection to confirm that modified or generated files exist on disk.
3. **No Fabricated Completions**: If a test suite fails, report the exact error, form a hypothesis, and fix the underlying issue before asserting resolution.
4. **Resumable State**: For multi-step tasks (3+ steps), record verification status in durable files (`task_plan.md`, `progress.md`).

