---
name: "bp-financial-forecast"
description: "FA承做创业公司融资BP的财务预测：从不完整的历史财务与经营参数出发，反推驱动假设、重建公式链，产出承做人员用的Word底稿和可交付企业的补全版Excel模型。当用户提到财务预测、BP财务、盈利预测、三年/五年预测、财务模型补全、承做底稿、尽调财务测算、把预测表补成公式版时使用。"
---

# 创业BP财务预测（FA承做版）

## 定位与边界

BP财务预测是初创企业针对高速增长与不确定性扩张的**外发参考资料**。它不承诺预测的真实性——这是项目方与投资人之间的默契。但"不承诺可实现"不等于可以编数据：

- 已发生的事实（历史财务、订单、客户、投运数量）不得虚构或混淆口径。
- 每个数字必须能追溯到历史、经营驱动、行业锚点或明确标注的反推。
- 增速、利用率、转化率这类不那么客观的参数，**可以合理推测**——但必须标注为反推值/情景假设，不得伪装成已验证事实。

实际业务中拿到的资料**基本都是不完整的**。创业企业的财务预测本质就是：给出部分数据，反推其余数据。这个skill的工作就是把这个反推过程做得可解释、可追问、可交付。

## 两份交付物

| | 给谁 | 内容 |
|---|---|---|
| **A · Word 承做底稿** | 内部承做人员 | 计算方法、反推逻辑、最好补充或核实的数据、简要财务分析、增长点分析、可直接写入BP的文本 |
| **B · Excel 补全模型** | 可交付初创企业 | 公式驱动的完整模型，改一个驱动参数全表联动 |

Word 解释为什么这样算，Excel 负责让数字自动联动。两者不得出现口径冲突。

## 六条硬约束

1. **唯一输入区**。所有可编辑输入只允许存在于「来源与假设」一张表，其余各表全部是公式。同一个指标只能是输入、公式或输出之一。
2. **不得三重硬编码**。业务增速、行业增速、市占率三者互相决定，最多指定两个为输入，剩余项必须由公式输出。
3. **反推值必须显形**。反推出来的利用率、增速、市占率、平衡差额一律标橙底，Word 里单列清单。
4. **缺数据就留空**。行业规模没有就不输出隐含市占率；资本开支没有就不输出自由现金流；投资者现金流没有就不算IRR，也不得用CAGR替代。
5. **历史与预测分离**。三情景（如做）只改驱动参数，永不改历史。
6. **FAIL不外发**。校验表 FAIL 必须修复；REVIEW 可以形成初版但必须书面解释待补事项并降低结论强度。

## 流程

```
资料摄取与口径锁定 → 数据体检 + 分部拆解 → 参数确认（文字问答）
  → A/B 模式分支 → 反推求解 → 生成Excel → LibreOffice重算校验
  → 写Word底稿 → 复核签出
```

### 1｜资料摄取与口径锁定

读取用户给的一切：历史财报、既有预测表、BP、访谈记录、行业研报、微信语音转录。锁定：币种、单位（万元/元）、含税或不含税、合并或单体、历史截止日、基准年与预测年数。

口径不明的直接问，不要猜。这一步问错，后面全错。

### 2｜数据体检与分部拆解

**按收入形成方式拆分业务，不按组织架构凑分类。** 一个业务如果收入公式不同（订阅 vs 项目制 vs 硬件出货），就是不同分部。

给每个分部判定驱动方式（见下表）和数据完整度。

### 3｜参数确认

用普通文字对话确认口径、分部划分、缺失参数。**不要求严谨的问答闸门，中途文字询问即可。** 一般来说第一轮项目方能给的数据都给了，给不了的最多让他口述估一个。项目方没回复不阻塞初版——把对应结果标为反推值，在Word里列进待核实清单。

问的时候一次性集中提出，说明用途和影响，不零散追问，不要求项目方为未知数据编造精确值。可接受区间、数量级、订单清单或管理层底线假设。

### 4｜模式判断

| 模式 | 触发条件 | 建模动作 | 校验依据 |
|---|---|---|---|
| **A 逆向复现** | 项目方已给成型预测表（通常全是硬编码死数） | 由目标收入/利润反推驱动参数，重建公式链，数值精确复现原表 | 逐年收入、营业利润与原表一致（容差0.01） |
| **B 正向构建** | 只有历史财务和零散经营参数 | 由历史基准+经营驱动自建预测 | 行业与经营边界：增速上限、费用率合计<毛利率、隐含市占率上限 |

模式A的价值是把死数变成可追问的公式链，同时把隐含假设暴露出来（"要达到这个收入，利用率必须是89%——依据是什么？"）。

### 5｜分部驱动方式

| driver | 适用 | 公式 | 需要的输入 |
|---|---|---|---|
| `unit` | 站点/机场/门店/付费客户等可数经营单元 | 收入 = 平均有效数量 × 单位年创收 × 利用率<br>平均有效数量 =（期初累计 + 期末累计）÷ 2 | 各年期末累计数量、首年期初、单位创收、利用率 |
| `growth` | 只知道收入、拿不到量价拆分 | 收入ₜ = 收入ₜ₋₁ × (1 + 增速ₜ) | 首年基数、各年增速 |
| `share` | 行业数据完整、内部数据稀疏 | 收入ₜ = 可服务市场规模ₜ × 目标市占率ₜ | 市场规模、市占率 |

**优先级：unit > share > growth。** `growth` 是降级方案——它无法回答"增长从哪来"。凡是用了 `growth` 的分部，Word 里必须写明"该分部暂用收入增速法，未做量价拆分"，并列入补数清单。

站点集中在年末投运时，简单平均会高估收入。若拿到投运月份，改用月度加权；拿不到就用简单平均并标注为隐含值。

### 6｜反推规则

| 已知 | 反推 | 披露方式 |
|---|---|---|
| 目标收入 + 数量 + 单价 | 利用率 | "为复现目标收入的隐含利用率" |
| 目标收入序列 | 增速 | "由原表收入反推的隐含增速" |
| 目标收入 + 市场规模 | 市占率 | "隐含市占率" |
| 目标营业利润 + 可见科目 | 平衡差额 | 单列为「未列示调整项（待核实）」，**不得写入BP** |
| 收入/利润/IRR目标 | 所需经营条件 | "达到该目标所需的隐含条件" |

平衡差额是常态而非异常：项目方的原表往往含政府补助、其他收益、资产处置等未列示科目。做法是单列一行让勾稽闭合，然后把它写进补数清单去问，而不是硬凑费用率。

**反推出的利用率超过100%说明单位创收假设与目标收入不自洽——这是 FAIL，不是 WARN。**

### 7｜生成 Excel

把参数写成 config.json，运行下方生成器脚本。

### 8｜重算校验

生成的 xlsx 里公式没有缓存值。用 LibreOffice 重算一遍再读回，确认校验表状态并取得 Word 需要的所有数字：

```bash
mkdir -p /tmp/rc && soffice --headless --norestore --convert-to xlsx --outdir /tmp/rc 模型.xlsx
python3 -c "
import openpyxl
wb=openpyxl.load_workbook('/tmp/rc/模型.xlsx', data_only=True)
ws=wb['校验']; print('状态:', ws['F3'].value)
for r in range(6,40):
    if ws.cell(r,1).value and ws.cell(r,6).value:
        print(ws.cell(r,6).value, ws.cell(r,1).value)
"
```

FAIL 就回去改 config 重生成。Word 里的每一个数字都从这次重算结果里取，不要心算。

### 9｜写 Word 底稿

读 docx skill，按下方结构写。

## config.json 规格

