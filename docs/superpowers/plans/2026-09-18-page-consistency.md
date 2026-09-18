# Page Consistency Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give every page one banded header carrying the blueprint grid, and put all geometry — spacing and corner radii — behind tokens with a build-failing gate that keeps it there.

**Architecture:** Six tasks, ordered so risk rises and each lands on a proven base. Task 1 adds the tokens, extracts the grid into a mixin (provably byte-neutral) and builds the geometry checker as a local tool, so Tasks 2, 3 and 4 can each verify themselves against it. Those three are independent of one another. Task 5 only wires the checker into CI, once the tree already passes. Task 6 updates the normative doc.

**Tech Stack:** Jekyll 4.4.1, native Sass via `jekyll-sass-converter` 3.1.0 / `sass-embedded` 1.93.2, Python 3 for the audit script, Playwright MCP for visual verification.

**Spec:** `docs/superpowers/specs/2026-09-17-page-consistency-design.md` — read it before starting. Every value in this plan comes from it; where they disagree, the spec wins and this plan is wrong.

## Global Constraints

- **The palette is closed.** Three literals are documented exceptions (`#f5f5f5`, `#c3cece`, `#8fd6d4`); do not add a fourth without a comment at the line.
- **Three breakpoints only**, via `@include respond-to(wide|nav|mobile)`. No bare `@media` outside `_tokens.scss`.
- **Dead selectors must stay at zero.** `python script/dead-css.py --count` → `0`, a build-failing CI gate. It reports **class** selectors; attribute selectors are invisible to it.
- **`script/verify-redesign.sh` must report 26 PASS, exit 0.**
- **`docs/**` is linted by CI** (ignores cover `docs/superpowers/**`, not `docs/**`).
- **`CLAUDE.md` is a symlink to `AGENTS.md`** (mode `120000`, content exactly `AGENTS.md`, no trailing newline). Never write to it.
- **The Bash sandbox discards writes to the project directory between calls.** Use `dangerouslyDisableSandbox: true` for anything that builds or writes. Five agents have lost time to this.
- **Equal-specificity rules setting the same property need a `COLLISION SET` comment**, including shorthand against longhand.
- **Deploy is `publish`.** `assets/css/styles.css` is generated, not committed.
- **Cloudflare caches assets 30 days** with no purge tooling here. Changing an image means changing its filename.

## Task dependency

```text
Task 1 (tokens + mixin + script/geometry.py)
   ├── Task 2 (radius)    ─┐   clears 8 of the 100
   ├── Task 3 (band)      ─┼─  clears 3 of the 100
   └── Task 4 (spacing)   ─┘   clears 89 of the 100
                            └── Task 5 (wire the gate into CI) ── Task 6 (docs)
```

`script/geometry.py` reports **100 violations** on the tree as it stands today — 8 `border-radius` literals, 3 in rules the band task rewrites, and 89 spacing declarations. Tasks 2, 3 and 4 each drive a known share of that to zero and can run in any order or in parallel once Task 1 is committed. Task 5 only adds the CI step, and must come last because the gate fails on anything the other three have not yet fixed.

---

### Task 1: Geometry tokens, the blueprint-grid mixin, and the checker

Pure addition plus one provably neutral extraction, and the tool the next three tasks measure themselves with. Nothing changes visually.

**Files:**

- Modify: `_sass/_tokens.scss:41-44` (the "Space & shape" block)
- Modify: `_sass/_pages.scss` (`.intro-band`), `_sass/_components.scss` (`.card-media`, `.wide-card-media`)

**Interfaces — later tasks rely on these exact names:**

- Produces: `$space-half`, `$space-1` … `$space-6`; `$radius-surface`, `$radius-chip`, `$radius-mark`; `$grid-pitch-band`, `$grid-pitch-media`, `$grid-alpha`; `@mixin blueprint-grid($pitch, $alpha)`; and `script/geometry.py`, whose `--count` flag Tasks 2-5 use as their acceptance measure.
- `$radius-card` is **retired** in Task 2, not here. It still exists after this task.

- [ ] **Step 1: Snapshot the compiled CSS**

```bash
bundle exec jekyll build
cp _site/assets/css/styles.css "$SCRATCH/t1-before.css"
```

`$SCRATCH` is the session scratchpad directory, never the project directory.

- [ ] **Step 2: Add the tokens**

Replace the "Space & shape" block at `_sass/_tokens.scss:41-44` with:

