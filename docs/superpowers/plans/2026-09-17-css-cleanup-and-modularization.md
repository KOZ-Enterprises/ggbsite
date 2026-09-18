# CSS Cleanup, Modularization & Review Fixes — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the ten findings from the whole-branch code review, delete the 129 dead selectors left behind by the redesign, and restructure a 3,337-line single stylesheet into documented Sass partials with one breakpoint system.

**Architecture:** Jekyll compiles Sass natively — `jekyll-sass-converter 3.1.0` and `sass-embedded` are already installed as Jekyll 4 dependencies, so this adds **no gems, no npm, and no build step**. Source moves to `_sass/` partials; `assets/css/styles.scss` becomes a thin manifest of `@use` rules and compiles to the same `/assets/css/styles.css` URL the site already links. One HTTP request, unchanged.

**Tech Stack:** Jekyll 4.4.1, jekyll-sass-converter 3.1.0, sass-embedded 1.93.2, Liquid, vanilla CSS/SCSS. No test framework — verification is `bundle exec jekyll build` plus `script/verify-redesign.sh` assertions against built `_site/` output, plus Playwright measurement at four viewport widths.

**Spec:** This plan is its own spec. The review findings it implements are reproduced verbatim in Task 1; the design decisions (Sass partials, full dead-code removal) were chosen by the user on 2026-09-17.

---

## Global Constraints

**The palette is closed.** Every colour must already exist in this table. No new values.

| Token | Hex | Use |
| --- | --- | --- |
| Page background | `#141818` | body, page ground |
| Surface | `#1a1e1e` | cards, navbar, sidebar modules |
| Surface deep | `#0f1111` | year-block headers, code blocks |
| Surface hover | `#1e2323` | card hover fill |
| Border | `#2e4c5b` | all 1px borders |
| Rule | `#1f2a2a` | section hairlines |
| Accent teal | `#64d5d2` | primary accent, active state, links |
| Accent hover | `#7fe3e0` | primary button hover |
| Amber | `#ffb300` | kickers, forward links, PLANNED |
| Blue | `#5bc0de` | tech chips, SHIPPED/COMPLETE |
| Ink | `#fafafa` | headings, primary text |
| Body | `#b9c4c4` | lead paragraphs, body copy |
| Body dim | `#9aa6a6` | excerpts, secondary copy |
| Muted | `#8a9696` | mono meta, dates, counts |
| Muted alt | `#8ba3a3` | inactive nav links, neutral status |
| Muted low | `#7d8a8a` | placeholder labels, separators |

- **Never use a text colour darker than `#7d8a8a`.**
- **Type scale is fixed at three roles.** `.page-title` `clamp(30px, 4.2vw, 44px)/1.08`, `.page-lead` `17px/1.65`, `.page-body` `16px/1.8`. Do not introduce a fourth.
- **Status vocabulary is exactly four values:** `active`, `planned`, `shipped`, `dormant`. Course pages add `completed` / `in-progress`.
- **Minimum touch target is 44px.** Minimum type: 9.5px mono, 14px body.
- **Do not change any rendered output.** This is a refactor. The built HTML must be byte-identical before and after every CSS-only task — that is the primary guard and it is asserted mechanically.
- **`assets/css/styles.css` must keep its URL.** `_includes/head.html` links `/assets/css/styles.css`; the Sass manifest must compile to exactly that path.

**Verification baseline:** `bundle exec jekyll build` exits 0; `script/verify-redesign.sh` reports 26 PASS; 153 HTML pages; 1,967 internal links resolve; zero horizontal overflow at 390px.

---

## The breakpoint problem

The stylesheet currently has **nine media queries at six different breakpoints** — 500, 700 (×3), 768, 800 (×2), 860, 992 — accreted from the pre-redesign site and tonight's work. There is no system, and the gap between them is where the review found a real bug: the navbar switches to the hamburger at 860px but `.detail-grid` does not collapse until 700px, so **701–860px renders a mobile nav above a desktop two-column body**. At 768px the sidebar (320px) is wider than the main column (318px).

This plan collapses everything to **three named breakpoints**:

| Name | Width | Meaning |
| --- | --- | --- |
| `$bp-wide` | 1024px | multi-column page layouts collapse below this |
| `$bp-nav` | 860px | navbar switches to the toggle (unchanged — spec-mandated) |
| `$bp-mobile` | 700px | single-column, mobile type scale, touch targets |

The 1024px tier is new and is what fixes the tablet band.

---

## File Structure

`_sass/` partials, each with one responsibility. A rule's home is decided by what it styles, not when it was written.

