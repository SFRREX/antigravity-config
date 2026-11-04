---
name: agent-skills-builder
description: "End-to-end AI agent skill lifecycle engine: converts documentation, repositories, PDFs, and codebases into structured skills via Skill Seekers, and diagnoses, fixes, and repairs broken skills and manifests. Use when creating, packaging, testing, or repairing agent skills."
---

# Agent Skills Builder & Repair Engine

A unified engine for the full AI agent skill lifecycle: scraping external documentation into ready-to-use skills, packaging them for LLM use, and diagnosing/repairing corrupted skill files or manifest entries.

---

## 1. BUILDING SKILLS FROM DOCUMENTATION & CODEBASES

Leverage the Skill Seekers MCP toolset (40 tools) to convert knowledge sources into structured skills:

### 1.A Source Type Detection Matrix
| Input Pattern | Knowledge Source | MCP Tool |
|---|---|---|
| `https://...` (docs website) | Documentation Site | `scrape_docs` |
| `owner/repo` or `github.com/...` | GitHub Repository | `scrape_github` |
| `*.pdf` | Technical Manual / PDF | `scrape_pdf` |
| YouTube/Vimeo link or video file | Video Tutorial / Transcript | `scrape_video` |
| Local folder path | Local Codebase | `scrape_codebase` |
| `*.ipynb`, `*.html`, `*.yaml` (OpenAPI) | Structured Specs | `scrape_generic` |

### 1.B Skill Creation Workflow
1. **Detect Source**: Identify whether the source is a URL, repository, PDF, or local code.
2. **Configure**: Use `generate_config` or `fetch_config` to establish crawling boundaries.
3. **Estimate**: Run `estimate_pages` for large documentation websites to avoid unbounded token consumption.
4. **Scrape & Structure**: Execute the appropriate `scrape_*` tool to extract API specs and code samples.
5. **Enhance**: Use `enhance_skill` to refine YAML frontmatter, remove noise, and add concise examples.
6. **Package**: Call `package_skill` to generate standard `SKILL.md` and resource directories.
7. **Vector Export (Optional)**: Export to vector databases (`export_to_weaviate`, `export_to_chroma`, `export_to_faiss`, `export_to_qdrant`) if requested.

---

## 2. SKILL REPAIR & MANIFEST DIAGNOSTICS

Use when a skill fails installation, has malformed frontmatter, or exhibits runtime errors:

### 2.A Diagnostic Procedure
1. **Analyze Error**: Review the specific failure output (e.g., YAML syntax error, missing frontmatter, broken scripts, or missing references).
2. **Inspect Full Skill Directory**:
   * Inspect `SKILL.md`: Verify YAML frontmatter starts on line 1 with `---`, has valid `name` and `description` keys, and contains no UTF-8 BOM (`\xef\xbb\xbf`).
   * Inspect Sub-directories: Check `scripts/` permissions and relative file paths in Python/Node scripts.
3. **Update Manifest**:
   * If a `manifest.json` or `.datacloud_skills_manifest` tracks the skill, locate the skill entry.
   * Update status:
     ```json
     {
       "skills": {
         "<skill-id>": {
           "status": "installed",
           "disabled": false,
           "error": null
         }
       }
     }
     ```
4. **Verify**: Ensure the skill directory is cleanly discovered and tested.