```scss
// ---- Space & shape ---------------------------------------------------------
// Vertical rhythm. Six steps on an 8px base; the 40px blueprint pitch is five
// steps, so texture and spacing share a grid. $space-half is legal ONLY in the
// compound `$space-1 + $space-half` and ONLY on .page-kicker's margin-bottom -
// see docs/css-architecture.md. A bare 12px is rejected by script/geometry.py.
$space-half:  4px;
$space-1:     8px;
$space-2:    16px;
$space-3:    24px;
$space-4:    32px;
$space-5:    40px;
$space-6:    48px;

$radius-surface:  6px;   // cards, bands, modules, heroes, code blocks, media
$radius-chip:     3px;   // chips, status pills, timeline markers
$radius-mark:    12px;   // the nav logo frame at desktop

$radius-card: 6px;       // DEPRECATED alias, removed in the radius migration
$touch-min:   44px;      // minimum interactive target

// ---- Blueprint grid --------------------------------------------------------
// The signature texture: faint accent-coloured graph paper. Two pitches only.
// Bands are large surfaces and take the coarser grid; media backplates are
// small 4:3 boxes where 40px would show barely two lines.
$grid-pitch-band:   40px;
$grid-pitch-media:  32px;
$grid-alpha:        0.045;

@mixin blueprint-grid($pitch: $grid-pitch-band, $alpha: $grid-alpha) {
    background-color: $c-bg;
    background-image:
        linear-gradient(rgba($c-accent, $alpha) 1px, transparent 1px),
        linear-gradient(90deg, rgba($c-accent, $alpha) 1px, transparent 1px);
    background-size: $pitch $pitch;
}
```

A mixin emits nothing until used, so `_tokens.scss` still compiles to zero CSS.

- [ ] **Step 3: Replace the three literal grid copies**

At each site, replace the **three declarations spanning five lines** — `background-color`, the three-line `background-image`, and `background-size` — with one `@include`, leaving every surrounding declaration untouched and in place.

`_sass/_pages.scss`, in `.intro-band`:

```scss
    @include blueprint-grid($grid-pitch-band);
```

`_sass/_components.scss`, in `.card-media` and again in `.wide-card-media`:

```scss
    @include blueprint-grid($grid-pitch-media);
```

- [ ] **Step 4: Prove the extraction changed nothing**

```bash
bundle exec jekyll build
cmp "$SCRATCH/t1-before.css" _site/assets/css/styles.css && echo "IDENTICAL" || echo "DIFFERS"
```

Expected: `IDENTICAL`. **This has been prototyped end to end and does pass** — all three sites already emit `background-color` → `background-image` → `background-size` contiguously in that order, and `style: compressed` makes whitespace irrelevant. If it differs, an argument or default is wrong. Do not weaken this check.

- [ ] **Step 5: Confirm the new tokens emit nothing**

```bash
grep -oE "radius-surface|grid-pitch-[a-z]+|space-half" _site/assets/css/styles.css | wc -l
```

Expected: `0`. Sass variables never reach the output.

Use `grep -o … | wc -l`, not `grep -c`. The compressed stylesheet is a single
line, so `grep -c` counts matching *lines* and returns 1 for any match at all.
A bare `space-` also matches the pre-existing `justify-content:space-between`,
which is a false positive unrelated to these tokens.

- [ ] **Step 6: Create the geometry checker**

Built here rather than with the CI wiring, so Tasks 2, 3 and 4 can each verify themselves against it. It is not wired into CI until Task 5.

Create `script/geometry.py`:

```python
#!/usr/bin/env python3
"""Rejects geometry that bypasses the token scales.

Rules, from docs/superpowers/specs/2026-09-17-page-consistency-design.md:

  1. The VERTICAL axis of margin/padding/gap must be on the spacing scale.
     Only the vertical axis is inspected - the scale is vertical rhythm, so a
     horizontal inset like `padding: 0 20px` is out of scope by construction.
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

ALLOWED = {4, 8, 16, 24, 32, 40, 48}   # 4 only via `$space-1 + $space-half`

DECL = re.compile(r'^\s*(margin|padding|gap|row-gap|column-gap)'
                  r'(-top|-bottom|-left|-right)?\s*:\s*([^;]+);')
RADIUS = re.compile(r'^\s*border-radius\s*:\s*([^;]+);')

def vertical(prop, side, parts):
    if prop in ("gap", "row-gap"): return parts
    if prop == "column-gap": return []
    if side in ("-left", "-right"): return []
    if side in ("-top", "-bottom"): return parts
    if len(parts) == 1: return parts
    if len(parts) in (2, 3): return parts[:1]
    if len(parts) == 4: return [parts[0], parts[2]]
    return []

def check(path):
    bad, sel = [], ""
    for n, raw in enumerate(io.open(path, encoding="utf-8").read().splitlines(), 1):
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
        if not m or marked:
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
```

- [ ] **Step 7: Confirm it reports the expected baseline**

```bash
python script/geometry.py --count
```

Expected: **100**. That is the debt Tasks 2, 3 and 4 pay off — 8 radius literals (Task 2), `.page-head`'s margin plus `.intro-band`'s two paddings (Task 3), and 89 spacing declarations (Task 4). A different number means the rules or the tree differ from what this plan was written against; investigate before continuing.

- [ ] **Step 8: Prove the checker works in both directions**

