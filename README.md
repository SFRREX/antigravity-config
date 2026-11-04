# Antigravity Developer Configuration & Skills

Personal curated configuration for **Google Antigravity** and **Gemini CLI**.

## 🛠️ Active Standalone Skills (13)
- **`master-frontend-ux`**: Unified master frontend design & UX engineering engine (3 dials, 21 hallmark macrostructures, offline BM25 search for 192 palettes & 74 fonts, sloplint linter, anti-slop rules, pre-flight gate).
- **`clean-code-craft`**: Unified code quality & simplification discipline (Karpathy's 4 core mental models, behavioral preservation, guard clauses, clarity over cleverness).
- **`git-workflow`**: End-to-end Git release management (Conventional Commits 1.0.0, atomic commit scopes, reviewer-friendly PR summaries with diff inspection).
- **`security-and-hardening`**: Application security, OWASP top 10, untrusted input sanitization, and vulnerability mitigation.
- **`performance-optimization`**: Frontend, query, N+1 pattern fixes, database, and Core Web Vitals optimization.
- **`webapp-testing`**: Headless Chromium end-to-end testing via Playwright.
- **`planning-with-files`**: Persistent disk-based task planning (`task_plan.md`, `progress.md`, `findings.md`).
- **`graphify`**: Codebase AST knowledge graph generation with Tree-sitter parsers.
- **`agent-skills-builder`**: End-to-end AI agent skill lifecycle engine (Skill Seekers scraping/packaging + skill repair & manifest diagnostics).
- **`mcp-builder`**: FastMCP / TypeScript MCP server architecture.
- **`managing-python-dependencies`**: Virtual environments and dependency isolation.
- **`web-artifacts-builder`**: Interactive React, Tailwind, and shadcn component builder.
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