```json
{
  "project": "项目名", "unit": "万元",
  "years": [2024, 2025, 2026, 2027],
  "hist_n": 1,
  "mode": "A",
  "check_date": "2026-08-14",
  "lead_segment": "主业务名（用于增长分析的占比指标）",
  "scope_note": "单位/口径/含税/合并说明",
  "limitation": "主要限制一句话",
  "disclaimer": "免责声明全文",
  "share_cap": 0.30,
  "growth_cap": 2.0,

  "segments": [
    {"name": "分部名", "driver": "unit",
     "unit_name": "机场", "qty_unit": "个",
     "qty": [15, 250, 450, 950], "qty_open0": 0,
     "price": [30, 24.5, 22.05, 21.83],
     "util": [0.5, 0.66, 0.89, 0.86],
     "target": [112.5, 2152.3, 6879.6, 13206.8],
     "src_qty": "来源说明", "src_price": "来源说明", "src_util": "来源说明",
     "verdict": "增长分析表里的一句判断"},

    {"name": "分部名", "driver": "growth",
     "base": 50.3, "growth": [null, 4.598, 0.692, 0.800],
     "target": [50.3, 281.6, 476.4, 857.5],
     "src_base": "来源", "src_growth": "来源", "verdict": "判断"},

    {"name": "分部名", "driver": "share",
     "market": [50000, 60000, 72000, 86000],
     "share": [0.002, 0.004, 0.007, 0.010],
     "market_src": "研报名称/年份/口径", "verdict": "判断"}
  ],

  "pnl": {
    "gross_margin": [0.426, 0.452, 0.459, 0.472],
    "sales_rate": [0.086, 0.085, 0.084, 0.082],
    "admin_rate": [0.117, 0.111, 0.106, 0.101],
    "rd_rate": [0.190, 0.170, 0.145, 0.138],
    "fin_exp": [0.08, 22.57, 40.63, 60.94],
    "tax_rate": [0, 0, 0.15, 0.15]
  },

  "reference": {
    "revenue": [...], "operating_profit": [...], "net_profit": [...],
    "file": "原文件名", "note": "提取说明"
  },

  "data_needs": [
    {"id": "D01", "item": "数据名", "status": "待口头核实", "priority": "极高",
     "why": "为何显著提升质量", "ask": "建议问法", "fallback": "未取得时处理"}
  ],
  "growth_notes": [["增长质量", "一句话"], ["主要风险", "一句话"]],
  "bp_text": [["规模增长", "可直接写入BP的段落"], ["风险提示", "..."]]
}
```

要点：

- **模式A**：给每个分部填 `target`（原表的分部收入序列），脚本自动反推 `growth` / `util` / `share`，并自动算出利润表的平衡差额。`growth`、`util`、`share` 可以留空。
- **模式B**：直接填 `growth` / `util` / `share`，不填 `target` 和 `reference`。
- `market` 只在行业锚点区输入一次；`share` 型分部的市场规模从那里链接，不重复输入。
- `growth` 数组首位固定为 `null`（首年用 `base`）。
- 单位统一，通常万元。所有比率用小数（0.15 不是 15）。

`data_needs` 常见十项模板（按项目实际增删）：最近一期实际分业务收入 / 经营单元投运时点与实际利用率 / 在手订单与确认节奏 / 各业务毛利率或单位成本 / 行业规模与增速及来源 / 量价拆分参数 / 资本开支与营运资金 / 融资与退出假设 / 未列示利润调整项 / 税收优惠与亏损结转。

## 生成器脚本