A gate that fails on correct code gets disabled, so both halves matter. Each probe appends to `_sass/_utilities.scss` and is reverted immediately.

```bash
# MUST flag: an off-scale vertical value
printf '
.probe {
    margin-bottom: 13px;
}
' >> _sass/_utilities.scss
python script/geometry.py --count      # expect 101 (100 + 1)
git checkout _sass/_utilities.scss

# MUST flag: an unmarked radius
printf '
.probe {
    border-radius: 7px;
}
' >> _sass/_utilities.scss
python script/geometry.py --count      # expect 101
git checkout _sass/_utilities.scss

# MUST flag: a violation after an optical rule. Regression test - an earlier
# draft tracked only class selectors, so `sel` stayed stale across an element
# rule and everything after it was silently skipped.
printf '
.tech-chip {
    padding: 2px 8px;
}

h2 {
    margin-bottom: 13px;
}
' >> _sass/_utilities.scss
python script/geometry.py --count      # expect 101, NOT 100
git checkout _sass/_utilities.scss

# must NOT flag: horizontal-only inset
printf '
.probe {
    padding: 0 22px;
}
' >> _sass/_utilities.scss
python script/geometry.py --count      # expect 100
git checkout _sass/_utilities.scss

# must NOT flag: optical <= 6px
printf '
.probe {
    padding: 2px 8px;
}
' >> _sass/_utilities.scss
python script/geometry.py --count      # expect 100
git checkout _sass/_utilities.scss

# must NOT flag: a marked optical radius
printf '
.probe {
    border-radius: 7px;  // OPTICAL - probe
}
' >> _sass/_utilities.scss
python script/geometry.py --count      # expect 100
git checkout _sass/_utilities.scss

# must NOT flag: a negative offset
printf '
.probe {
    margin-top: -96px;
}
' >> _sass/_utilities.scss
python script/geometry.py --count      # expect 100
git checkout _sass/_utilities.scss

git status --porcelain _sass/_utilities.scss   # must be empty
```

All seven probes above have been verified against this exact script, along with four more covering tokens, the half-step compound, comments and an element selector; if any disagrees, the script was transcribed wrongly.

- [ ] **Step 9: Commit**

```bash
chmod +x script/geometry.py
git update-index --chmod=+x script/geometry.py
git add _sass/_tokens.scss _sass/_pages.scss _sass/_components.scss script/geometry.py
git commit -m "refactor(css): add geometry tokens and the blueprint-grid mixin

Spacing scale, radius scale, grid pitch tokens, and a mixin replacing three
hand-copied gradient pairs at two pitches. Compiled CSS is byte-identical, so
the migrations that follow land on a proven-neutral base.

Also adds script/geometry.py, which reports 100 violations on the tree as it
stands. It is a local tool for now; the next three tasks each drive a known
share of that to zero, and only then is it wired into CI.

\$radius-card stays as a deprecated alias until the radius migration retires it."
```

---

### Task 2: Radius scale migration

Mechanical, 21 sites, near-zero risk. Independent of Tasks 3 and 4.

**Files:**

- Modify: `_sass/_components.scss` (5 alias sites + `.tech-chip`, `.tl-marker`), `_sass/_content.scss` (4), `_sass/_layout.scss` (2 + `.portrait-frame img`), `_sass/_pages.scss` (5 + `.intro-band`, `.feature-hero`), `_sass/_nav.scss` (`.nav-mark` ×2, `.nav-icon-bar`), `_sass/_tokens.scss` (retire the alias)

**Interfaces:**

- Consumes: `$radius-surface`, `$radius-chip`, `$radius-mark` from Task 1.
- Produces: `$radius-card` no longer exists.

- [ ] **Step 1: Rename the 16 alias call sites**

```bash
sed -i 's/\$radius-card/\$radius-surface/g' _sass/_components.scss _sass/_content.scss _sass/_layout.scss _sass/_pages.scss
grep -rn 'radius-card' _sass/ || echo "no call sites remain"
```

Two of those sites are multi-corner shorthands (`border-radius: 0 $radius-card $radius-card 0;` at `_sass/_components.scss:505` and `_sass/_content.scss:105`); the sed handles both.

- [ ] **Step 2: Retire the alias**

Delete this line from `_sass/_tokens.scss`:

```scss
$radius-card: 6px;       // DEPRECATED alias, removed in the radius migration
```

- [ ] **Step 3: Remap the five literals**

| File:line | Selector | From | To |
| --- | --- | --- | --- |
| `_sass/_components.scss:21` | `.tech-chip` | `12px` | `$radius-chip` |
| `_sass/_components.scss:640` | `.tl-marker` | `2px` | `$radius-chip` |
| `_sass/_layout.scss:219` | `.portrait-frame img` | `4px` | `$radius-surface` |
| `_sass/_pages.scss:22` | `.intro-band` | `4px` | `$radius-surface` |
| `_sass/_pages.scss:72` | `.feature-hero` | `4px` | `$radius-surface` |

