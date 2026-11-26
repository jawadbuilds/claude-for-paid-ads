"""Checks the kit before every release. Run from the repo root: python scripts/check.py

It fails if a skill or agent is malformed, a linked reference file is missing,
or a paid-product hook has crept into the core kit.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []

# Vendor names and link patterns that must never appear in the core kit.
BANNED = [
    r"get-ryze", r"ryze mcp", r"scrapecreators", r"skool\.com", r"utm_source=github",
    r"blob/main/tools", r"tools/(clis|integrations)/", r"tools/(REGISTRY|SETUP)\.md",
    r"verified partner", r"supermetrics", r"affiliate link",
]
# Files allowed to name a source in order to credit it.
CREDIT_FILES = {"CREDITS.md", "CHANGELOG.md"}
ORIGIN_LINE = re.compile(r'^\s*origin:\s*".*"\s*$')


def frontmatter(path):
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        errors.append(f"{path.relative_to(ROOT)}: no frontmatter")
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        k = re.match(r"^([a-z_-]+):\s*(.*)$", line)
        if k:
            fields[k.group(1)] = k.group(2).strip().strip('"')
    return fields


def check_named(path, expected):
    f = frontmatter(path)
    rel = path.relative_to(ROOT)
    if f.get("name") != expected:
        errors.append(f"{rel}: name is '{f.get('name')}', expected '{expected}'")
    desc = f.get("description", "")
    if not desc:
        errors.append(f"{rel}: no description")
    elif len(desc) > 1024:
        errors.append(f"{rel}: description is {len(desc)} characters, limit 1024")


def check_links(md):
    text = md.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(((?!https?:|#|mailto:)[^)#\s]+)", text):
        if not (md.parent / target).exists():
            errors.append(f"{md.relative_to(ROOT)}: link to missing file {target}")


def check_banned(path):
    rel = path.relative_to(ROOT)
    for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if ORIGIN_LINE.match(line):
            continue
        for pat in BANNED:
            if re.search(pat, line, re.I):
                errors.append(f"{rel}:{n}: banned pattern '{pat}'")


skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
for s in skills:
    md = s / "SKILL.md"
    if not md.exists():
        errors.append(f"skills/{s.name}: no SKILL.md")
        continue
    check_named(md, s.name)
    for doc in s.rglob("*.md"):
        check_links(doc)

agents = sorted((ROOT / "agents").glob("*.md"))
for a in agents:
    check_named(a, a.stem)

core = [ROOT / "README.md", *(ROOT / "docs").rglob("*.md"),
        *(ROOT / "skills").rglob("*.md"), *(ROOT / "agents").rglob("*.md")]
for p in core:
    if p.exists() and p.name not in CREDIT_FILES:
        check_banned(p)

# House style for the kit's own writing: no dashes used as punctuation, none of the stock AI words.
SLOP = re.compile(
    r"\b(seamless(ly)?|effortless(ly)?|robust|comprehensive|cutting-edge|world-class|next-level|"
    r"game-chang\w+|revolutionary|leverag\w+|unlock\w*|elevat\w+|streamlin\w+|supercharg\w+|"
    r"empower\w*|reimagin\w+|delv\w+|in today's|whether you('re| are)|not just)\b", re.I)
own = [ROOT / n for n in ("README.md", "CREDITS.md", "CONTRIBUTING.md", "SECURITY.md", "CHANGELOG.md")]
own += list((ROOT / "docs").rglob("*.md")) + list(agents)
own += [s / "SKILL.md" for s in skills]
for p in own:
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if "—" in line or "–" in line:
            errors.append(f"{p.relative_to(ROOT)}:{n}: dash used as punctuation")
        m = SLOP.search(line)
        if m and p.parent.name not in ("human-copy-check", "ad-creative"):  # these two have to name the words they ban
            errors.append(f"{p.relative_to(ROOT)}:{n}: stock phrase '{m.group(0)}'")

# The vendored plugins must stay free of the community promotion that was removed.
for p in (ROOT / "plugins").rglob("*.md"):
    if "skool.com" in p.read_text(encoding="utf-8", errors="replace"):
        errors.append(f"{p.relative_to(ROOT)}: community promotion link is back")

print(f"{len(skills)} skills, {len(agents)} agents checked")
if errors:
    print(f"\n{len(errors)} problem(s):")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("All checks passed.")
