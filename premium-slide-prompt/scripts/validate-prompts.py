#!/usr/bin/env python3
"""Validate a multi-slide prompt bundle for deck-wide Style Lock drift."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


PAGE_RE = re.compile(r"^\s*#{1,4}\s+(?:P(?P<p>\d+)\b|第(?P<cn>\d+)页)", re.IGNORECASE)
LOCK_RE = re.compile(r"^\s*Deck-wide Style Lock:\s*(?P<value>.+?)\s*$", re.IGNORECASE)
PROMPT_RE = re.compile(r"^\s*Page-specific Prompt:\s*(?P<value>.*)$", re.IGNORECASE)
COPY_GUARD_RE = re.compile(
    r"Render only this supplied on-slide copy; add no other words, labels, badges, numbers, or microcopy\.",
    re.IGNORECASE,
)
VAGUE_CONTINUITY_RE = re.compile(
    r"same (?:style|design) as (?:the )?previous|consistent with previous|延续上一页|与上一页一致",
    re.IGNORECASE,
)


@dataclass
class Page:
    number: int
    start_line: int
    lines: list[str]

    @property
    def text(self) -> str:
        return "\n".join(self.lines)


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


def parse_pages(text: str) -> list[Page]:
    pages: list[Page] = []
    current: Page | None = None
    for line_number, line in enumerate(text.splitlines(), start=1):
        match = PAGE_RE.match(line)
        if match:
            number = int(match.group("p") or match.group("cn"))
            current = Page(number=number, start_line=line_number, lines=[])
            pages.append(current)
        elif current is not None:
            current.lines.append(line)
    return pages


def normalize_lock(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def validate(text: str) -> tuple[list[Page], list[Finding]]:
    pages = parse_pages(text)
    findings: list[Finding] = []
    locks: list[tuple[Page, str, int]] = []

    if len(pages) < 2:
        findings.append(
            Finding(
                "error",
                None,
                None,
                "Expected at least two page sections headed as P1/P2 or 第1页/第2页.",
            )
        )
        return pages, findings

    for page in pages:
        lock_matches: list[tuple[str, int]] = []
        prompt_line: int | None = None
        for offset, line in enumerate(page.lines, start=1):
            line_number = page.start_line + offset
            lock_match = LOCK_RE.match(line)
            if lock_match:
                lock_matches.append((normalize_lock(lock_match.group("value")), line_number))
            if PROMPT_RE.match(line):
                prompt_line = line_number

        if len(lock_matches) != 1:
            findings.append(
                Finding(
                    "error",
                    page.number,
                    page.start_line,
                    f"Expected exactly one non-empty Deck-wide Style Lock line; found {len(lock_matches)}.",
                )
            )
        else:
            locks.append((page, lock_matches[0][0], lock_matches[0][1]))

        if prompt_line is None:
            findings.append(
                Finding("error", page.number, page.start_line, "Missing Page-specific Prompt marker.")
            )
        if not COPY_GUARD_RE.search(page.text):
            findings.append(
                Finding(
                    "warning",
                    page.number,
                    prompt_line or page.start_line,
                    "Missing the exact-copy guard that prohibits invented on-slide microcopy.",
                )
            )
        if VAGUE_CONTINUITY_RE.search(page.text):
            findings.append(
                Finding(
                    "error",
                    page.number,
                    page.start_line,
                    "Uses vague previous-page continuity instead of a self-contained Style Lock.",
                )
            )

    if locks:
        canonical = locks[0][1]
        for page, value, line_number in locks[1:]:
            if value != canonical:
                findings.append(
                    Finding(
                        "error",
                        page.number,
                        line_number,
                        "Deck-wide Style Lock differs from P1; repeat the lock verbatim.",
                    )
                )

    return pages, findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt_bundle", type=Path, help="Markdown prompt bundle to validate")
    parser.add_argument("--json", action="store_true", help="Emit findings as JSON")
    args = parser.parse_args()

    try:
        text = args.prompt_bundle.read_text(encoding="utf-8-sig")
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    pages, findings = validate(text)
    errors = sum(item.severity == "error" for item in findings)
    warnings = sum(item.severity == "warning" for item in findings)

    if args.json:
        print(
            json.dumps(
                {
                    "pages": len(pages),
                    "errors": errors,
                    "warnings": warnings,
                    "findings": [item.as_dict() for item in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        for item in findings:
            location = ""
            if item.page is not None:
                location += f"P{item.page}"
            if item.line is not None:
                location += f":{item.line}"
            prefix = f"{location}: " if location else ""
            print(f"{item.severity.upper()}: {prefix}{item.message}")
        print(f"Validated {len(pages)} pages: {errors} error(s), {warnings} warning(s).")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