Line numbers shift as you edit; find each by selector rather than trusting them.

- [ ] **Step 4: Token the desktop nav mark, mark the two exemptions**

`_sass/_nav.scss:75` (`.nav-mark`) becomes `border-radius: $radius-mark;`.

The two exemptions keep their literals and gain the marker the gate looks for:

```scss
    border-radius: 10px;  // OPTICAL - scales with the 52->42px box; $radius-mark
                          // would reshape the brand mark on phones
```

```scss
    border-radius: 1px;   // OPTICAL - 2px-tall bar; $radius-chip exceeds half
                          // its height
```

- [ ] **Step 5: Verify every radius is accounted for**

```bash
bundle exec jekyll build
grep -rn "border-radius:[^;]*px" _sass/
```

Expected: exactly two lines, both carrying `// OPTICAL`. Everything else resolves from a token.

- [ ] **Step 6: Confirm `.tech-chip` is a zero-diff change**

Its 12px base rule never applied — all four usages sit inside `.card-chips` or `.side-chips`, whose `(0,2,0)` rules already set `$radius-chip`. Prove it:

```bash
grep -o "tech-chip[^\"]*" _site/projects/ggswarm/index.html | head -3
```

Then in the browser at 1280px on `/projects/ggswarm/`, confirm every `.tech-chip` computes `border-radius: 3px`, as it did before this task.

- [ ] **Step 7: Run the gates, and confirm this task's share is clear**

```bash
bash script/verify-redesign.sh          # 26 PASS
python script/dead-css.py --count       # 0
python script/geometry.py | grep -c border-radius    # expect 0
python script/geometry.py --count                     # expect 92, down from 100
```

Every radius violation is now gone; the 92 remaining are the three the band task owns and the 89 spacing declarations. If a radius line still reports, it is missing either a token or its `// OPTICAL` marker.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "refactor(css): three radius tokens replace seven values

\$radius-card becomes \$radius-surface across 16 call sites; five literals move
onto tokens; the nav mark's desktop radius is named. Two optical exemptions keep
their literals with an // OPTICAL marker: the mobile mark scales with its box,
and the 2px hamburger bar is shorter than \$radius-chip.

.tech-chip's 12px was dead - all four usages sit inside .card-chips or
.side-chips, which already set \$radius-chip - so that line is a zero-diff
cleanup."
```

---

### Task 3: The band

The visible one. Independent of Tasks 2 and 4.

**Files:**

- Modify: `_sass/_layout.scss:15-18` (`.page-head`), `:82-84` (delete `.detail-head`), `_sass/_pages.scss` (`.intro-band`, delete `.intro-inner`, delete `.intro-kicker`)
- Modify: `index.html:8-19`, `_layouts/course.html`, `about.html`
- Modify: `projects.html:17`, `archives.html:39`, `_layouts/tag.html:40` (remove `.page-rule`)

**Interfaces:**

- Consumes: `$space-2`, `$space-3`, `$space-4`, `$space-5`, `$space-6`, `$radius-surface`, `$grid-pitch-band`, `blueprint-grid()` from Task 1.

- [ ] **Step 1: Write the shared band rule**

Replace `.page-head` at `_sass/_layout.scss:15-18` with this, and **delete the standalone `.detail-head` rule at `:82-84`** — the band owns its margin now.

```scss
// The page's opening surface: one per page, always at the top, and the only
// place the blueprint grid shows. Blog posts are deliberately excluded -
// .post-head is a reading surface and the texture fights body prose.
//
// max-width is deliberately NOT set. It used to sit on .page-head, but a band
// has to span the content column or index and detail pages get visibly
// different widths. The reading measure is carried by .page-lead's own 820px.
.page-head,
.detail-head,
.intro-band {
    @include blueprint-grid($grid-pitch-band);
    border: 1px solid $c-border;
    border-radius: $radius-surface;
    padding: $space-4;
    margin: 0 0 $space-4;

    @include respond-to(mobile) {
        padding: $space-3 $space-2;
        margin: 0 0 $space-3;
    }
}
```

- [ ] **Step 2: Reduce `.intro-band` to its overrides**

In `_sass/_pages.scss`, delete `.intro-band`'s `background-*`, `border`, `border-radius` and the `@include blueprint-grid(...)` Task 1 added — the shared rule supplies all of them. Keep only the larger padding and margin, with the collision comment the architecture doc requires:

```scss
// COLLISION SET - the home band is the shared treatment from _layout.scss,
// scaled up. Both rules are (0,1,0) and both set padding and margin, so this
// wins only because _pages.scss loads after _layout.scss. Do not move it
// earlier, and do not restate the border, the radius or the grid here.
.intro-band {
    padding: $space-6;
    margin: 0 0 $space-5;

    @include respond-to(mobile) {
        padding: $space-4 $space-2;
        margin: 0 0 $space-3;
    }
}
```

- [ ] **Step 3: Unify the home kicker**

In `index.html:9`, change `class="intro-kicker"` to `class="page-kicker"`, then delete the `.intro-kicker` rule from `_sass/_pages.scss`.

The two rules are identical but for `text-transform: uppercase` — a no-op, since the markup text is already uppercase — and their margin. `script/verify-redesign.sh` asserts on the kicker's *text*, not its class, so the gate is unaffected.

- [ ] **Step 4: Delete `.intro-inner`**

Remove the `<div class="intro-inner">` wrapper from `index.html` (keeping its children) and the `.intro-inner` rule from `_sass/_pages.scss`. Its 780px measure would otherwise sit inside `.page-lead`'s 820px and make the home lead narrower than every other page's.

Nothing depends on it: no descendant selector references it, and `.intro-kicker`/`.intro-actions` are top-level rules. Removing one half without the other fails the dead-selector gate.

- [ ] **Step 5: Give `course.html` the header it never had**

Its kicker, title and note sit bare inside `.detail-main` — a grid column. `project.html` puts `.detail-head` above `.detail-grid` at full width. Match that. Move these three elements out of `.detail-main` to just above `<div class="detail-grid detail-grid-narrow">`:

```html
<header class="detail-head">
    <p class="page-kicker">
        {{ page.course_code }}{% if page.term %} &middot; {{ page.term }}{% endif %}
    </p>
    <h1 class="page-title">{{ course_name }}</h1>
    {% if page.note %}
    <p class="page-lead">{{ page.note }}</p>
    {% endif %}