| File | Responsibility |
| --- | --- |
| `_sass/_tokens.scss` | palette, type scale, spacing, radii, breakpoints — variables only, emits no CSS |
| `_sass/_base.scss` | element defaults: `html`, `body`, headings, links, lists, tables, `#main` |
| `_sass/_layout.scss` | page shells: `.page-head`, `.page-rule`, `.detail-grid`, `.bio-grid`, `.about-cols` |
| `_sass/_nav.scss` | `.nav-shell` and everything inside it, including its 860px behaviour |
| `_sass/_footer.scss` | `footer`, `.footer-mark`, `.social-icons` |
| `_sass/_components.scss` | reusable units: `.card`, `.wide-card`, `.log-row`, `.status-tag`/`.status-badge`, `.rule-header`, `.side-module`, `.tech-chip`, `.btn-*`, `.breadcrumb` |
| `_sass/_pages.scss` | page-specific: `.intro-band`, `.feature-hero`, `.capstone-card`, `.registry`, `.year-block`, `.xp-list`, `.edu-list`, `.post-*` |
| `_sass/_content.scss` | prose rendered from Markdown: `.page-body` descendants, code blocks, embeds, Mermaid |
| `_sass/_utilities.scss` | the surviving utility classes |
| `assets/css/styles.scss` | manifest — `@use` rules and a header comment, nothing else |

**Responsive rules live with their component**, inside the partial that owns them, using the mixins from `_tokens.scss`. There is no separate `_responsive.scss` — a single mobile block at the end of a 3,000-line file is exactly what let the 768px gap hide.

---

### Task 0: Establish the Sass pipeline with zero visual change

Prove the toolchain before moving a single rule. This task produces **byte-identical CSS output**.

**Files:**
- Create: `_sass/_tokens.scss`
- Create: `assets/css/styles.scss`
- Delete: `assets/css/styles.css` (content moves into a temporary partial)
- Create: `_sass/_legacy.scss` (the entire current stylesheet, verbatim, to be dismantled in later tasks)
- Modify: `_config.yml` (Sass output style)

**Interfaces:**
- Produces: a working `_sass/` → `/assets/css/styles.css` pipeline, and `$bp-wide` / `$bp-nav` / `$bp-mobile` plus the `respond-to()` mixin every later task uses.

- [ ] **Step 1: Capture the current CSS as the comparison baseline**

```bash
cd /g/Code/ggbsite
bundle exec jekyll build
cp _site/assets/css/styles.css /g/tmp/css-baseline.css
wc -l /g/tmp/css-baseline.css
```

- [ ] **Step 2: Move the stylesheet verbatim into a partial**

```bash
mkdir -p _sass
git mv assets/css/styles.css _sass/_legacy.scss
```

Nothing is edited. `_legacy.scss` is valid SCSS because SCSS is a CSS superset.

- [ ] **Step 3: Write the token partial**

Create `_sass/_tokens.scss`:

```scss
// =============================================================================
// TOKENS
// Variables only. This file must emit no CSS.
// Every colour here already existed in the pre-refactor stylesheet; the
// palette is closed and additions need a design decision, not a commit.
// =============================================================================

// ---- Colour ----------------------------------------------------------------
$c-bg:            #141818;  // page ground
$c-surface:       #1a1e1e;  // cards, navbar, sidebar modules
$c-surface-deep:  #0f1111;  // year headers, code blocks
$c-surface-hover: #1e2323;  // card hover fill
$c-border:        #2e4c5b;  // every 1px border
$c-rule:          #1f2a2a;  // section hairlines
$c-accent:        #64d5d2;  // primary teal
$c-accent-hover:  #7fe3e0;
$c-amber:         #ffb300;
$c-blue:          #5bc0de;
$c-ink:           #fafafa;
$c-body:          #b9c4c4;
$c-body-dim:      #9aa6a6;
$c-muted:         #8a9696;
$c-muted-alt:     #8ba3a3;
$c-muted-low:     #7d8a8a;  // darkest permitted text colour

// ---- Type ------------------------------------------------------------------
$font-display: "Chakra Petch", "Roboto", sans-serif;
$font-body:    "Roboto", sans-serif;
$font-mono:    "Roboto Mono", monospace;

$text-title: clamp(30px, 4.2vw, 44px);
$text-lead:  17px;
$text-body:  16px;
$text-excerpt: 14.5px;
$text-meta:  11px;

$lh-title: 1.08;
$lh-lead:  1.65;
$lh-body:  1.8;

// ---- Space & shape ---------------------------------------------------------
$radius-card: 6px;
$radius-chip: 3px;
$touch-min:   44px;  // minimum interactive target

// ---- Breakpoints -----------------------------------------------------------
// Three tiers, no more. Anything else re-creates the 701-860px gap where a
// mobile navbar sat above a desktop two-column body.
$bp-wide:   1024px;  // multi-column page layouts collapse below this
$bp-nav:     860px;  // navbar switches to the toggle
$bp-mobile:  700px;  // single column, mobile type scale

@mixin respond-to($bp) {
  @if $bp == wide       { @media screen and (max-width: $bp-wide)   { @content; } }
  @else if $bp == nav   { @media screen and (max-width: $bp-nav)    { @content; } }
  @else if $bp == mobile{ @media screen and (max-width: $bp-mobile) { @content; } }
  @else { @error "Unknown breakpoint `#{$bp}`. Use wide, nav, or mobile."; }
}
```

- [ ] **Step 4: Write the manifest**

Create `assets/css/styles.scss` — note the empty front matter, which is what tells Jekyll to process the file:

```scss
---
# Empty front matter is required: it marks this file for Jekyll processing.
---

