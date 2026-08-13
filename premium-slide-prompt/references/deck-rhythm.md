# Deck Rhythm and State

Use this module when generating more than one slide. Establish one internal Deck Visual Contract before compiling the first prompt. Convert it into the compact `Deck-wide Style Lock` defined in `deck-preflight.md`, then repeat that lock verbatim at the start of every page prompt. Do not rely on conversational memory or “same as previous page”.

## Deck Visual Contract

Lock these shared decisions:

```text
style_personality
brand_source_and_confidence
canvas_and_resolution
background_family
semantic_palette
type_character_and_weight_hierarchy
outer_margins_and_grid
headline_position_and_max_width
container_shell_and_corner_language
icon_and_diagram_language
figurative_image_language
source_and_footnote_treatment
effects_ceiling
hero_page_quota
repetition_limit
```

For each page, add:

```text
page_expression
page_temperature
image_role
material_budget
```

Derive the shared contract in this order:

1. explicit user direction and brand guidelines;
2. consistent observable cues from supplied brand assets and reference images;
3. selected mother style and optional overlay;
4. neutral visual foundation.

Record brand confidence internally as high, medium, or low. When confidence is low, keep the system neutral rather than manufacturing a brand identity.

Once the Style Lock is chosen, do not change its palette, typography, margins, headline geometry, container family, diagram language, image treatment, or effects ceiling because an individual page looks difficult. Solve the page through expression, temperature, composition, and evidence selection.

## Argument and visual rhythm

Make Quiet Evidence and Standard evidence-led pages the argumentative backbone. Add Scientific Mechanism, Commercial Momentum, and Strategic Hero expressions only when the content benefits.

Use Strategic Hero for covers, major section turns, decisive breakthroughs, strategic contrasts, or terminal vision. A normal investor deck should usually contain no more than 2–4 Hero pages.

Let finance, competition, team, financing, and qualifications become quieter and make the case. Do not make every page compete for maximum visual intensity.

Use this rhythm as a useful default rather than a mandatory sequence:

`Hero -> Quiet or Standard -> Quiet -> Standard -> Hero`

Avoid:

- three consecutive Hero pages;
- four consecutive pages with the same container grammar;
- repeated circular diagrams or glowing platforms across adjacent pages;
- identical image placement across several pages unless exact comparison requires it;
- forced novelty that breaks the deck identity.

## Cross-page consistency

- keep repeated numbers, units, dates, labels, colors, and data statuses consistent;
- assign one semantic color to one kind of information;
- maintain stable headline geometry, source treatment, and core typography;
- distinguish historical facts, current facts, targets, and FA scenarios consistently;
- repeat a product, scene, or metaphor only when recurrence strengthens the narrative;
- vary image share, density within the attention budget, background value, and material expression without changing the deck's identity.

For independent image-generation calls, repeat the same concrete style language in every prompt. A deck-level rule that appears only in an introduction or in the first prompt is not a reliable lock.

## Brand-reference discipline

Preserve observable visual grammar from references rather than copying a page literally. Reuse coherent traits such as headline hierarchy, density, palette relationship, image role, container material, or depth. Adapt composition to the current evidence.

Do not copy confidential content, customer identities, unsupported claims, or recognizable third-party branding from a style reference.