</header>
```

`.page-body` and everything after it stays inside `.detail-main`.

- [ ] **Step 6: Give `about.html` the same treatment**

Its kicker, title and lead sit bare inside `.bio-grid > .bio-main`. Move those three elements out of `.bio-grid` entirely into a `<header class="detail-head">` above it, so the band spans full width like every other page. The portrait and prose stay in `.bio-grid`.

Then check `.bio-grid`'s two-column layout still resolves with the heading gone — it may have been relying on `.bio-main` carrying that content.

- [ ] **Step 7: Remove the redundant hairlines**

Delete `<div class="page-rule"></div>` from `projects.html:17`, `archives.html:39` and `_layouts/tag.html:40`.

Two sit directly under the header, where a bordered band makes the hairline a second line doing the same job. `archives.html` is different: there it separates the tag strip from the year list. It is removed because `.tag-strip` already carries a bottom margin and `.year-block` is itself bordered, so the boundary survives.

Then check whether `.page-rule` is used anywhere else:

```bash
grep -rn "page-rule" --include=*.html --include=*.md . | grep -v _site
```

If nothing uses it, delete the rule from the Sass too — otherwise the dead-selector gate fails the build.

- [ ] **Step 8: Build and run the gates**

```bash
bundle exec jekyll build
bash script/verify-redesign.sh          # 26 PASS
python script/dead-css.py --count       # 0
python script/geometry.py | grep -c intro-band       # expect 0
find _site -name "*.html" | wc -l       # 153
grep -rn "@media" _sass/ | grep -v _tokens.scss || echo ok
```

This task owns three violations: `.page-head`'s `margin: 0 0 28px`, and `.intro-band`'s desktop `52px 48px` and mobile `28px 20px` paddings. All three become tokens, so the total drops from 92 to 89.

- [ ] **Step 9: Verify one band per page, at every breakpoint**

Serve with `bash script/preview.sh 4325` (`jekyll serve --detach` crashes on Windows). With Playwright, visit `/`, `/about/`, `/projects/`, `/csumb/`, `/archives/`, `/projects/ggswarm/`, `/csumb/cst363/`, `/tags/ggswarm/` at **390, 768, 861, 1280**:

```js
() => {
  const sel = '.page-head, .detail-head, .intro-band';
  const band = document.querySelector(sel);
  return {
    overflow: document.documentElement.scrollWidth > window.innerWidth,
    bandCount: document.querySelectorAll(sel).length,
    bandImage: band ? getComputedStyle(band).backgroundImage.slice(0, 48) : 'NO BAND',
    bandWidth: band ? Math.round(band.getBoundingClientRect().width) : null
  };
}
```

Assert on every page: no horizontal overflow, `bandCount === 1`, `bandImage` contains `linear-gradient`, and `bandWidth` identical between `/projects/` and `/projects/ggswarm/` at a given viewport. The null guard matters — a page with no band must report `NO BAND`, not throw.

Then load any blog post and confirm `bandCount === 0`.

- [ ] **Step 10: Confirm the grid costs no contrast**

The grid is `rgba($c-accent, 0.045)` over `$c-bg`, so the shift should be negligible — but this site has already shipped one AA failure from stacked transparency, so measure. On `/`, `/projects/` and `/projects/ggswarm/` at 1280, check `.page-kicker`, `.page-title` and `.page-lead` compute to at least 4.5:1 against `rgb(20,24,24)`.

- [ ] **Step 11: Commit**

```bash
git add -A
git commit -m "feat(css): one banded, blueprint-gridded header on every page