// =============================================================================
// GGBytes stylesheet
//
// Source lives in _sass/. This manifest only composes it. Compiles to
// /assets/css/styles.css, the path _includes/head.html links.
//
// Where does a new rule go?
//   a colour or size literal ......... _tokens.scss (then reference it)
//   an element default ............... _base.scss
//   a page shell or grid ............. _layout.scss
//   reused on 2+ pages ............... _components.scss
//   used on exactly one page ......... _pages.scss
//   styles Markdown-rendered prose ... _content.scss
//
// Responsive rules live WITH their component, via @include respond-to().
// =============================================================================

@use "tokens" as *;
@use "legacy";
```

- [ ] **Step 5: Set Sass output style**

In `_config.yml`, add:

```yaml
sass:
  style: compressed
```

- [ ] **Step 6: Build and prove the output is equivalent**

Run:
```bash
bundle exec jekyll build
ls -la _site/assets/css/styles.css
```
Expected: the file exists at the same path.

Because Step 5 compresses the output, compare *semantically* rather than byte-wise — strip whitespace and comments from both and diff:

```bash
python - <<'PY'
import re, io
def norm(p):
    s = io.open(p, encoding='utf-8').read()
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.S)   # comments
    s = re.sub(r'\s+', '', s)                      # all whitespace
    return s
a = norm('/g/tmp/css-baseline.css')
b = norm('_site/assets/css/styles.css')
print('baseline chars:', len(a))
print('compiled chars:', len(b))
print('IDENTICAL' if a == b else 'DIFFERS')
if a != b:
    for i,(x,y) in enumerate(zip(a,b)):
        if x != y:
            print('first divergence at', i)
            print('  baseline:', a[max(0,i-60):i+60])
            print('  compiled:', b[max(0,i-60):i+60])
            break
PY
```
Expected: `IDENTICAL`. If it differs, do not proceed — the pipeline is not equivalent and every later task's guard depends on it.

- [ ] **Step 7: Confirm the site is unchanged**

Run:
```bash
bash script/verify-redesign.sh
find _site -name "*.html" | wc -l
```
Expected: 26 PASS, 153 pages.

- [ ] **Step 8: Commit**

```bash
git add -A
git commit -m "build: compile CSS from _sass partials

Moves the stylesheet into _sass/_legacy.scss verbatim and adds a manifest at
assets/css/styles.scss. jekyll-sass-converter is already a Jekyll 4
dependency, so this adds no gems and no build step, and still compiles to the
same /assets/css/styles.css URL.

Adds _sass/_tokens.scss with the palette, type scale, and three named
breakpoints, replacing the six ad-hoc widths the stylesheet had accreted.

No rendered change: compiled CSS is semantically identical to the previous
file (whitespace- and comment-stripped comparison).

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 1: Fix the ten code-review findings

Behaviour changes, done before the refactor so the refactor has a correct target. Grouped into one task because each is small and they share a verification pass.

**Files:**
- Modify: `_layouts/tag.html`, `_layouts/course.html`, `_layouts/post.html`, `_includes/nav.html`, `_includes/head.html`, `csumb.html`, `_sass/_legacy.scss`, `assets/js/scripts.js`

**Interfaces:**
- Produces: `.card-head` that cannot overflow; `.detail-grid` with a 1024px tier; `tagged_docs` filtered to projects; `aria-expanded` wired to `toggleNavbar()`.

- [ ] **Step 1: MEDIUM — stop course docs rendering as project cards**

`_plugins/tag_generator.rb` fills `tagged_docs` from *any* non-post collection doc carrying `tags`/`tools`/`tech_stack`. `_csumb/cst370.md` and `_csumb/cst462s.md` declare `tags:`, so `/tags/csumb/` renders two course pages as `wide-card` project cards with "No preview" and an empty body, and counts them as "2 projects".

In `_layouts/tag.html`, filter to the projects collection. Replace:

```liquid
{%- assign doc_count = page.tagged_docs | size -%}
```

with:

```liquid
{%- comment -%}
tagged_docs is filled from every non-post collection doc with tags, which
includes _csumb course pages. Courses have no description or image, so they
render as empty "No preview" project cards. Restrict to real projects.
{%- endcomment -%}
{%- assign project_urls = site.projects | map: "url" -%}
{%- assign tagged_projects = page.tagged_docs | where_exp: "d", "project_urls contains d.url" -%}
{%- assign doc_count = tagged_projects | size -%}
```

