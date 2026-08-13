#!/usr/bin/env python3
"""Lint a Markdown investor-slide outline before prompt compilation."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PAGE_RE = re.compile(r"^\s*#{1,4}\s+(?:P(?P<p>\d+)\b|第(?P<cn>\d+)页)", re.IGNORECASE)
FIELD_RE = re.compile(r"^\s*-\s*(?P<key>[^：:|]+?)[：:]\s*(?P<value>.*)\s*$")
MODULE_RE = re.compile(r"^\s*-\s*模块\s*(?P<number>\d+)(?:\s*/\s*\d+)*\s*[：:]", re.IGNORECASE)

MODE_ALIASES = {
    "资本封面": "Investor-cover",
    "投资亮点总览": "Investment-highlight-grid",
    "竞争力目录": "Argument-map",
    "结论数字": "Conclusion-number",
    "严谨比较": "Rigorous-comparison",
    "能力沿革": "Capability-progression",
    "资本演进": "Capital-progression",
    "能力结构": "Capability-structure",
    "因果机制": "Causal-mechanism",
    "视觉隐喻": "Visual-metaphor",
}
INTERNAL_MODES = {
    "Investor-cover",
    "Investment-highlight-grid",
    "Argument-map",
    "Evidence-portfolio",
    "Conclusion-number",
    "Rigorous-comparison",
    "Capability-progression",
    "Capital-progression",
    "Capability-structure",
    "Causal-mechanism",
    "Visual-metaphor",
}
MODE_LOOKUP = {mode.casefold(): mode for mode in INTERNAL_MODES}
ROUND_RE = re.compile(
    r"(?:融资轮次|融资阶段|Pre[- ]?[A-Z0-9+]*\s*轮?|种子轮|天使轮|战略融资|[A-C](?:\+)?轮)",
    re.IGNORECASE,
)
SENSITIVE_FINANCING_RE = re.compile(r"投前估值|投后估值|估值区间|出让比例|释放股权|股权比例")


@dataclass
class Page:
    number: int
    start_line: int
    heading: str
    lines: list[str]

    @property
    def text(self) -> str:
        return "\n".join(self.lines)

    @property
    def fields(self) -> dict[str, list[str]]:
        result: dict[str, list[str]] = {}
        for line in self.lines:
            match = FIELD_RE.match(line)
            if match:
                key = match.group("key").strip()
                result.setdefault(key, []).append(match.group("value").strip())
        return result


@dataclass
class Finding:
    severity: str
    page: int | None
    line: int | None
    message: str

    def as_dict(self) -> dict[str, object]:
        return {
            "severity": self.severity,
            "page": self.page,
            "line": self.line,
            "message": self.message,
        }


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.buffer.read().decode("utf-8-sig")
    return Path(path).read_text(encoding="utf-8-sig")


def split_pages(text: str) -> list[Page]:
    lines = text.splitlines()
    starts: list[tuple[int, int]] = []
    for index, line in enumerate(lines):
        match = PAGE_RE.match(line)
        if match:
            starts.append((index, int(match.group("p") or match.group("cn"))))

    pages: list[Page] = []
    for position, (start, number) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        pages.append(Page(number, start + 1, lines[start], lines[start:end]))
    return pages


def normalize_mode(raw: str) -> str | None:
    value = raw.strip().strip("[]`* ")
    for alias, mode in MODE_ALIASES.items():
        if alias in value:
            return mode
    for candidate in re.split(r"[\s/|,，]+", value):
        normalized = MODE_LOOKUP.get(candidate.casefold())
        if normalized:
            return normalized
    return None


def field_value(fields: dict[str, list[str]], *names: str) -> str:
    for name in names:
        if name in fields:
            return " ".join(fields[name])
    return ""


def lint(text: str, strict: bool) -> tuple[list[Page], list[Finding]]:
    pages = split_pages(text)
    findings: list[Finding] = []
    if not pages:
        return pages, [Finding("error", None, None, "No page headings such as '### P1' or '# 第1页' were found.")]

    seen: set[int] = set()
    for page in pages:
        if page.number in seen:
            findings.append(Finding("error", page.number, page.start_line, "Duplicate page number."))
        seen.add(page.number)

        fields = page.fields
        structured = any(name in fields for name in ("投资任务", "核心结论", "标题", "页面模式"))
        severity = "error" if strict and structured else "warning"

        for name in ("核心结论", "标题", "页面模式"):
            if structured and not field_value(fields, name):
                findings.append(Finding(severity, page.number, page.start_line, f"Structured page is missing '{name}'."))

        raw_mode = field_value(fields, "页面模式")
        mode = normalize_mode(raw_mode) if raw_mode else None
        if raw_mode and not mode:
            findings.append(Finding("error", page.number, page.start_line, f"Unknown page mode: {raw_mode}"))

        module_numbers = {int(match.group("number")) for line in page.lines if (match := MODULE_RE.match(line))}
        if len(module_numbers) > 5:
            findings.append(Finding("error", page.number, page.start_line, f"Found {len(module_numbers)} modules; maximum is 5."))
        if mode == "Investment-highlight-grid" and module_numbers and len(module_numbers) != 4:
            findings.append(Finding("error", page.number, page.start_line, "Investment-highlight-grid must contain exactly four modules."))

        anchor = field_value(fields, "视觉锚点", "记忆锚点")
        if structured and mode not in {"Investment-highlight-grid", "Argument-map"} and not anchor:
            findings.append(Finding("warning", page.number, page.start_line, "No visual or memory anchor is declared."))

        if mode == "Investor-cover" and not ROUND_RE.search(page.text):
            findings.append(Finding("warning", page.number, page.start_line, "Investor-cover has no financing-round label or explicit placeholder."))

        if SENSITIVE_FINANCING_RE.search(page.text):
            findings.append(Finding("warning", page.number, page.start_line, "Sensitive valuation or equity-disclosure field found; confirm explicit authorization before putting it on-slide."))

    return pages, findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("outline", help="UTF-8 Markdown outline, or '-' for stdin")
    parser.add_argument("--strict", action="store_true", help="Treat missing fields on structured pages as errors")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Emit machine-readable JSON")
    args = parser.parse_args()

    try:
        text = read_text(args.outline)
    except (OSError, UnicodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    pages, findings = lint(text, args.strict)
    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)

    if args.as_json:
        print(json.dumps({"pages": len(pages), "errors": errors, "warnings": warnings, "findings": [item.as_dict() for item in findings]}, ensure_ascii=False, indent=2))
    else:
        for item in findings:
            location = f"P{item.page}" if item.page is not None else "outline"
            if item.line is not None:
                location += f":L{item.line}"
            print(f"{item.severity.upper()} {location} {item.message}")
        print(f"SUMMARY pages={len(pages)} errors={errors} warnings={warnings}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
