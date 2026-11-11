---
trigger: model_decision
description: Enforces Andrej Karpathy clean code minimalism, surgical diffs, cognitive load reduction, and comment preservation when editing, refactoring, or writing code.
---

# Clean Code & Minimalist Engineering Discipline

When writing, refactoring, or debugging code:

## 1. Karpathy Clean Code Invariants
- **Surgical Diffs**: Modify only the lines strictly necessary to fix the issue or implement the requirement. Never reformat entire files or reorder unrelated imports.
- **Cognitive Load Reduction**: Avoid speculative abstractions, unnecessary wrapper classes, deep inheritance hierarchies, or complex design patterns for simple logic. Flatten control flow.
- **Preserve Existing Documentation**: Preserve all existing comments, docstrings, and type annotations that are unrelated to your code changes.
- **Zero Premature Optimization**: Do not optimize for hypothetical future requirements. Implement the simplest viable solution that satisfies all constraints.

## 2. Refactoring Safety Checks
1. Before touching existing logic, identify existing tests or create a minimal reproduction.
2. Maintain identical external API signatures unless a breaking change is explicitly approved.
3. Validate behavior preservation by running test suites immediately after each discrete change.