Then change the loop from `{% for doc in page.tagged_docs %}` to `{% for doc in tagged_projects %}`.

- [ ] **Step 2: Verify the tag fix**

Run:
```bash
bundle exec jekyll build
# Anchor the class name: a bare `wide-card` also matches wide-card-list,
# wide-card-media, wide-card-body and wide-card-head, over-counting 3 as 13.
echo "csumb tag projects:  $(grep -o 'class="wide-card"' _site/tags/csumb/index.html | wc -l)"
echo "python tag projects: $(grep -o 'class="wide-card"' _site/tags/python/index.html | wc -l)"
```
Expected: `csumb` → `0` (was 2 bogus course cards); `python` → `3` (real projects, unchanged).

- [ ] **Step 3: MEDIUM — stop status badges overflowing project cards**

At 768px each card is ~210px wide and `.card-head` is a flex row with no wrap, so the badge is pushed past the card's padding box and clipped by `overflow: hidden`.

In `_sass/_legacy.scss`, find `.card-head` and `.card-title`, and amend:

```css
.card-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 10px;
    flex-wrap: wrap;          /* added: badge drops to its own line before clipping */
}

.card-title {
    /* … existing declarations … */
    min-width: 0;             /* added: allows the title to shrink instead of shoving the badge out */
}
```

And on the shared badge rule, add:

```css
.status-badge {
    /* … existing declarations … */
    flex: 0 0 auto;
    white-space: nowrap;
}
```

- [ ] **Step 4: MEDIUM — add the 1024px tier that fixes the tablet band**

Append a new media block to `_sass/_legacy.scss`, immediately **before** the existing 700px block so the mobile rules still win:

```css
/* ---------- Wide tablet (≤1024px) ----------
   The navbar switches to the toggle at 860px but the page grids only
   collapsed at 700px, so 701-860px rendered a mobile navbar above a desktop
   two-column body. At 768px the 320px sidebar was wider than the 318px main
   column. This tier collapses the page grids before that can happen. */
@media screen and (max-width: 1024px) {
    .detail-grid,
    .detail-grid-narrow {
        grid-template-columns: minmax(0, 1fr);
        gap: 32px;
    }

    .card-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .bio-grid,
    .about-cols {
        grid-template-columns: minmax(0, 1fr);
        gap: 32px;
    }

    .bio-portrait {
        max-width: 320px;
    }
}
```

- [ ] **Step 5: Verify the tablet band renders correctly**

Build, serve, and measure at the three widths that were broken:

```bash
bundle exec jekyll build
bash script/preview.sh 4300 &
sleep 2
```

Using Playwright at **768px**, **861px**, and **1024px**, navigate to `/projects/ggswarm/` and evaluate:

```js
(() => {
  const g = document.querySelector('.detail-grid');
  const main = document.querySelector('.detail-main');
  const side = document.querySelector('.detail-side');
  return {
    cols: getComputedStyle(g).gridTemplateColumns,
    mainW: Math.round(main.getBoundingClientRect().width),
    sideW: Math.round(side.getBoundingClientRect().width),
    sidebarWiderThanMain: side.getBoundingClientRect().width > main.getBoundingClientRect().width,
    overflow: document.documentElement.scrollWidth > window.innerWidth
  };
})()
```

Expected at 768px and 861px: a single column, `sidebarWiderThanMain: false`, `overflow: false`. Expected at 1024px: single column (the tier is inclusive). Also check `/projects/` at 768px — `.card-grid` should report two columns and no card should clip its badge.

**Stop the server when done.** `pkill -f "http.server"` may not match; find the PID under `/proc/*/cmdline` and `kill -9`, then confirm with curl.

- [ ] **Step 6: LOW — give the hamburger a real accessible state**

This was deliberately skipped during the redesign because the spec forbade touching `scripts.js`. That constraint expired with the redesign; it is now a two-line change.

In `_includes/nav.html`:

```html
    <button class="nav-icon" type="button" onclick="toggleNavbar()" aria-label="Menu"
        aria-expanded="false" aria-controls="myNavbar">
```

In `assets/js/scripts.js`, replace `toggleNavbar` with:

```js
function toggleNavbar() {
  const nav = document.getElementById("myNavbar");
  const open = nav.classList.toggle("responsive");
  const btn = nav.querySelector(".nav-icon");
  if (btn) btn.setAttribute("aria-expanded", String(open));
}
```

- [ ] **Step 7: LOW — five consistency and dead-code fixes**

1. **Breadcrumb label.** `_layouts/post.html` labels `/archives/` as "Log" while `_layouts/tag.html` and `archives.html` call it "Archives". Change post's to `Archives`.

2. **Capstone pill vocabulary.** `csumb.html` uses `data-status="submitted"`, outside the four-value set, so it silently falls back to grey — indistinguishable from `dormant`. Change to `data-status="shipped"` and keep the label text `As submitted &middot; Apr 2026`.