Six header shapes become one band treatment applied to the elements that
already existed, and the grid appears there and nowhere else. course.html and
about.html gain the wrapper they never had, both above their grid so the band
is full width everywhere.

.page-head loses its 820px cap - the reading measure moves to .page-lead, which
already carries its own. .intro-inner is deleted for the same reason, and
.intro-kicker is unified into .page-kicker so the home band gets the same kicker
rhythm as every other page.

Blog posts keep their plain header: a post is a reading surface and the texture
fights body prose."
```

---

### Task 4: Spacing remap

100 declarations. Mechanical but large, so it is scripted and then reviewed, not hand-edited. Independent of Tasks 2 and 3.

**Files:**

- Create: `script/remap-spacing.py` (a one-shot migration, deleted in Step 6)
- Modify: all seven partials under `_sass/`

**Interfaces:**

- Consumes: `$space-half`, `$space-1` … `$space-6` from Task 1.

- [ ] **Step 1: Snapshot, so the diff can be reviewed as a whole**

```bash
bundle exec jekyll build
cp _site/assets/css/styles.css "$SCRATCH/t4-before.css"
git rev-parse HEAD > "$SCRATCH/t4-base.txt"
```

- [ ] **Step 2: Write the migration script**

Create `script/remap-spacing.py`. It applies the spec's table, skips comments, ignores horizontal-only components, and leaves every named exemption alone.

```python
#!/usr/bin/env python3
"""One-shot spacing migration. Applies the remap table from
docs/superpowers/specs/2026-09-17-page-consistency-design.md and is deleted
once the change is committed. Not a permanent tool: script/geometry.py is.
"""
import io, re, glob

TARGET = {7: "$space-1", 9: "$space-1", 10: "$space-1",
          12: "$space-2", 13: "$space-2", 14: "$space-2", 15: "$space-2",
          18: "$space-2", 20: "$space-3", 22: "$space-3", 26: "$space-3",
          28: "$space-3", 36: "$space-4", 44: "$space-5"}

# No selector table on purpose: it must agree with script/geometry.py, which
# has none. TARGET holds only values above 6px, so optical values are untouched
# by construction, and vertical_indices() ignores the horizontal axis. An
# earlier draft carried an exemption list here and it disagreed with the
# checker - .status-tag { gap: 9px } would have been skipped by the migration
# and then flagged by the gate.
DECL = re.compile(r'^(\s*)(margin|padding|gap|row-gap|column-gap)'
                  r'(-top|-bottom|-left|-right)?(\s*:\s*)([^;]+)(;.*)$')

def vertical_indices(prop, side, parts):
    """Which components of a shorthand are vertical."""
    if prop in ("gap", "row-gap"): return list(range(len(parts)))
    if prop == "column-gap": return []
    if side in ("-left", "-right"): return []
    if side in ("-top", "-bottom"): return list(range(len(parts)))
    if len(parts) == 1: return [0]
    if len(parts) in (2, 3): return [0]
    if len(parts) == 4: return [0, 2]
    return []

def migrate(path):
    src = io.open(path, encoding="utf-8").read()
    out, sel, changed = [], "", 0
    for line in src.splitlines(keepends=True):
        stripped = line.strip()
        if re.match(r'^[^\s{}/@][^{}]*\{', line):
            sel = stripped.split("{")[0].strip()
        m = DECL.match(line.rstrip("\n"))
        if not m or stripped.startswith("//"):
            out.append(line); continue
        indent, prop, side, colon, value, tail = m.groups()
        parts = value.split()
        vidx = vertical_indices(prop, side or "", parts)
        new_parts, hit = list(parts), False
        for i in vidx:
            pm = re.fullmatch(r'(\d+)px', parts[i])
            if not pm: continue
            n = int(pm.group(1))
            if n in TARGET:
                new_parts[i] = TARGET[n]; hit = True
        if hit:
            out.append(f"{indent}{prop}{side or ''}{colon}{' '.join(new_parts)}{tail}\n")
            changed += 1
        else:
            out.append(line)
    io.open(path, "w", encoding="utf-8", newline="").write("".join(out))
    return changed

total = 0
for p in sorted(glob.glob("_sass/*.scss")):
    n = migrate(p)
    total += n
    print(f"  {p}: {n}")
