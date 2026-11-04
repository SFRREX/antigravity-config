---
name: master-frontend-ux
description: "Unified master frontend design & UX engineering engine for web applications, landing pages, portfolios, and redesigns. Combines anti-slop design taste, 3 dials (variance, motion, density), 21 hallmark macrostructures, searchable local UI/UX databases (192 product palettes, 74 font pairings, 119 UX guidelines, 22 technology stacks), automated sloplint verification, and a strict pre-flight quality gate. Use when designing, building, reviewing, or refactoring user interfaces."
---

# Master Frontend & UX Design Engine

> Complete, non-redundant frontend intelligence: Landing pages, marketing websites, web applications, and portfolios.
> Every rule below is **contextual**. First infer the brief and read the room, then apply only what fits.

---

## 0. CORE PHILOSOPHY & ANTI-DEFAULT POSTURE

1. **Spend Boldness in One Place**: Let one signature element be the unforgettable moment (the hero asset, an interactive simulator, or bold typography). Keep everything else quiet, disciplined, and refined. As Coco Chanel advised: *before leaving the house, take a look in the mirror and remove one accessory.*
2. **Ground Designs in Subject Matter**: Authentic visual identities come from the subject's industry, materials, and vernacular. A fintech trading terminal differs radically from a toy store or an artisanal bakery. Never apply generic SaaS templates across different domains.
3. **Distinctiveness over Cliché**: AI-generated design tends to converge on specific defaults: cream backgrounds with terracotta accents, AI-purple button glows, tracked uppercase eyebrows on every header, and generic 3-card feature rows. Actively push past these defaults.

---

## 1. BRIEF INFERENCE & DISCOVERY (Read the Room)

Before writing any code or styles, infer what the project genuinely requires:

### 1.A The 4 Discovery Signals
1. **Material Inventory**:
   * *Real*: Screenshots of working code, actual brand assets, exact metrics, genuine customer quotes.
   * *Pictures*: Visual assets needed (use image generation tools or descriptive placeholder seeds; never fake screenshots with divs).
   * *Absent*: Facts or assets not supplied (never invent numbers, fake case studies, or mock testimonials).
2. **Audience**: Technical B2B buyers vs. consumer retail vs. design recruiters vs. regulated public-sector users.
3. **Primary Use**: The single conversion action the screen drives (e.g., subscribe, purchase, test live demo, sign up).
4. **Tone & Genre**:
   * **`modern-minimal`**: SaaS, developer tools, B2B platforms, enterprise APIs.
   * **`atmospheric`**: AI tools, creative studios, media, audio/video, dark tech.
   * **`editorial`**: High-end consumer, journalism, publishing, luxury, portfolio.
   * **`playful`**: Consumer social, education, kids, gaming, community apps.

### 1.B The Mandatory One-Line "Design Read"
Before generating code, declare your design read in one line:
> **"Reading this as: \<page kind> for \<audience>, with a \<vibe> language, leaning toward \<design system or aesthetic family>."**

*If ambiguous:* Ask **exactly one** clarifying question. If you can confidently deduce the intent from context, declare the read and proceed without interrupting.

---

## 2. THE THREE DIALS (Core Configuration)

Set three dials to govern layout asymmetry, interaction physics, and information density:

* **`DESIGN_VARIANCE: 8`** (1 = Symmetrical Grid, 10 = Asymmetric / Expressive)
* **`MOTION_INTENSITY: 6`** (1 = Completely Static, 10 = Kinetic / Spring Physics)
* **`VISUAL_DENSITY: 4`** (1 = Airy Art Gallery, 10 = Compact Cockpit / Data-Dense)

### Dial Presets by Use Case
| Category | VARIANCE | MOTION | DENSITY | Primary Rationale |
|---|---|---|---|---|
| Mainstream SaaS Landing | 7 | 6 | 4 | Clear hierarchy with subtle entrance reveals |
| Creative Agency / Portfolio | 9 | 8 | 3 | High asymmetry, kinetic type, expressive space |
| Luxury / Premium Consumer | 7 | 6 | 3 | Generous whitespace, restrained motion, rich imagery |
| Developer Portfolio | 6 | 5 | 4 | Clean typography, focused technical showcases |
| Editorial / Publication | 6 | 4 | 3 | Strong serif/sans contrast, article rhythm |
| Dashboard / Data App | 3 | 2 | 8-9 | Symmetrical grids, tight data spacing, zero fluff |
| Public Sector / Accessible | 3 | 2 | 5 | Utmost predictability, WCAG AAA contrast |
| Redesign (Preserve) | Match existing | +1 | Match existing | Modernize styling while preserving existing layout |
| Redesign (Overhaul) | +2 | +2 | Match existing | Fresh visual language over existing information architecture |

