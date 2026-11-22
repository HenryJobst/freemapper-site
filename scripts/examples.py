"""Reads the two example tables (sprint, forest) of freemapper's examples/README.md and README.en.md and writes the
gallery data. Usage: examples.py <examples dir> <json out> <image out dir>."""

import json
import re
import shutil
import sys
from pathlib import Path

ROW = re.compile(
    r'^\| <a href="(?P<dir>[^/"]+)/preview\.webp">.*?</a><br>(?P<links>.*?) \| (?P<state>[^|]+?) \| '
    r'\[(?P<title>[^\]]+)\]\([^)]*\): (?P<desc>.*?) \| (?P<objects>\d+) \| (?P<candidates>\d+) \| (?P<symbols>\d+) \|$'
)
INTL_ROW = re.compile(
    r'^\| <a href="(?P<dir>[^/"]+)/preview\.webp">.*?</a><br>(?P<links>.*?) \| (?P<kind>[^|]+?) \| '
    r'\[(?P<title>[^\]]+)\]\([^)]*\): (?P<desc>.*?) \| (?P<objects>\d+) \| (?P<candidates>\d+) \| (?P<symbols>\d+) \|$'
)
LINK = re.compile(r'<a href="[^/"]+/(?P<file>[^"]+\.pdf)">(?P<label>[^<]+)</a>')


def tables(readme: Path) -> list[list[dict]]:
    """The rows of the example tables in the order they come; a heading starts the next table."""
    found: list[list[dict]] = []
    current: list[dict] | None = None
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("| Vorschau") or line.startswith("| Preview"):
            current = []
            found.append(current)
            continue
        m = ROW.match(line)
        if m and current is not None:
            current.append(
                {
                    "dir": m["dir"],
                    "state": m["state"].strip(),
                    "title": m["title"].strip(),
                    "desc": m["desc"].strip(),
                    "objects": int(m["objects"]),
                    "candidates": int(m["candidates"]),
                    "symbols": int(m["symbols"]),
                    "pdfs": [{"file": l["file"]} for l in LINK.finditer(m["links"])],
                }
            )
    return [t for t in found if t]


def international(readme: Path) -> list[dict]:
    """The rows of international.md / international.en.md; the heading `## <country>` above a table names the country."""
    rows: list[dict] = []
    country = ""
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            country = line[3:].strip()
            continue
        m = INTL_ROW.match(line)
        if m:
            rows.append(
                {
                    "dir": m["dir"],
                    "state": country,
                    "kind": "forest" if m["kind"].startswith(("Wald", "Forest")) else "sprint",
                    "title": m["title"].strip(),
                    "desc": m["desc"].strip(),
                    "objects": int(m["objects"]),
                    "candidates": int(m["candidates"]),
                    "symbols": int(m["symbols"]),
                    "pdfs": [{"file": l["file"]} for l in LINK.finditer(m["links"])],
                }
            )
    return rows


def main() -> None:
    examples, out_json, out_images = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    de, en = tables(examples / "README.md"), tables(examples / "README.en.md")
    if len(de) != 2 or len(en) != 2 or [len(t) for t in de] != [len(t) for t in en]:
        sys.exit(f"unexpected tables: de {[len(t) for t in de]}, en {[len(t) for t in en]}")
    data = {}
    for kind, t_de, t_en in zip(["sprint", "forest"], de, en):
        rows = []
        for a, b in zip(t_de, t_en):
            if a["dir"] != b["dir"]:
                sys.exit(f"tables differ: {a['dir']} and {b['dir']}")
            pdfs = [
                {"file": p["file"], "kind": "training" if p["file"].endswith("-training.pdf") else "check"}
                for p in a["pdfs"]
            ]
            rows.append(
                {
                    "dir": a["dir"],
                    "objects": a["objects"],
                    "candidates": a["candidates"],
                    "symbols": a["symbols"],
                    "pdfs": pdfs,
                    "de": {"state": a["state"], "title": a["title"], "desc": a["desc"]},
                    "en": {"state": b["state"], "title": b["title"], "desc": b["desc"]},
                }
            )
            target = out_images / a["dir"]
            target.mkdir(parents=True, exist_ok=True)
            for name in ("preview.webp", "preview-thumb.webp"):
                shutil.copyfile(examples / a["dir"] / name, target / name)
        data[kind] = rows
    intl = []
    for a, b in zip(international(examples / "international.md"), international(examples / "international.en.md")):
        if a["dir"] != b["dir"]:
            sys.exit(f"international tables differ: {a['dir']} and {b['dir']}")
        intl.append(
            {
                "dir": a["dir"],
                "kind": a["kind"],
                "objects": a["objects"],
                "candidates": a["candidates"],
                "symbols": a["symbols"],
                "pdfs": [
                    {"file": p["file"], "kind": "training" if p["file"].endswith("-training.pdf") else "check"}
                    for p in a["pdfs"]
                ],
                "de": {"state": a["state"], "title": a["title"], "desc": a["desc"]},
                "en": {"state": b["state"], "title": b["title"], "desc": b["desc"]},
            }
        )
        target = out_images / a["dir"]
        target.mkdir(parents=True, exist_ok=True)
        for name in ("preview.webp", "preview-thumb.webp"):
            shutil.copyfile(examples / a["dir"] / name, target / name)
    data["international"] = intl
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"examples: {len(data['sprint'])} sprint, {len(data['forest'])} forest, {len(intl)} international")


if __name__ == "__main__":
    main()
