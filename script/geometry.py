#!/usr/bin/env python3
"""Rejects geometry that bypasses the token scales.

Rules, from docs/superpowers/specs/2026-09-17-page-consistency-design.md:

  1. The VERTICAL axis of margin/padding/gap must be on the spacing scale.
     Only the vertical axis is inspected - the scale is vertical rhythm, so a
     horizontal inset like `padding: 0 20px` is out of scope by construction.
     Per shorthand form: a 1-value margin/padding applies to all sides and is
     checked. A 2-value form is `[vertical, horizontal]`, so only the first
     component is checked. A 3-value form is `[top, horizontal, bottom]`, so
     the first AND third components are checked - the third is a real bottom
     value, not a horizontal one. A 4-value form is
     `[top, right, bottom, left]`, so again the first and third are checked.
     `-top`/`-bottom` longhands are always checked; `-left`/`-right` never
     are. For `gap`/`row-gap`, only the first (row) component is checked - a
     2-value `gap`'s second component is the column gap, which is
     horizontal; `column-gap` alone is entirely horizontal and is never
     checked.
  2. Values of 6px or less are optical and always allowed: chips, badges,
     hairline gaps, icon spacing.
  3. Negative values are offsets, not rhythm, and are skipped.
  4. border-radius carries no px literal at all, unless the line is marked
     // OPTICAL.

There is deliberately no exemption list. An earlier draft named individual
selectors; the three rules above subsume every one of them and several that
draft had missed. A rule applied uniformly beats a list someone maintains.

Assumes one declaration per line and top-level rules opened at column 0, which
is this codebase's style throughout.
"""
import io, re, sys, glob

ALLOWED = {8, 16, 24, 32, 40, 48}

DECL = re.compile(r'^\s*(margin|padding|gap|row-gap|column-gap)'
                  r'(-top|-bottom|-left|-right)?\s*:\s*([^;]+);')
RADIUS = re.compile(r'^\s*border-radius\s*:\s*([^;]+);')

def vertical(prop, side, parts):
    if prop in ("gap", "row-gap"): return parts[:1]
    if prop == "column-gap": return []
    if side in ("-left", "-right"): return []
    if side in ("-top", "-bottom"): return parts
    if len(parts) == 1: return parts
    if len(parts) == 2: return parts[:1]
    if len(parts) in (3, 4): return [parts[0], parts[2]]
    return []

def strip_block_comments(raw, in_comment):
    """Removes /* ... */ spans from a line, tracking state across lines."""
    out = []
    i = 0
    while i < len(raw):
        if in_comment:
            end = raw.find("*/", i)
            if end == -1:
                i = len(raw)
            else:
                i = end + 2
                in_comment = False
        else:
            start = raw.find("/*", i)
            if start == -1:
                out.append(raw[i:])
                i = len(raw)
            else:
                out.append(raw[i:start])
                i = start + 2
                in_comment = True
    return "".join(out), in_comment

def check(path):
    bad, sel = [], ""
    in_comment = False
    for n, raw in enumerate(io.open(path, encoding="utf-8").read().splitlines(), 1):
        raw, in_comment = strip_block_comments(raw, in_comment)
        line = raw.strip()
        # Track the top-level selector (a rule opened at column 0) purely so
        # violations can be reported with a useful name. Nested blocks are
        # indented and keep the parent, which is what you want in the report.
        if re.match(r'^[^\s{}/@][^{}]*\{', raw):
            sel = raw.split("{")[0].strip()
        if line.startswith("//"):
            continue
        code = raw.split("//")[0]
        marked = "// OPTICAL" in raw

        r = RADIUS.match(code)
        if r and re.search(r'\d+px', r.group(1)) and not marked:
            bad.append((path, n, sel, "border-radius", r.group(1).strip()))
            continue

        m = DECL.match(code)
        if not m:
            continue
        prop, side, value = m.group(1), m.group(2) or "", m.group(3)
        for part in vertical(prop, side, value.split()):
            pm = re.fullmatch(r'(-?\d+)px', part)
            if not pm: continue
            v = int(pm.group(1))
            if v < 0 or abs(v) <= 6: continue   # negative offsets; optical
            if v not in ALLOWED:
                bad.append((path, n, sel, prop + side, value.strip()))
                break
    return bad

def main():
    bad = [b for p in sorted(glob.glob("_sass/*.scss")) for b in check(p)]
    if "--count" in sys.argv:
        print(len(bad)); return 0
    for path, n, sel, prop, val in bad:
        print(f"{path}:{n}  {sel}  {prop}: {val}")
    print(f"\n{len(bad)} geometry violations")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
