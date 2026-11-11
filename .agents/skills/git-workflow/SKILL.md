---
name: git-workflow
description: "End-to-end Git release management: writes Conventional Commits 1.0.0 messages and generates reviewer-friendly PR descriptions from branch diffs. Use when staging/committing changes, writing commit messages, opening PRs, or summarizing branches for review."
---

# Git Delivery & Release Workflow

A unified skill for the complete Git commit and pull request delivery lifecycle: from atomic Conventional Commits to concise, reviewer-friendly PR summaries.

---

## 1. CONVENTIONAL COMMITS (1.0.0)

When creating or proposing a commit message, follow the Conventional Commits 1.0.0 specification.

### 1.A The Workflow
1. **Inspect Before Writing**: Always run `git diff --staged` (or `git diff` if unstaged). Never invent a commit message from memory.
2. **Select the Proper Type**:
   * `feat`: User-visible behavior or feature added
   * `fix`: User-visible bug resolved
   * `refactor`: Behavior-preserving code restructure (neither adds a feature nor fixes a bug)
   * `perf`: Performance improvement
   * `docs`: Documentation changes only
   * `test`: Adding or correcting tests
   * `build`: Build system or external dependency updates
   * `ci`: CI configuration files and scripts
   * `style`: Code style/formatting changes that do not affect meaning
   * `chore`: Routine maintenance tasks
   * `revert`: Reverting a previous commit (reference the reverted SHA)
3. **House Style & Scope**:
   * Inspect recent repository commits via `git log --oneline -20` to detect existing scope conventions.
   * Add a scope when applicable: `feat(auth): add OAuth2 refresh token handling`.
4. **Subject Line Formatting**:
   * Use the imperative mood ("add", not "added" or "adds").
   * Lowercase after the colon.
   * No trailing period.
   * Keep subject length ≤ 72 characters.
5. **Body & Footer**:
   * Body (optional): Explain the *why* and context, wrapped at 72 characters.
   * Footer: Mark breaking changes (`BREAKING CHANGE: <explanation>`) or link issues (`Closes #123`, `Fixes #456`).

### 1.B Commit Decision Tree
* **Mixed unrelated changes**: Propose splitting the diff into multiple focused commits instead of a single vague `chore` commit.
* **Unsure between `fix` and `refactor`**: Does an end-user observe a behavioral difference? If yes → `fix`; if no → `refactor`.
* **Done verification**:
  ```bash
  git log -1 --format=%s
  ```
  Matches `^(feat|fix|refactor|docs|test|build|ci|chore|style|perf|revert)(\(.+\))?!?: .+` and honestly reflects the diff.

---

## 2. PULL REQUEST DESCRIPTIONS

Produce a PR description that a busy reviewer can understand and act on in under a minute.

### 2.A The Workflow
1. **Collect the Change Surface**: Never write a PR description from memory. Run:
   ```bash
   git log main..HEAD --oneline
   git diff main...HEAD --stat
   ```
2. **Structure the Description**:
   * **What**: 1-2 sentences summarizing the user-visible outcome, not internal mechanics.
   * **Why**: The business problem, user request, or issue ticket this solves; link relevant issues.
   * **How**: Key non-obvious architecture decisions, trade-offs made, or rejected alternatives. (Skip tedious file-by-file tours; the diff already shows this).
   * **Testing**: Specific verification commands executed and their output results, not theoretical assumptions.
   * **Risk & Rollback**: Potential side effects, failure modes, and exact steps to revert if issues occur in production.
3. **Critical Callouts**:
   * Explicitly highlight high-risk changes: database migrations, security/auth modifications, API schema changes, or breaking deletions.

### 2.B PR Decision Tree
* **Diff > ~800 lines**: Prepend a "Review Order" section indicating which core files to inspect first.
* **Pure dependency upgrade**: Compress into **What** + changelog link + test execution evidence.
* **Breaking API change**: Place a prominent **BREAKING CHANGE** banner at the very top detailing migration steps.

---

## 3. SUMMARY TEMPLATE

When drafting a full PR description, use this standard format:

```markdown
## What
Brief summary of the user-visible change.

## Why
Resolves #<issue-number>. Context on why this change is necessary.

## Key Decisions & Trade-offs
- Technical highlight 1
- Key architectural choice 2

## Verification & Testing
- Command executed: `npm test` -> 42 passing
- Manual checks: Verified locally on Chrome and Firefox

## Risk & Rollback
- Risk Level: Low / Medium / High
- Rollback: Revert commit <SHA>
```
