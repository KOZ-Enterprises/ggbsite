#!/usr/bin/env python3
"""Report class selectors defined in the stylesheet that appear in no built page.

Run AFTER `bundle exec jekyll build`, since _site is the oracle: it contains
every page Jekyll renders, which source templates alone do not.

  python script/dead-css.py            # list dead selectors
  python script/dead-css.py --count    # just the number, for scripting
"""
import os, re, io, sys, glob

# Added by assets/js/scripts.js and head.html at runtime, so they never appear
# in static output. Not dead.
RUNTIME = {"responsive", "mermaid"}

# Referenced by a template, but on a conditional branch that current content
# never takes. Real code guarding a real state - not debris.
TEMPLATE_FALLBACK = {
    "card-noimg",   # _includes/project-card.html, _layouts/tag.html:55:
                    # "No preview" placeholder for a project with no image:.
                    # All 7 projects currently have one.
}

EXEMPT = RUNTIME | TEMPLATE_FALLBACK


def strip_comments(src):
    """Drop /* ... */ and // ... comments from SCSS source.

    The class-name regex below runs over raw source, so anything that looks
    like `.foo` counts as a definition - including a name that only appears in
    a comment. Every partial in _sass/ opens with a `// Contains:` header that
    lists the classes it owns, and the rules themselves carry prose about the
    cascade, so without this the audit reports names it merely read about.

    Hand-rolled rather than a regex because `//` is legal inside a quoted
    string and inside url(https://...). Neither appears in _sass/ today, but a
    web-font @import would add one, and a stripper that ate the rest of that
    line would silently drop real selectors.
    """
    out, i, n, quote = [], 0, len(src), None
    while i < n:
        c = src[i]
        if quote:                                  # inside "..." or '...'
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(src[i + 1])
                i += 2
                continue
            if c == quote:
                quote = None
            i += 1
        elif c in "\"'":
            quote = c
            out.append(c)
            i += 1
        elif src.startswith("url(", i):            # url(...) is opaque
            j = src.find(")", i)
            j = n if j < 0 else j + 1
            out.append(src[i:j])
            i = j
        elif src.startswith("/*", i):
            j = src.find("*/", i + 2)
            i = n if j < 0 else j + 2
            out.append(" ")
        elif src.startswith("//", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
            out.append(" ")
        else:
            out.append(c)
            i += 1
    return "".join(out)


def main():
    css = "".join(strip_comments(io.open(p, encoding="utf-8").read())
                  for p in sorted(glob.glob("_sass/*.scss")))
    defined = set(re.findall(r"\.([a-zA-Z][\w-]*)\s*[,{:\s]", css))

    used = set()
    pages = 0
    for root, _, files in os.walk("_site"):
        for f in files:
            if not f.endswith(".html"):
                continue
            pages += 1
            s = io.open(os.path.join(root, f), encoding="utf-8", errors="ignore").read()
            for m in re.findall(r'class="([^"]*)"', s):
                used.update(m.split())

    dead = sorted(d for d in defined if d not in used and d not in EXEMPT)

    if "--count" in sys.argv:
        print(len(dead))
        return 0

    print(f"scanned {pages} built pages")
    print(f"defined: {len(defined)}   used: {len(used)}   dead: {len(dead)}")
    for d in dead:
        print(f"  {d}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