print(f"total: {total}")
```

- [ ] **Step 3: Run it and check the count**

```bash
python script/remap-spacing.py
```

Expected: **89**, the share of the 100 baseline this task owns. (Task 2 clears 8 radius literals; Task 3 clears 3 band declarations.) A materially different total means the axis logic or the target table differs from what this plan was written against; investigate before building.

- [ ] **Step 4: Apply the one hand edit the script cannot make**

`.page-kicker`'s `margin-bottom` is the sole place `$space-half` is legal. The script will have turned its `14px` into `$space-2`; change it to the compound:

```scss
    margin: 0 0 $space-1 + $space-half;
```

This is 12px, and keeps the kicker bound tighter to the title than the title is to the lead — the distinction a flat scale would erase.

- [ ] **Step 5: Verify with the checker, not a grep**

```bash
bundle exec jekyll build
python script/geometry.py --count
```

Expected: **0** if Tasks 2 and 3 have already run; otherwise exactly the count they still owe — 8 radius literals if Task 2 has not run, 3 band declarations if Task 3 has not.

Run `python script/geometry.py` and confirm every remaining line belongs to one of those two tasks. A *spacing* violation surviving here is a miss in the migration, and the `--count` is the acceptance measure — do not substitute a grep, which is how the axis and optical rules get accidentally re-implemented wrongly.

- [ ] **Step 6: Delete the migration script**

```bash
rm script/remap-spacing.py
```

It is a one-shot. Leaving it invites someone to run it twice.

- [ ] **Step 7: Review the visual diff at every breakpoint**

This task cannot be verified by byte comparison — it is a deliberate change to 100 declarations. Serve with `bash script/preview.sh 4325` and compare against `$SCRATCH/t4-before.css` by swapping the stylesheet, at **390, 768, 861, 1280**, on `/`, `/about/`, `/projects/`, `/csumb/`, `/archives/`, `/projects/ggswarm/`, `/csumb/cst363/`, `/tags/ggswarm/`, and one blog post.

You are looking for: no horizontal overflow, no element overlapping another, no collapsed or doubled gap, and 44px touch targets still met at 390px. Individual 2-4px shifts are expected and correct.

- [ ] **Step 8: Run the gates**

```bash
bash script/verify-redesign.sh          # 26 PASS
python script/dead-css.py --count       # 0
find _site -name "*.html" | wc -l       # 153
```

- [ ] **Step 9: Commit**

```bash
git add -A
git commit -m "refactor(css): put all vertical spacing on the 8px scale

100 declarations across seven partials move onto \$space-1..6. Nothing shifts
more than 4px individually; collectively this is the rhythm the site never had.

Exemptions are by named selector, not category: chip and badge optical padding,
horizontal-only nav and footer insets, and one negative overlap offset. A
linter cannot infer those from the source, so they are listed in the spec.

.page-kicker is the one place \$space-half is legal, keeping the kicker bound
tighter to the title than the title is to the lead."
```

---

### Task 5: Wire the gate into CI

The checker already exists and already passes — Task 1 built it and Tasks 2, 3 and 4 drove it to zero. This task only makes it binding.

**Files:**

- Modify: `.github/workflows/lint.yml`

**Interfaces:**

- Consumes: `script/geometry.py` from Task 1, and a tree that Tasks 2-4 have taken to `--count` → `0`.

- [ ] **Step 1: Confirm the tree is actually clean first**

```bash
python script/geometry.py --count
```

Expected: **0**. If it is not, a preceding task is incomplete — **stop and finish it**. Wiring a gate onto a tree that cannot pass it turns the next person's unrelated commit into a red build, and the usual response to that is to delete the gate.

- [ ] **Step 2: Add the CI step**

In `.github/workflows/lint.yml`, add this immediately after the existing `Dead CSS check` step. It needs no build — it reads `_sass/`, not `_site/` — so its position relative to the Jekyll build does not matter, but keeping the two audits adjacent makes them easy to find.

```yaml
      - name: Geometry check
        run: |
          count=$(python3 script/geometry.py --count)
          echo "geometry violations: $count"
          if [ "$count" -gt 0 ]; then
            python3 script/geometry.py
            echo "::error::$count geometry violations. Use the token scales in _sass/_tokens.scss, or change the rule in the spec - not the script's constants."
            exit 1
          fi
```

- [ ] **Step 3: Validate the workflow**

```bash
ruby -ryaml -e "y=YAML.load_file('.github/workflows/lint.yml'); y['jobs'].each{|k,j| j['steps'].each_with_index{|s,i| puts \"#{i}: #{s['name']}\"}}"
docker run --rm -v "/$(pwd)://repo" -w //repo rhysd/actionlint:latest
```

Expected: the step is listed in order, and actionlint exits 0. `python3` is the correct invocation on `ubuntu-latest`; plain `python` is not on PATH there.

- [ ] **Step 4: Prove the gate actually fails the job**

The checker's own behaviour was verified in Task 1. What is unverified here is the shell wrapper — that a non-zero count reaches `exit 1`.

```bash
printf '
.probe {
    margin-bottom: 13px;
}
' >> _sass/_utilities.scss
count=$(python3 script/geometry.py --count); echo "count=$count"
if [ "$count" -gt 0 ]; then echo "GATE WOULD EXIT 1"; fi
git checkout _sass/_utilities.scss
python3 script/geometry.py --count      # back to 0
git status --porcelain                  # empty
```

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/lint.yml
git commit -m "build: fail the build on geometry that bypasses the scales

script/geometry.py has reported zero since the radius and spacing migrations
landed; this makes it binding. Rejects a px literal on the vertical axis of
margin/padding/gap above the optical 6px threshold, and any unmarked px
border-radius.

A new exemption is a spec change, not an edit to the script's constants."
```

