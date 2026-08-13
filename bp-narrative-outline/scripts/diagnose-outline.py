#!/usr/bin/env python3
"""Emit non-blocking diagnostics for a bp-narrative-outline Markdown file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PAGE_RE = re.compile(r"^###\s+P(\d+)\s*[·.\-:]\s*(.+)$", re.MULTILINE)
MODULE_RE = re.compile(r"^-\s*模块(\d+)", re.MULTILINE)


def diagnose(text: str) -> list[str]:
    warnings: list[str] = []
    pages = list(PAGE_RE.finditer(text))
    if not pages:
        warnings.append("未识别到 `### P{N} · 页面功能` 页面标题。")
        return warnings

    numbers = [int(match.group(1)) for match in pages]
    expected = list(range(numbers[0], numbers[0] + len(numbers)))
    if numbers != expected:
        warnings.append(f"页码可能不连续：{numbers}")

    for index, match in enumerate(pages):
        start = match.start()
        end = pages[index + 1].start() if index + 1 < len(pages) else len(text)
        block = text[start:end]
        page = f"P{match.group(1)} {match.group(2).strip()}"
        special = any(name in match.group(2) for name in ("资本封面", "核心竞争力地图"))
        for field in ("投资任务", "页面模式"):
            if f"- {field}：" not in block:
                warnings.append(f"{page} 缺少 `{field}`。")
        if not special and "- 核心结论：" not in block:
            warnings.append(f"{page} 缺少 `核心结论`。")
        modules = [int(value) for value in MODULE_RE.findall(block)]
        if modules and max(modules) > 5:
            warnings.append(f"{page} 出现模块 {max(modules)}，可能超过 5 个主容器。")

    sensitive = ("投前估值", "投后估值", "估值区间", "出让比例", "每股价格", "单价")
    for term in sensitive:
        if term in text:
            warnings.append(f"发现融资敏感字段 `{term}`；确认是否为用户明确要求披露。")

    if "投资委员会六问覆盖" not in text:
        warnings.append("未发现投资委员会六问覆盖检查。")
    if "DD材料表" not in text and "DD 材料表" not in text:
        warnings.append("未发现 DD 材料表。")
    if "核心投资叙事" not in text:
        warnings.append("未发现核心投资叙事总结。")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("outline", type=Path, help="Markdown outline to diagnose")
    args = parser.parse_args()

    try:
        text = args.outline.read_text(encoding="utf-8-sig")
        warnings = diagnose(text)
        if warnings:
            print(f"NON-BLOCKING: {len(warnings)} diagnostic(s)")
            for item in warnings:
                print(f"- {item}")
        else:
            print("NON-BLOCKING: no structural diagnostics")
    except Exception as exc:  # Diagnostics must never block the outline workflow.
        print(f"NON-BLOCKING: diagnostic could not run: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