3. **Raw status on tag pages.** `_layouts/tag.html` emits `{{ doc.status }}` raw. Wrap it in the same mapping the other two templates use:
```liquid
{%- if doc.status == "completed" -%}Complete
{%- elsif doc.status == "in-progress" -%}In progress
{%- else -%}{{ doc.status }}{%- endif -%}
```

4. **Uninitialized `idx`.** In `_layouts/course.html`, `idx` is only set inside the lookup loop. If `page.url` matches nothing, `idx` stays nil and `nil | plus: 1` yields `1`, rendering a wrong "next" link. Add `{%- assign idx = -1 -%}` before the loop and guard the next branch on `{% if idx >= 0 and next_idx < course_total %}`.

5. **Dead 700px block.** `_sass/_legacy.scss` has a `@media (max-width: 700px)` block setting `.intro-band { padding: 32px 22px }` and `.feature-hero-body { padding: 32px 22px }`. Both are unconditionally overridden by the later 700px block (`28px 20px`, `0 20px 28px`). Delete the earlier block entirely.

- [ ] **Step 8: LOW — drop unused font payload**

`_includes/head.html` still requests `Open+Sans` and `Roboto+Flex`; neither appears anywhere in the stylesheet. Chakra Petch requests weights `400;500` that are never used.

Verify first:
```bash
grep -c "Open Sans\|Roboto Flex" _sass/_legacy.scss
```
Expected: `0`. If non-zero, STOP and report rather than removing.

Then replace the font link's `href` with:

```
https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@600;700&family=Roboto+Mono:wght@400;500&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap
```

- [ ] **Step 9: Full verification**

Run:
```bash
bundle exec jekyll build && echo "build=$?"
bash script/verify-redesign.sh
grep -c 'aria-expanded' _site/index.html          # expect >= 1
grep -c '>Archives<' _site/2026/09/03/the-long-way-around.html   # breadcrumb
grep -o 'data-status="[a-z-]*"' _site/csumb/index.html | sort -u
```
Expected: build 0, 26 PASS, aria present, breadcrumb reads Archives, capstone pill reports `shipped`.

- [ ] **Step 10: Commit**

```bash
git add -A
git commit -m "fix: address whole-branch review findings

Medium:
- tag pages rendered _csumb course docs as empty project cards, because
  tagged_docs is filled from any collection doc with tags. /tags/csumb/
  showed two courses as 'No preview' cards counted as projects. Filtered to
  the projects collection.
- status badges overflowed and were clipped on project cards at 768px;
  .card-head now wraps and .card-title can shrink.
- 701-860px rendered a mobile navbar above a desktop two-column body, with
  the sidebar wider than the main column at 768px. Adds a 1024px tier.

Low: aria-expanded wired to toggleNavbar; post breadcrumb says Archives like
everywhere else; capstone pill uses the real vocabulary instead of an
unmatched value that fell back to grey; tag pages map status labels like the
other templates; course idx initialised so a missed lookup cannot render a
wrong next link; deleted a 700px block fully overridden by a later one;
dropped Open Sans and Roboto Flex, which nothing references.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 2: Delete the 129 dead selectors

45% of the stylesheet's selectors have zero occurrences across 153 built pages. They are debris from the templates the redesign replaced.

**Files:**
- Modify: `_sass/_legacy.scss`
- Create: `script/dead-css.py` (the audit tool, kept — it is how this is re-checked later)

**Interfaces:**
- Consumes: the Sass pipeline from Task 0, the corrected templates from Task 1.
- Produces: a `_legacy.scss` roughly half its former size, ready to be split in Task 3.

- [ ] **Step 1: Write the audit as a reusable script**

Create `script/dead-css.py`:

```python
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

