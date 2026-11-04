# 🚀 Antigravity Intelligent Agent Operating System (IAOS)

[![Platform](https://img.shields.io/badge/Platform-Google%20Antigravity%20%7C%20Gemini%20CLI-blue.svg)](https://antigravity.google)
[![OS](https://img.shields.io/badge/OS-Windows%20%28PowerShell%20First%29-0078D6.svg)](#-environment-requirements)
[![Skills](https://img.shields.io/badge/Skills-12%20Orthogonal%20Master%20Skills-brightgreen.svg)](#-the-12-master-skills)
[![Verification](https://img.shields.io/badge/CLI%20Tests-42%2F42%20Passed-success.svg)](#-verification--system-health)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Production-grade developer configuration, behavioral guardrails, and master skills architecture for **Google Antigravity** and the **Gemini CLI** on Windows.

Designed for high-agency software engineering, autonomous debugging, full-stack web development, document processing, and verifiable task completion with zero context drift and minimal token waste.

---

## 🌟 Highlights

- **⚡ 12 Orthogonal Master Skills**: Zero overlap, zero sibling hijacking. Every domain (frontend UI, clean refactoring, Office/PDF documents, Git, security, performance, browser testing, planning, AST knowledge graphs, MCP) is covered by a dedicated, tested master skill.
- **🛡️ Evidence Before Assertions**: Hardened with a mandatory **6-Step Verification Ladder**. The agent is strictly prohibited from claiming code is completed, fixed, or passing without executing tests, inspecting exit code 0, and confirming files exist on disk.
- **🪟 100% Windows PowerShell Native**: Built specifically for Windows hosts. No broken Linux bashisms (`grep`, `cat`, `sed`, `export FOO=bar`), pure-Python fallback renderers (`pypdfium2`), native LibreOffice path detection, and UTF-8 console crash prevention.
- **🧠 Context Engineering & Token Economy**: Cuts token bloat by 50%–70% using bounded line reading (`StartLine`/`EndLine`), PowerShell filtered CLI streams (`Select-Object -First 30`), externalized disk planning (`task_plan.md`), and subagent context shielding.
- **🎨 Anti-Slop UI/UX Standards**: Prohibits generic AI templates, placeholder text, and unstyled buttons. Enforces curated palettes (192 product schemes), font pairings (74 typographic scales), and strict WCAG 4.5:1 accessible contrast.
- **🤖 Mandatory Autonomous Skill Routing**: The agent automatically identifies, announces, and invokes the appropriate master skill based on intent—no manual slash commands required.

---

## ⚡ Quick Start (1-Minute Setup)

### 1. Clone into your global Antigravity config directory
Open **PowerShell** and clone this repository into your user profile's Gemini configuration directory:

```powershell
git clone https://github.com/SFRREX/antigravity-config.git "$HOME\.gemini\config"
```

### 2. Install runtime dependencies
Install the required Python libraries for document processing, AST graph generation, and browser testing:

```powershell
python -m pip install playwright graphifyy openpyxl pandas pypdf pdfplumber reportlab pypdfium2 lxml mcp
python -m playwright install chromium
```

### 3. Restart Antigravity / Gemini CLI
Launch or restart **Antigravity** or the **Gemini CLI**. The system will automatically detect the global rules in `GEMINI.md` and index all 12 master skills at Turn 0!

---

## 🛠️ The 12 Master Skills

Every skill is structured with progressive disclosure (lightweight intent frontmatter at Turn 0, deep manuals in `references/`, and executable CLI tools in `scripts/`):

| # | Master Skill | Core Domain & Capability | Automatic Trigger Conditions | Key Scripts / Tools |
| :---: | :--- | :--- | :--- | :--- |
| **1** | [`master-frontend-ux`](skills/master-frontend-ux/SKILL.md) | Full-stack UI/UX engineering, 50+ aesthetic themes, 192 product palettes, 74 font pairings, sloplint pre-flight gate. | Building or redesigning web UIs, React/Vue/HTML/CSS, landing pages, responsive styling, color palettes. | `validate_data.py`<br>`search.py`<br>`core.py` |
| **2** | [`clean-code-craft`](skills/clean-code-craft/SKILL.md) | Andrej Karpathy clean code discipline, surgical minimal diffs, cognitive load reduction, behavioral preservation. | Code reviews, refactoring, simplifying complex logic, removing dead code, flattening complexity. | Reference guides |
| **3** | [`document-master`](skills/document-master/SKILL.md) | Word (`.docx`), Excel (`.xlsx`), PowerPoint (`.pptx`), and PDF forms, OCR, table extraction, and headless LibreOffice conversion. | Generating, editing, calculating, or converting documents, spreadsheets, presentations, or PDF files. | `recalc.py`<br>`soffice.py`<br>`convert_pdf_to_images.py` |
| **4** | [`git-workflow`](skills/git-workflow/SKILL.md) | Conventional Commits 1.0.0, atomic commit scopes, reviewer-friendly PR descriptions with branch diff inspection. | Staging changes, creating commits, writing PR descriptions, changelogs, summarizing diffs. | Reference guides |
| **5** | [`security-and-hardening`](skills/security-and-hardening/SKILL.md) | OWASP Top 10 mitigation, untrusted input sanitization, JWT/auth flows, secret leak prevention, SQLi/XSS defense. | Auditing security, creating auth endpoints, handling user uploads, reviewing external dependencies. | Hardening patterns |
| **6** | [`performance-optimization`](skills/performance-optimization/SKILL.md) | Database query profiling, N+1 pattern elimination, bundle size reduction, Core Web Vitals (LCP, CLS, INP). | Optimizing slow queries, memory leaks, high latency, page load performance, database indexing. | Optimization patterns |
| **7** | [`webapp-testing`](skills/webapp-testing/SKILL.md) | Headless Chromium automated end-to-end testing, UI interaction verification, screenshot capture via Playwright. | Running E2E tests, verifying UI behavior in the browser, testing web applications, capturing console logs. | `with_server.py`<br>Playwright harness |
| **8** | [`planning-with-files`](skills/planning-with-files/SKILL.md) | Persistent on-disk task planning (`task_plan.md`, `progress.md`, `findings.md`) with native PowerShell automation. | Complex tasks requiring 3+ steps or multi-file changes, long research runs, resumable sessions. | `init-session.ps1`<br>`check-complete.ps1`<br>`session-catchup.py` |
| **9** | [`graphify`](skills/graphify/SKILL.md) | Codebase knowledge graphs, Tree-sitter AST parsing, community detection, architecture queries. | Exploring new codebases, mapping dependencies, structural questions, architecture analysis. | Tree-sitter AST engine |
| **10** | [`agent-skills-builder`](skills/agent-skills-builder/SKILL.md) | End-to-end AI agent skill lifecycle engine: scraping, packaging, validating, testing, repairing agent skills. | Authoring new skills, benchmarking skills, validating manifests, optimizing YAML descriptions. | `package_skill.py`<br>`quick_validate.py`<br>`improve_description.py` |
| **11** | [`mcp-builder`](skills/mcp-builder/SKILL.md) | Model Context Protocol server development in Python (FastMCP) and TypeScript (MCP SDK), tool schemas, connections. | Building MCP servers, exposing tools to LLMs, configuring stdio/HTTP transports. | `connections.py`<br>`evaluation.py` |
| **12** | [`managing-python-dependencies`](skills/managing-python-dependencies/SKILL.md) | Virtual environment isolation (`venv`, `uv`), deterministic lockfiles, package conflict resolution. | Setting up Python projects, managing dependencies, fixing pip conflicts, virtual environment management. | uv / venv workflows |

---

## 🧠 The Intelligent Agent Operating System (IAOS)

All agent actions, reasoning, and tool calls are governed by global rules in [`GEMINI.md`](GEMINI.md) and [`AGENTS.md`](AGENTS.md), based on the [Production AI Agent Engineering & Optimization Guide](docs/AGENT_ENGINEERING_OPTIMIZATION_GUIDE.md):

```
[User Prompt]
      │
      ▼
1. PRE-FLIGHT ANALYSIS ──► Determine true objective, deliverables, and constraints.
      │
      ▼
2. ADAPTIVE REASONING  ──► FAST (routine), BALANCED (coding), DEEP (complex bugs/architecture).
      │
      ▼
3. AUTO SKILL ROUTING  ──► Proactively activate the matching Master Skill from the catalog.
      │
      ▼
4. BOUNDED EXECUTION   ──► PowerShell-first, bounded line reads, filtered logs, UTF-8 stdio.
      │
      ▼
5. VERIFICATION LADDER ──► Mandatory Level 1-6 verification before declaring completion.
      │
      ▼
6. MINIMALIST HANDOFF  ──► Concise direct summary; extensive technical reports in artifacts.
```

### The 6-Step Verification Ladder
```
[Level 6] Explicit Confirmation (for Level 3 irreversible actions)
    ▲
[Level 5] Independent Review (syntax & logic verification against requirements)
    ▲
[Level 4] Integration / Live State Confirmation (dev server / CLI invocation)
    ▲
[Level 3] Targeted Unit & Regression Tests (execute test suites, inspect exit code 0)
    ▲
[Level 2] Deterministic Invariants & Assertions (file exists on disk, correct schema)
    ▲
[Level 1] Syntax & Type Validation (linting, compiler checks, parser verification)
```

---

## 📦 Active Plugins Ecosystem (14)

In addition to the 12 master skills, the configuration registers and manages 14 production plugins:

- **`superpowers`**: 15 engineering sub-skills (TDD, systematic debugging, brainstorming, worktree management, plan execution).
- **`stitch-build`**, **`stitch-design`**, **`stitch-utilities`**: Google Stitch design-to-code suite (React, React Native, shadcn/ui, design tokens).
- **`chrome-devtools-plugin`**: Live Chrome DevTools browser inspection, a11y auditing, memory profiling, and network inspection.
- **`cloudflare`**: Cloudflare Workers, Wrangler, Durable Objects, Turnstile, and Agents SDK.
- **`firebase`**: Firestore, App Hosting, Cloud Functions, and Security Rules authoring.
- **`flutter`**: Full Dart/Flutter cross-platform mobile suite (unit tests, layouts, widget previews).
- **`android-cli-plugin`**: Native Android SDK CLI integration and Compose previews.
- **`modern-web-guidance-plugin`**: Web standards, Chrome extensions, and browser APIs.
- **`gemini-api`**: Gemini API & Gemini Live bidirectional streaming SDKs.
- **`google-cloud-developer`**: Google Cloud Platform `gcloud` CLI and Application Default Credentials (ADC).
- **`google-antigravity-sdk`**: Programmatic Antigravity agent leasing and orchestration.
- **`google_maps_platform`**: Google Maps APIs, geocoding, and routing.

---

## 📁 Repository Structure

```
antigravity-config/
├── GEMINI.md                                  # Global Antigravity behavioral rules (100% inlined)
├── AGENTS.md                                  # Project & repository mirror rules
├── README.md                                  # Public documentation and quick-start guide
├── config.json                                # Antigravity plugin and user settings (Turbo mode)
├── mcp_config.json                            # Model Context Protocol server configuration
├── docs/
│   └── AGENT_ENGINEERING_OPTIMIZATION_GUIDE.md # Production AI Agent Architecture Manual
├── plugins/                                   # 14 active plugins & extensions
└── skills/                                    # 12 consolidated master skills
    ├── master-frontend-ux/                    # UI/UX engineering, 50+ themes, palettes, sloplint
    ├── clean-code-craft/                      # Karpathy clean code minimalism & refactoring
    ├── document-master/                       # Word, Excel, PowerPoint, and PDF engine
    ├── git-workflow/                          # Conventional Commits 1.0.0 & PR generator
    ├── security-and-hardening/                # OWASP Top 10 & input sanitization
    ├── performance-optimization/              # Query, bundle, and Core Web Vitals tuning
    ├── webapp-testing/                        # Playwright automated browser test suite
    ├── planning-with-files/                   # Task planning & PowerShell lifecycle automation
    ├── graphify/                              # Codebase AST knowledge graph generator
    ├── agent-skills-builder/                  # Skill lifecycle, scraping, and benchmarking
    ├── mcp-builder/                           # FastMCP & TypeScript MCP server development
    └── managing-python-dependencies/          # Virtual environment management (uv, venv)
```

---

## 💻 Environment Requirements

- **Operating System:** Windows 10/11 (or Linux/macOS with equivalent shell configuration)
- **Shell:** PowerShell 5.1 or PowerShell 7+
- **Python:** Python 3.10+ (configured on PATH)
- **Node.js:** Node.js 18+ (for frontend linters and TypeScript MCP servers)
- **Git:** Git 2.30+

---

## 🤝 Contributing

Contributions, additional domain skills, and enhancements to the Intelligent Agent Operating System are welcome!

1. Fork this repository.
2. Create your feature branch (`git checkout -b feat/new-master-skill`).
3. Ensure all scripts exit cleanly with code `0` on `--help`.
4. Commit your changes with Conventional Commits (`git commit -m 'feat(skills): add docker-orchestration'`).
5. Push to the branch (`git push origin feat/new-master-skill`).
6. Open a Pull Request.

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE). Built for the global developer community using Google Antigravity and Gemini.
