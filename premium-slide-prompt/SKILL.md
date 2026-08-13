---
name: premium-slide-prompt
description: Transform a Chinese or English slide outline into one ready-to-use English image-generation prompt for a premium 16:9 investor-pitch slide, refining on-slide copy and adapting the visual language to brand assets or supplied references when useful. Use for investor covers, four-card investment-highlight grids, competition argument maps, AI-image slides, 文生图提示词, keynote-quality BP pages, pitch-deck visuals, or slide beautification. Preserve confidential masks exactly and prioritize evidence-led numbers, comparisons, capability evolution, capital timelines, matrices, diagrams, and deck-wide visual consistency.
---

# Premium Slide Prompt Designer

Compile a slide outline into one English image-generation prompt for a complete premium 16:9 investor-pitch slide. Art-direct the evidence structure, on-slide copy, and visual system without changing factual identity.

## Output contract

Produce only the image-generation prompt unless the user asks for reasoning, alternatives, or review.

For multiple slides, inspect the complete outline before writing any prompt. Produce one self-contained prompt per slide. Start every prompt with the same compact `Deck-wide Style Lock` wording, repeated verbatim, so separately generated slides retain one visual identity. Vary only composition, page expression, temperature, image role, and evidence emphasis within that lock.

Write the prompt in English. Keep on-slide copy in the language best suited to the source and audience.

## Run the pipeline

1. **Preflight the complete deck.** When the input contains multiple slides or a complete outline, read [references/deck-preflight.md](references/deck-preflight.md). Scan every page before producing page 1. Establish one qualified Style Lock and an internal deck manifest. Do not improvise a new visual identity page by page.
2. **Normalize the input.** Extract the conclusion, title, evidence modules, data status, memory anchor, page mode, sources, masks, brand assets, reference-image cues, and optional style request. When input comes from `bp-narrative-outline`, uses structured fields, or contains ambiguous field names, read [references/input-contract.md](references/input-contract.md).
3. **Rank and compress the evidence.** Always read [references/investor-attention.md](references/investor-attention.md). Treat the outline as source material, not a display checklist. Keep only facts that change the investment judgment or directly prove the conclusion.
4. **Lock the investor task.** Decide silently what the investor must retain, which belief or objection the slide changes, what evidence carries that change, which structure communicates it fastest, and what deserves strongest emphasis.
5. **Route the page.** Select one primary page mode from the table below. Follow a supplied mode unless the content clearly contradicts it. Then read [references/page-modes.md](references/page-modes.md) and apply the selected mode's complete grammar.
6. **Build the evidence hierarchy.** Use the core hierarchy rules below before selecting effects or imagery.
7. **Extract the visual identity.** Derive a compact brand DNA from explicit user direction, supplied brand assets, and qualified reference images. When evidence is weak or inconsistent, choose the default mother style and lock it instead of mirroring low-quality references.
8. **Route the visual expression.** Always read [references/style-router.md](references/style-router.md). Select one expression, one page temperature, and a material budget independently from the page mode.
9. **Apply the visual language.** Always read [references/visual-system.md](references/visual-system.md) as the neutral foundation and [references/style-capital-tech-editorial.md](references/style-capital-tech-editorial.md) as the default mother style. If the user explicitly names `Institutional Capital Deck`, asks for `机构路演风格`, or requests a polished conventional BP with visibly glazed material richness, also read [references/style-institutional-capital.md](references/style-institutional-capital.md) as a narrower overlay.
10. **Maintain deck state.** For multiple slides, read [references/deck-rhythm.md](references/deck-rhythm.md). Keep the Style Lock immutable across prompts while varying expression and temperature deliberately.
11. **Compile and check.** List only the on-slide copy and visual elements that survive the attention budget. Instruct the image model not to add extra labels, icons, facts, or decoration. Before returning, read and apply [references/disclosure-and-qa.md](references/disclosure-and-qa.md).

