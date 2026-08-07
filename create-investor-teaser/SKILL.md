---
name: create-investor-teaser
description: Create, review, or optimize a high-impact 2K-class 9:20 vertical investor teaser from project materials, an existing poster, a BP, or a text brief. Use for 投资推介图、融资长图、项目一图流、朋友圈融资海报、9:20手机全屏投资图, or when Codex must compress a full investment story into one evidence-led image-generation prompt or finished image. First surface 2–3 defensible investment highlights and require the user to rank them, then order the teaser by that ranking. Require 1440 × 3200 px output, use capital-marketing poster energy with 25–35% skeuomorphic imagery, preserve confidential masks, distinguish company results from team history and forecasts, and disclose only the fundraising amount—not valuation or other transaction terms.
---

# Create Investor Teaser

Turn scattered project evidence into one mobile-readable investment argument. Optimize for investor attention, belief, and a next conversation—not for exhaustive company introduction.

## Workflow

### 1. Read before deciding

Read all supplied files and inspect every referenced image. Do not ask for information already present in the materials.

Treat image text extraction as fallible. Mark uncertain OCR tokens instead of silently normalizing them, then proofread final on-image copy character by character against the source.

Extract an evidence ledger with:

- company identity and current fundraising need, including the financing amount when supplied;
- strongest team credentials;
- product or technology wedge;
- market ceiling and timing;
- company-level commercial proof;
- capital, customer, or institutional validation;
- targets, forecasts, and FA upside scenarios;
- confidentiality masks and disclosure limits.

Classify each important claim internally as `[事实]`, `[推断]`, `[目标/预测]`, or `[待研究]`. Also record whether it is company performance, team historical experience, or third-party market data.

Never restore an anonymized name, amount, location, customer, or institutional relationship. Preserve masks and placeholders exactly.

### 2. Surface 2–3 candidate highlights and pause

Distill exactly 2–3 candidate investment highlights from the evidence ledger. Use only the strongest defensible candidates from:

1. **Team-first** — recognizable operating pedigree or an unusually complete founding team lowers execution risk.
2. **Traction-first** — revenue, orders, customers, certifications, or deployments already prove demand.
3. **Market-first** — a structural change creates a large, time-sensitive opportunity.
4. **Product-first** — a product or technical breakpoint makes a previously uneconomic solution viable.
5. **Capital-validation-first** — a verified strategic investor or comparable capital event validates the asset category.

Describe each candidate in one compact line using `亮点名称｜关键证据｜投资含义`. Do not expose private chain-of-thought; show only the evidence-backed conclusions needed for the user to decide.

Present the numbered candidates to the user and ask them to rank the candidates by importance, for example `2 > 1 > 3`. This is a required checkpoint. Do not produce the final blueprint, on-image copy, image-generation prompt, or finished image until the user supplies the ranking. Skip the checkpoint only when the user has already provided an explicit ranking in the current request.

If a candidate is weak, conflicting, or legally risky, disclose that beside the candidate before ranking. Treat employer heritage as a credential, not endorsement. Do not use another company's logo unless authorization or an official relationship is verified.

### 3. Apply the user's ranking

Map the user's order directly to the teaser's reading order and visual hierarchy:

1. **Rank 1** — dominant hook, largest headline, largest proof-bearing zone, and first content module after identity.
2. **Rank 2** — first supporting argument, medium emphasis, immediately after Rank 1.
3. **Rank 3** — compact supporting argument or footer proof, always after Rank 2.

Do not place a lower-ranked highlight before a higher-ranked highlight, give them equal visual weight, or silently replace the user's order. If the highest-ranked claim is not safe to state as fact, keep its priority but qualify it visibly as `[目标/预测]`, `[推断]`, or `[待研究]` and avoid unsupported certainty.

### 4. Write the investment thesis

Write one sentence using this logic:

`credible right to win + specific product wedge + expanding value pool = reason to engage now`

Prefer a sharp capital judgment over mission language. Avoid “致力于、赋能、领先解决方案、卡位赛道” unless evidence makes the phrase meaningful.

When defensible, select one capital-scale number—market ceiling, revenue, order, installed base, or clearly labeled forecast—to show why the opportunity can become large. This number supports the ranked story; it does not override the user's highlight order. Never fabricate a capital-scale number merely to fill the design.

### 5. Enforce the vertical composition

Every image-generation prompt and finished teaser must specify exactly `9:20 vertical`, `1440 × 3200 px`, `2K/QHD+ class`, full-screen mobile. Require native high-resolution rendering with crisp Chinese typography, sharp thin rules, and clean numerical labels; do not accept a low-resolution draft merely described as “2K.” Do not output, recommend, or adapt to any horizontal, square, or alternate aspect ratio. Use 64–96 px safe margins and preserve readable type at normal phone scale.

