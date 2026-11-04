# Antigravity Developer Configuration & Skills

Personal curated configuration for **Google Antigravity** and **Gemini CLI**.

## 🛠️ Active Standalone Skills (16)
- **`master-frontend-ux`**: Unified master frontend design & UX engineering engine (3 dials, 21 hallmark macrostructures, offline BM25 search for 192 palettes & 74 fonts, sloplint linter, anti-slop rules, pre-flight gate).
- **`karpathy-guidelines`**: Behavioral guidelines to reduce common LLM coding mistakes (Think before coding, Simplicity first, Surgical changes, Goal-driven execution).
- **`planning-with-files`**: Persistent disk-based task planning (`task_plan.md`, `progress.md`, `findings.md`).
- **`graphify`**: Codebase AST knowledge graph generation with Tree-sitter parsers.
- **`webapp-testing`**: Headless Chromium end-to-end testing via Playwright.
- **`code-simplification`**: Code refactoring for maximum clarity and maintainability.
- **`security-and-hardening`**: Application security, OWASP top 10, and vulnerability mitigation.
- **`performance-optimization`**: Frontend, query, and web vitals optimization.
- **`conventional-commits`**: Standardized Conventional Commits generator.
- **`pr-description`**: Reviewer-friendly pull request descriptions from git diffs.
- **`web-artifacts-builder`**: Interactive React, Tailwind, and shadcn component builder.
- **`mcp-builder`**: FastMCP / TypeScript MCP server architecture.
- **`managing-python-dependencies`**: Virtual environments and dependency isolation.
- **`skill-seekers`**: Scraper and generator for turning docs/repos into agent skills.
- **`skill-repair`**: Skill diagnostics and manifest repair.
- **`pdf`**: PDF extraction, tables, and architectural specification inspection.

## 📦 Active Plugins (14)
- **`superpowers`**: 15 engineering skills (TDD, systematic debugging, brainstorming, worktrees, plan execution).
- **`stitch-build`**, **`stitch-design`**, **`stitch-utilities`**: Google Stitch design-to-code suite (React, React Native, shadcn/ui, design tokens).
- **`chrome-devtools-plugin`**: DevTools browser inspection, a11y, memory profiling, and network audits.
- **`cloudflare`**: Wrangler, Next.js on Workers, Durable Objects, Turnstile, and Agents SDK.
- **`firebase`**: Firestore, App Hosting, Cloud Functions, and Security Rules.
- **`flutter`**: Full Dart/Flutter mobile application development suite.
- **`android-cli-plugin`**: Native Android SDK CLI integration.
- **`modern-web-guidance-plugin`**: Modern web standards, Chrome extensions, and browser APIs.
- **`gemini-api`**: Gemini API & Gemini Live bidirectional streaming SDKs.
- **`google-cloud-developer`**: Google Cloud Platform gcloud CLI and ADC authentication.
- **`google-antigravity-sdk`**: Antigravity agent SDK orchestration.
- **`google_maps_platform`**: Maps Platform APIs, geocoding, and routing.

---

## 🚀 How to Restore on a New PC

When setting up Antigravity on a new computer:

1. **Clone this repository into your user config folder**:
   ```powershell
   git clone https://github.com/SFRREX/antigravity-config.git $HOME\.gemini\config
   ```

2. **Install the two runtime packages**:
   ```powershell
   python -m pip install playwright graphifyy
   python -m playwright install chromium
   ```

3. **Restart Antigravity / IDE**. All your skills, plugins, and settings will load instantly!