把下面的代码写成 `build_forecast_model.py`，然后 `python3 build_forecast_model.py config.json 输出.xlsx`。需要 openpyxl。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""创业BP财务预测模型生成器。仅「来源与假设」为可编辑输入区，其余全部为公式。"""
import json, sys, copy
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import LineChart, PieChart, Reference

FN = '微软雅黑'
F_TITLE = Font(name=FN, size=13, bold=True)
F_SEC   = Font(name=FN, size=10, bold=True, color='1F3864')
F_HDR   = Font(name=FN, size=10, bold=True)
F_IN    = Font(name=FN, size=10, color='0070C0')
F_LINK  = Font(name=FN, size=10, color='008000')
F_CALC  = Font(name=FN, size=10)
F_TXT   = Font(name=FN, size=10)
F_NOTE  = Font(name=FN, size=9, color='7F7F7F')
FILL_BACK = PatternFill('solid', fgColor='FCE4D6')
FILL_TODO = PatternFill('solid', fgColor='FFF2CC')
FILL_HIST = PatternFill('solid', fgColor='F2F2F2')
FILL_HDR  = PatternFill('solid', fgColor='D9E1F2')
WRAP = Alignment(wrap_text=True, vertical='top')
THIN = Side(style='thin', color='BFBFBF')
BOX  = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
FMT_AMT, FMT_PCT, FMT_QTY = '#,##0.0', '0.0%', '#,##0'


def col(i):
    return get_column_letter(3 + i)


def xref(sheet, row, i):
    return f"'{sheet}'!{col(i)}{row}"


def solve(cfg):
    n = len(cfg['years'])
    for seg in cfg['segments']:
        tgt = seg.get('target')
        if cfg['mode'] != 'A' or not tgt:
            continue
        if seg['driver'] == 'growth':
            seg['base'] = tgt[0]
            seg['growth'] = [None] + [
                (tgt[t] / tgt[t - 1] - 1) if tgt[t - 1] else None for t in range(1, n)]
        elif seg['driver'] == 'unit':
            qty, price = seg['qty'], seg['price']
            beg = [seg.get('qty_open0', 0)] + qty[:-1]
            seg['qty_open'] = beg
            avg = [(beg[t] + qty[t]) / 2 for t in range(n)]
            seg['util'] = [
                (tgt[t] / (avg[t] * price[t])) if avg[t] * price[t] else None for t in range(n)]
        elif seg['driver'] == 'share':
            mkt = seg['market']
            seg['share'] = [(tgt[t] / mkt[t]) if mkt[t] else None for t in range(n)]
    p = cfg['pnl']
    ref = cfg.get('reference') or {}
    if cfg['mode'] == 'A' and ref.get('operating_profit'):
        adj = []
        for t in range(n):
            rev = sum(_seg_rev(s, t) for s in cfg['segments'])
            gross = rev * p['gross_margin'][t]
            visible = (gross - rev * p['sales_rate'][t] - rev * p['admin_rate'][t]
                       - rev * p['rd_rate'][t] - p['fin_exp'][t])
            d = ref['operating_profit'][t] - visible
            adj.append(round(d, 6) if abs(d) > 0.005 else 0)
        p['other_adj'] = adj
    p.setdefault('other_adj', [0] * n)
    return cfg


def _seg_rev(seg, t):
    if seg['driver'] == 'growth':
        r = seg['base']
        for k in range(1, t + 1):
            r *= (1 + (seg['growth'][k] or 0))
        return r
    if seg['driver'] == 'unit':
        beg = seg.get('qty_open', [0] + seg['qty'][:-1])
        return (beg[t] + seg['qty'][t]) / 2 * seg['price'][t] * (seg['util'][t] or 0)
    if seg['driver'] == 'share':
        return seg['market'][t] * (seg['share'][t] or 0)
    return 0


def put(ws, r, label, unit='', font=F_TXT):
    ws.cell(r, 1, label).font = font
    if unit:
        ws.cell(r, 2, unit).font = F_NOTE
    return r


def year_header(ws, r, cfg):
    ws.cell(r, 1, '科目/指标').font = F_HDR
    ws.cell(r, 2, '单位').font = F_HDR
    ws.cell(r, 1).fill = FILL_HDR
    ws.cell(r, 2).fill = FILL_HDR
    for i, y in enumerate(cfg['years']):
        c = ws.cell(r, 3 + i, f"{y}{'A' if i < cfg['hist_n'] else 'E'}")
        c.font = F_HDR
        c.fill = FILL_HDR
        c.alignment = Alignment(horizontal='center')


def row_vals(ws, r, vals, fmt, font, fill=None):
    for i, v in enumerate(vals):
        c = ws.cell(r, 3 + i)
        if v is not None:
            c.value = v
        c.number_format = fmt
        c.font = font
        if fill:
            c.fill = fill


def _role(ws, r, n, role, src):
    ws.cell(r, 3 + n, role).font = F_NOTE
    c = ws.cell(r, 4 + n, src); c.font = F_NOTE; c.alignment = WRAP


def sheet_readme(wb, cfg):
    ws = wb.create_sheet('使用说明')
    ws['A1'] = f"{cfg['project']}｜创业BP财务预测模型 · 使用说明"
    ws['A1'].font = F_TITLE
    ws['A3'] = ('使用边界：本模型用于初创企业融资BP的外发参考，反映高速增长与不确定扩张下的经营情景，'
                '不构成业绩承诺或真实性保证。项目方与投资人通常理解这一属性；但每项数据仍须来源明确、'
                '计算可追溯、增长逻辑自洽，并能说明实现条件与风险。')
    ws['A3'].alignment = WRAP
    ws.merge_cells('A3:H5')
    ws['A7'] = '模型状态与关键结果'; ws['A7'].font = F_SEC
    lbl = ['模型状态', '收入CAGR', '末年净利率', '主业务末年占比']
    frm = ["='校验'!F3", "='增长分析'!B5", "='增长分析'!D5", "='增长分析'!F5"]
    for k in range(4):
        ws.cell(8, 1 + k * 2, lbl[k]).font = F_HDR
        c = ws.cell(9, 1 + k * 2, frm[k]); c.font = F_LINK
        c.number_format = FMT_PCT if k else 'General'
    ws['A11'] = '建模模式'; ws['A11'].font = F_HDR
    ws['B11'] = ('A｜逆向复现：项目方已提供成型预测表，本模型反推驱动参数并重建公式链，'
                 '校验以复现原表为准。' if cfg['mode'] == 'A' else
                 'B｜正向构建：无既有预测表，由历史基准与经营驱动自建，校验以行业与经营边界为准。')
    ws['A12'] = '主要限制'; ws['A12'].font = F_HDR
    ws['B12'] = cfg.get('limitation', '行业规模/市占率、分业务毛利率、现金流及IRR参数尚待补充')
    ws['A13'] = '更新原则'; ws['A13'].font = F_HDR
    ws['B13'] = '只改「来源与假设」中的蓝字；其余各表为公式，不得手改。'
    ws['A15'] = '颜色约定'; ws['A15'].font = F_SEC
    conv = [('蓝字', '可编辑输入'), ('绿字', '跨表链接'), ('黑字', '公式计算'),
            ('橙底', '反推/插值结果'), ('黄底', '待核实/高影响'), ('灰底', '历史或来源数据')]
    for k, (a, b) in enumerate(conv):
        ws.cell(16 + k // 3, 1 + (k % 3) * 3, a).font = F_HDR
        ws.cell(16 + k // 3, 2 + (k % 3) * 3, b).font = F_TXT
    ws['A19'] = '状态含义'; ws['A19'].font = F_SEC
    ws['A20'] = 'PASS'; ws['B20'] = '公式勾稽通过。不代表预测真实、可实现或构成承诺。'
    ws['A21'] = 'REVIEW'; ws['B21'] = '公式可用但关键资料待补。可形成初版，外发时必须解释并降低结论强度。'
    ws['A22'] = 'FAIL'; ws['B22'] = '公式或数据勾稽错误，不得外发。'
    for r in (20, 21, 22):
        ws.cell(r, 1).font = F_HDR
    ws.column_dimensions['A'].width = 16
    for c in 'BCDEFGH':
        ws.column_dimensions[c].width = 18
    return ws


def sheet_needs(wb, cfg):
    ws = wb.create_sheet('数据需求')
    ws['A1'] = '高影响数据需求｜承做人应集中口头索取'; ws['A1'].font = F_TITLE
    ws['A3'] = ('原则：基础参数录入后，若某项数据项目方口头即可提供，且能显著降低反推、改善增长逻辑'
                '或回答投资人核心追问，应一次性集中索取；未获得不阻塞初版，但必须在模型和Word中标注待核实。')
    ws['A3'].alignment = WRAP; ws.merge_cells('A3:G4')
    hdr = ['编号', '建议索取的数据', '当前状态', '优先级', '为何显著提升质量', '建议问法', '未取得时处理']
    for j, h in enumerate(hdr):
        c = ws.cell(6, 1 + j, h); c.font = F_HDR; c.fill = FILL_HDR; c.border = BOX
    for k, d in enumerate(cfg['data_needs']):
        r = 7 + k
        for j, key in enumerate(['id', 'item', 'status', 'priority', 'why', 'ask', 'fallback']):
            c = ws.cell(r, 1 + j, d.get(key, ''))
            c.font = F_TXT; c.alignment = WRAP; c.border = BOX
            if key == 'priority' and d.get(key) in ('极高', '高'):
                c.fill = FILL_TODO
    end = 7 + len(cfg['data_needs'])
    ws.cell(end + 1, 1, '口头请求纪律').font = F_HDR
    ws.cell(end + 1, 2, '一次性集中提出，不零散追问；说明用途和影响；不要求项目方为未知数据编造精确值。')
    ws.cell(end + 2, 1, '可接受替代').font = F_HDR
    ws.cell(end + 2, 2, '精确数没有时，可接受区间、数量级、订单清单、合同截图或管理层底线假设。')
    ws.cell(end + 3, 1, '版本处理').font = F_HDR
    ws.cell(end + 3, 2, '项目方未回复不阻塞初版；对应结果标为反推/情景值，并在BP中避免承诺式措辞。')
    for c, w in zip('ABCDEFG', [8, 30, 12, 10, 34, 38, 26]):
        ws.column_dimensions[c].width = w
    return ws


def sheet_assump(wb, cfg, R):
    ws = wb.create_sheet('来源与假设')
    n = len(cfg['years'])
    ws['A1'] = '来源与假设｜唯一可编辑输入区（蓝字），其余各表均为公式'; ws['A1'].font = F_TITLE
    ws['A3'] = '模型口径'; ws['A3'].font = F_HDR
    ws['B3'] = cfg['scope_note']
    year_header(ws, 5, cfg)
    ws.cell(5, 3 + n, '数据角色').font = F_HDR; ws.cell(5, 3 + n).fill = FILL_HDR
    ws.cell(5, 4 + n, '来源/说明').font = F_HDR; ws.cell(5, 4 + n).fill = FILL_HDR
    r = 6
    put(ws, r, '收入驱动', font=F_SEC); r += 1
    for s in cfg['segments']:
        R[s['name']] = {}
        if s['driver'] == 'growth':
            put(ws, r, f"{s['name']}｜收入基数", cfg['unit'])
            ws.cell(r, 3, s['base']).font = F_IN
            ws.cell(r, 3).number_format = FMT_AMT
            ws.cell(r, 3).fill = FILL_HIST
            R[s['name']]['base'] = r
            _role(ws, r, n, '历史基数', s.get('src_base', '项目方历史报表'))
            r += 1
            put(ws, r, f"{s['name']}｜收入增速", '%')
            row_vals(ws, r, s['growth'], FMT_PCT, F_IN,
                     FILL_BACK if cfg['mode'] == 'A' else None)
            R[s['name']]['growth'] = r
            _role(ws, r, n, '反推输入' if cfg['mode'] == 'A' else '预测输入',
                  s.get('src_growth', '由原表收入反推，保留为可编辑假设'))
            r += 1
        elif s['driver'] == 'unit':
            put(ws, r, f"{s['name']}｜期末累计{s['unit_name']}", s.get('qty_unit', '个'))
            row_vals(ws, r, s['qty'], FMT_QTY, F_IN)
            R[s['name']]['qty'] = r
            _role(ws, r, n, '经营输入', s.get('src_qty', '项目方经营计划'))
            r += 1
            put(ws, r, f"{s['name']}｜期初累计{s['unit_name']}", s.get('qty_unit', '个'))
            ws.cell(r, 3, s.get('qty_open0', 0)).font = F_IN
            ws.cell(r, 3).number_format = FMT_QTY
            for i in range(1, n):
                c = ws.cell(r, 3 + i, f"={col(i-1)}{R[s['name']]['qty']}")
                c.font = F_CALC; c.number_format = FMT_QTY
            R[s['name']]['qty_open'] = r
            _role(ws, r, n, '公式/起点', '首年期初由项目方确认；其后取上年期末')
            r += 1
            put(ws, r, f"{s['name']}｜单{s['unit_name']}年创收", f"{cfg['unit']}/年")
            row_vals(ws, r, s['price'], FMT_AMT, F_IN)
            R[s['name']]['price'] = r
            _role(ws, r, n, '经营输入', s.get('src_price', '项目方定价/运营数据'))
            r += 1
            put(ws, r, f"{s['name']}｜利用率/投运系数", '%')
            row_vals(ws, r, s['util'], FMT_PCT, F_IN,
                     FILL_BACK if cfg['mode'] == 'A' else FILL_TODO)
            R[s['name']]['util'] = r
            _role(ws, r, n, '反推输入' if cfg['mode'] == 'A' else '待核实输入',
                  s.get('src_util', '按平均数量反推以复现目标收入，须由投运月份和真实使用率核实'))
            r += 1
        elif s['driver'] == 'share':
            put(ws, r, f"{s['name']}｜目标市占率", '%')
            row_vals(ws, r, s['share'], FMT_PCT, F_IN,
                     FILL_BACK if cfg['mode'] == 'A' else None)
            R[s['name']]['share'] = r
            _role(ws, r, n, '预测输入', s.get('src_share', '管理层目标，须与订单和产能校验'))
            r += 1
    r += 1
    put(ws, r, '利润表假设', font=F_SEC); r += 1
    p = cfg['pnl']
    spec = [('综合毛利率', '%', 'gross_margin', FMT_PCT, '缺分业务毛利率时只能使用综合口径'),
            ('销售费用率', '%', 'sales_rate', FMT_PCT, ''),
            ('管理费用率', '%', 'admin_rate', FMT_PCT, ''),
            ('研发费用率', '%', 'rd_rate', FMT_PCT, ''),
            ('财务费用', cfg['unit'], 'fin_exp', FMT_AMT, ''),
            ('未列示调整项（待核实）', cfg['unit'], 'other_adj', FMT_AMT,
             '使可见科目与目标营业利润勾稽的差额，必须向项目方核实，不得直接写入BP'),
            ('所得税率', '%', 'tax_rate', FMT_PCT, '须核实亏损结转与税收优惠')]
    for label, unit, key, fmt, note in spec:
        put(ws, r, label, unit)
        fill = FILL_BACK if (key == 'other_adj' and any(p[key])) else None
        row_vals(ws, r, p[key], fmt, F_IN, fill)
        R[key] = r
        _role(ws, r, n, '反推项' if key == 'other_adj' else '预测输入', note or '项目方/原表')
        r += 1
    r += 1
    put(ws, r, '外部行业锚点（待补；不阻塞初版）', font=F_SEC); r += 1
    ws.cell(r, 1, '业务').font = F_HDR
    ws.cell(r, 2, '口径').font = F_HDR
    for i, y in enumerate(cfg['years']):
        ws.cell(r, 3 + i, f'{y}行业规模').font = F_HDR
    ws.cell(r, 3 + n, '行业平均毛利率').font = F_HDR
    ws.cell(r, 4 + n, '来源/报告').font = F_HDR
    r += 1
    R['market_top'] = r
    for s in cfg['segments']:
        ws.cell(r, 1, s['name']).font = F_TXT
        ws.cell(r, 2, '金额口径').font = F_NOTE
        for i in range(n):
            c = ws.cell(r, 3 + i, s.get('market', [None] * n)[i] if s.get('market') else None)
            c.font = F_IN; c.number_format = FMT_AMT; c.fill = FILL_TODO
        ws.cell(r, 3 + n).fill = FILL_TODO
        ws.cell(r, 4 + n, s.get('market_src', '待补')).font = F_NOTE
        R[s['name']]['mkt_row'] = r
        r += 1
    R['market_bot'] = r - 1
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 10
    for i in range(n):
        ws.column_dimensions[col(i)].width = 14
    ws.column_dimensions[col(n)].width = 14
    ws.column_dimensions[col(n + 1)].width = 46
    return ws


def sheet_biz(wb, cfg, R):
    ws = wb.create_sheet('业务预测')
    A, n = '来源与假设', len(cfg['years'])
    ws['A1'] = '业务预测｜经营驱动与市场边界校验'; ws['A1'].font = F_TITLE
    year_header(ws, 3, cfg)
    r = 5
    rev_rows = {}
    for s in cfg['segments']:
        put(ws, r, s['name'], font=F_SEC); r += 1
        if s['driver'] == 'growth':
            put(ws, r, '收入', cfg['unit'])
            ws.cell(r, 3, f"={xref(A, R[s['name']]['base'], 0)}").font = F_LINK
            ws.cell(r, 3).number_format = FMT_AMT
            for i in range(1, n):
                c = ws.cell(r, 3 + i,
                            f"={col(i-1)}{r}*(1+{xref(A, R[s['name']]['growth'], i)})")
                c.font = F_CALC; c.number_format = FMT_AMT
            rev_rows[s['name']] = r; r += 1
        elif s['driver'] == 'unit':
            base = r
            for lbl, key, fmt in [('期初累计', 'qty_open', FMT_QTY),
                                  ('期末累计', 'qty', FMT_QTY),
                                  (f"单{s['unit_name']}年创收", 'price', FMT_AMT),
                                  ('利用率/投运系数', 'util', FMT_PCT)]:
                put(ws, r, lbl, s.get('qty_unit', '个') if 'qty' in key else '')
                for i in range(n):
                    c = ws.cell(r, 3 + i, f"={xref(A, R[s['name']][key], i)}")
                    c.font = F_LINK; c.number_format = fmt
                R[s['name']][key + '_b'] = r
                r += 1
            put(ws, r, '平均有效数量', s.get('qty_unit', '个'))
            for i in range(n):
                c = ws.cell(r, 3 + i, f"=AVERAGE({col(i)}{base},{col(i)}{base+1})")
                c.font = F_CALC; c.number_format = FMT_QTY
            avg_r = r; r += 1
            put(ws, r, '收入', cfg['unit'])
            for i in range(n):
                c = ws.cell(r, 3 + i, f"={col(i)}{avg_r}*{col(i)}{base+2}*{col(i)}{base+3}")
                c.font = F_CALC; c.number_format = FMT_AMT
            rev_rows[s['name']] = r; r += 1
        elif s['driver'] == 'share':
            put(ws, r, '可服务市场规模', cfg['unit'])
            for i in range(n):
                c = ws.cell(r, 3 + i, f"={xref(A, R[s['name']]['mkt_row'], i)}")
                c.font = F_LINK; c.number_format = FMT_AMT
            m_r = r; r += 1
            put(ws, r, '目标市占率', '%')
            for i in range(n):
                c = ws.cell(r, 3 + i, f"={xref(A, R[s['name']]['share'], i)}")
                c.font = F_LINK; c.number_format = FMT_PCT
            s_r = r; r += 1
            put(ws, r, '收入', cfg['unit'])
            for i in range(n):
                c = ws.cell(r, 3 + i, f"={col(i)}{m_r}*{col(i)}{s_r}")
                c.font = F_CALC; c.number_format = FMT_AMT
            rev_rows[s['name']] = r; r += 1
        put(ws, r, '收入增速', '%')
        for i in range(1, n):
            c = ws.cell(r, 3 + i,
                        f"=IFERROR({col(i)}{rev_rows[s['name']]}/{col(i-1)}{rev_rows[s['name']]}-1,\"\")")
            c.font = F_CALC; c.number_format = FMT_PCT
        r += 2
    put(ws, r, '收入汇总', font=F_SEC); r += 1
    R['rev_top'] = r
    for s in cfg['segments']:
        put(ws, r, s['name'], cfg['unit'])
        for i in range(n):
            c = ws.cell(r, 3 + i, f"={col(i)}{rev_rows[s['name']]}")
            c.font = F_CALC; c.number_format = FMT_AMT
        R[s['name']]['rev'] = r
        r += 1
    R['rev_bot'] = r - 1
    put(ws, r, '营业收入', cfg['unit'], font=F_HDR)
    for i in range(n):
        c = ws.cell(r, 3 + i, f"=SUM({col(i)}{R['rev_top']}:{col(i)}{R['rev_bot']})")
        c.font = F_HDR; c.number_format = FMT_AMT
    R['revenue'] = r; r += 1
    R['mix_top'] = r
    for s in cfg['segments']:
        put(ws, r, f"{s['name']}占比", '%')
        for i in range(n):
            c = ws.cell(r, 3 + i,
                        f"=IFERROR({col(i)}{R[s['name']]['rev']}/{col(i)}{R['revenue']},0)")
            c.font = F_CALC; c.number_format = FMT_PCT
        R[s['name']]['mix'] = r
        r += 1
    R['mix_bot'] = r - 1
    put(ws, r, '业务占比合计', '%')
    for i in range(n):
        c = ws.cell(r, 3 + i, f"=SUM({col(i)}{R['mix_top']}:{col(i)}{R['mix_bot']})")
        c.font = F_CALC; c.number_format = FMT_PCT
    R['mix_sum'] = r; r += 2
    put(ws, r, '外部基本面校验（行业规模未补时留空，不输出伪精度）', font=F_SEC); r += 1
    R['imp_top'] = r
    for s in cfg['segments']:
        put(ws, r, f"{s['name']}隐含市占率", '%')
        for i in range(n):
            c = ws.cell(r, 3 + i,
                        f"=IFERROR({col(i)}{R[s['name']]['rev']}/{xref('来源与假设', R[s['name']]['mkt_row'], i)},\"\")")
            c.font = F_CALC; c.number_format = FMT_PCT
        r += 1
    R['imp_bot'] = r - 1
    ws.column_dimensions['A'].width = 28
    ws.column_dimensions['B'].width = 10
    for i in range(n):
        ws.column_dimensions[col(i)].width = 14
    return ws


def sheet_pnl(wb, cfg, R):
    ws = wb.create_sheet('利润表')
    A, B, n = '来源与假设', '业务预测', len(cfg['years'])
    ws['A1'] = f"利润表预测｜单位：{cfg['unit']}"; ws['A1'].font = F_TITLE
    year_header(ws, 3, cfg)
    r = 5

    def line(label, unit, formula, fmt, font=F_CALC, key=None):
        nonlocal r
        put(ws, r, label, unit, font=F_HDR if font is F_HDR else F_TXT)
        for i in range(n):
            c = ws.cell(r, 3 + i, formula(i))
            c.font = font; c.number_format = fmt
        if key:
            R[key] = r
        r += 1

    line('营业收入', cfg['unit'], lambda i: f"={xref(B, R['revenue'], i)}", FMT_AMT, F_LINK, 'p_rev')
    line('收入增速', '%', lambda i: f"=IFERROR({col(i)}{R['p_rev']}/{col(i-1)}{R['p_rev']}-1,\"\")" if i else None, FMT_PCT)
    line('综合毛利率', '%', lambda i: f"={xref(A, R['gross_margin'], i)}", FMT_PCT, F_LINK, 'p_gm')
    line('营业成本', cfg['unit'], lambda i: f"={col(i)}{R['p_rev']}*(1-{col(i)}{R['p_gm']})", FMT_AMT, F_CALC, 'p_cost')
    line('毛利润', cfg['unit'], lambda i: f"={col(i)}{R['p_rev']}-{col(i)}{R['p_cost']}", FMT_AMT, F_CALC, 'p_gross')
    line('销售费用率', '%', lambda i: f"={xref(A, R['sales_rate'], i)}", FMT_PCT, F_LINK, 'p_sr')
    line('销售费用', cfg['unit'], lambda i: f"={col(i)}{R['p_rev']}*{col(i)}{R['p_sr']}", FMT_AMT, F_CALC, 'p_sales')
    line('管理费用率', '%', lambda i: f"={xref(A, R['admin_rate'], i)}", FMT_PCT, F_LINK, 'p_ar')
    line('管理费用', cfg['unit'], lambda i: f"={col(i)}{R['p_rev']}*{col(i)}{R['p_ar']}", FMT_AMT, F_CALC, 'p_admin')
    line('研发费用率', '%', lambda i: f"={xref(A, R['rd_rate'], i)}", FMT_PCT, F_LINK, 'p_rr')
    line('研发费用', cfg['unit'], lambda i: f"={col(i)}{R['p_rev']}*{col(i)}{R['p_rr']}", FMT_AMT, F_CALC, 'p_rd')
    line('财务费用', cfg['unit'], lambda i: f"={xref(A, R['fin_exp'], i)}", FMT_AMT, F_LINK, 'p_fin')
    line('未列示调整项（待核实）', cfg['unit'], lambda i: f"={xref(A, R['other_adj'], i)}", FMT_AMT, F_LINK, 'p_adj')
    line('营业利润', cfg['unit'],
         lambda i: (f"={col(i)}{R['p_gross']}-{col(i)}{R['p_sales']}-{col(i)}{R['p_admin']}"
                    f"-{col(i)}{R['p_rd']}-{col(i)}{R['p_fin']}+{col(i)}{R['p_adj']}"),
         FMT_AMT, F_HDR, 'p_op')
    line('所得税率', '%', lambda i: f"={xref(A, R['tax_rate'], i)}", FMT_PCT, F_LINK, 'p_tr')
    line('所得税', cfg['unit'], lambda i: f"=MAX(0,{col(i)}{R['p_op']}*{col(i)}{R['p_tr']})", FMT_AMT, F_CALC, 'p_tax')
    line('净利润', cfg['unit'], lambda i: f"={col(i)}{R['p_op']}-{col(i)}{R['p_tax']}", FMT_AMT, F_HDR, 'p_ni')
    line('净利率', '%', lambda i: f"=IFERROR({col(i)}{R['p_ni']}/{col(i)}{R['p_rev']},0)", FMT_PCT, F_CALC, 'p_nm')
    r += 1
    for lbl, txt in [('调整项', '「未列示调整项」为使可见科目与目标营业利润勾稽的差额，须向项目方核实，不得直接写入BP。'),
                     ('毛利限制', '缺少分业务毛利率时只能使用综合毛利率，不得声称毛利改善来自业务结构变化。'),
                     ('税务', '税率沿用项目方口径，须核实亏损结转、税收优惠及资质有效期。')]:
        ws.cell(r, 1, lbl).font = F_HDR
        ws.cell(r, 2, txt).font = F_NOTE
        r += 1
    ws.column_dimensions['A'].width = 24
    ws.column_dimensions['B'].width = 10
    for i in range(n):
        ws.column_dimensions[col(i)].width = 14
    return ws


def sheet_growth(wb, cfg, R):
    ws = wb.create_sheet('增长分析')
    B, P, n = '业务预测', '利润表', len(cfg['years'])
    k = n - 1
    ws['A1'] = '增长与基本面分析'; ws['A1'].font = F_TITLE
    span = f"{cfg['years'][0]}A-{cfg['years'][-1]}E"
    hdrs = [('收入CAGR', f"=IFERROR(('{P}'!{col(k)}{R['p_rev']}/'{P}'!C{R['p_rev']})^(1/{k})-1,0)"),
            ('末年净利率', f"=IFERROR('{P}'!{col(k)}{R['p_ni']}/'{P}'!{col(k)}{R['p_rev']},0)"),
            ('主业务末年占比', f"=IFERROR('{B}'!{col(k)}{R[cfg['lead_segment']]['mix']},0)"),
            ('净利润CAGR', f"=IFERROR(('{P}'!{col(k)}{R['p_ni']}/'{P}'!C{R['p_ni']})^(1/{k})-1,0)")]
    for j, (lbl, f) in enumerate(hdrs):
        ws.cell(4, 1 + j * 2, '口径').font = F_HDR
        ws.cell(4, 2 + j * 2, lbl).font = F_HDR
        ws.cell(5, 1 + j * 2, span).font = F_TXT
        c = ws.cell(5, 2 + j * 2, f); c.font = F_LINK; c.number_format = FMT_PCT
    ws['A7'] = '分业务增长与结构'; ws['A7'].font = F_SEC
    for j, h in enumerate(['业务', '首年收入', '末年收入', f'{k}年CAGR', '首年占比', '末年占比', '判断']):
        c = ws.cell(8, 1 + j, h); c.font = F_HDR; c.fill = FILL_HDR
    for m, s in enumerate(cfg['segments']):
        r = 9 + m
        ws.cell(r, 1, s['name']).font = F_TXT
        ws.cell(r, 2, f"='{B}'!C{R[s['name']]['rev']}").font = F_LINK
        ws.cell(r, 3, f"='{B}'!{col(k)}{R[s['name']]['rev']}").font = F_LINK
        ws.cell(r, 4, f"=IFERROR((C{r}/B{r})^(1/{k})-1,\"\")").font = F_CALC
        ws.cell(r, 5, f"='{B}'!C{R[s['name']]['mix']}").font = F_LINK
        ws.cell(r, 6, f"='{B}'!{col(k)}{R[s['name']]['mix']}").font = F_LINK
        ws.cell(r, 7, s.get('verdict', '')).font = F_TXT
        for cc in (2, 3):
            ws.cell(r, cc).number_format = FMT_AMT
        for cc in (4, 5, 6):
            ws.cell(r, cc).number_format = FMT_PCT
    base = 9 + len(cfg['segments']) + 1
    ws.cell(base, 1, '年度收入增量贡献').font = F_SEC
    ws.cell(base + 1, 1, '业务').font = F_HDR
    for i in range(1, n):
        ws.cell(base + 1, 1 + i, f"{cfg['years'][i]}增量").font = F_HDR
    ws.cell(base + 1, 1 + n, '末年增量贡献').font = F_HDR
    for m, s in enumerate(cfg['segments']):
        r = base + 2 + m
        ws.cell(r, 1, s['name']).font = F_TXT
        rr = R[s['name']]['rev']
        for i in range(1, n):
            c = ws.cell(r, 1 + i, f"='{B}'!{col(i)}{rr}-'{B}'!{col(i-1)}{rr}")
            c.font = F_CALC; c.number_format = FMT_AMT
        c = ws.cell(r, 1 + n,
                    f"=IFERROR(('{B}'!{col(k)}{rr}-'{B}'!{col(k-1)}{rr})/"
                    f"('{B}'!{col(k)}{R['revenue']}-'{B}'!{col(k-1)}{R['revenue']}),\"\")")
        c.font = F_CALC; c.number_format = FMT_PCT
    note = base + 2 + len(cfg['segments']) + 1
    for j, (a, b) in enumerate(cfg['growth_notes']):
        ws.cell(note + j, 1, a).font = F_HDR
        c = ws.cell(note + j, 2, b); c.font = F_TXT; c.alignment = WRAP
        ws.merge_cells(start_row=note + j, start_column=2, end_row=note + j, end_column=7)
    ws.column_dimensions['A'].width = 20
    for c in 'BCDEF':
        ws.column_dimensions[c].width = 16
    ws.column_dimensions['G'].width = 34
    return ws


def sheet_cash(wb, cfg, R):
    ws = wb.create_sheet('现金流与IRR')
    P, n = '利润表', len(cfg['years'])
    ws['A1'] = '现金流与IRR｜数据不足时保持空白，不制造伪精度'; ws['A1'].font = F_TITLE
    year_header(ws, 3, cfg)
    ws['A5'] = '公司自由现金流'; ws['A5'].font = F_SEC
    rows = [('营业利润', lambda i: f"='{P}'!{col(i)}{R['p_op']}", F_LINK),
            ('现金所得税', lambda i: f"='{P}'!{col(i)}{R['p_tax']}", F_LINK),
            ('税后经营利润（简化）', lambda i: f"={col(i)}6-{col(i)}7", F_CALC),
            ('折旧摊销', lambda i: None, F_IN),
            ('资本开支', lambda i: None, F_IN),
            ('营运资金增加', lambda i: None, F_IN)]
    r = 6
    for lbl, f, fo in rows:
        put(ws, r, lbl, cfg['unit'])
        for i in range(n):
            c = ws.cell(r, 3 + i, f(i)); c.font = fo; c.number_format = FMT_AMT
            if fo is F_IN:
                c.fill = FILL_TODO
        r += 1
    put(ws, r, '自由现金流', cfg['unit'], font=F_HDR)
    for i in range(n):
        c = ws.cell(r, 3 + i,
                    f"=IF(COUNT({col(i)}9:{col(i)}11)<3,\"\",{col(i)}8+{col(i)}9-{col(i)}10-{col(i)}11)")
        c.font = F_HDR; c.number_format = FMT_AMT
    r += 2
    ws.cell(r, 1, '投资者现金流与IRR').font = F_SEC
    r += 1
    top = r
    for lbl in ['投资现金流（负数）', '追加投资（负数）', '分红/回购回款', '退出回款']:
        put(ws, r, lbl, cfg['unit'])
        for i in range(n):
            c = ws.cell(r, 3 + i); c.font = F_IN; c.number_format = FMT_AMT; c.fill = FILL_TODO
        r += 1
    put(ws, r, '投资者净现金流', cfg['unit'], font=F_HDR)
    for i in range(n):
        c = ws.cell(r, 3 + i, f"=SUM({col(i)}{top}:{col(i)}{r-1})")
        c.font = F_HDR; c.number_format = FMT_AMT
    net = r; r += 1
    put(ws, r, 'IRR', '%', font=F_HDR)
    rng = f"C{net}:{col(n-1)}{net}"
    c = ws.cell(r, 3, f"=IF(AND(COUNTIF({rng},\"<0\")>0,COUNTIF({rng},\">0\")>0),IRR({rng}),\"待补充现金流\")")
    c.font = F_HDR; c.number_format = FMT_PCT
    R['irr_net'] = net
    r += 2
    ws.cell(r, 1, '说明').font = F_HDR
    ws.cell(r, 2, 'IRR是融资与退出现金流的结果，不由经营增长率推导；CAGR与IRR不可互相替代。').font = F_NOTE
    ws.column_dimensions['A'].width = 24
    ws.column_dimensions['B'].width = 10
    for i in range(n):
        ws.column_dimensions[col(i)].width = 14
    return ws


def sheet_check(wb, cfg, R):
    ws = wb.create_sheet('校验')
    B, P, n = '业务预测', '利润表', len(cfg['years'])
    k = n - 1
    ws['A1'] = '模型校验｜FAIL必须修复，REVIEW必须解释'; ws['A1'].font = F_TITLE
    ws['A3'] = '模型状态'; ws['A3'].font = F_HDR
    ws['C3'] = '检查日期'; ws['C3'].font = F_HDR
    ws['D3'] = cfg['check_date']
    for j, h in enumerate(['检查项', '实际', '预期', '差异', '容差', '状态', '修复位置/说明']):
        c = ws.cell(5, 1 + j, h); c.font = F_HDR; c.fill = FILL_HDR; c.border = BOX
    checks = []
    checks.append(('收入分部合计=利润表收入', f"='{B}'!{col(k)}{R['revenue']}",
                   f"='{P}'!{col(k)}{R['p_rev']}", 0.01, 'hard', '业务预测/利润表'))
    checks.append(('业务占比合计=100%', f"='{B}'!{col(k)}{R['mix_sum']}", 1, 0.0001, 'hard', '业务预测'))
    checks.append(('综合毛利率在0%-100%',
                   f"=MIN('{P}'!C{R['p_gm']}:{col(k)}{R['p_gm']})", 0, 0, 'range', '来源与假设'))
    checks.append(('净利率不超过毛利率',
                   f"=MAX('{P}'!C{R['p_nm']}:{col(k)}{R['p_nm']})-MAX('{P}'!C{R['p_gm']}:{col(k)}{R['p_gm']})",
                   0, 0.0001, 'le', '利润表'))
    if cfg['mode'] == 'A' and cfg.get('reference'):
        for i, y in enumerate(cfg['years']):
            checks.append((f'{y}收入与原始参考一致', f"='{P}'!{col(i)}{R['p_rev']}",
                           f"='原始参考'!{col(i)}{R['ref_rev']}", 0.01, 'hard', '来源与假设'))
        for i, y in enumerate(cfg['years']):
            checks.append((f'{y}营业利润与原始参考一致', f"='{P}'!{col(i)}{R['p_op']}",
                           f"='原始参考'!{col(i)}{R['ref_op']}", 0.01, 'hard', '未列示调整项'))
    else:
        checks.append(('末年收入增速未超过设定上限',
                       f"=IFERROR('{P}'!{col(k)}{R['p_rev']}/'{P}'!{col(k-1)}{R['p_rev']}-1,0)",
                       cfg.get('growth_cap', 3.0), 0, 'le', '来源与假设：驱动参数'))
        checks.append(('三项费用率合计小于综合毛利率',
                       f"='{P}'!{col(k)}{R['p_sr']}+'{P}'!{col(k)}{R['p_ar']}+'{P}'!{col(k)}{R['p_rr']}",
                       f"='{P}'!{col(k)}{R['p_gm']}", 0, 'le', '来源与假设：费用率'))
    for s in cfg['segments']:
        if s['driver'] == 'unit':
            ur = R[s['name']]['util_b']
            checks.append((f"{s['name']}｜利用率不超过100%",
                           f"=MAX('{B}'!C{ur}:{col(k)}{ur})", 1, 0, 'lefail',
                           '来源与假设：利用率>100%说明单位创收假设与目标收入不自洽'))
    if R.get('imp_top') is not None:
        cap = cfg.get('share_cap', 0.30)
        checks.append(('隐含市占率未超过上限',
                       f"=IF(COUNT('{B}'!C{R['imp_top']}:{col(k)}{R['imp_bot']})=0,\"\","
                       f"MAX('{B}'!C{R['imp_top']}:{col(k)}{R['imp_bot']}))",
                       cap, 0, 'cap', '行业规模未补时不判定；补齐后超上限须回调驱动或重定义市场'))
    checks.append(('行业市场规模已补充',
                   f"=COUNT('来源与假设'!C{R['market_top']}:{col(k)}{R['market_bot']})",
                   n * len(cfg['segments']), 0, 'soft', '数据需求：行业规模'))
    irng = f"'现金流与IRR'!C{R['irr_net']}:{col(k)}{R['irr_net']}"
    checks.append(('IRR现金流已补充（需一负一正）',
                   f"=COUNTIF({irng},\"<0\")+COUNTIF({irng},\">0\")", '需一负一正', 0, 'irr',
                   '数据需求：融资与退出'))
    r = 6
    for name, act, exp, tol, kind, fix in checks:
        ws.cell(r, 1, name).font = F_TXT
        ws.cell(r, 2, act).font = F_LINK
        ws.cell(r, 3, exp).font = F_TXT
        ws.cell(r, 5, tol).font = F_NOTE
        if kind == 'range':
            ws.cell(r, 4, f"=IF(AND(MIN('{P}'!C{R['p_gm']}:{col(k)}{R['p_gm']})>=0,"
                          f"MAX('{P}'!C{R['p_gm']}:{col(k)}{R['p_gm']})<=1),0,1)")
            ws.cell(r, 6, f'=IF(D{r}=0,"PASS","FAIL")')
        elif kind == 'le':
            ws.cell(r, 4, f"=B{r}-C{r}")
            ws.cell(r, 6, f'=IF(D{r}<=E{r},"PASS","WARN")')
        elif kind == 'lefail':
            ws.cell(r, 4, f"=B{r}-C{r}")
            ws.cell(r, 6, f'=IF(D{r}<=E{r},"PASS","FAIL")')
        elif kind == 'soft':
            ws.cell(r, 4, f"=B{r}-C{r}")
            ws.cell(r, 6, f'=IF(B{r}>=C{r},"PASS","WARN")')
        elif kind == 'cap':
            ws.cell(r, 4, f'=IF(B{r}="","",B{r}-C{r})')
            ws.cell(r, 6, f'=IF(B{r}="","N/A",IF(B{r}<=C{r},"PASS","FAIL"))')
        elif kind == 'irr':
            ws.cell(r, 4, '')
            ws.cell(r, 6, f'=IF(AND(COUNTIF({irng},"<0")>0,COUNTIF({irng},">0")>0),"PASS","WARN")')
        else:
            ws.cell(r, 4, f"=B{r}-C{r}")
            ws.cell(r, 6, f'=IF(ABS(D{r})<=E{r},"PASS","FAIL")')
        ws.cell(r, 4).number_format = FMT_AMT
        ws.cell(r, 6).font = F_HDR
        ws.cell(r, 6).alignment = Alignment(horizontal='center')
        ws.cell(r, 7, fix).font = F_NOTE
        for j in range(1, 8):
            ws.cell(r, j).border = BOX
        r += 1
    ws['F3'] = (f'=IF(COUNTIF(F6:F{r-1},"FAIL")>0,"FAIL",'
                f'IF(COUNTIF(F6:F{r-1},"WARN")>0,"REVIEW","PASS"))')
    ws['F3'].font = Font(name=FN, size=12, bold=True)
    ws['E3'] = '状态'; ws['E3'].font = F_HDR
    r += 1
    ws.cell(r, 1, '人工复核').font = F_HDR
    ws.cell(r, 2, cfg.get('manual_check', '反推值与未列示调整项必须向项目方核实；行业和IRR数据未补时保持REVIEW。')).font = F_NOTE
    ws.cell(r + 1, 1, '模型含义').font = F_HDR
    ws.cell(r + 1, 2, 'PASS仅代表公式勾稽，不代表预测真实、可实现或构成承诺。').font = F_NOTE
    for c, w in zip('ABCDEFG', [34, 16, 16, 14, 10, 10, 30]):
        ws.column_dimensions[c].width = w
    return ws


def sheet_bp(wb, cfg, R):
    ws = wb.create_sheet('BP输出')
    B, P, G, n = '业务预测', '利润表', '增长分析', len(cfg['years'])
    k = n - 1
    ws['A1'] = f"{cfg['years'][0]}A-{cfg['years'][-1]}E财务预测｜BP外发参考"; ws['A1'].font = F_TITLE
    ws['A3'] = cfg['disclaimer']; ws['A3'].alignment = WRAP
    ws.merge_cells('A3:H4')
    hdr = ['核心指标'] + [f"{y}{'A' if i < cfg['hist_n'] else 'E'}" for i, y in enumerate(cfg['years'])] + ['CAGR', '模型状态']
    for j, h in enumerate(hdr):
        c = ws.cell(6, 1 + j, h); c.font = F_HDR; c.fill = FILL_HDR; c.border = BOX
    metrics = [('营业收入', R['p_rev'], FMT_AMT, f"='{G}'!B5"),
               ('综合毛利率', R['p_gm'], FMT_PCT, None),
               ('净利润', R['p_ni'], FMT_AMT, f"='{G}'!H5"),
               ('净利率', R['p_nm'], FMT_PCT, None)]
    for m, (lbl, row, fmt, cagr) in enumerate(metrics):
        r = 7 + m
        ws.cell(r, 1, lbl).font = F_TXT
        for i in range(n):
            c = ws.cell(r, 2 + i, f"='{P}'!{col(i)}{row}")
            c.font = F_LINK; c.number_format = fmt
        if cagr:
            c = ws.cell(r, 2 + n, cagr); c.font = F_LINK; c.number_format = FMT_PCT
        if m == 0:
            ws.cell(r, 3 + n, "='校验'!F3").font = F_HDR
    base = 7 + len(metrics) + 1
    ws.cell(base, 1, '分业务收入').font = F_SEC
    for j, h in enumerate(['业务'] + [str(y) for y in cfg['years']] + ['末年占比']):
        c = ws.cell(base + 1, 1 + j, h); c.font = F_HDR; c.fill = FILL_HDR
    for m, s in enumerate(cfg['segments']):
        r = base + 2 + m
        ws.cell(r, 1, s['name']).font = F_TXT
        for i in range(n):
            c = ws.cell(r, 2 + i, f"='{B}'!{col(i)}{R[s['name']]['rev']}")
            c.font = F_LINK; c.number_format = FMT_AMT
        c = ws.cell(r, 2 + n, f"='{B}'!{col(k)}{R[s['name']]['mix']}")
        c.font = F_LINK; c.number_format = FMT_PCT
    txt = base + 1 + len(cfg['segments']) + 2
    ws.cell(txt, 1, '可直接写入BP的财务与增长判断').font = F_SEC
    for j, (a, b) in enumerate(cfg['bp_text']):
        ws.cell(txt + 1 + j, 1, a).font = F_HDR
        c = ws.cell(txt + 1 + j, 2, b); c.font = F_TXT; c.alignment = WRAP
        ws.merge_cells(start_row=txt + 1 + j, start_column=2, end_row=txt + 1 + j, end_column=8)
        ws.row_dimensions[txt + 1 + j].height = 32
    d = 20 + len(cfg['segments'])
    ws.cell(2, d, '年份').font = F_NOTE
    ws.cell(2, d + 1, '营业收入').font = F_NOTE
    ws.cell(2, d + 2, '净利润').font = F_NOTE
    for i, y in enumerate(cfg['years']):
        ws.cell(3 + i, d, str(y))
        ws.cell(3 + i, d + 1, f"='{P}'!{col(i)}{R['p_rev']}")
        ws.cell(3 + i, d + 2, f"='{P}'!{col(i)}{R['p_ni']}")
    ch = LineChart(); ch.title = '营业收入与净利润趋势'; ch.height = 7; ch.width = 13
    ch.add_data(Reference(ws, min_col=d + 1, max_col=d + 2, min_row=2, max_row=2 + n), titles_from_data=True)
    ch.set_categories(Reference(ws, min_col=d, min_row=3, max_row=2 + n))
    ws.add_chart(ch, f"A{txt + len(cfg['bp_text']) + 3}")
    pd_ = d + 4
    ws.cell(2, pd_, '业务').font = F_NOTE
    ws.cell(2, pd_ + 1, '末年收入').font = F_NOTE
    for m, s in enumerate(cfg['segments']):
        ws.cell(3 + m, pd_, s['name'])
        ws.cell(3 + m, pd_ + 1, f"='{B}'!{col(k)}{R[s['name']]['rev']}")
    pie = PieChart(); pie.title = f"{cfg['years'][-1]}E收入结构"; pie.height = 7; pie.width = 10
    pie.add_data(Reference(ws, min_col=pd_ + 1, min_row=2, max_row=2 + len(cfg['segments'])), titles_from_data=True)
    pie.set_categories(Reference(ws, min_col=pd_, min_row=3, max_row=2 + len(cfg['segments'])))
    ws.add_chart(pie, f"E{txt + len(cfg['bp_text']) + 3}")
    ws.column_dimensions['A'].width = 20
    for c in 'BCDEFGH':
        ws.column_dimensions[c].width = 15
    return ws


def sheet_ref(wb, cfg, R):
    ws = wb.create_sheet('原始参考')
    ref = cfg['reference']
    n = len(cfg['years'])
    ws['A1'] = '原始参考数据（保留原口径，仅作审计轨迹，不参与公式）'; ws['A1'].font = F_TITLE
    year_header(ws, 3, cfg)
    r = 5
    for lbl, key in [('营业收入', 'revenue'), ('营业利润', 'operating_profit'), ('净利润', 'net_profit')]:
        if not ref.get(key):
            continue
        put(ws, r, lbl, cfg['unit'])
        row_vals(ws, r, ref[key], FMT_AMT, F_TXT, FILL_HIST)
        R['ref_' + {'revenue': 'rev', 'operating_profit': 'op', 'net_profit': 'ni'}[key]] = r
        r += 1
    r += 1
    for s in cfg['segments']:
        if s.get('target'):
            put(ws, r, f"{s['name']}收入", cfg['unit'])
            row_vals(ws, r, s['target'], FMT_AMT, F_TXT, FILL_HIST)
            r += 1
    r += 1
    ws.cell(r, 1, '来源文件').font = F_HDR
    ws.cell(r, 2, ref.get('file', '')).font = F_NOTE
    ws.cell(r + 1, 1, '提取说明').font = F_HDR
    ws.cell(r + 1, 2, ref.get('note', '原文件未保留公式链，本模型据可见数值重建。')).font = F_NOTE
    ws.column_dimensions['A'].width = 24
    ws.column_dimensions['B'].width = 12
    for i in range(n):
        ws.column_dimensions[col(i)].width = 14
    return ws


def build(cfg, out):
    cfg = solve(copy.deepcopy(cfg))
    cfg['hist_n'] = cfg.get('hist_n', 1)
    cfg.setdefault('lead_segment', cfg['segments'][0]['name'])
    wb = Workbook(); wb.remove(wb.active)
    R = {}
    sheet_readme(wb, cfg)
    sheet_needs(wb, cfg)
    sheet_assump(wb, cfg, R)
    sheet_biz(wb, cfg, R)
    sheet_pnl(wb, cfg, R)
    sheet_growth(wb, cfg, R)
    sheet_cash(wb, cfg, R)
    if cfg['mode'] == 'A' and cfg.get('reference'):
        sheet_ref(wb, cfg, R)
    sheet_check(wb, cfg, R)
    sheet_bp(wb, cfg, R)
    order = ['使用说明', '数据需求', '来源与假设', '业务预测', '利润表', '增长分析',
             '现金流与IRR', '校验', 'BP输出', '原始参考']
    wb._sheets.sort(key=lambda s: order.index(s.title) if s.title in order else 99)
    wb.save(out)
    return out


if __name__ == '__main__':
    cfg = json.load(open(sys.argv[1], encoding='utf-8'))
    print(build(cfg, sys.argv[2]))
```

生成的工作簿：使用说明 / 数据需求 / 来源与假设 / 业务预测 / 利润表 / 增长分析 / 现金流与IRR / 校验 / BP输出 / 原始参考（仅模式A）。表间依赖严格单向：来源与假设 → 业务预测 → 利润表 → 现金流；业务预测与利润表 → 增长分析 → BP输出；校验横切读取全部。

## Word 承做底稿结构

用 docx skill 生成。数字全部取自上一步 LibreOffice 重算后的读回结果。

1. **交付说明与模型状态** — 用途、外发属性、PASS/REVIEW/FAIL 及理由
2. **口径与资料清单** — 币种单位、含税口径、合并范围、历史截止日、每份资料的来源与可信度分层（A可核验事实 / B项目方管理数据 / C外部参考 / D管理层假设 / E反推值）
3. **业务分部与驱动方式** — 每个分部：驱动方式、公式、数据来源，以及**是否做了量价拆分**（用 growth 的必须写明"暂用收入增速法"）
4. **计算方法** — 完整公式链，逐层展开：驱动 → 分部收入 → 综合毛利 → 期间费用 → 营业利润 → 所得税 → 净利润 → 现金流 → IRR
5. **反推值与假设清单** — 逐条列出反推了什么、怎么反推的、须核实什么。这是Word最核心的一节
6. **建议补充或核实的数据** — D01…Dn，含优先级、为何提升质量、建议问法、未取得时的处理
7. **简要财务分析（可写入BP）** — 收入与利润规模、CAGR、毛利率与净利率变化、驱动来源
8. **增长点分析（可写入BP）** — 各增长点的逻辑、所需证据、判断；投资人最可能追问的5个问题
9. **风险与实现条件** — 集中度风险、现金需求、交付约束、组织承载
10. **BP可直接引用的文本** — 财务分析段、增长点分析段、风险提示段，均为情景式措辞
11. **复核记录与签出结论**

第7、8、10节是要进BP的，措辞必须按下表。第1—6、9、11节是内部底稿，不外发。

## 措辞黑白名单

| 避免 | 推荐 |
|---|---|
| 确保实现 / 必然达到 / 承诺 | 预计 / 计划 / 目标 / 在该情景下 |
| 未来三年收入将达到 | 按现有经营假设，收入预计达到 |
| 市占率快速提升 | 在该行业规模口径下，隐含市占率预计稳步提升 |
| 毛利率随业务结构必然改善 | 按现有综合毛利率假设，盈利能力预计改善 |
| 投资人可获得X% IRR | 在所列投资、分红和退出假设下，测算IRR为X% |

BP文本结尾必须带一句前瞻性声明：预测基于现有资料、管理层经营计划和行业判断，用于展示业务发展情景，不构成对未来业绩的承诺或保证。

## 交付前复核清单

**Excel**

- 收入分部合计等于利润表收入；成本、毛利、费用、营业利润、所得税、净利润逐层勾稽
- 业务占比合计100%；综合毛利率在0%–100%；反推利用率不超过100%
- 模式A：历史与各年数值与原始参考一致
- 反推值和可编辑输入有明确颜色；行业数据未补时隐含市占率留空
- IRR现金流不足时保持空白，不用CAGR替代
- 公式错误扫描为0；FAIL为0；REVIEW均有书面解释

**Word 与 BP**

- 财务分析和增长点分析与Excel同口径，数字来自重算结果而非心算
- 预测使用情景式措辞，不写成业绩承诺
- 历史事实、预测值、团队历史业绩、行业数据四者不混淆
- 关键实现条件和集中风险已披露
- 来源、报告年份、口径和项目方确认日期已记录
- 敏感信息按项目要求脱敏，底稿不对外发送

## 签出规则

| 状态 | 能否外发 | 处理 |
|---|---|---|
| PASS | 可以 | 公式、来源和核心资料齐备；仍保留前瞻性声明 |
| REVIEW | 有条件 | 可形成初版或内部讨论版；必须解释待补事项并降低结论强度 |
| FAIL | 不可以 | 先修复公式、口径或数据矛盾 |