Use 5–8 coherent visual modules. A three-number metric grid, credential matrix, timeline, process loop, or coordinated hero composition counts as one module when it shares one visual system. Avoid dozens of unrelated cards.

Typical vertical allocation, adjusted to the user's ranking:

- 4–7%: company identity, financing amount only, track;
- 30–38%: Rank 1 headline, decisive proof, and high-impact hero composition;
- 18–24%: Rank 2 conclusion and proof;
- 12–18%: Rank 3 conclusion and proof;
- 10–16%: capital-scale number, forecast strip, or supporting evidence visualization when defensible;
- 6–10%: source notes, transaction CTA, and contact.

Adjust the ratios according to the lead hook. Read [layout-patterns.md](references/layout-patterns.md) when choosing a composition or when the user requests a materially different version.

### 6. Control information density

Use high density only inside a clear structure. Do not convert every fact into a separate card.

- Standard 9:20 teaser: target 130–220 Chinese characters excluding sources.
- Dense team-first or platform-first teaser: allow up to roughly 260 Chinese characters when credentials or process steps are organized as one matrix or flow.
- Keep paragraphs off the image. Use short verdicts, rows, proof strips, equations, labels, and footnotes.
- Give each container one primary assertion or number and no more than 1–3 proof-bearing details.
- Prefer one 3-row credential matrix over three biography cards.
- Keep important qualifiers, years, units, regions, prediction labels, and source markers readable.
- If the material cannot fit without shrinking the type, remove secondary evidence or create a second image; do not make unreadable fine print.

### 7. Translate evidence into visuals

Use high-impact imagery to create immediate category recognition, then anchor it with proof.

- Target 25–35% of the total canvas for purely skeuomorphic imagery and never exceed 35%. This includes photorealistic product renders, device mockups, people, environmental scenes, glossy 3D objects, and material-rich physical elements.
- Keep at least 65% of the canvas for information-bearing typography, numbers, charts, matrices, timelines, equations, process flows, labeled diagrams, source notes, and whitespace.
- Use one cohesive hero scene or hero object rather than several unrelated decorative renders. Let it occupy roughly 20–30% when it materially improves category recognition.
- A labeled technical cutaway, mechanism diagram, or evidence chart remains information-bearing when its primary function is explanation; decorative or unlabeled realism counts toward the 35% cap.
- Use exploded views or technical cutaways only when the mechanism itself is the investment thesis.
- Use category-scale imagery such as a global network, installed-base field, factory, infrastructure system, chip stack, equipment cluster, or product ecosystem when it directly supports the thesis.
- Use people only when operations, service capability, or team execution is part of the proof. Unless authentic team images are supplied, keep people non-identifiable and avoid implying they are actual employees.
- Do not add unrelated handshakes, rockets, generic boardrooms, or random technology objects.

### 8. Apply the high-impact capital-marketing style

Default to a high-impact capital-marketing poster with institutional-grade evidence discipline—not a quiet research memo and not a chaotic startup-event poster.

- Use luminous white or ice-blue backgrounds, saturated cobalt/electric blue, deep navy, and restrained metallic gold for one decisive capital or commercial number.
- Use one oversized one- or two-line category headline, strong condensed Chinese typography, controlled bevel or extrusion, crisp dark-blue shadows, and large high-contrast numerals.
- Allow polished blue gradient bands, lightly rounded glass panels, glossy 3D icons, rim lighting, controlled glow, rising arrows, and translucent chart columns when they strengthen hierarchy.
- Use a recognizable rhythm: category headline and hero scene; financing badge; capital-scale band; three-number proof grid; Rank 2 module; Rank 3 module; closing moat or CTA.
- Keep one dominant focal point per screen section. Do not give every card, icon, and label equal visual weight or render all text in 3D.
- Avoid rainbow palettes, childish cartoons, cheap template effects, uncontrolled bloom, excessive plastic shine, illegible glassmorphism, and decorative clutter.
- Reserve gold for verified credentials, financing information, commercial validation, or clearly labeled capital-scale figures; do not spread it decoratively.
- Keep source notes quiet but legible.

### 9. Protect factual and transaction integrity

