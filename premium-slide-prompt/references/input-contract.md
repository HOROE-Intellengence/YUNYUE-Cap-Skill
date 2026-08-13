# Input Contract

Use this contract to normalize structured or semi-structured slide outlines before designing. Do not require every input to use this exact schema; infer missing structural fields when the source evidence supports them, and preserve explicit gaps when it does not.

## Canonical page object

Normalize each page internally to:

```text
page_number
page_function
investor_task
core_conclusion
final_title
content_modules[]
candidate_facts[]
facts_to_keep[]
facts_to_cut_or_demote[]
container_plan
outside_container_text
data_status[]
memory_anchor
page_mode
investor_followup
dd_material
footnotes
missing_data
style_request
brand_assets
reference_style_cues
```

Do not print this internal object unless the user asks for analysis.

## Field handling

- Treat `投资任务`, `核心结论`, `数字身份`, `视觉锚点`, `记忆锚点`, `页面模式`, `投资人追问`, `右侧拟物`, `DD材料`, and `待补数据` as design metadata rather than automatic on-slide copy.
- Treat `视觉锚点` and `记忆锚点` as aliases for the internal `memory_anchor` field.
- Treat supplied modules as candidate facts rather than mandatory on-slide containers. Rank, select, merge, demote, or omit them according to the investor-attention budget.
- Select, refine, and synthesize on-slide copy from the supplied title, capital labels, modules, `公司名/Logo`, footnotes, sources, and other presentation material.
- Retain a supplied headline when it is already effective. Otherwise synthesize a sharper headline only from supported evidence.
- Keep `事实`, `推断`, `FA上行情景`, `待研究`, `待核`, and equivalent statuses visible whenever omission could make a claim look more certain than it is.
- Keep “available during diligence”, NDA notes, or equivalent evidence-availability statements when they are part of the supplied proof structure.

## Brand and reference handling

- Treat supplied logos, colors, fonts, product photography, existing decks, screenshots, and explicit style instructions as brand evidence.
- Extract only observable cues from reference images: layout density, image role, palette relationships, typography character, container treatment, depth, lighting, and page rhythm.
- Do not reproduce confidential text, logos, customer identities, or unsupported claims merely because they appear in a style reference.
- Do not copy a reference layout mechanically. Preserve its useful visual grammar while adapting composition to the current page's evidence.
- Assign an internal confidence level to the brand DNA: `high` for explicit brand guidelines or consistent assets, `medium` for several coherent references, and `low` for sparse or contradictory cues.
- When confidence is low, use a neutral institutional foundation and one restrained industry-relevant accent rather than inventing a complete brand identity.

## Upstream page-mode mapping

Map `bp-narrative-outline` values as follows:

| Upstream mode | Internal mode |
|---|---|
| `资本封面` | Investor-cover |
| `投资亮点总览` | Investment-highlight-grid |
| `竞争力目录` | Argument-map |
| `结论数字` | Conclusion-number |
| `严谨比较` | Rigorous-comparison |
| `能力沿革` | Capability-progression |
| `资本演进` | Capital-progression |
| `能力结构` | Capability-structure |
| `因果机制` | Causal-mechanism |
| `视觉隐喻` | Visual-metaphor |

Select Evidence-portfolio when a page needs three or four distinct investment reasons and no supplied upstream mode describes that structure better.

## Conflict resolution

Resolve conflicts in this order:

1. factual identity, masks, and disclosure status;
2. explicit user instruction;
3. supported core conclusion and evidence;
4. investor attention and readability;
5. supplied page mode and module plan;
6. default visual and composition guidance.

If a supplied page mode or container plan would overload or distort the evidence, choose the better-supported, simpler structure without changing the underlying claim. If the conflict is material to financing direction rather than presentation structure, surface it instead of silently resolving it.
