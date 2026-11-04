# Antigravity Developer Configuration & Skills

Personal curated configuration for **Google Antigravity** and **Gemini CLI** on Windows.

## 🛠️ Active Standalone Skills (15)

All 15 standalone skills are 100% orthogonal, zero-overlap, and optimized for native Windows & Google Antigravity execution:

1. **`master-frontend-ux`**: Unified master frontend design & UX engineering engine (3 dials, 21 hallmark macrostructures, 50+ themes, 10 aesthetic presets, offline BM25 search for 192 palettes & 74 fonts, sloplint linter, anti-slop rules, pre-flight gate).
2. **`clean-code-craft`**: Unified code quality & simplification discipline (Karpathy's 4 core mental models, behavioral preservation, guard clauses, clarity over cleverness, refactoring principles).
3. **`git-workflow`**: End-to-end Git release management (Conventional Commits 1.0.0, atomic commit scopes, reviewer-friendly PR summaries with diff inspection).
4. **`security-and-hardening`**: Application security, OWASP top 10, untrusted input sanitization, and vulnerability mitigation.
5. **`performance-optimization`**: Frontend, query, N+1 pattern fixes, database, and Core Web Vitals optimization.
6. **`webapp-testing`**: Headless Chromium end-to-end testing via Playwright.
7. **`docx`**: Programmatic creation, editing, XML manipulation, and table formatting for Microsoft Word (.docx/.dotx) documents.
8. **`xlsx`**: Programmatic creation, formula modeling, formatting, and data analysis for Microsoft Excel (.xlsx/.xlsm) spreadsheets with openpyxl and pandas.
9. **`pptx`**: Programmatic creation, template cloning, shape styling, and layout management for PowerPoint (.pptx/.potx) presentations with pptxgenjs.
10. **`pdf`**: PDF extraction, tables, forms, annotations, page splitting/merging, and OCR inspection.
11. **`planning-with-files`**: Persistent file-based task planning (`task_plan.md`, `progress.md`, `findings.md`) with native PowerShell tooling.
12. **`graphify`**: Codebase AST knowledge graph generation with Tree-sitter parsers, community detection, and architectural queries.
13. **`agent-skills-builder`**: End-to-end AI agent skill lifecycle engine (Skill Seekers scraping/packaging + skill validation, description optimization, and repair).
14. **`mcp-builder`**: FastMCP / TypeScript MCP server architecture (includes v1 and v2 `@modelcontextprotocol/sdk` specifications).
15. **`managing-python-dependencies`**: Virtual environments and dependency isolation (uv, pip, venv).

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

2. **Install the runtime packages**:
   ```powershell
   python -m pip install playwright graphifyy openpyxl pandas
   python -m playwright install chromium
   ```

3. **Restart Antigravity / IDE**. All your skills, plugins, and settings will load instantly!
