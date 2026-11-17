from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REQUIRED = (
    "README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "SECURITY.md", "SUPPORT.md", "GOVERNANCE.md", "DISCLAIMER.md",
    "docs/model-card.md", "docs/dataset-card.md",
    "docs/data-governance.md", "docs/testing.md",
    "docs/assets/application-flow.svg",
)


def markdown_files() -> list[Path]:
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and ".venv" not in p.parts]


def check_links(files: list[Path]) -> list[str]:
    errors = []
    for file in files:
        for raw in LINK.findall(file.read_text(encoding="utf-8")):
            target = raw.strip().split(" ", 1)[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if relative and not (file.parent / relative).resolve().exists():
                errors.append(f"{file.relative_to(ROOT)} -> {target}")
    return errors


def check_svgs() -> list[str]:
    errors = []
    for file in (ROOT / "docs" / "assets").glob("*.svg"):
        try:
            ET.parse(file)
        except ET.ParseError as exc:
            errors.append(f"{file.relative_to(ROOT)}: {exc}")
    return errors


def main() -> int:
    missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
    errors = check_links(markdown_files()) + check_svgs()
    errors.extend(f"Missing required file: {p}" for p in missing)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Repository checks passed. Markdown files and SVG assets validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