---

## 3. MACROSTRUCTURES & ANATOMY

Avoid default feature-card runs. Select a deliberate layout archetype from Hallmark's 21 macrostructures:

1. **Split-Screen Scroll**: 50/50 division; pinned media asset on one side, scrolling narrative on the other.
2. **Asymmetric Split Hero**: Strong headline + subtext on left, dominant product asset offset right.
3. **Editorial Manifesto**: Type-driven poster hero; oversized display headline, no immediate image clutter.
4. **Bento Grid**: Asymmetric, rhythmic tile grouping (mix of 1x1, 2x1, and 2x2 cells with visual variation).
5. **Sticky Scroll Stack**: Cards pin and physically scale/stack as the user scrolls vertically.
6. **Horizontal Pan**: Vertical scroll mapped to horizontal ribbon traverse via GSAP ScrollTrigger.
7. **Curtain Reveal**: Hero layer parts vertically on scroll to reveal underlying content.
8. **Index / Directory First**: Direct tabular or structured listing for catalogs and archives.

*Detailed macrostructure guides and templates live in `references/macrostructures.md`.*

---

## 4. LOCAL SEARCHABLE DESIGN INTELLIGENCE

Use the offline search tool to retrieve curated palettes, font pairings, chart specs, and stack guidance without guessing:

```bash
# Query product styles, palettes, fonts, or UX rules
python "C:\Users\Razedus Safar\.gemini\config\skills\master-frontend-ux\scripts\search.py" "<query>" --domain <domain>
```

### Supported Domains
* **`product`**: Product archetypes, recommended styles, and color directions (`saas`, `fintech`, `ecommerce`, `portfolio`).
* **`color`**: Complete 18-token semantic palettes (Primary, Secondary, Accent, Background, Card, Destructive).
* **`typography`**: Curated font pairings, mood fit, display/body roles, and recommended CSS scales.
* **`style`**: 79 searchable design styles (Glassmorphism, Bento, Brutalism, Swiss Minimal, Flat Design, etc.).
* **`ux`**: 119 WCAG-grounded UX guidelines with rationale and implementation checklists.
* **`icons`**: Curated Phosphor icon naming and semantic mapping.
* **`chart`**: Data visualization selection, threshold limits, and accessibility grades.
* **`stack`**: Stack-specific patterns across 22 technologies (`react`, `nextjs`, `vue`, `svelte`, `tailwind`, `flutter`).

---

## 5. DESIGN SYSTEM MAPPING

Always use official, maintained design systems when the brief calls for one:

| Brief Flavor | Recommended Foundation | Implementation Notes |
|---|---|---|
| Enterprise SaaS / Admin | `@fluentui/react-components` | Official Microsoft Fluent 2 tokens |
| Enterprise Analytics / B2B | `@carbon/react` + `@carbon/styles` | IBM Carbon data-dense patterns |
| Google / Android-flavored | `@material/web` | Material 3 web components |
| Shopify App Ecosystem | `@shopify/polaris` | Standard Polaris components |
| Developer / GitHub Style | `@primer/react-brand` | Official GitHub brand marketing kit |
| Public Sector (UK / US) | `govuk-frontend` / `uswds` | Legally mandated accessibility |
| Custom Modern React / SaaS | `shadcn/ui` + Tailwind v4 | Owned components; customize radii and tokens |
| Utility-First Web | Tailwind v4 + CSS variables | Modern standard; use `@tailwindcss/postcss` |

**Rule of Isolation:** Use exactly **one** design system per project tree. Never mix Fluent with Carbon or shadcn with Material 3.

---

## 6. TYPOGRAPHIC & SPATIAL ENGINEERING

### 6.A Typography Discipline
* **Body Line Length**: Default to `max-w-[65ch]` (never exceed 80 characters per line).
* **Sans-Serif Defaults**: Avoid plain `Inter` unless explicitly requested. Default to `Geist`, `Satoshi`, `Cabinet Grotesk`, or `Outfit`.
* **Serif Discipline**:
  * Serif is **strictly discouraged as a default**. Only use it when the brand is explicitly editorial, luxury, publication, or heritage.
  * Banned LLM defaults: `Fraunces` and `Instrument_Serif`. Rotate among `PP Editorial New`, `Tiempos Headline`, `Cormorant Garamond`, `Reckless Neue`, or `Playfair Display`.
