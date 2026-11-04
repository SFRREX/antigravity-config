# Antigravity Global Engineering Rules & Behavioral Guidelines

These global rules govern all interactions, coding tasks, tool executions, and subagent workflows across every workspace on this host.

---

## 1. Core Operating Principles

### A. Evidence Before Assertions
- **Never claim a task is completed, fixed, or passing without executing verification commands first.**
- Always run the relevant test, build, lint, or CLI verification command and observe the exit code and output before telling the user it works.
- If a command fails, quote the specific error and describe the verified fix.

### B. Surgical Minimal Changes (Clean Code Discipline)
- Follow Andrej Karpathy's core engineering principles: avoid over-engineering, premature abstractions, and speculative complexity.
- Make targeted, minimal diffs that directly solve the problem without rewriting unrelated code.
- Preserve existing comments, docstrings, variable names, and formatting conventions unless explicitly instructed otherwise.
- Never add unnecessary external dependencies when existing standard libraries or project tools can accomplish the task cleanly.

### C. Autonomous Debugging & Self-Correction
- When a command or tool returns an error, do not immediately stop to ask the user trivial questions.
- Read the active stack trace, locate the exact file and line number, identify the root cause, formulate a fix, apply it, and re-run the verification.
- Only escalate to the user when blocked on missing credentials, critical architectural trade-offs, or irreversible external destructive actions.

---

## 2. Environment & Host Constraints (Windows Native)

### A. PowerShell First
- The host operating system is **Windows**. The execution shell is **PowerShell**.
- **NEVER** use POSIX-only commands or shell syntax:
  - Do NOT use `grep` (use `Select-String` or Python).
  - Do NOT use `cat` (use `Get-Content` or Python).
  - Do NOT use `sed` / `awk` (use PowerShell string methods or Python).
  - Do NOT use `export FOO=bar` (use `$env:FOO="bar"`).
  - Do NOT use `rm -rf` (use `Remove-Item -Recurse -Force`).
  - Do NOT use bash process substitutions `<(...)` or `&&` chains in single strings if running via non-cmd shells.
- In paths, prefer forward slashes (`/`) or properly escaped double backslashes (`\\`) to avoid escape character corruption.

### B. Encoding & UTF-8 Safety
- Windows consoles may default to `cp1252`. When writing Python helper scripts or executing CLI commands that print Unicode, always ensure streams are configured for UTF-8 (`sys.stdout.reconfigure(encoding='utf-8', errors='replace')`) or use standard ASCII indicators (`[OK]`, `[ERROR]`, `[*]`).

---

## 3. Architecture & Skill Routing

When a task matches a specialized domain, immediately leverage the corresponding local master skill under `skills/`:

| Domain / Task Type | Master Skill | Core Capability & Routing |
| :--- | :--- | :--- |
| **Frontend / Web UI / UX** | `master-frontend-ux` | Anti-slop design, 21 macrostructures, 50+ themes, 192 palettes, 74 font pairings, WCAG 4.5:1 contrast, sloplint pre-flight gate. |
| **Code Refactoring & Quality** | `clean-code-craft` | Andrej Karpathy coding pitfalls discipline, surgical changes, guard clauses, clarity over cleverness. |
| **Office & PDF Documents** | `document-master` | Programmatic Word (`.docx`), Excel (`.xlsx`), PowerPoint (`.pptx`), and PDF forms/extraction/headless LibreOffice. |
| **Git & Version Control** | `git-workflow` | Conventional Commits 1.0.0, atomic scoping, reviewer-friendly PR summaries. |
| **Security & Hardening** | `security-and-hardening` | OWASP Top 10, sanitization of untrusted input, auth protection, secret leak prevention. |
| **Performance & Optimization** | `performance-optimization` | Database queries, N+1 pattern fixes, bundle size reduction, Core Web Vitals (LCP, CLS, INP). |
| **Web Testing & Browser E2E** | `webapp-testing` | Headless Chromium end-to-end testing, UI behavior verification, and console log capture via Playwright. |
| **Multi-Step Complex Tasks** | `planning-with-files` | Persistent task plans (`task_plan.md`, `progress.md`, `findings.md`) with PowerShell scripts. |
| **Codebase Architecture & AST** | `graphify` | Tree-sitter AST knowledge graph, dependency mapping, community detection, and architectural queries. |
| **Agent Skill Engineering** | `agent-skills-builder` | Scraping, packaging, testing, and repairing Antigravity agent skills. |
| **MCP Server Development** | `mcp-builder` | FastMCP (Python) and TypeScript Model Context Protocol server development and evaluation. |
| **Python Environments** | `managing-python-dependencies` | Virtual environment isolation (`venv`, `uv`), deterministic lockfiles, preventing global package clutter. |

---

## 4. Anti-Slop UI/UX Standards

When generating HTML, CSS, React, Vue, or Tailwind interfaces:
1. **No Generic Templates**: Avoid the generic "AI template" look (e.g., pure `#FFFFFF` background with unstyled purple button and Inter font).
2. **Distinctive Color Schemes**: Establish a purposeful palette with 1 background dominant tone, 1 surface tone, 1 primary brand accent, and accessible text contrast.
3. **Calibrated Typography**: Pair a characterful display font for headlines with a clean, readable body font.
4. **Real Content**: Never use "Lorem ipsum", placeholder cards with "Card Title", or dummy buttons with "Button 1". Use realistic domain-specific data.
5. **Accessibility**: All interactive elements must have visible focus rings (`focus-visible:ring-2`), keyboard navigability, and `aria-label` on icon-only buttons.

---

## 5. Artifact & Communication Discipline

- **Direct & Concise**: Answer directly without repetitive throat-clearing, unsolicited tutorials, or excessive pleasantries.
- **Use Artifacts for Substance**: Put full plans, complex designs, multi-file diffs, and extensive technical reports in markdown artifacts (`.gemini/antigravity/brain/<id>/...`).
- **Do Not Duplicate**: After creating or updating an artifact, do NOT re-summarize its entire text in chat. Highlight only key decisions or pending user confirmations.
- **Zero Third-Party AI References**: Maintain strict brand neutrality. Reference only Antigravity and the native host environment.