---

### Task 6: Update the architecture guide

`docs/css-architecture.md` is the normative reference and is stale on five points after Tasks 1-5.

**Files:**

- Modify: `docs/css-architecture.md`

- [ ] **Step 1: Correct the partial table**

- The `_tokens.scss` row says "variables only; emits no CSS". Still true — a mixin emits only where used — but it now also holds the spacing scale, the radius scale, the grid pitch tokens and `blueprint-grid()`. Say so.
- The `_layout.scss` row gains the band.
- The `_pages.scss` row loses `.intro-band` as a one-page component; it is now an override of a shared rule.

- [ ] **Step 2: Add the page skeleton**

State the three-part anatomy — header band, body, page actions — and the archetype table from the spec's Section 1, including that blog posts are the one deliberate exclusion and why.

- [ ] **Step 3: Add the two scales**

The six spacing steps and the half-step's single legal use; the three radius tokens and the two `// OPTICAL` exemptions. State the three mechanical rules that define what the scale governs — vertical axis only, 6px and under is optical, negatives are offsets — and point at the spec rather than restating them at length. The spec deliberately has no exemption list: an earlier draft named ten selectors and the rules turned out to subsume all of them plus nine it had missed.

- [ ] **Step 4: Document the gate**

List `script/geometry.py` alongside the dead-selector audit: what it rejects, how to run it, and that a new exemption is a spec change rather than an edit to the script's constant.

- [ ] **Step 5: Keep it under 150 lines and passing lint**

```bash
wc -l < docs/css-architecture.md
npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml
```

The guide is currently 149 lines and the budget is real — a guide nobody reads is worse than none. Cut older prose to make room rather than letting it sprawl.

- [ ] **Step 6: Commit**

```bash
git add docs/css-architecture.md
git commit -m "docs: document the page skeleton, both geometry scales and the gate"
```

---

## Final verification

- [ ] **Everything green**

```bash
bundle exec jekyll build && echo "build=$?"
bash script/verify-redesign.sh              # 26 PASS
python script/dead-css.py --count           # 0
python script/geometry.py --count           # 0
bundle exec rubocop
npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml
find _site -name "*.html" | wc -l           # 153
grep -rn "@media" _sass/ | grep -v _tokens.scss || echo ok
grep -rn "border-radius:[^;]*px" _sass/     # exactly 2, both // OPTICAL
git ls-files -s CLAUDE.md                   # mode 120000, blob 47dc3e3d...
```

- [ ] **The spec's success criteria, one at a time**

Walk the nine criteria in the spec's Success Criteria section and confirm each. They are the acceptance test; this plan is only the route to them.

- [ ] **Four viewports, eight archetypes**

390, 768, 861, 1280 on `/`, `/about/`, `/projects/`, `/csumb/`, `/archives/`, `/projects/ggswarm/`, `/csumb/cst363/`, `/tags/ggswarm/`, plus one blog post: exactly one band per page (zero on the post), no horizontal overflow, single column below 1024px, 44px touch targets at mobile.

- [ ] **Shipping**

Merge to `publish` and push. If any image changed, its filename must change too.

## Notes for the executor

- **Tasks 2, 3 and 4 are independent.** If you are running them in sequence and one fails review, the other two are unaffected.
- **Task 1 and Task 5 are the bookends**: Task 1 must be first because everything consumes its tokens, and Task 5 must be last because the gate fails on anything the middle tasks have not fixed.
- **Task 4 is the only task that cannot be verified by byte comparison.** It is a deliberate change to 100 declarations; its verification is visual and per-viewport. Budget for that.
- **Task 5 is the task most likely to be got wrong**, per the spec. Do not skip Step 4 — the checker tolerating correct code matters as much as it catching violations.
- This plan's spec was reviewed twice and rewritten twice, both times for defects in the spacing and enforcement halves. If a step here cannot be satisfied as written, **say so and stop** — do not substitute a weaker check.
- The older plan at `docs/superpowers/plans/2026-09-17-blueprint-consistency-and-backlog.md` has its Task 1 superseded by this plan. **Its Tasks 2-5 are unaffected and still stand**: the GG Swarm roadmap, the tag-page fix, content metadata, and the `main`/`publish` sync.