* **Italic Descender Clearance**: When italic display type has descenders (`y, g, j, p, q`), enforce `leading-[1.1]` minimum and `pb-1` to prevent clipping.
* **Single-Family Emphasis**: Emphasize words using italic or bold of the **same font family**. Never inject an orphaned serif word into a sans headline.

### 6.B Spatial & Layout Hygiene
* **Viewport Stability**: Never use `h-screen` for hero sections. Always use `min-h-[100dvh]` to prevent mobile Safari address-bar jumps.
* **Horizontal Overflow**: Enforce `overflow-x: clip` on both `html` and `body` (never `hidden`, never `100vw`).
* **Image Grid Tracks**: Use `minmax(0, 1fr)` for responsive image tracks to prevent blowouts.
* **Display Head Wrapping**: Apply `overflow-wrap: break-word; min-width: 0` to all large headline containers.
* **Hero Top Padding Cap**: Max `pt-24` desktop padding. Hero headlines, subtext, and CTAs must be visible above the fold without scrolling at 1280x800.
* **Hero Stack Discipline**: Max 4 text elements: (1) Optional small eyebrow, (2) Headline (max 2 lines), (3) Subtext (max 20 words), (4) Action buttons (1 primary + max 1 secondary).

---

## 7. COLOR, MATERIALITY & ACCESSIBILITY

* **One Primary Accent**: Max 1 accent color with saturation < 80%. Never fluctuate between warm and cool neutrals on the same screen.
* **The Lila Rule**: No automatic neon purple/blue glowing buttons or generic AI mesh blobs. Use refined neutral bases (Zinc, Slate, Stone) with a high-contrast accent.
* **Banned Cliché Palettes**: For artisan/cookware/luxury goods, avoid the default warm cream (`#f5f1ea`) + brass/oxblood (`#b08947`) + espresso (`#1a1714`) combo. Reach instead for:
  * *Cold Luxury*: Silver-grey + brushed chrome + crisp smoke.
  * *Forest & Amber*: Deep emerald + bone + warm amber.
  * *Cobalt & Paper*: High-contrast cobalt blue on crisp neutral white.
* **Shape Consistency Lock**: Pick one corner-radius family and enforce it everywhere (e.g., all-sharp `rounded-none`, all-soft `rounded-xl`, or pill `rounded-full`). Never mix round buttons with square cards.
* **WCAG AA Compliance**:
  * Body text contrast ≥ 4.5:1; large headings ≥ 3:1.
  * Always verify button text contrast against button backgrounds (no white text on light buttons).
  * Visible `:focus-visible` rings on all interactive elements.

---

## 8. INTERACTION & MOTION ENGINEERING

* **Motivated Motion**: Every animation must communicate something real: hierarchy, narrative progression, action feedback, or state transition. Never add animation merely because it is possible.
* **Client Island Isolation**: Keep server components static. Isolate interactive animations in dedicated client leaf components with `'use client'`.
* **Reduced Motion (Mandatory)**: Always wrap motion in `useReducedMotion()` or `@media (prefers-reduced-motion: reduce)` fallbacks.
* **Spring Physics**: Use natural spring physics (`type: "spring", stiffness: 100, damping: 20`) instead of generic linear easing.
* **Never use `window.addEventListener('scroll')`**: Use Motion's `useScroll()` or GSAP `ScrollTrigger` with proper context cleanup.

### Canonical GSAP Sticky-Stack Skeleton
```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function StickyStack({ cards }: { cards: React.ReactNode[] }) {
  const ref = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !ref.current) return;
    const ctx = gsap.context(() => {
      const cardEls = gsap.utils.toArray<HTMLElement>(".stack-card");
      cardEls.forEach((card, i) => {
        if (i === cardEls.length - 1) return;
        ScrollTrigger.create({
          trigger: card,
          start: "top top",
          endTrigger: cardEls[cardEls.length - 1],
          end: "top top",
          pin: true,
          pinSpacing: false,
        });
        gsap.to(card, {
          scale: 0.92,
          opacity: 0.55,
          ease: "none",
          scrollTrigger: {
            trigger: cardEls[i + 1],
            start: "top bottom",
            end: "top top",
            scrub: true,
          },
        });
      });
    }, ref);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <div ref={ref} className="relative">
      {cards.map((card, i) => (
        <div key={i} className="stack-card sticky top-0 min-h-[100dvh] flex items-center justify-center">
          {card}
        </div>
      ))}
    </div>
  );
}
```

---

