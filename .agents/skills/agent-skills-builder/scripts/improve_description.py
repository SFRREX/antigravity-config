#!/usr/bin/env python3
"""Improve and optimize an agent skill description.

Analyzes a skill's description against agent best practices:
- Length constraints (max 1024 chars, ideal 150-400 chars)
- Trigger phrasing ("Use this skill when...", "Triggers on...")
- Negative boundaries ("Do NOT use when...")
- Symbol safety (no raw angle brackets)
- Keyword alignment with skill capabilities

Outputs a structured diagnostic report and provides concrete recommendations
or an agent-ready prompt for LLM-assisted refinement.
"""

import argparse
import os
import re
import sys
from pathlib import Path

# Add parent directory to path so scripts.utils can be imported
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.utils import parse_skill_md


def analyze_description(name: str, desc: str, full_content: str) -> dict:
    """Analyze the trigger description and return score and diagnostics."""
    issues = []
    strengths = []
    recommendations = []

    # 1. Length check
    length = len(desc)
    if length == 0:
        issues.append("Description is empty.")
    elif length > 1024:
        issues.append(f"Description exceeds maximum 1024 characters ({length} chars).")
    elif length < 50:
        issues.append(f"Description is too short ({length} chars). May fail to trigger.")
    else:
        strengths.append(f"Description length is within bounds ({length} chars).")

    # 2. Angle brackets
    if "<" in desc or ">" in desc:
        issues.append("Description contains angle brackets ('<' or '>'), which may break XML/HTML parsers.")

    # 3. Action / Trigger guidance
    has_trigger = bool(re.search(r'\b(use this skill|trigger|when|covers|provides|handles)\b', desc, re.I))
    if has_trigger:
        strengths.append("Contains explicit trigger and usage verbs.")
    else:
        issues.append("Missing explicit trigger phrasing (e.g. 'Use this skill when...').")

    # 4. Negative trigger / Boundaries
    has_boundaries = bool(re.search(r'\b(do not use|don\'t use|exclude|not for)\b', desc, re.I))
    if has_boundaries:
        strengths.append("Defines negative boundaries to prevent false activations.")
    else:
        recommendations.append("Consider adding negative boundary phrasing ('Do NOT use for...') to prevent false activations.")

    # 5. Extract keywords from body to check coverage
    headings = re.findall(r'^#{1,3}\s+(.+)$', full_content, re.M)
    heading_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', " ".join(headings).lower()))
    desc_words = set(re.findall(r'\b[a-zA-Z]{4,}\b', desc.lower()))
    overlap = heading_words.intersection(desc_words)

    if len(overlap) >= 3:
        strengths.append(f"Good keyword alignment with skill headings ({len(overlap)} matching concepts).")
    else:
        recommendations.append("Align description keywords with key sections in SKILL.md.")

    score = 100 - (len(issues) * 25) - (len(recommendations) * 10)
    score = max(0, min(100, score))

    return {
        "name": name,
        "score": score,
        "length": length,
        "issues": issues,
        "strengths": strengths,
        "recommendations": recommendations,
    }


def generate_llm_prompt(name: str, desc: str, full_content: str, diagnostics: dict) -> str:
    """Generate a prompt that an AI assistant can use to produce an improved description."""
    body_excerpt = "\n".join(full_content.split("\n")[:80])
    return f"""You are optimizing an agent skill description for "{name}".

Available Skills Context:
When an AI agent receives a prompt, it inspects available skill names and descriptions to decide whether to activate the skill. An optimal description must:
1. Clearly state what the skill does in the first sentence.
2. Provide explicit triggers ("Use this skill when...").
3. Include specific keywords, technologies, and file formats involved.
4. Specify negative boundaries ("Do NOT use when...") to avoid false positives.
5. Be strictly under 1024 characters (ideally 200-400 characters).
6. Contain NO angle brackets (< or >).

Current Description:
\"{desc}\"

Diagnostics:
- Current Length: {diagnostics['length']} characters
- Identified Issues: {', '.join(diagnostics['issues']) if diagnostics['issues'] else 'None'}
- Recommendations: {', '.join(diagnostics['recommendations']) if diagnostics['recommendations'] else 'None'}

Skill Content Excerpt:
{body_excerpt}

Task:
Write an improved, high-precision skill description that resolves all issues and maximizes triggering accuracy.
Output ONLY the optimized description enclosed in quotes.
"""


def main():
    parser = argparse.ArgumentParser(description="Analyze and improve agent skill description.")
    parser.add_argument("skill_dir", type=Path, help="Path to the skill directory")
    parser.add_argument("--prompt", action="store_true", help="Output LLM prompt for AI-assisted refinement")
    args = parser.parse_args()

    skill_dir = args.skill_dir.resolve()
    if not (skill_dir / "SKILL.md").exists():
        print(f"Error: {skill_dir}/SKILL.md not found.", file=sys.stderr)
        sys.exit(1)

    name, desc, full_content = parse_skill_md(skill_dir)
    diag = analyze_description(name, desc, full_content)

    print(f"\n=== Skill Description Analysis: {name} ===")
    print(f"Quality Score: {diag['score']}/100")
    print(f"Character Count: {diag['length']} / 1024 chars\n")

    if diag["strengths"]:
        print("[+] Strengths:")
        for s in diag["strengths"]:
            print(f"  - {s}")

    if diag["issues"]:
        print("\n[-] Issues to Fix:")
        for i in diag["issues"]:
            print(f"  - {i}")

    if diag["recommendations"]:
        print("\n[*] Recommendations:")
        for r in diag["recommendations"]:
            print(f"  - {r}")

    if args.prompt:
        print("\n=== Agent Optimization Prompt ===")
        print(generate_llm_prompt(name, desc, full_content, diag))


if __name__ == "__main__":
    main()
