---
name: bp-narrative-outline
description: 手动调用。面向投资人，从项目资料中提炼兼顾注意力、投资确信与交易推进的核心叙事，生成含资本标签封面、投资亮点、竞争力地图和融资页的逐页BP大纲；重点论证市场容量、项目能力沿革、资本市场对标、进攻楔子、复利护城河、兑现证据与FA上行情景，并把不适合在BP披露的严谨来源、计算与保密证据归入DD材料表。输出直接对接 premium-slide-prompt。
---

# BP 投资叙事大纲生成器（Step 2 of 3）

把项目材料编译成投资确信链，而不是项目说明书。上游读取材料与锁定事实；本 skill 生成投资人大纲；下游由 `premium-slide-prompt` 生成逐页美工提示词。

## 不可妥协的结果

- 先读完用户材料、历史文件和可用知识库，不询问材料中已有的信息。
- 只写有证据身份的主张；禁止编造当前事实、来源、机构关系或恢复任何掩码。
- 用一句核心投资叙事统领整 deck。
- 普通证据页只承担一个投资任务：放大回报上限、降低失败概率或制造投资紧迫性。框架页与交易页分别服务理解和行动；投资亮点总览是四类证据合并的明确例外。
- 证据不足时标记 `[待补数据]` 或 `[待研究]`，照常交付 v0。任何诊断都只提示、不拦截、不暂停输出。

## 工作拓扑

按以下状态推进；缺口随状态向后传递，不让整套工作停摆：

`项目材料 → Fact Ledger → Claim–Evidence Graph → Narrative Contract → Deck Architecture → Page Specs → BP / DD / Research Queue → 最终大纲`

1. **归一事实**：按 [input-evidence-contract.md](references/input-evidence-contract.md) 建立 Fact Ledger，分清公司结果、团队历史、合作方资产和未来情景。
2. **连接证据**：把重要主张映射到证据、反证、强度与缺口，形成 Claim–Evidence Graph。
3. **选择叙事**：按 [narrative-router.md](references/narrative-router.md) 生成 2–3 个候选，选择证据基础最强的版本并冻结 Narrative Contract。用户已锁定叙事时先检验，不可靠就直接提出更强版本。
4. **路由论证**：按 [investment-arguments.md](references/investment-arguments.md) 选择真正需要的市场、对标、成长路径、进攻/防守和 FA 上行情景，不机械凑页。
5. **编排页面**：按 [deck-architecture.md](references/deck-architecture.md) 建立页面依赖、前五页节奏和投资委员会六问覆盖。
6. **编译页面**：按 [page-specs.md](references/page-specs.md) 将每个架构节点编译成可直接交给美化 skill 的 Page Spec。
7. **拆分披露**：按 [disclosure-and-dd.md](references/disclosure-and-dd.md) 从同一证据图派生 BP 公开内容与 DD 材料表。
8. **抛回研究**：按 [research-queue.md](references/research-queue.md) 生成精确研究任务；研究与大纲交付并行，不能成为前置门槛。
9. **交付复核**：按 [delivery-and-qa.md](references/delivery-and-qa.md) 输出大纲与附录。可运行 `python scripts/diagnose-outline.py <outline.md>` 做非阻断提示。

## 五个中间契约

中间契约是推理接口，不要求默认逐项展示给用户。

### Fact Ledger

至少记录 `fact_id、陈述、来源、日期、单位与口径、主体归属、数字身份、置信度、保密状态`。

### Claim–Evidence Graph

至少记录 `claim、投资作用、支持 facts、反证/边界、证据强度、状态、待补动作`。

### Narrative Contract

至少冻结 `核心投资叙事、开局类型、目标投资人、市场天花板、right-to-win、进攻楔子、复利护城河、商业兑现、下一催化剂、终局形态、叙事击穿点`。

### Deck Architecture

每页先定义 `页面功能、投资问题、看前认知、证据增量、看后认知、依赖页面、优先级`，暂不决定构图。

### Page Spec

再定义 `页面职责、投资任务、核心结论、标题、信息模块、证据载体、数字身份、视觉锚点、页面模式、投资人追问、DD 映射、底注、待补数据`。

## 三组强制解耦

1. **叙事与研究解耦**：Narrative Contract 只消费当前证据图；研究缺口进入 Research Queue。新研究返回后才更新证据图和叙事版本。
2. **页面职责与视觉结构解耦**：页面职责回答“为什么存在”，页面模式回答“如何表达”。不得由某种投资任务自动推导固定版式，也不得用视觉结构代替投资论证。
3. **BP 与 DD 解耦**：二者从同一 Claim–Evidence Graph 派生。BP 负责兴趣、确信和行动；DD 保存完整来源、计算、口径、保密证据与追问接法。DD 内容不得反向泄露到 BP。

## 非阻断原则

- 发现身份混用、数字冲突、证据缺失、页面职责冲突或敏感披露时，先在不改变事实的前提下修正。
- 无法安全修正时保留原始掩码或占位，追加 `[需复核]`、`[待补数据]` 或 `[待研究]`。
- 始终交付当前最佳版本和诊断清单；不得因检查未通过而拒绝、终止或延迟交付。

## 下游交接

逐页输出必须保留明确的 `页面模式`，且普通页主内容容器不超过 5 个。完成后可将单页或整套 Page Specs 直接交给 `premium-slide-prompt`；本 skill 决定投资逻辑与信息结构，不绑定固定蓝白科技风或具体美术材料。