## 9. ANTI-SLOP DISCIPLINE & FORBIDDEN AI TELLS

* 🚫 **ZERO Em-Dashes (`—`) or En-Dashes (`–`) as Separators**: The #1 dead giveaway of LLM writing. Use hyphens (`-`), periods, commas, or clean line breaks.
* 🚫 **No Eyebrow Overload**: Max 1 uppercase tracked eyebrow per 3 page sections. Let headings speak for themselves.
* 🚫 **No Middle-Dot Chains**: Max 1 middle-dot (`·`) per metadata strip. Do not string together `A · B · C · D`.
* 🚫 **No Decorative Status Dots**: No green/colored circles before nav items or list rows unless reporting real server status.
* 🚫 **No Div-Based Fake Screenshots**: Do not build mock dashboards or terminals using `<div>` rectangles. Use real screenshots, generated imagery, or omit the preview.
* 🚫 **No Generic 3-Card Feature Rows**: Replace with asymmetric bentos, 2-column alternating layouts, or tabbed feature switches.
* 🚫 **No Duplicate CTA Intent**: Do not mix "Get in touch" and "Let's talk" on the same page. Pick one label and stick with it.
* 🚫 **No CTA Button Text Wrapping**: CTA buttons must fit on one line at desktop.

---

## 10. UX COPYWRITING & MICRO-COPY

* **Active Voice & User Centricity**: Label actions by what happens: "Create account", not "Submit"; "Save invoice", not "Process data".
* **One Verb Per Action**: If the deletion action is labeled "Delete", use "Delete" everywhere (never mix "Delete", "Remove", and "Trash" for the identical action).
* **Errors Don't Apologize**: Explain plainly what occurred and how to resolve it without conversational fluff ("Card expired. Enter a valid expiration date.").
* **Emptiness is an Invitation**: Empty states must direct users forward with clear CTAs rather than displaying blank containers.

---

## 11. REDESIGN & REFERENCE CODIFICATION

* **Preserve Mode vs. Overhaul Mode**:
  * *Preserve*: Maintain URL slugs, SEO meta tags, navigation structure, and brand colors; modernize typography, spacing, and micro-interactions.
  * *Overhaul*: Restructure visual design from scratch while keeping core information architecture stable.
* **Measure, Don't Describe**: When given an image or URL reference, extract literal values (exact hex colors, exact padding in px, aspect ratios, corner radii). Never rely on vague verbal descriptions like "clean and airy".
* **Falsifiable Rule Tests**: Turn reference findings into pass/fail tests (e.g., *"Is every section padding exactly 64px?"*).

---

## 12. MECHANICAL VERIFICATION (Sloplint Linter)

Run the built-in Hallmark linter on your markup before delivering to catch mechanical design slips:

```bash
# Run sloplint against the generated HTML/JSX
node "C:\Users\Razedus Safar\.gemini\config\skills\master-frontend-ux\scripts\sloplint.mjs" <path-to-file> --render
```

All `FAIL` items must be fixed before the task is complete.

---

## 13. FINAL PRE-FLIGHT QUALITY CHECKLIST

Verify every item before declaring work finished:

- [ ] **Design Read Declared**: One-line brief read stated before code?
- [ ] **Three Dials Set**: `VARIANCE`, `MOTION`, and `DENSITY` explicitly reasoned?
- [ ] **Zero Em-Dashes**: No `—` or `–` anywhere in visible copy, headlines, buttons, or alt text?
- [ ] **Theme Lock**: Single unified theme (light or dark) across all page sections?
- [ ] **Hero Fits Initial Viewport**: Headline ≤ 2 lines, subtext ≤ 20 words, CTA visible without scrolling?
- [ ] **Eyebrow Restraint**: Count of uppercase tracked eyebrows ≤ ceil(sectionCount / 3)?
- [ ] **No Div Screenshots**: All product previews use real screenshots or generated assets?
- [ ] **Button Contrast Checked**: All buttons pass WCAG AA (4.5:1 min contrast)?
- [ ] **CTA On One Line**: No primary CTA button text wraps on desktop?
- [ ] **Single Accent Color**: One consistent accent color locked throughout the entire layout?
- [ ] **One Corner-Radius Scale**: Button, card, and input radii adhere to one unified scale?
- [ ] **Reduced Motion Supported**: All motion wrapped with `useReducedMotion` or CSS media queries?
- [ ] **Mobile Collapse Explicit**: Multi-column layouts cleanly collapse to single-column under `< 768px`?
- [ ] **Sloplint Clean**: Automated linter passes without blocking failures?