- In the public teaser, fundraising disclosure is limited to the financing amount. Show the verified amount or `[待补融资额]`; never guess it.
- Do not show the financing round, valuation (pre- or post-money, including ranges), ownership percentage, security price, share count, dilution, cap table, investor terms, or any other transaction field. Do not use calculations, diagrams, wording, or visual cues that could infer or reverse-engineer them.
- Keep any valuation or transaction-term evidence exclusively in the private DD list; never place it in the blueprint's public copy, on-image copy, or image-generation prompt, even if it appears in source materials or is explicitly requested.
- Preserve the subject of every credential. Do not merge adjacent facts into a new composite claim, extend one member's experience to another member, or extend experience in one product category to a related category without explicit support.
- When source materials conflict on financing round, market definition, timing, units, or achievement status, do not silently reconcile them. Preserve the conflict in the working notes and use an exact placeholder or a clearly qualified version on the image.
- Distinguish team historical track record from current company results in the on-image copy.
- Label forecasts, targets, and FA scenarios when investors could read them as facts.
- Give market figures a year, geography, definition, and source status. Keep full calculations and confidential evidence in a DD list rather than cramming them on the image.
- Never imply endorsement, technology transfer, customer status, or institutional affiliation through logos, proximity, connecting lines, or visual grouping.

## Team-first rules

When team pedigree is the lead hook, place it before the product and market sections. Use a compact credential matrix or stacked evidence rows with strong icons rather than three unrelated biography cards.

Preferred matrix:

`核心成员 | 关键履历 | 可迁移能力`

For each member, select only credentials that reduce execution risk: tenure, responsibility level, named product ownership, technical depth, scale delivered, supply-chain scope, or verified awards. Translate credentials into a transferable capability such as product definition, algorithm, hardware integration, cost control, supply chain, certification, or mass production.

Add one compact team coverage line and one historical evidence strip when supported. Explicitly label team-derived numbers as `团队历史履历`.

## Output contract

Before the user ranks the 2–3 candidate highlights, output only the numbered candidates and the ranking question. After the user ranks them, follow the requested artifact mode below.

Unless the user requests only one artifact, return:

1. **Investment judgment** — one short paragraph naming the lead hook and what to remove.
2. **One-page blueprint** — thesis, headline, section order, approximate canvas allocation, evidence containers, visual anchor, and footer.
3. **Final on-image copy** — exact copy grouped by visual zone; retain placeholders and masks.
4. **Image-generation prompt** — one self-contained English prompt; keep on-image copy in the audience's language and specify the requested aspect ratio.
5. **DD gaps** — at most three missing items that could materially weaken investor belief.

If the user asks for:

- **review only**: diagnose and propose the blueprint without generating an image;
- **prompt only**: output only the ready-to-use image-generation prompt;
- **a finished image**: first finalize the evidence and prompt, then use the image-generation capability; inspect the result and iterate for legibility, hierarchy, factual accuracy, and aspect ratio;
- **another version**: change the lead hook, evidence order, or visual logic—not just adjectives and colors.

## Blueprint template

```text
### 单张投资推介图
- 页面职责：放大回报上限 / 降低失败概率 / 制造投资紧迫性
- 核心投资叙事：
- 用户亮点排序：1 > 2 > 3
- 输出规格：9:20竖屏 | 1440 × 3200 px | 2K/QHD+
- 主钩子：团队 / 兑现 / 市场 / 产品 / 资本验证
- 标题：
- 顶部身份带：公司名 | 融资额（或`[待补融资额]`） | 细分赛道
- 模块1：容器类型 | 结论 | 证明
- 模块2：容器类型 | 结论 | 证明
- 模块3/4/5：按需使用
- 画面分配：各模块占比
- 纯拟物占比：25–35%，不得超过35%
- 视觉模式：高冲击融资海报 | 机构级证据纪律
- 主视觉：对象 | 它证明什么
- 数字身份（后台）：
- 上片限定词：
- 底注：
- DD材料：
- 待补数据：
```

## Quality gate

Before delivery, verify:

- Has the user ranked the 2–3 candidate highlights, or supplied an explicit ranking in the request?
- Does the reading order and visual emphasis exactly follow that ranking?
- Does the prompt specify only `9:20 vertical, 1440 × 3200 px, 2K/QHD+ class` and explicitly require native high-resolution rendering?
- Is purely skeuomorphic imagery between roughly 25–35% and never above 35% of the total canvas area?
- Can an investor identify the company level, financing amount (when supplied), and lead hook in three seconds?
- Does every public-facing artifact show financing amount as the only transaction disclosure, with no valuation or other terms that could reveal or reverse-engineer it?
- Does every section strengthen the same investment thesis?
- Is company traction separated from team history?
- Are predictions and targets visibly qualified where needed?
- Is every market number internally consistent and source-ready?
- Are confidential masks preserved exactly?
- Are 5–8 coherent visual modules used without fragmenting the page into unrelated cards?
- Is all key text readable at normal phone scale?
- Has every final text string been checked for OCR artifacts, misspellings, altered numerals, and unsupported editorial expansion?
- Do images explain the category, product, or mechanism rather than decorate empty space?
- Does the page have immediate commercial-poster impact while preserving institutional evidence discipline?

If any answer is no, revise before delivering.
