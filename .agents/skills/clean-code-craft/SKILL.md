---
name: clean-code-craft
description: Unified code quality, simplification, and engineering discipline engine. Merges Andrej Karpathy's coding pitfalls discipline with structured refactoring principles. Use when writing, reviewing, refactoring, or simplifying code to avoid over-engineering, make surgical changes, flatten complexity, and define verifiable success criteria.
---

# Clean Code Craft & Engineering Discipline

A unified discipline for writing clean, maintainable, and bug-free code. Combines Andrej Karpathy's mental models for avoiding LLM coding traps with battle-tested code simplification techniques.

---

## 1. THE FOUR CORE PILLARS (Karpathy Discipline)

### 1.A Think Before Coding
**Don't assume. Don't hide confusion. Surface tradeoffs.**
* State your assumptions explicitly before touching code. If uncertain, ask.
* If multiple valid interpretations exist, present them rather than silently guessing.
* If a simpler approach exists, propose it. Push back against speculative requirements when warranted.
* If something in the codebase is unclear, pause and clarify before making edits.

### 1.B Simplicity First
**Minimum code that solves the problem. Nothing speculative.**
* Build no features beyond what was requested.
* Never introduce single-use abstractions or premature frameworks.
* Avoid speculative "flexibility" or "configurability" that wasn't asked for.
* Do not write defensive error handling for mathematically impossible scenarios.
* *The Golden Rule*: "Would a senior engineer say this is overcomplicated?" If yes, rewrite it simply. If 200 lines can be expressed clearly in 50, rewrite it.

### 1.C Surgical Changes
**Touch only what you must. Clean up only your own mess.**
* When editing existing code, never arbitrarily "improve" adjacent formatting, comments, or unrelated modules.
* Match the existing repository style, even if you would personally format it differently.
* If you notice pre-existing dead code, mention it to the user rather than silently deleting it.
* Clean up your own orphans: remove imports, variables, or helpers that *your* changes made unused.
* *The Test*: Every modified line must trace directly back to the user's request.

### 1.D Goal-Driven Execution
**Define success criteria. Loop until verified.**
* Transform tasks into verifiable goals:
  * *"Add validation"* → Write tests for invalid inputs, then make them pass.
  * *"Fix the bug"* → Write a reproducing test case, then make it pass.
  * *"Refactor module"* → Ensure comprehensive test coverage passes before and after.
* For multi-step tasks, state a brief plan with verifiable checkpoints:
  ```markdown
  1. [Step A] → verify: [check]
  2. [Step B] → verify: [check]
  3. [Step C] → verify: [check]
  ```

---

## 2. THE FIVE REFACTORING PRINCIPLES

### 2.1 Preserve Behavior Exactly
Refactoring changes how code is expressed, not what it does.
* **Ask before every edit**:
  * Does this produce the identical output for all inputs?
  * Does this maintain identical error handling and thrown exceptions?
  * Does this preserve the same side-effect ordering?
  * Do all existing unit and integration tests still pass without modification?

### 2.2 Follow Project Conventions
Simplification aligns code with the existing codebase rather than imposing personal preferences.
* Study neighboring files for:
  * Import ordering and module resolution.
  * Function declaration styles (e.g., arrow functions vs. function statements).
  * Naming conventions and casing.
  * Error propagation patterns and type annotation density.

### 2.3 Prefer Clarity Over Cleverness
Explicit, easily parsed code is superior to dense, "clever" one-liners that require mental effort to untangle.

```typescript
// ❌ UNCLEAR: Dense nested ternary
const label = isNew ? 'New' : isUpdated ? 'Updated' : isArchived ? 'Archived' : 'Active';

// ✅ CLEAR: Readable guard structure
function getStatusLabel(item: Item): string {
  if (item.isNew) return 'New';
  if (item.isUpdated) return 'Updated';
  if (item.isArchived) return 'Archived';
  return 'Active';
}
```

```typescript
// ❌ UNCLEAR: Chained inline reduce
const counts = items.reduce((acc, item) => ({
  ...acc,
  [item.id]: (acc[item.id] || 0) + 1
}), {});

// ✅ CLEAR: Explicit, performant map
const counts = new Map<string, number>();
for (const item of items) {
  counts.set(item.id, (counts.get(item.id) ?? 0) + 1);
}
```

### 2.4 Maintain Balance (Avoid Over-Simplification)
* **Do not inline too aggressively**: Removing a helper function that provides a meaningful name makes the call site harder to read.
* **Do not merge unrelated functions**: Combining two simple, distinct functions into one multi-purpose utility creates complexity, not simplicity.
* **Do not optimize purely for line count**: Fewer lines is never the primary goal; faster human comprehension is.

### 2.5 Work Incrementally
Make small, verifiable changes. Run the test suite after each change. If an issue occurs, you immediately know which surgical edit caused it.

---

## 3. TACTICAL SIMPLIFICATION RECIPES

### 3.A Flatten Nested Control Flow (Early Returns)
Replace deeply nested `if/else` ladders with early returns (guard clauses) at the top of functions:

```typescript
// ❌ Deeply nested
function processUser(user: User | null) {
  if (user) {
    if (user.isActive) {
      if (user.hasSubscription) {
        return grantAccess(user);
      }
    }
  }
  return null;
}

// ✅ Flattened guard clauses
function processUser(user: User | null) {
  if (!user || !user.isActive || !user.hasSubscription) {
    return null;
  }
  return grantAccess(user);
}
```

### 3.B Eliminate Redundant State & Flag Variables
Avoid maintaining temporary flags when state can be derived directly:

```typescript
// ❌ Redundant tracking variable
let hasError = false;
if (value < 0) hasError = true;
if (hasError) throw new Error("Invalid");

// ✅ Direct evaluation
if (value < 0) {
  throw new Error("Invalid");
}
```

### 3.C Split Long Functions at Natural Boundaries
When a function handles multiple phases (parsing, validating, transforming, storing), break it into well-named private helper functions that read like a table of contents.

---

## 4. WHEN TO APPLY

* **Apply when**:
  * Writing new business logic or reviewing pull requests.
  * A feature is working and tested, but the implementation feels heavier than necessary.
  * Reviewing code with high cyclomatic complexity, deeply nested logic, or unclear variable naming.
* **Do NOT apply when**:
  * Code is already clean and readable.
  * You do not yet understand the full domain logic of the code.
  * The code is in an ultra-hot performance loop where micro-optimizations dictate the structure.

