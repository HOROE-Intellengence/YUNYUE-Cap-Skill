# Whole-Deck Preflight and Style Lock

Use this workflow whenever the user provides more than one slide, a complete outline, or asks for prompts for an entire deck. Complete the preflight silently before writing the first page prompt.

## Contents

- Read the whole deck first
- Qualify the style source
- Build the Style Lock
- Build the deck manifest
- Emit self-contained prompts

## Read the whole deck first

Scan every page and identify:

- the investment argument and its narrative peaks;
- repeated claims, numbers, products, and diagrams;
- likely page modes and evidence density;
- supplied brand assets and reference-image cues;
- pages that need Quiet, Standard, or Hero temperature;
- facts that belong on-slide, in a source line, or only in DD.

Do not start page 1 until the whole-deck scan is complete. A page-by-page start encourages style drift and repeated evidence.

## Qualify the style source

Choose one style source in this priority order:

1. explicit brand guidelines or a user-approved design system;
2. several coherent, high-quality reference slides designated by the user;
3. a consistent existing deck whose typography, hierarchy, and material language are usable;
4. the default `Institutional Capital-Tech Editorial` mother style.

A reference qualifies only when its hierarchy is readable, its visual language is internally consistent, and its density and tone fit an investor deck. One attractive but inconsistent screenshot does not define a deck system.

When references conflict, preserve verified brand assets, reject weak or contradictory stylistic cues, and choose one coherent direction. Never average incompatible styles into a hybrid.

When no reference clears the quality gate, actively choose the default mother style. Lack of a good reference is not permission to let each page choose its own palette, background, typography, or material.

## Build the Style Lock

Create one compact internal lock with immutable values for:

```text
mother_style
brand_confidence
canvas_and_safe_margins
primary_and_authorized_dark_backgrounds
primary_text_and_muted_text
primary_hue_and_one_semantic_accent
type_character_and_weight_hierarchy
headline_position_and_max_width
container_shell_and_corner_language
rule_icon_and_diagram_language
product_and_scene_image_treatment
depth_shadow_and_lighting_ceiling
source_and_page_furniture
forbidden_recurring_motifs
```

Make the lock concrete enough to reproduce: use stable color names or values, fixed compositional language, and explicit effect ceilings. Do not use vague instructions such as “premium”, “high-tech”, or “consistent with previous slides” as the lock.

Authorize at most one light base and one dark Hero variant. Do not invent a new background family or palette for individual pages.

## Build the deck manifest

Before drafting prompts, make an internal table for every page:

```text
page_number
one_investor_conclusion
facts_to_keep
facts_to_cut_or_demote
page_mode
page_expression
page_temperature
memory_anchor
image_role
material_budget
duplicate_evidence_to_avoid
```

Use the manifest to prevent one fact from becoming a headline on several pages and to keep Hero pages within quota.

Do not print the manifest unless the user asks for it.

## Emit self-contained prompts

Start every page prompt with a compact `Deck-wide Style Lock:` block. Repeat the wording verbatim across all prompts, including exact palette, typography, grid, container, image, and effects language.

After the lock, add only page-specific composition, content, expression, temperature, imagery, and constraints.

Use this stable multi-slide output shape so each prompt can be copied and generated independently:

```text
### P{page_number}
Deck-wide Style Lock: {one compact paragraph repeated verbatim}
Page-specific Prompt: {one self-contained English image-generation prompt}
```

Inside `Page-specific Prompt`, enumerate the exact surviving on-slide copy once and state: `Render only this supplied on-slide copy; add no other words, labels, badges, numbers, or microcopy.`

Never write “same style as the previous slide” because image-generation calls may be independent. Never silently change the lock because one page is a different content type.

Permit only these controlled variations:

- light base versus the single authorized dark Hero variant;
- Quiet, Standard, or Hero temperature;
- page expression and image role;
- evidence-specific semantic accent already authorized by the lock;
- composition required by the selected page mode.
