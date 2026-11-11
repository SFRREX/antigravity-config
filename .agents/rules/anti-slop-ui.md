---
trigger: model_decision
description: Enforces production-grade anti-slop UI/UX standards, curated palettes, typography pairings, and accessible contrast when designing or modifying HTML, CSS, React, Vue, or Tailwind interfaces.
---

# Anti-Slop UI/UX Design Standards

When generating or editing user interfaces, web applications, landing pages, or components:

## 1. Eliminate Generic AI Templates
- **No Default Purple Gradients**: Avoid pure `#FFFFFF` backgrounds paired with generic purple gradient buttons and standard Inter font.
- **Calibrated Color Harmony**: Follow the 60-30-10 rule:
  - 60% dominant canvas / surface tone
  - 30% structural / secondary tone
  - 10% purposeful brand accent
- **Contrast Ratios**: Enforce minimum WCAG AA 4.5:1 contrast for all text and 3:1 for graphical UI controls.

## 2. Characterful Typography
- Pair an expressive display font for headlines (e.g. Syne, Outfit, Space Grotesk, Bricolage Grotesque) with a clean, readable body font (e.g. Plus Jakarta Sans, Inter, Geist).
- Never use more than 2 distinct font families per interface.

## 3. Real Content Over Dummy Placeholders
- Never use "Lorem Ipsum", "Card Title", "Feature 1", or "Button 1". Use realistic, domain-specific text, metrics, and labels.

## 4. Interaction & Accessibility Invariants
- All interactive elements must have visible focus rings (`focus-visible:ring-2`).
- Icon-only buttons must have an `aria-label`.
- Form inputs must have associated labels and descriptive validation messages.