For a structured Markdown outline, optionally run `python scripts/validate-outline.py <outline.md>` before compiling. Treat its warnings as review cues, not permission to rewrite unsupported facts.

For a multi-slide prompt bundle, run `python scripts/validate-prompts.py <prompts.md>` when local execution is available. Fix every Style Lock error before returning the prompts; treat exact-copy-guard warnings as mandatory editorial review.

## Page-mode router

| Page mode | Use for |
|---|---|
| **Investor-cover** | Investment-defining headline, capital labels, optional credential band, and restrained hero object |
| **Investment-highlight-grid** | Exactly four cards: market, technology, commercial proof, and team |
| **Argument-map** | Up to five parallel strengths that frame proof developed later |
| **Evidence-portfolio** | Two or three aligned containers summarizing distinct investment reasons; four only when each is decision-relevant |
| **Conclusion-number** | One decisive number, ratio, equation, waterfall, or quantified chain |
| **Rigorous-comparison** | Parameter table, competitor matrix, before/after, or benchmark columns |
| **Capability-progression** | Technical lineage, productization, inherited assets, and capability expansion |
| **Capital-progression** | Timeline, valuation staircase, financing, M&A, milestones, or category evolution |
| **Capability-structure** | Team matrix, system modules, product stack, or complementary capabilities |
| **Causal-mechanism** | Process, value chain, multi-loop flywheel, funnel, or explanatory architecture |
| **Visual-metaphor** | A physical metaphor or coordinated symbols embodying an abstract mechanism or vision |

## Core hierarchy rules

Design around proof and fast recognition. Default to editorial compression. Permit higher density only when an exact comparison or technical mechanism genuinely requires it and the three-second scan still works.

Use this reading order unless the content demands another:

`conclusion headline -> memory anchor -> supporting evidence -> bottom-line verdict -> source/footnote`

Treat the bottom-line verdict as optional. Omit it when it merely repeats the headline. One page gets one conclusion, not a headline, subtitle, central slogan, and footer that all say the same thing.

On standard evidence pages, preserve one conclusion and one memory anchor while allowing several supporting modules. The anchor may be a decisive number, comparison, equation, highlighted row or column, timeline, verdict, product visual, or page-appropriate metaphor. One focal point does not mean one giant object.

Apply two explicit exceptions:

- Investment-highlight-grid allows one controlled hook in each of four cards.
- Argument-map allows up to five equal-weight entries under one shared conclusion.

Neither exception permits a second focal point inside an individual card or entry.

For dense evidence pages:

- default to 2–3 scanable evidence zones; use four only when the selected page mode requires four parallel items;
- introduce asymmetry only when it improves emphasis or reading order;
- highlight decisive differences, keep labels short and aligned, and preserve sources and units;
- connect modules only when a real sequence, dependency, feedback loop, or value transfer exists.

Never shrink text, multiply cards, or enumerate every source module to preserve an overloaded outline. Compress, synthesize, demote to footnote, or omit lower-priority detail.

## Visual separation rule

Keep these decisions independent:

- **Page mode** controls how evidence is organized.
- **Mother style** controls the deck's visual personality.
- **Page expression** controls the visual grammar used on this page.
- **Page temperature** controls the level of visual intensity.
- **Material budget** limits imagery, 3D, glass, gradients, lighting, and decorative texture.

Never translate a page mode directly into a fixed color palette, glass-card template, 3D scene, or glowing diagram.

## Non-negotiable constraints

- Preserve every mask, placeholder, range, redaction, anonymized label, unit, date, qualifier, asterisk, bracket, source, and data-status distinction exactly when it affects interpretation.
- Never invent claims, numbers, financing stages, affiliations, customer relationships, institutional relationships, sources, endorsements, or forecasts.
- Never infer hidden customer names, amounts, locations, relationships, or affiliations from context.
- Treat design metadata as instructions, not automatic on-slide copy.
- Do not return commentary or options when the user requested only a prompt.
