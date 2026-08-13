# Disclosure and Output QA

Apply these checks after drafting every prompt and before returning it.

## Contents

- Disclosure integrity
- Prompt completeness
- Attention-budget QA
- Structural QA
- Visual-system QA
- Final silent questions
- Rejected failure modes

## Disclosure integrity

- Preserve factual meaning and data identity when shortening, combining, translating, or synthesizing copy.
- Preserve every mask, placeholder, range, redaction, anonymized label, unit, date, qualifier, asterisk, bracket, source, and data-status label exactly when it affects interpretation.
- Never reconstruct hidden customer names, contract values, locations, institutional relationships, affiliations, or other confidential details from context.
- Never invent an unsupported claim, number, relationship, endorsement, source, financing round, or forecast.
- Retain NDA or “available during diligence” notes when they are part of the evidence structure.
- Follow stricter disclosure rules supplied by the user or upstream outline. Do not promote design metadata or DD-only evidence onto the slide automatically.
- Use logos only for verified relationships. Do not imply technology transfer, endorsement, or affiliation through proximity, connecting lines, or visual grouping.

## Prompt completeness

Include only elements that materially affect the result:

- page mode and composition;
- placement and hierarchy of refined on-slide copy;
- evidence containers and logical connections;
- memory anchor and highlighted differences;
- palette, typography, spacing, and background;
- selected icons, images, lighting, depth, and effects;
- page-specific constraints that prevent a likely misreading.

Select metaphors, large objects, arrows, textures, lighting, and 3D scenes according to communication value. Neither require nor forbid them by default.

For multi-slide work, start every prompt with the same verbatim `Deck-wide Style Lock`. Then list the exact on-slide copy that survives compression. Explicitly prohibit the image model from adding labels, icons, facts, badges, product names, or microcopy not supplied in the prompt.

## Attention-budget QA

Confirm that the prompt:

- treats source modules as candidate evidence rather than mandatory containers;
- contains one investor conclusion and one memory anchor;
- defaults to 2–3 evidence groups unless an explicit page-mode exception applies;
- keeps one decisive fact and at most one necessary supporting line per evidence group;
- uses no more than three dominant numbers on a standard page;
- removes repeated conclusions, product inventories, feature lists, geography lists, and biography trivia;
- demotes calculation detail, methodology, qualifications, and secondary proof to a compact source or status line;
- never solves overload by shrinking copy, nesting containers, or adding rows of small icons.

Reject the draft and compress again if an investor cannot state the conclusion and primary proof after a three-second scan.

## Structural QA

Confirm that the prompt:

- communicates one investor conclusion;
- follows the selected page-mode grammar;
- uses one memory anchor except for the explicit grid and argument-map exceptions;
- compresses any necessary dense content into a clear hierarchy and scan order;
- keeps sources, units, qualifiers, and statuses readable;
- uses charts and arrows only for supported quantities or causal relationships;
- keeps team pages credential-led and technical pages evidence-led;
- keeps supporting imagery subordinate unless it carries the explanation;
- remains consistent with the Deck Visual Contract when part of a multi-slide deck.
- repeats an identical concrete Style Lock when prompts will be generated independently.

## Visual-system QA

Confirm that the prompt:

- keeps page mode, mother style, visual expression, temperature, and material budget as separate decisions;
- assigns every image the role of evidence, explanation, category recognition, or memory;
- uses brand evidence when available and stays neutral when brand confidence is low;
- keeps effects within the selected material budget;
- differs enough from adjacent pages to create rhythm without breaking shared typography, grid, semantic colors, and source treatment;
- reserves Strategic Hero intensity for a genuine narrative peak;
- uses Corporate Ceremony only for explicit brand, contact, thank-you, or formal partnership functions.

Ask these final questions silently:

1. If glass, glow, gradients, and grids were removed, would the page logic still work?
2. Does the main image verify, explain, identify, or create a necessary memory?
3. Is the page overusing the same composition or material as the previous two pages?
4. Is prestige being simulated with medals, shields, laurels, mountains, or gold instead of evidence?
5. Is a blue-cyan palette being applied mechanically because the company is labeled technology or AI?
6. Does this page deserve to consume one of the deck's Hero peaks?
7. Has imagery displaced numbers, sources, qualifiers, or data-status labels?
8. Which visible fact could be removed without weakening the investment judgment? Remove it.
9. Is the same conclusion stated more than once? Keep the strongest version only.
10. Does the page enumerate the source outline instead of designing an investor argument?

## Reject these failure modes

- making an investor cover look like a product brochure;
- inventing or omitting the financing-round label on a cover;
- treating one focal point as one enormous object;
- making every Evidence-portfolio container equally loud;
- forcing an Investment-highlight-grid into one slide-level anchor;
- adding a second focal point inside an individual grid card or argument-map entry;
- filling a required but unsupported highlight category with generic copy;
- removing useful detail in the name of minimalism;
- preserving every outline module and subpoint merely because it was supplied;
- shrinking text or multiplying nested cards to avoid making editorial choices;
- repeating the same conclusion in headline, subtitle, center slogan, and bottom banner;
- showing complete product, software, geography, or service inventories on a strategic progression page;
- using decorative arrows that imply unsupported causality;
- turning capability evolution into a generic company milestone timeline;
- decorating a technical page with unrelated circuitry;
- making a team page image-heavy and credential-light;
- adding a numeric result to a cross-dimensional rhetorical equation without reconciling units;
- altering, guessing, or visually revealing masked information;
- using identical white-blue glass cards as the default solution across the deck;
- placing every object on a glowing pedestal or surrounding every module with a halo;
- adding engineering grids, circuit patterns, ambient waves, shields, globes, trophies, or laurels without an information role;
- rendering every process as a circular track or generic flywheel;
- using Corporate Ceremony styling on evidence pages;
- copying a reference layout mechanically instead of adapting its visual grammar;
- sustaining Hero intensity across too many consecutive pages;
- generating a multi-slide deck without first locking one qualified visual system;
- changing palette, typography, background family, container language, or effects page by page;
- writing “same style as previous slide” instead of repeating a concrete Style Lock;
- returning commentary or alternatives when the user requested only a prompt.