def main():
    css = "".join(io.open(p, encoding="utf-8").read()
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

    dead = sorted(d for d in defined if d not in used and d not in RUNTIME)

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
```

```bash
chmod +x script/dead-css.py
git update-index --chmod=+x script/dead-css.py
```

- [ ] **Step 2: Record the starting count**

Run:
```bash
bundle exec jekyll build
python script/dead-css.py --count
```
Expected: `129` (or fewer, if Task 1 already removed some). Record the number — Step 6 asserts it reaches 0.

- [ ] **Step 3: Snapshot the rendered HTML as the safety net**

CSS removal cannot change markup. If any built page differs after this task, something other than CSS was touched.

```bash
mkdir -p /g/tmp/htmlsnap
find _site -name "*.html" -exec md5sum {} \; | sed 's|_site/||' | sort > /g/tmp/htmlsnap/before.txt
wc -l /g/tmp/htmlsnap/before.txt
```

- [ ] **Step 4: Delete the dead component blocks**

Work group by group, rebuilding and re-running the audit after each so a mistake is caught immediately. The 89 dead component selectors fall into these families:

| Group | Count | Examples |
| --- | --- | --- |
| old post layout | 13 | `.post-content`, `.post-date`, `.post-footer`, `.post-h1`, `.post-title`, `.post-meta` |
| old project layout | 13 | `.project-summary`, `.overlay-details`, `.project-container`, `.project-grid`, `.project-sidebar`, `.stretched-link` |
| old feed | 8 | `.update-feed`, `.update-item`, `.update-icon`, `.update-content`, `.update-link` |
| old timeline | 7 | `.timeline-item`, `.timeline-marker`, `.timeline-content`, `.timeline-title` |
| old cards | 8 | `.content-card`, `.featured-box`, `.featured-img`, `.mission-card`, `.pop-heading` |
| old course grid | 5 | `.course-item`, `.course-grid`, `.course-code-tag`, `.course-status-icon` |
| orphaned by this session | 4 | `.project-status-line`, `.project-status-detail`, `.intro-title`, `.detail-title`, `.post-h1`, `.course-title` |
| everything else | ~31 | `.archive-btn`, `.blueprint-grid`, `.headshot`, `.section-header`, `.objective-box`, `.tag`, `.resource-list` |

`.project-status-line` and `.project-status-detail` were added earlier in this session for `status_detail`, then orphaned when `_layouts/project.html` was rebuilt for artboard 4a — the feature still renders through `.detail-meta-text`.

After each group:
```bash
bundle exec jekyll build && python script/dead-css.py --count
```

- [ ] **Step 5: Delete the 40 dead utility classes**

The user chose full removal over keeping utilities. They are: the `m-*` / `mb-*` / `mt-*` / `my-*` / `p-*` / `gap-*` spacing set, `text-center` / `text-left` / `text-lg` / `text-italic`, `color-*` (`accent`, `amber`, `ccc`, `ddd`, `fafafa`, `muted`, `dark-muted`), `flex-*`, `font-bold`, `d-block`, `w-full`, `no-*`, `opacity-8`, `span-*`.

**Before deleting, re-verify against post Markdown**, since a hand-written post could use one inline and `_site` would then contain it — in which case the audit already excluded it. The audit is the authority; if `script/dead-css.py` lists it, it is unused.

- [ ] **Step 6: Assert the audit reaches zero**

Run:
```bash
bundle exec jekyll build
python script/dead-css.py --count
```
Expected: `0`.

- [ ] **Step 7: Assert no rendered HTML changed**

```bash
find _site -name "*.html" -exec md5sum {} \; | sed 's|_site/||' | sort > /g/tmp/htmlsnap/after.txt
diff /g/tmp/htmlsnap/before.txt /g/tmp/htmlsnap/after.txt && echo "IDENTICAL — no markup changed"
```
Expected: no diff. **If any page differs, stop** — a CSS-only task changed markup, which means something was deleted from a template by mistake.

- [ ] **Step 8: Confirm the site still renders**

```bash
bash script/verify-redesign.sh
wc -l _sass/_legacy.scss
```
Expected: 26 PASS, and a materially smaller file (roughly 1,700–1,900 lines, down from 3,337).

Then render `/`, `/projects/`, `/about/`, `/projects/ggswarm/` at 1280px and confirm nothing lost its styling — the audit proves selectors are unused, not that deletion was surgical.

- [ ] **Step 9: Commit**

```bash
git add -A
git commit -m "refactor(css): delete 129 dead selectors

45% of the stylesheet's class selectors had zero occurrences across all 153
built pages - debris from the templates the redesign replaced: the old post
and project layouts, the update feed, the old timeline and course grid, and
the utility set nothing referenced.

Four were orphaned by this session itself, including .project-status-line,
added for status_detail and then stranded when _layouts/project.html was
rebuilt for artboard 4a. The feature still renders via .detail-meta-text.

Adds script/dead-css.py so this is re-checkable rather than a one-off audit.
It reads _site rather than the templates, because built output is the only
oracle that includes everything Jekyll renders.

Guard: every built page's md5 is unchanged. A CSS-only change cannot alter
markup, so an identical HTML snapshot proves nothing else was touched.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 3: Split `_legacy.scss` into documented partials

The mechanical move. Every rule goes to the partial that owns it; responsive rules move inside their component via `respond-to()`.

**Files:**
- Create: `_sass/_base.scss`, `_layout.scss`, `_nav.scss`, `_footer.scss`, `_components.scss`, `_pages.scss`, `_content.scss`, `_utilities.scss`
- Delete: `_sass/_legacy.scss`
- Modify: `assets/css/styles.scss`

- [ ] **Step 1: Snapshot the compiled CSS before the split**

```bash
bundle exec jekyll build
cp _site/assets/css/styles.css /g/tmp/css-presplit.css
```

- [ ] **Step 2: Create each partial with a documented header**

Every partial opens with the same shape so a maintainer can tell at a glance what belongs there:

```scss
// =============================================================================
// COMPONENTS
// Reusable units that appear on two or more pages. A rule belongs here only
// if more than one page uses it; single-page styling lives in _pages.scss.
//
// Contains: .card, .wide-card, .log-row, .status-tag/.status-badge,
//           .rule-header, .side-module, .tech-chip, .btn-*, .breadcrumb
// =============================================================================

@use "tokens" as *;
```

- [ ] **Step 3: Move rules, converting literals to tokens as you go**

Move each block verbatim, then replace hard-coded values with the variables from `_tokens.scss` — `#64d5d2` → `$c-accent`, `6px` → `$radius-card`, and so on. Do not change any value while converting; a token must resolve to the identical literal.

- [ ] **Step 4: Move responsive rules into their components**

Each media block's contents move into the partial that owns the selector, wrapped in `@include respond-to(mobile)` / `(nav)` / `(wide)`. For example, in `_nav.scss`:

```scss
.nav-shell {
  min-height: 86px;
  // …

  @include respond-to(nav) {
    flex-wrap: wrap;
    padding: 0 20px;
  }

  @include respond-to(mobile) {
    min-height: 68px;
  }
}
```

When finished, `_legacy.scss` is empty and can be deleted, and **no partial should contain a bare `@media`** — every one goes through the mixin.

- [ ] **Step 5: Update the manifest**

```scss
@use "tokens" as *;
@use "base";
@use "layout";
@use "nav";
@use "components";
@use "pages";
@use "content";
@use "footer";
@use "utilities";
```

Order matters: tokens first, then broad-to-specific, so later rules win on equal specificity exactly as they did in the single file.

- [ ] **Step 6: Prove the compiled output is equivalent**

> **Corrected after execution.** This step originally reused Task 0's
> normalise-and-string-compare and expected `IDENTICAL`. That is **impossible
> given Step 4**, and the contradiction is an authoring error, not an
> implementation problem. Sass emits a nested `@media` at the position of the
> rule that contains it, so moving one trailing `max-width: 700px` block into
> ~65 per-component `respond-to(mobile)` blocks necessarily rearranges the
> output text. Measured on this repo: **4 media blocks become 77, and the file
> grows 26,583 -> 29,783 bytes (+12%)**, every byte of it extra `@media {`
> wrappers. Expect that growth; it is not a regression. Compare *cascade
> behaviour*, not text.

```bash
bundle exec jekyll build
```

Two checks, both required:

1. **Declaration multiset.** Parse both stylesheets into `(media, selector,
   property, value)` tuples and assert the multisets are equal. This proves
   nothing was lost, added, duplicated, or value-changed by tokenisation, and
   it discharges Step 3's "no value changed" requirement without auditing
   tokens by hand.

2. **Rendering diff.** Build both commits, then for each page load it once and
   swap the stylesheet in place - the HTML is identical between the two
   commits, so the DOM is guaranteed identical and only CSS varies. Diff
   `getComputedStyle` over **every** element in `<body>` plus `::before` and
   `::after`. Do not sample: run all built pages, all breakpoint edges
   (390/700/701/768/860/861/1024/1025/1280), and every computed property
   (`getComputedStyle(el).length`, 416 here), not a hand-picked subset.
   Expect `totalDiffs: 0`.

A static source-order check over "colliding" declarations is a useful third
signal but is **necessary, not sufficient** - it is easy to build one that
silently under-reports. Two traps, both hit in practice: comparing literal
property names misses shorthand-vs-longhand collisions (`margin` vs
`margin-bottom`), and an ancestor-subset heuristic for "can these match the
same element" wrongly rejects real collisions like `.detail-grid .x` vs
`.card .x`. If a pair is flagged, settle it against the real DOM
(`querySelectorAll(A).some(e => e.matches(B))`) rather than by heuristic.

**If the rendering diff is non-zero, stop** - a changed rule order altering the
cascade is a real regression even though no value changed.

- [ ] **Step 7: Assert no bare media queries survive**

```bash
grep -rn "@media" _sass/ | grep -v "_tokens.scss" || echo "all responsive rules go through respond-to()"
```
Expected: only `_tokens.scss` contains `@media`, inside the mixin.

- [ ] **Step 8: Verify the site and both breakpoint fixes still hold**

```bash
bundle exec jekyll build && bash script/verify-redesign.sh
python script/dead-css.py --count     # expect 0
```

Then re-render at 390px, 768px, 861px, and 1280px and confirm: no horizontal overflow, single-column layouts below 1024px, uniform type scale, and 44px touch targets.

- [ ] **Step 9: Commit**

```bash
git add -A
git commit -m "refactor(css): split into documented Sass partials

_legacy.scss becomes eight partials, each with one responsibility and a
header stating what belongs in it. The manifest documents where a new rule
goes, so the decision is written down rather than inferred.

Hard-coded literals become tokens. Responsive rules move inside the component
they modify, via respond-to() - the single mobile block at the end of a
3,000-line file is what let the 701-860px gap hide in the first place. No
partial contains a bare @media.

Pure reorganisation: compiled CSS is semantically identical to before the
split, which also proves the cascade order was preserved.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 4: Write the maintenance guide and wire the audit into CI

Documentation that is checkable, not aspirational.

**Files:**
- Create: `docs/css-architecture.md`
- Modify: `.github/workflows/lint.yml`
- Modify: `AGENTS.md`

- [ ] **Step 1: Write `docs/css-architecture.md`**

Cover, in this order: the token table and the rule that the palette is closed; the three breakpoints and why there are only three (with the 701–860px bug as the worked example); the partial map and the "where does a new rule go" decision list; the naming convention (`.page-*` for page shells, `.card`/`.log-row`/`.side-*` for components, `data-status` for state); and how to run `script/dead-css.py`.

Keep it under 150 lines. A guide nobody reads is worse than none.

- [ ] **Step 2: Add the dead-CSS check to CI**

In `.github/workflows/lint.yml`, after the Jekyll build step:

```yaml
      - name: Dead CSS check
        run: |
          count=$(python3 script/dead-css.py --count)
          echo "dead selectors: $count"
          if [ "$count" -gt 0 ]; then
            python3 script/dead-css.py
            echo "::error::$count unused CSS selectors. Remove them or add the class to a template."
            exit 1
          fi
```

This makes the cleanup permanent: the next dead selector fails the build rather than accumulating for a year.

- [ ] **Step 3: Note the architecture in AGENTS.md**

Add a short section pointing at `docs/css-architecture.md` and stating the three rules that matter: palette is closed, three breakpoints only, responsive rules live with their component.

- [ ] **Step 4: Verify CI locally**

```bash
bundle exec jekyll build
python script/dead-css.py --count     # expect 0, so the gate passes
```

Then confirm the gate actually fails when it should:
```bash
printf '\n.deliberately-unused-test-class { color: #64d5d2; }\n' >> _sass/_utilities.scss
bundle exec jekyll build && python script/dead-css.py --count    # expect 1
git checkout _sass/_utilities.scss
bundle exec jekyll build && python script/dead-css.py --count    # expect 0
```
A gate that cannot fail is not a gate.

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "docs: CSS architecture guide, dead-selector gate in CI

Documents the closed palette, the three breakpoints and the bug that motivated
collapsing six into three, the partial map, and where a new rule goes.

Wires script/dead-css.py into the Lint workflow so unused selectors fail the
build instead of accumulating. Verified the gate fails on a deliberately
unused class and passes once removed.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

## Final verification

- [ ] **Everything green**

```bash
bundle exec jekyll build && echo "build=$?"
bash script/verify-redesign.sh
python script/dead-css.py --count            # 0
bundle exec rubocop
npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml
find _site -name "*.html" | wc -l            # 153
```

- [ ] **No bare media queries, no dead selectors, no orphaned partials**

```bash
grep -rn "@media" _sass/ | grep -v _tokens.scss || echo ok
ls _sass/
grep -c "@use" assets/css/styles.scss
```

- [ ] **Four viewports render correctly**

390px, 768px, 861px, 1280px on `/`, `/projects/`, `/about/`, `/projects/ggswarm/`, `/csumb/cst363/`: no horizontal overflow, page grids single-column below 1024px, title 44px / lead 17px / body 16px at desktop, 44px touch targets at mobile.

- [ ] **Rendered output unchanged where it should be**

Tasks 2 and 3 are refactors; their HTML snapshots must match. Task 1 deliberately changes markup — that diff should touch only `tag.html`, `course.html`, `post.html`, `nav.html`, `head.html`, and `csumb.html`.

---

## Notes for the executor

**The HTML snapshot is the real guard.** Tasks 2 and 3 cannot change rendered markup. If `before.txt` and `after.txt` differ, stop and find out why rather than reconciling the snapshot.

**Semantic CSS comparison, not byte comparison.** Sass output differs from hand-written CSS in whitespace and comments. The normalising Python snippet in Task 0 Step 6 is the comparison to use throughout.

**`jekyll serve --detach` crashes on this machine.** Use `bash script/preview.sh <port>` — it serves the built `_site` statically. `pkill -f "http.server"` may not match; find the PID under `/proc/*/cmdline`.

**`git cat-file`, not `git show | grep`, for line endings.** Git Bash pipes translate CRLF and will lie to you. This cost an hour on 2026-09-16.

**Out of scope** — do not start these:
- `term:` / `skills:` front matter for the 12 `_csumb` files (content only the user has)
- `project-tag:` for the 18 posts lacking it (same)
- a small-format GG Swarm mark (separate design task)
- fast-forwarding `main`, which is 240 commits behind (separate decision)
