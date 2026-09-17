# Navbar & Home Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the "paste-in path" of the GGBytes navbar + home redesign — new navbar with the inset-underline active state, the 2a home layout, the four-value status vocabulary, the footer logo lockup, and the ≤700px mobile layer for all of it.

**Architecture:** Jekyll static site, no build step beyond Jekyll, no framework. All new CSS is appended to the single stylesheet `assets/css/styles.css`; Tasks 1–4 append sections lifted verbatim from the handoff's `redesign.css` and delete the old rules each section replaces, then Task 5 appends one mobile media block last so its overrides win on source order. Markup changes are Liquid template replacements. There is no JS change — the existing `toggleNavbar()` keeps working because the new navbar preserves `id="myNavbar"`.

**Tech Stack:** Jekyll 4.3, Liquid, vanilla CSS, jekyll-paginate, jekyll-redirect-from. Ruby 3.4.7, bundler. No test framework — verification is `bundle exec jekyll build` plus assertions grepped against the generated `_site/` output, plus Playwright screenshots at 390px for the mobile task.

**Spec:** `docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/` — the unpacked **v3** handoff (`README.md` is the spec; `code/` holds paste-ready source; `screenshots/` holds a rendered PNG per screen). Task 0 places it there.

**Handoff version note:** v3 supersedes v1 and v2. Its `code/` directory is byte-identical to v2, so all CSS line ranges below remain valid. What v3 adds is a **Mobile (≤700px) specification** and 13 reference screenshots. The mobile spec is *not* implemented in `redesign.css` — Task 5 writes it from prose. Do not assume pasting `redesign.css` delivers the mobile design.

---

## Global Constraints

Copied verbatim from the spec. Every task's requirements implicitly include this section.

**Palette — no new colors. Every value below already exists in the repo.**

| Token | Hex |
| --- | --- |
| Page background | `#141818` |
| Surface | `#1a1e1e` |
| Surface deep | `#0f1111` |
| Surface hover | `#1e2323` |
| Border | `#2e4c5b` |
| Border faint | `rgba(46,76,91,0.3)` |
| Rule | `#1f2a2a` |
| Accent (teal) | `#64d5d2` |
| Accent hover | `#7fe3e0` |
| Amber | `#ffb300` |
| Blue | `#5bc0de` |
| Ink | `#fafafa` |
| Body | `#b9c4c4` |
| Body dim | `#9aa6a6` |
| Muted | `#8a9696` |
| Muted alt | `#8ba3a3` |
| Muted low | `#7d8a8a` |

- **Never use a text color darker than `#7d8a8a`.** An earlier draft used `#5f6b6b`/`#4e5a5a` and failed the 4.5:1 contrast target on `#141818` and `#1a1e1e`.
- **Fonts:** Chakra Petch (display/headings/nav), Roboto Mono (meta/kickers/pills/dates), Roboto (body). Chakra Petch and Roboto Mono are BOTH new to the page — neither is currently loaded.
- **Status vocabulary is exactly four values:** `active`, `planned`, `shipped`, `dormant`. Anything else falls back to the grey neutral by design.
- **Borders are always 1px `#2e4c5b`.** No shadows anywhere except the navbar mark's `inset 0 0 16px rgba(100,213,210,0.25)` and the active-underline glow `0 0 10px rgba(100,213,210,0.8)`.
- **No transforms on hover.** The old `translateX(5px)` row slide and `translateY(-5px)` card lift are both dropped. Transitions are 0.25s ease on nav/button/card color and border, 0.2s on row hover tints.
- **Do not touch `assets/js/scripts.js`.** The mobile nav keeps `toggleNavbar()` and the `responsive` class.

**Mobile minimums (v3 spec, verified at 390px):**

- **Minimum touch target is 44px.** Applies to nav links, buttons, social links, and breadcrumb links.
- **Minimum type: 9.5px** for mono meta, **14px** for body. The nav caption floors at **10px** — if it will not fit, drop the caption rather than shrink it.
- Breakpoints: nav switches to the toggle at **860px**; layout collapses at **700px**. These are two different breakpoints by design — do not merge them.
- Several elements **change treatment** at ≤700px rather than merely reflowing (the featured hero's gradient direction, the log-row date gutter, the nav toggle icon). Reflow alone is not compliance.
- **Do not modify `Home Redesign.dc.html` or `support.js`.** They are design reference, never shipped.
- **`nav { position: sticky }` in `styles.css` stays.** The new bar is sticky too.
- **CSS is appended, never interleaved.** New sections go at the end of `styles.css`; old rules are deleted from their original position.

**Verification baseline (established in Task 0):** `bundle exec jekyll build` exits 0 in ~3.5s. Every task must leave the build green.

---

## File Structure

| File | Responsibility | Touched by |
| --- | --- | --- |
| `_includes/head.html` | font loading | Task 1 |
| `_projects/*.md` (7 files) | `status:` / `status_detail:` front matter | Task 1 |
| `assets/css/styles.css` | the single stylesheet — append new sections, delete replaced blocks | Tasks 1–4 |
| `_includes/nav.html` | navbar markup | Task 2 |
| `index.html` | home page markup | Task 3 |
| `_includes/footer.html` | footer lockup | Task 4 |
| `_config.yml` | add `flowchart.html` to existing `exclude:` | Task 4 |
| `_layouts/tags.html`, `_includes/header.html` | deleted | Task 4 |
| `script/verify-redesign.sh` | build-output assertions, extended per task | Tasks 1–4 |
| `script/preview.sh` | static server for Playwright screenshots | Task 0, used by Task 5 |

**CSS section map** — `code/assets/css/redesign.css` in the spec bundle is 589 lines, sectioned by comment banners. Each task appends only its own slice:

| Lines | Section | Task |
| --- | --- | --- |
| 1–6 | file header comment | Task 1 (append once, first) |
| 8–196 | `/* ---------- Navbar ---------- */` | Task 2 |
| 197–283 | `/* ---------- Home: intro band ---------- */` | Task 3 |
| 284–348 | `/* ---------- Home: featured project hero ---------- */` | Task 3 |
| 349–431 | `/* ---------- Status tag system ---------- */` | Task 1 |
| 432–566 | `/* ---------- Home: project log list ---------- */` | Task 3 |
| 567–589 | `/* ---------- Footer ---------- */` | Task 4 |
| — | **Mobile ≤700px — not in the file, written from spec prose** | Task 5 |

**What `redesign.css` actually ships for mobile.** Only three media queries, and they are partial:

| Line | Query | Covers | Gap vs v3 spec |
| --- | --- | --- | --- |
| 155 | `max-width: 860px` | nav toggle mechanics, 48px links, left-bar active indicator | complete — matches spec |
| 339 | `max-width: 700px` | `.intro-band` and `.feature-hero-body` padding only (32px/22px) | spec wants 20px/28px, plus type step-downs and full-width buttons |
| 554 | `max-width: 700px` | log row collapse to one column, gutter as flex row | spec wants 18px padding and 10.5px mono |

Everything else in the v3 Mobile section — nav sizing, the hamburger icon, the hero's bottom-up overlay, footer stacking, touch targets — has **no CSS at all**. Task 5 writes it.

**Deletion order matters.** Line numbers in `styles.css` shift as blocks are removed. All deletions in this plan are expressed against the *original* 1500-line file and MUST be applied in descending line order. Task 2 and Task 3 each delete from a different region, and no two tasks delete overlapping ranges.

---

### Task 0: Stage the spec and capture the build baseline

Setup task. Puts the spec where later tasks (and reviewers) can read it, and proves the build is green before any change.

**Files:**
- Create: `docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/` (unpacked from `GGBsite navbar improvementv3.zip`)
- Create: `.gitignore` entry for `_site/` if not already present

**Interfaces:**
- Produces: the spec path every later task's brief references; `BASELINE_SITE` snapshot used by Task 3's regression check.

- [ ] **Step 1: Confirm the working tree is clean and branch off `publish`**

```bash
cd /g/Code/ggbsite
git status --short          # expect: empty
git checkout publish && git pull
git checkout -b redesign/nav-and-layout
```

- [ ] **Step 2: Unpack the v3 handoff into the spec directory**

Use **v3**, not v1 or v2. v3 is the only one with the Mobile specification and the screenshots.

```bash
mkdir -p docs/superpowers/specs/2026-09-16-navbar-and-home-redesign
unzip -q -o "GGBsite navbar improvementv3.zip" \
  -d docs/superpowers/specs/2026-09-16-navbar-and-home-redesign
mv docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/design_handoff_nav_and_layout/* \
   docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/
rmdir docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/design_handoff_nav_and_layout
```

- [ ] **Step 3: Drop the two files that must never ship**

`support.js` is the design-canvas runtime and `Home Redesign.dc.html` is 171KB of mockup. Keep the mockup as reference, drop the runtime — it is dead weight in git and the mockup is only read, never opened in a browser from the repo.

```bash
rm -f docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/support.js
```

- [ ] **Step 4: Verify the spec landed**

Run:
```bash
ls docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/
```
Expected output contains: `README.md`, `code`, `assets`, `screenshots`, `Home Redesign.dc.html`

```bash
wc -l docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/code/assets/css/redesign.css
ls docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/screenshots/ | wc -l
grep -c "^## Mobile" docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/README.md
```
Expected: `589`, `13`, `1`. If the Mobile heading count is 0 you unpacked v1 or v2 — redo Step 2 with v3.

The `screenshots/` directory is 6.5MB. Commit it: it is the visual reference Task 5 verifies against, and the nine desktop shots are the reference for the out-of-scope pages when they are built later.

- [ ] **Step 5: Capture the build baseline**

Run:
```bash
bundle install
bundle exec jekyll build
echo "exit=$?"
```
Expected: `exit=0`, "done in ~3.5 seconds".

If `bundle install` reports missing gems, that is expected on a fresh checkout — it resolves them. Do not edit `Gemfile.lock` by hand.

- [ ] **Step 6: Snapshot the baseline home page for later comparison**

```bash
mkdir -p .superpowers/baseline
cp _site/index.html .superpowers/baseline/index.html
grep -c "hero-quote" .superpowers/baseline/index.html   # expect: 1
```

- [ ] **Step 6b: Create the preview server helper**

Task 5 verifies mobile layout visually, which needs the built site served over HTTP. **`bundle exec jekyll serve --detach` does not work on this machine** — it crashes on Windows. Serve the static output instead. Create `script/preview.sh`:

```bash
#!/usr/bin/env bash
# Serve the built _site for visual checks. Usage: ./script/preview.sh [port]
# Build first - this serves static output and does NOT rebuild on change.
set -eu
PORT="${1:-4111}"
cd "$(dirname "$0")/../_site"
echo "Serving _site on http://127.0.0.1:${PORT}/  (Ctrl-C to stop)"
python -m http.server "$PORT"
```

```bash
chmod +x script/preview.sh
```

- [ ] **Step 6c: Verify the preview server answers**

Run in one shell:
```bash
./script/preview.sh 4111 &
sleep 2
curl -s -o /dev/null -w "HTTP %{http_code}\n" http://127.0.0.1:4111/
```
Expected: `HTTP 200`.

Stop it when done: `pkill -f "http.server"`.

- [ ] **Step 7: Confirm `_site/` is git-ignored**

```bash
git check-ignore _site && echo IGNORED || echo "NOT IGNORED - add it"
```
If not ignored, add `_site/` and `.superpowers/` to `.gitignore`. Also add `.playwright-mcp/` — Playwright drops snapshot and console logs there during Task 5.

- [ ] **Step 8: Commit**

```bash
git add docs/superpowers script .gitignore
git commit -m "docs: stage navbar redesign spec (v3 handoff)

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 1: Foundation — fonts and the status vocabulary

The two changes everything else depends on. Fonts must load before any Chakra Petch / Roboto Mono rule renders correctly, and the status pills must key off the four-value vocabulary before the home hero (Task 3) renders one.

**Files:**
- Modify: `_includes/head.html:26-28` (the Google Fonts `<link>`)
- Modify: `_projects/drone.md:7`, `_projects/ggbytes.md:7`, `_projects/ggswarm.md:7`, `_projects/ggtrader.md:7`, `_projects/hexmaster.md:7`, `_projects/rover.md:8`, `_projects/smartmirror.md:8`
- Modify: `assets/css/styles.css` — append status section, delete lines 466–478 then 399–408
- Modify: `_layouts/project.html:167-206` — four `or`-chain additions only, no other change (see Step 6b: `shipped`→progress-4, `planned`→progress-0.5, `dormant`→progress-2.0, `shipped`→step-4 relabel)
- Verify only (no edit): `_includes/project-card.html:16`

**Interfaces:**
- Produces: `status:` front-matter values drawn from `{active, planned, shipped, dormant}`; a new optional `status_detail:` string field; CSS classes `.status-tag` (with child `.status-dot`) and `.status-badge`, both keyed on a `data-status` attribute.
- Consumed by: Task 3's featured hero, which emits `<span class="status-tag" data-status="...">`.

- [ ] **Step 1: Write the failing assertion**

There is no test framework here; the assertion is a grep against built output. Create `script/verify-redesign.sh`:

```bash
#!/usr/bin/env bash
# Verification assertions for the navbar/home redesign.
# Each check greps the BUILT site, not the source, so Liquid errors surface.
set -u
fail=0
check() { # check <name> <expected-count> <pattern> <file>
  local n; n=$(grep -c -- "$3" "$4" 2>/dev/null || echo 0)
  if [ "$n" -ge "$2" ]; then
    echo "  PASS  $1"
  else
    echo "  FAIL  $1 (found $n, wanted >=$2) in $4"
    fail=1
  fi
}
absent() { # absent <name> <pattern> <file>
  if grep -q -- "$2" "$3" 2>/dev/null; then
    echo "  FAIL  $1 (pattern still present) in $3"
    fail=1
  else
    echo "  PASS  $1"
  fi
}

echo "== Task 1: fonts + status =="
check "Chakra Petch loaded"  1 "Chakra+Petch"  _site/index.html
check "Roboto Mono loaded"   1 "Roboto+Mono"   _site/index.html

exit $fail
```

```bash
chmod +x script/verify-redesign.sh
```

- [ ] **Step 2: Run it to make sure it fails**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: both checks FAIL — neither font is loaded yet.

- [ ] **Step 3: Add both fonts to `_includes/head.html`**

Replace the existing font `<link>` (currently lines 26–28, the one whose `href` starts `https://fonts.googleapis.com/css2?family=Open+Sans`) with this **single** link. Do not add a second `<link>` — one request is cheaper and the existing `preconnect` hints already cover it.

```html
    <link
        href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Roboto+Flex:opsz,wght@8..144,100..1000&family=Roboto+Mono:wght@400;500&family=Roboto:ital,wght@0,100..900;1,100..900&display=swap"
        rel="stylesheet">
```

The existing families (Open Sans, Roboto Flex, Roboto) are preserved — `styles.css` still references all three.

- [ ] **Step 4: Run the build and the assertions**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: both font checks PASS.

- [ ] **Step 5: Commit the font change**

```bash
git add _includes/head.html script/verify-redesign.sh
git commit -m "feat(fonts): load Chakra Petch and Roboto Mono

Roboto Mono was referenced throughout styles.css but never loaded, so all
existing mono meta text was falling back to a system monospace. Chakra Petch
is new for the redesign's display type.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

- [ ] **Step 6: Migrate the seven project `status:` fields**

Apply this table exactly. `status:` takes the four-value state; the descriptive phrase moves to a new `status_detail:` field on the line immediately after. Where `status_detail` is `—`, add no `status_detail` line at all.

| File | Current `status:` | New `status:` | New `status_detail:` |
| --- | --- | --- | --- |
| `_projects/drone.md` | `"Conceptualization"` | `"planned"` | `"Conceptualization"` |
| `_projects/ggbytes.md` | `"On-going"` | `"active"` | — |
| `_projects/ggswarm.md` | `"Active - Hardware Deployment"` | `"active"` | `"Hardware deployment"` |
| `_projects/ggtrader.md` | `"Optimization of Core Code"` | `"active"` | `"Core optimization"` |
| `_projects/hexmaster.md` | `"Testing"` | `"active"` | `"Testing"` |
| `_projects/rover.md` | `"Conceptualization"` | `"planned"` | `"Conceptualization"` |
| `_projects/smartmirror.md` | `"Completed"` | `"shipped"` | — |

For example, `_projects/ggswarm.md` line 7 becomes:

```yaml
status: "active"
status_detail: "Hardware deployment"
```

and `_projects/ggbytes.md` line 7 becomes:

```yaml
status: "active"
```

Leave every other front-matter key untouched. Do not reorder keys.

- [ ] **Step 6b: Teach the project-detail timeline the new vocabulary**

*Added by the controller's pre-flight scan. Without this, Step 6 ships a visible regression.*

`_layouts/project.html:167` drives a programmatic 4-step timeline off exact `status` string matches. `shipped`, `planned`, and `dormant` match none of its conditionals (`active` already does). Two projects use this path — the other five define explicit `timeline:` front matter and are unaffected:

| Project | Before | After Step 6, unfixed | Effect |
| --- | --- | --- | --- |
| `smartmirror` | `Completed` → 4 steps lit | `shipped` → **0 steps lit** | regression |
| `ggswarm` | `Active - Hardware…` → 0 lit | `active` → 2 lit | improvement |

Make three additions inside the existing `or` chains. Change nothing else in this file — no markup, no new branches.

Add `shipped` to the progress-4 branch:

```liquid
                    {% if status == "completed" or status == "finished" or status == "live" or status == "production" or
                    status == "done" or status == "archived" or status == "maintenance" or status == "shipped" %}
                    {% assign progress = 4 %}
```

Add `planned` to the progress-0.5 branch:

```liquid
                    {% elsif status == "research" or status == "discovery" or status == "concept" or status ==
                    "ideation" or status == "planning" or status == "planned" %}
                    {% assign progress = 0.5 %}
```

Add `dormant` to the progress-2.0 branch:

```liquid
                    {% elsif status == "on hold" or status == "paused" or status == "dormant" %}
                    {% assign progress = 2.0 %} <!-- Middle state for paused projects -->
```

Also add `shipped` to the step-4 relabel chain further down, so a shipped project's final step reads "Completed" rather than the default "Test":

```liquid
                    {% elsif status == "completed" or status == "finished" or status == "done" or status == "shipped" %}
                    {% assign step4_name = "Completed" %}
                    {% assign step4_desc = "Project Finalized" %}
```

- [ ] **Step 7: Verify the migration**

Run:
```bash
grep -h "^status:" _projects/*.md | sort | uniq -c
```
Expected exactly:
```
      4 status: "active"
      2 status: "planned"
      1 status: "shipped"
```

Run:
```bash
grep -c "^status_detail:" _projects/*.md
```
Expected: 5 files with a `status_detail` line (drone, ggswarm, ggtrader, hexmaster, rover), 2 without (ggbytes, smartmirror).

- [ ] **Step 7b: Verify the timeline did not regress**

Run:
```bash
bundle exec jekyll build >/dev/null 2>&1
for f in _site/projects/*/index.html; do
  printf "%s: %s\n" "$(basename "$(dirname "$f")")" \
    "$(grep -o 'timeline-title highlight' "$f" | wc -l)"
done
```

Expected exactly:
```
drone: 0
ggbytes: 7
ggswarm: 2
ggtrader: 3
hexmaster: 3
rover: 0
smartmirror: 4
```

`smartmirror: 4` is the regression guard — if it reads `0`, Step 6b did not land. `ggswarm: 2` is the intended improvement (was `0`; the vocabulary now actually matches). Every other value must be unchanged from baseline.

- [ ] **Step 8: Append the status CSS section**

Append lines **349–431** of `docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/code/assets/css/redesign.css` to the end of `assets/css/styles.css`, preceded by the file-header comment (lines 1–6 of the same file, appended once here since this is the first CSS task).

```bash
SPEC=docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/code/assets/css/redesign.css
{ echo ""; sed -n '1,6p' "$SPEC"; echo ""; sed -n '349,431p' "$SPEC"; } >> assets/css/styles.css
```

Verify the appended text ends with the `.status-badge[data-status="dormant"]` rule and does NOT include the `/* ---------- Home: project log list ---------- */` banner:

```bash
tail -8 assets/css/styles.css
```

- [ ] **Step 9: Delete the two old `.status-badge` blocks — descending order**

These are the original line numbers in the 1500-line file. Delete the **higher** range first.

```bash
sed -i '466,478d' assets/css/styles.css   # second .status-badge (bordered teal variant)
sed -i '399,408d' assets/css/styles.css   # first .status-badge (filled #2e4c5b variant)
```

- [ ] **Step 10: Verify exactly one `.status-badge` base rule survives**

Run:
```bash
grep -c "^\.status-badge {" assets/css/styles.css
```
Expected: `1`

Run:
```bash
awk '{o+=gsub(/\{/,"{"); c+=gsub(/\}/,"}")} END{print "open="o" close="c; exit (o==c)?0:1}' assets/css/styles.css
```
Expected: `open=N close=N` with matching counts, exit 0. Unbalanced braces mean the deletion clipped a neighbouring rule — restore from git and redo.

- [ ] **Step 11: Confirm `project-card.html` needs no change**

Read `_includes/project-card.html:16`. It already emits:

```liquid
<span class="status-badge" data-status="{{ project.status | downcase }}">{{ project.status }}</span>
```

The new `.status-badge` CSS uppercases via `text-transform` and needs no `.status-dot` child, so this markup works unchanged. **Make no edit.** If you believe an edit is required, say so in your report rather than making it.

- [ ] **Step 12: Build and verify the pills render**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: font checks PASS, build exits 0.

Run:
```bash
grep -o 'data-status="[a-z]*"' _site/index.html | sort -u
```
Expected: only values from `{active, planned, shipped, dormant}` — no multi-word strings like `data-status="active - hardware deployment"`.

- [ ] **Step 13: Commit**

```bash
git add _projects assets/css/styles.css
git commit -m "feat(status): migrate to four-value status vocabulary

status: now takes exactly one of active/planned/shipped/dormant. The prose
that was in status: moves to a new status_detail: field so the descriptive
phrase survives for the detail-page meta row.

Replaces both old .status-badge rules with one data-status-keyed set shared
by .status-tag and .status-badge.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 2: Navbar

The original brief. Replaces the filled-block active state with an inset teal underline plus bracket ticks.

**Files:**
- Replace: `_includes/nav.html` (entire file) from `docs/superpowers/specs/.../code/_includes/nav.html`
- Modify: `assets/css/styles.css` — append navbar section, delete original lines 97–194

**Interfaces:**
- Consumes: Chakra Petch + Roboto Mono from Task 1.
- Produces: `.nav-shell` (carrying `id="myNavbar"`), `.nav-brand`, `.nav-mark`, `.nav-wordmark`, `.nav-name`, `.nav-caption`, `.nav-menu`, `.nav-item`, `.nav-icon`. The mobile breakpoint moves from 700px to 860px.

- [ ] **Step 1: Add the navbar assertions to `script/verify-redesign.sh`**

Insert before the final `exit $fail`:

```bash
echo "== Task 2: navbar =="
check  "nav-shell present"       1 'class="nav-shell"'          _site/index.html
check  "toggle id preserved"     1 'id="myNavbar"'              _site/index.html
check  "nav mark image"          1 'branding/logo/ggbytes-transparent-g.png' _site/index.html
check  "Coursework label"        1 '>Coursework<'               _site/index.html
check  "home link active"        1 'nav-item active'            _site/index.html
check  "caption tail splittable" 1 'class="nav-caption-rest"'   _site/index.html
check  "hamburger bars"          3 'class="nav-icon-bar"'       _site/index.html
absent "old navbar markup gone"    'class="navbar"'             _site/index.html
absent "old nav-links gone"        'class="nav-links"'          _site/index.html
absent "fa-bars glyph gone"        'fa fa-bars'                 _site/index.html
```

- [ ] **Step 2: Run it to make sure the new checks fail**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: Task 1 checks PASS; all ten Task 2 checks FAIL.

- [ ] **Step 3: Replace the navbar include, then apply two mobile-required markup edits**

```bash
cp docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/code/_includes/nav.html \
   _includes/nav.html
```

Then read the copied file and confirm three things, because these are the spots where v1 of the handoff was wrong:

1. The `<img src>` is `/assets/branding/logo/ggbytes-transparent-g.png` — this path **does** exist in the repo (`assets/branding/logo/` holds the full mark set). Do not "correct" it to `assets/imgs/ggbytes/`.
2. The third nav item reads `Coursework`, not `Academic`.
3. The wrapper is `<div class="nav-shell" id="myNavbar">` — the id must survive for `toggleNavbar()`.

**The shipped `nav.html` cannot express the v3 mobile design.** Two edits are required. They are additive and change nothing at desktop width.

**Edit A — split the caption.** The mobile spec shortens `ENGINEERING LOG & PORTFOLIO` to `ENGINEERING LOG` (confirmed in screenshot `11-mobile-menu.png`). CSS cannot truncate at a word boundary, so the tail needs its own element. Replace:

```html
            <span class="nav-caption">ENGINEERING LOG &amp; PORTFOLIO</span>
```

with:

```html
            <span class="nav-caption">ENGINEERING LOG<span class="nav-caption-rest"> &amp; PORTFOLIO</span></span>
```

**Edit B — replace the Font Awesome glyph with drawn bars.** The spec calls for "a 22×2px three-bar icon"; `<i class="fa fa-bars">` is a font glyph whose bars cannot be sized. Screenshot `11-mobile-menu.png` shows three distinct rules. Replace:

```html
    <button class="nav-icon" type="button" onclick="toggleNavbar()" aria-label="Menu">
        <i class="fa fa-bars"></i>
    </button>
```

with:

```html
    <button class="nav-icon" type="button" onclick="toggleNavbar()" aria-label="Menu">
        <span class="nav-icon-bar"></span>
        <span class="nav-icon-bar"></span>
        <span class="nav-icon-bar"></span>
    </button>
```

Do **not** add `aria-expanded` — `toggleNavbar()` is off-limits and would never update it, so a hardcoded value would be a lie to screen readers. `aria-label="Menu"` stays.

Font Awesome is still loaded and still used elsewhere (social icons, in-content icons) — do not remove it from `head.html`.

- [ ] **Step 4: Append the navbar CSS section plus the hamburger bar rules**

```bash
SPEC=docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/code/assets/css/redesign.css
{ echo ""; sed -n '8,196p' "$SPEC"; } >> assets/css/styles.css
```

Then append these rules, which have no counterpart in `redesign.css` because they support Edit B:

```css

/* hamburger bars — replaces the Font Awesome glyph (see nav.html) */
.nav-icon-bar {
    display: block;
    width: 22px;
    height: 2px;
    border-radius: 1px;
    background: #8ba3a3;
    transition: background 0.25s ease;
}

.nav-icon-bar + .nav-icon-bar {
    margin-top: 5px;
}

.nav-shell.responsive .nav-icon-bar {
    background: #64d5d2;
}
```

**Touch-target arithmetic, and a deliberate deviation from the spec.** The v3 spec says the toggle gets "10px vertical padding for reach", but three 2px bars with two 5px gaps are 16px tall, so 10px padding yields a 36px target — which violates the same spec's "Minimum touch target is 44px". The pasted `.nav-icon` rule already carries `padding: 14px 16px`, giving `16 + 28 = 44px` exactly. **Keep 14px.** Do not change it to 10px.

- [ ] **Step 5: Delete the old navbar CSS**

Original lines 97–194 — the whole run from `.navbar {` through `.navbar .logo img`'s closing brace and its trailing blank line. This includes the old `@media (max-width: 700px)` navbar block at 151–179.

**`nav { position: sticky }` at lines 91–95 must survive.** It is above the deletion range; do not widen the range to include it.

Because Task 1 already deleted lines below 466, these original line numbers have NOT shifted for this range (all Task 1 deletions were at higher line numbers). Verify before deleting:

```bash
sed -n '97p;194p' assets/css/styles.css
```
Expected: line 97 is `.navbar {`, line 194 is blank. If either differs, recompute the range by locating `.navbar {` and the closing brace of `.navbar .logo img` — do not delete blind.

```bash
sed -i '97,194d' assets/css/styles.css
```

- [ ] **Step 6: Verify the sticky rule survived and braces balance**

Run:
```bash
grep -A4 "^nav {" assets/css/styles.css
```
Expected: the `position: sticky; top: 0; z-index: 1000;` block, intact.

Run:
```bash
grep -c "^\.navbar" assets/css/styles.css
```
Expected: `0`

Run:
```bash
awk '{o+=gsub(/\{/,"{"); c+=gsub(/\}/,"}")} END{print "open="o" close="c; exit (o==c)?0:1}' assets/css/styles.css
```
Expected: matching counts, exit 0.

- [ ] **Step 7: Build and run all assertions**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: every check PASSES.

- [ ] **Step 8: Verify the active state is route-derived on a detail page**

The spec requires section highlighting to survive onto detail pages — `page.url contains '/projects/'`, not an exact match.

Run:
```bash
grep -o 'nav-item active[^>]*>[A-Za-z]*' _site/projects/ggswarm/index.html
```
Expected: `nav-item active">Projects` — the Projects link is active on a project detail page, which the old exact-match include did not do.

- [ ] **Step 9: Commit**

```bash
git add _includes/nav.html assets/css/styles.css script/verify-redesign.sh
git commit -m "feat(nav): redesigned navbar with inset underline active state

Replaces the filled-block active state with a 2px teal underline inset 14px
each side, glow, and bracket ticks. Adds the G mark + two-line wordmark.
Renames Academic Projects to Coursework. Mobile breakpoint moves 700->860px.

Swaps the Font Awesome bars glyph for three drawn spans so the mobile spec's
22x2px icon is expressible, and splits the wordmark caption so the
'& PORTFOLIO' tail can be hidden at <=700px. Both are inert at desktop width.

toggleNavbar() and the responsive class are untouched; id=myNavbar survives
on the new .nav-shell wrapper.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 3: Home page — the 2a layout

Drops the quote hero card and the unbalanced two-column block. New order: intro band → featured project hero → project logs → pagination.

**Files:**
- Replace: `index.html` (entire file) from `docs/superpowers/specs/.../code/index.html`
- Modify: `assets/css/styles.css` — append three sections, delete original lines 560–592

**Interfaces:**
- Consumes: `.status-tag` / `.status-dot` and the migrated `status:` values from Task 1; Chakra Petch + Roboto Mono from Task 1.
- Produces: `.intro-band`, `.intro-inner`, `.intro-kicker`, `.intro-title`, `.intro-body`, `.intro-actions`, `.btn-primary`, `.btn-ghost`, `.feature-hero*`, `.rule-header`, `.rule-title`, `.rule-line`, `.rule-link`, `.log-list`, `.log-row`, `.log-gutter`, `.log-date`, `.log-tag`, `.log-title`, `.log-excerpt`, `.log-more`, `.log-pagination`, `.log-page-number`.

- [ ] **Step 1: Add the home assertions to `script/verify-redesign.sh`**

Insert before the final `exit $fail`:

```bash
echo "== Task 3: home layout =="
check  "intro band"          1 'class="intro-band"'      _site/index.html
check  "intro kicker"        1 'ECS ANALYSIS ENGINEER'   _site/index.html
check  "featured hero"       1 'class="feature-hero"'    _site/index.html
check  "status tag on hero"  1 'class="status-tag"'      _site/index.html
check  "rule header"         1 'class="rule-header"'     _site/index.html
check  "log rows"            3 'class="log-row"'         _site/index.html
check  "primary button"      1 'class="btn-primary"'     _site/index.html
absent "quote card gone"       'hero-quote'              _site/index.html
absent "quote icon gone"       'fa-quote-left'           _site/index.html
absent "old grid block gone"   'grid-container grid-start' _site/index.html
```

- [ ] **Step 2: Run it to make sure the new checks fail**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: Tasks 1–2 PASS; all ten Task 3 checks FAIL.

- [ ] **Step 3: Replace `index.html`**

```bash
cp docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/code/index.html index.html
```

Note: the current `index.html` ends with a stray unbalanced `</div>`. The replacement fixes it — this is intended, not a regression.

- [ ] **Step 4: Append the three home CSS sections**

Append in source order so the section banners read correctly:

```bash
SPEC=docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/code/assets/css/redesign.css
{ echo ""; sed -n '197,348p' "$SPEC"; echo ""; sed -n '432,566p' "$SPEC"; } >> assets/css/styles.css
```

Lines 197–348 cover the intro band and featured hero; 432–566 cover the project log list. Lines 349–431 (status) were already appended in Task 1 — do **not** append them again.

- [ ] **Step 5: Verify the status section was not duplicated**

Run:
```bash
grep -c "^\.status-tag {" assets/css/styles.css
```
Expected: `1`

- [ ] **Step 6: Delete the old hero card CSS**

Original lines 560–592: the `/* Hero Card */` banner through `.hero-quote`'s closing brace and its trailing blank line.

These line numbers HAVE shifted — Task 1 deleted 23 lines below this point (466–478 = 13 lines, 399–408 = 10 lines) and Task 2 deleted 98 lines (97–194). Total upward shift: 121 lines. So verify before deleting rather than trusting arithmetic:

```bash
grep -n "^/\* Hero Card \*/" assets/css/styles.css
grep -n "^\.hero-quote {" assets/css/styles.css
```

Delete from the `/* Hero Card */` line through the blank line after `.hero-quote`'s closing brace. The block is 33 lines: banner, `.hero-card` (13 lines), blank, `.hero-card p` (7), blank, `.hero-quote` (9), blank.

```bash
START=$(grep -n "^/\* Hero Card \*/" assets/css/styles.css | cut -d: -f1)
sed -i "${START},$((START+32))d" assets/css/styles.css
```

- [ ] **Step 7: Verify the deletion landed correctly**

Run:
```bash
grep -c "hero-card\|hero-quote" assets/css/styles.css
```
Expected: `0`

Run:
```bash
grep -n "Updates Feed (Home)" assets/css/styles.css
```
Expected: the `/* Updates Feed (Home) */` banner still exists and its `.update-feed` rule is intact — the deletion must not have eaten into it. `.update-feed` is still used by `_includes/post.html` on other pages.

Run:
```bash
awk '{o+=gsub(/\{/,"{"); c+=gsub(/\}/,"}")} END{print "open="o" close="c; exit (o==c)?0:1}' assets/css/styles.css
```
Expected: matching counts, exit 0.

- [ ] **Step 8: Build and run all assertions**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: every check PASSES.

- [ ] **Step 9: Verify the featured hero resolved real project data**

The hero reads `image`/`status`/`description`/`title` from the `ggswarm` project front matter.

Run:
```bash
grep -o 'data-status="[a-z]*"' _site/index.html | head -1
```
Expected: `data-status="active"` — proving Task 1's migration feeds Task 3's markup.

Run:
```bash
grep -o 'feature-hero-img" src="[^"]*"' _site/index.html
```
Expected: the ggswarm image path, not an empty `src`.

Run:
```bash
grep -o 'All [0-9]* Projects' _site/index.html
```
Expected: `All 7 Projects`.

- [ ] **Step 10: Verify pagination still works**

Run:
```bash
ls _site/page2/index.html && grep -c "log-row" _site/page2/index.html
```
Expected: the file exists and contains log rows. `jekyll-paginate` requires the paginator loop to live in the root `index.html`, which the replacement preserves.

- [ ] **Step 11: Commit**

```bash
git add index.html assets/css/styles.css script/verify-redesign.sh
git commit -m "feat(home): 2a layout - intro band, featured hero, log rows

Drops the .hero-card quote block and the unbalanced two-column
grid-container. New order: intro band, featured project hero, paginated
project log rows.

Also fixes the stray unbalanced </div> at the end of the old index.html.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 4: Footer lockup and dead-file removal

Two independent cleanups, committed separately. The navbar now carries a wordmark, so the full logo lockup moves to the footer.

**Files:**
- Modify: `_includes/footer.html:10` (the copyright `<p>`)
- Modify: `assets/css/styles.css` — append footer section
- Modify: `_config.yml:13-15` (the existing `exclude:` list)
- Delete: `_layouts/tags.html`, `_includes/header.html`

**Interfaces:**
- Consumes: Roboto Mono from Task 1.
- Produces: `.footer-mark`.

- [ ] **Step 1: Add the footer assertions to `script/verify-redesign.sh`**

Insert before the final `exit $fail`:

```bash
echo "== Task 4: footer + cleanup =="
check  "footer lockup"      1 'class="footer-mark"'                  _site/index.html
check  "footer logo img"    1 'ggbytes-transparent-cropped.png'      _site/index.html
check  "coordinates line"   1 '33.77'                                _site/index.html
absent "old copyright gone"   'All rights reserved'                  _site/index.html
```

- [ ] **Step 2: Run it to make sure the new checks fail**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: Tasks 1–3 PASS; all four Task 4 checks FAIL.

- [ ] **Step 3: Replace the copyright line in `_includes/footer.html`**

Replace this line:

```html
    <p>&#169; {{ 'now' | date: "%Y" }} Gary Gigabytes. All rights reserved.</p>
```

with:

```html
    <div class="footer-mark">
        <img src="/assets/imgs/ggbytes/ggbytes-transparent-cropped.png" alt="Gary Gigabytes" />
        <p>&#169; {{ 'now' | date: "%Y" }} &middot; BUILT IN LONG BEACH, CA &middot; 33.77&deg;N 118.19&deg;W</p>
    </div>
```

"GARY GIGABYTES" is intentionally dropped from the text — the logo says it. Leave `.social-icons` and `.ai-disclaimer` untouched.

- [ ] **Step 4: Append the footer CSS section**

```bash
SPEC=docs/superpowers/specs/2026-09-16-navbar-and-home-redesign/code/assets/css/redesign.css
{ echo ""; sed -n '567,589p' "$SPEC"; } >> assets/css/styles.css
```

- [ ] **Step 4b: Fix the social-link touch targets**

The v3 spec flags this explicitly: the social links "as bare inline anchors measure 13px tall and fail touch sizing". The existing rule at `.social-icons a` sets `padding-bottom: 10px` on an inline anchor, which does not create height. Append:

```css

/* social links need a real touch target — bare inline anchors measure ~13px */
.social-icons a {
    display: inline-flex;
    align-items: center;
    min-height: 44px;
    padding: 0 14px;
}
```

This intentionally overrides the earlier `padding-bottom: 10px` by cascade order (later rule, equal specificity). The `border-bottom` from the original rule survives and now sits flush under a 44px-tall target. Do not delete the original `.social-icons a` block — `color`, `font-size`, and `margin` still come from it.

Note this applies at **all** widths, not just mobile. A 13px touch target is a defect on tablets too.

- [ ] **Step 5: Build and verify the footer**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: every check PASSES.

- [ ] **Step 6: Commit the footer**

```bash
git add _includes/footer.html assets/css/styles.css script/verify-redesign.sh
git commit -m "feat(footer): full logo lockup with coordinates

The navbar now carries the G mark plus a type wordmark, so the full lockup
moves to the footer - one appearance per page.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

- [ ] **Step 7: Confirm the two orphaned templates are truly unreferenced**

Before deleting, prove nothing uses them.

Run:
```bash
grep -rn "layout: tags" --include=*.html --include=*.md . --exclude-dir=_site --exclude-dir=.git
grep -rn "include header.html" --include=*.html --include=*.md . --exclude-dir=_site --exclude-dir=.git
```
Expected: no output for either. If either returns a hit, STOP and report it rather than deleting.

**Keep `_layouts/tag.html`** (singular) — individual tag pages are linked from every post. Only `tags.html` (plural) goes.

- [ ] **Step 8: Delete the orphans and exclude the flowchart**

```bash
git rm _layouts/tags.html _includes/header.html
```

In `_config.yml`, add `flowchart.html` to the **existing** `exclude:` list (currently `template/`, `test.html`, and `docs/`):

```yaml
exclude:
  - template/
  - test.html
  # Internal planning and design-handoff docs. Tracked in git, not published.
  - docs/
  - flowchart.html
```

Leave the explanatory comment above the block in place.

- [ ] **Step 9: Verify the build drops the flowchart and nothing else broke**

Run:
```bash
bundle exec jekyll build && ./script/verify-redesign.sh
```
Expected: every check PASSES, build exits 0.

Run:
```bash
ls _site/flowchart.html 2>&1
```
Expected: "No such file or directory".

Run:
```bash
ls _site/tags/ _site/projects/ _site/csumb/ >/dev/null && echo "sections intact"
```
Expected: `sections intact` — deleting `_layouts/tags.html` must not have removed individual tag pages, which use `tag.html`.

- [ ] **Step 10: Commit the cleanup**

```bash
git add _config.yml _layouts _includes
git commit -m "chore: drop orphaned templates, exclude flowchart.html

_layouts/tags.html styled a .tag-list class that does not exist in the
stylesheet; the Archives tag strip is the better entry point.
_includes/header.html was orphaned and pointed at a missing logo.
flowchart.html is a one-off roadmap, entirely off-system, and overlaps the
GG Swarm timeline.

_layouts/tag.html (singular) is kept - individual tag pages link from posts.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

### Task 5: Mobile (≤700px)

The v3 spec's Mobile section, written from prose — **none of this exists in `redesign.css`**. This is the one task that is not transcription, and the one task whose output cannot be verified by grep. It is verified visually against the reference screenshots.

Dispatch this task on a **standard model, not the cheapest tier** — it is design judgment against a rendered target, not transcription.

**Files:**
- Modify: `assets/css/styles.css` — append one `@media screen and (max-width: 700px)` block at the very end

**Interfaces:**
- Consumes: every class produced by Tasks 1–4. This block only overrides; it introduces no new class except `.nav-caption-rest`, which Task 2's markup already emits.

**Reference screenshots** (in the spec dir): `screenshots/10-mobile-home.png` (artboard `6a`) and `screenshots/11-mobile-menu.png` (artboard `6b`). The other two mobile shots (`12-mobile-coursework.png`, `13-mobile-project-detail.png`) are for out-of-scope pages — ignore them.

**Cascade requirement:** this block must be the **last** thing in `styles.css`. It overrides rules appended by Tasks 1–4, and equal-specificity overrides depend on source order. Appending it anywhere earlier will silently fail.

- [ ] **Step 1: Capture the "before" screenshot**

Build, serve, and screenshot at 390×844 so the review has a before/after pair.

```bash
bundle exec jekyll build
./script/preview.sh 4111 &
sleep 2
```

Then, using Playwright: resize the browser to 390×844, navigate to `http://127.0.0.1:4111/`, and screenshot to `.superpowers/mobile-before.png`.

Expect the desktop layout crammed into 390px: oversized wordmark, nav overflowing, side-gradient hero unreadable. Note in your report whether a **horizontal scrollbar** is present — the baseline has one, and its absence afterwards is a pass condition.

- [ ] **Step 2: Append the mobile block**

Append verbatim to the end of `assets/css/styles.css`. Every value traces to the v3 spec's Mobile section or to a token in Global Constraints.

```css

/* ---------- Mobile (≤700px) ---------- */
@media screen and (max-width: 700px) {

    /* --- Navbar --- */
    .nav-shell {
        min-height: 68px;
        padding: 0 20px;
    }

    .nav-brand {
        gap: 12px;
    }

    .nav-mark {
        width: 42px;
        height: 42px;
        border-radius: 10px;
    }

    .nav-mark img {
        height: 21px;
    }

    .nav-name {
        font-size: 16px;
        letter-spacing: 2.5px;
    }

    .nav-caption {
        font-size: 10px;
        letter-spacing: 1.5px;
    }

    .nav-caption-rest {
        display: none;
    }

    /* --- Page rhythm --- */
    #main {
        width: auto;
        padding: 28px 20px;
        margin: 0 0 24px;
    }

    /* --- Intro band --- */
    .intro-band {
        padding: 28px 20px;
        margin-bottom: 24px;
    }

    .intro-title {
        font-size: 30px;
    }

    .intro-body {
        font-size: 15px;
        line-height: 1.75;
    }

    /* --- Buttons stack full width --- */
    .intro-actions {
        flex-direction: column;
        gap: 10px;
    }

    .intro-actions .btn-primary,
    .intro-actions .btn-ghost {
        display: block;
        width: 100%;
        padding: 14px 22px;
        text-align: center;
    }

    /* --- Featured hero: side gradient does not work at 390px --- */
    .feature-hero {
        display: block;
        min-height: 0;
        margin-bottom: 24px;
    }

    .feature-hero-img {
        position: static;
        width: 100%;
        height: auto;
        aspect-ratio: 4 / 3;
    }

    .feature-hero::after {
        background: linear-gradient(to top,
                rgba(20, 24, 24, 0.96) 22%,
                rgba(20, 24, 24, 0.3) 75%);
    }

    .feature-hero-body {
        margin-top: -96px;
        padding: 0 20px 28px;
        max-width: none;
    }

    .feature-hero-title {
        font-size: 32px;
    }

    .feature-hero-desc {
        font-size: 15px;
        line-height: 1.75;
    }

    .feature-hero .status-tag {
        background: rgba(15, 17, 17, 0.7);
    }

    /* --- Section rule headers --- */
    .rule-title {
        font-size: 18px;
    }

    /* --- Log rows: date gutter is dropped, rows stack --- */
    .log-row {
        padding: 18px 0;
    }

    .log-gutter {
        font-size: 10.5px;
    }

    .log-title {
        font-size: 19px;
    }

    /* --- Footer stacks and centers --- */
    footer {
        padding: 24px 20px;
    }

    .footer-mark {
        flex-direction: column;
        gap: 10px;
    }

    .footer-mark img {
        height: 24px;
    }

    .footer-mark p {
        font-size: 9.5px;
        line-height: 1.7;
        text-align: center;
    }
}
```

- [ ] **Step 3: Confirm the block is last and braces balance**

Run:
```bash
tail -3 assets/css/styles.css
```
Expected: the closing `}` of the media query, nothing after it.

Run:
```bash
awk '{o+=gsub(/\{/,"{"); c+=gsub(/\}/,"}")} END{print "open="o" close="c; exit (o==c)?0:1}' assets/css/styles.css
```
Expected: matching counts, exit 0.

- [ ] **Step 4: Rebuild and capture the "after" screenshot**

```bash
bundle exec jekyll build
```

Playwright at 390×844 against `http://127.0.0.1:4111/`, screenshot to `.superpowers/mobile-after.png`.

- [ ] **Step 5: Check it against the reference, point by point**

Open `screenshots/10-mobile-home.png` and your after-shot side by side. Every one of these must hold — report any that do not rather than quietly adjusting:

1. **No horizontal scrollbar.** Nothing exceeds 390px.
2. Nav bar is ~68px tall; the mark is a small rounded square; the wordmark fits on one line.
3. Caption reads exactly `ENGINEERING LOG` — no `& PORTFOLIO`.
4. The toggle is three distinct horizontal rules, not a glyph.
5. Intro band: kicker wraps to two lines, h1 is two lines, both buttons are **full-width and stacked**.
6. Featured hero: image is a 4:3 block at the **top**, text sits below it pulled up over the image's lower edge, and the `ACTIVE` pill has a dark backing.
7. Log rows: date and `#tag` share one line above the title; no left date column.
8. Footer: logo centered, meta text centered below it, social links below that.

- [ ] **Step 6: Verify the menu-open state**

Playwright: click the toggle, screenshot to `.superpowers/mobile-menu.png`, compare against `screenshots/11-mobile-menu.png`.

Must hold:
1. Four links stack, each at least 48px tall, divided by hairlines.
2. The active link's indicator is a **2px vertical bar on the left**, not an underline, and it keeps its glow.
3. The toggle bars turn teal (`#64d5d2`) while open.

- [ ] **Step 7: Verify touch targets measure up**

With the menu open, use Playwright to evaluate:

```js
[...document.querySelectorAll('.nav-item, .social-icons a, .nav-icon')]
  .map(e => `${e.className||e.tagName}: ${Math.round(e.getBoundingClientRect().height)}px`)
```

Expected: every `.nav-item` ≥ 48px, `.nav-icon` ≥ 44px, every `.social-icons a` ≥ 44px. Any value below its floor is a spec failure — report it.

- [ ] **Step 8: Confirm desktop did not regress**

Playwright: resize to 1280×900, navigate, screenshot to `.superpowers/desktop-after.png`, and compare against `screenshots/01-home.png`. The media query must not leak — the hero should still use the **side** gradient with the image filling the full block, and the buttons should sit side by side.

- [ ] **Step 9: Stop the preview server**

```bash
pkill -f "http.server"
```

- [ ] **Step 10: Commit**

```bash
git add assets/css/styles.css
git commit -m "feat(mobile): implement the <=700px layout

The v3 handoff specifies mobile in prose but ships no CSS for it - the
paste-ready redesign.css covers only nav toggle mechanics, two padding
overrides, and the log-row collapse. This writes the rest.

Elements that change treatment rather than reflowing: the featured hero
swaps its side gradient for a 4:3 image with a bottom-up overlay and the
body pulled up over it; the log-row date gutter is dropped for an inline
date+tag line; the footer stacks and centers.

Verified at 390x844 against screenshots/10-mobile-home.png and
11-mobile-menu.png, and at 1280px against 01-home.png for non-regression.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01FPqrVEyTB6njC6LKjZofzH"
```

---

## Final verification

After all tasks, before `finishing-a-development-branch`:

- [ ] **Full assertion suite green**

```bash
bundle exec jekyll build && ./script/verify-redesign.sh; echo "exit=$?"
```
Expected: every check PASS, `exit=0`.

- [ ] **No dead selectors left behind**

```bash
grep -c "\.navbar\|hero-card\|hero-quote" assets/css/styles.css
```
Expected: `0`

- [ ] **Stylesheet braces balance**

```bash
awk '{o+=gsub(/\{/,"{"); c+=gsub(/\}/,"}")} END{print "open="o" close="c; exit (o==c)?0:1}' assets/css/styles.css
```
Expected: matching counts, exit 0.

- [ ] **Link check against the built site**

`html-proofer` is already in the Gemfile's development group. Run it, but compare against a baseline — this repo has pre-existing external-link noise, so a non-zero exit is not automatically a regression.

```bash
bundle exec htmlproofer _site --disable-external --allow-hash-href 2>&1 | tail -20
```
Expected: no *new* internal-link failures versus `publish`. Investigate any failure naming a file this branch touched.

- [ ] **Every page still builds**

```bash
find _site -name "*.html" | wc -l
```
Compare to the same count on `publish`. Expected: one fewer (flowchart.html), everything else present.

- [ ] **Both breakpoints render**

Serve and screenshot at 390×844 and 1280×900. Neither may show a horizontal scrollbar; the mobile shot must match `screenshots/10-mobile-home.png` on the eight points in Task 5 Step 5.

---

## Rulings made while writing this plan

These are decisions taken on the user's behalf where the spec was silent or self-contradictory. Each is cheap to reverse.

1. **Nav toggle keeps 14px vertical padding, not the spec's 10px.** The spec's own 44px touch-target minimum is violated by 10px (yields 36px). Cost if wrong: the icon sits 8px taller than the mockup.
2. **The featured hero's second button (`All 7 Projects`) is kept on mobile.** Screenshot `10-mobile-home.png` appears to show only `OPEN PROJECT`, but the spec text never says to drop it, and hiding it would contradict the spec's own principle that touch users get the same information. Cost if wrong: one extra full-width ghost button on the mobile home page. **Flag this one to the user** — it is the only place the plan knowingly diverges from a screenshot.
3. **Social-link touch targets are fixed at all widths, not only ≤700px.** The spec frames it as mobile, but a 13px target is a defect on any touch device. Cost if wrong: slightly taller footer links on desktop.
4. **Screenshots (6.5MB) are committed** rather than gitignored, since they are the reference for the nine out-of-scope pages when those are built. Cost if wrong: 6.5MB in git history.
5. **`support.js` is dropped from the committed spec** — it is the design-canvas runtime, never shipped, and adds 69KB of generated code to the repo. The mockup HTML is kept as reference. Cost if wrong: the `.dc.html` mockup will not be interactive if opened in a browser; its static content is still readable.

## Open question for the user

**Ruling 2 above** — on mobile, should the featured hero show both buttons (`OPEN PROJECT` + `ALL 7 PROJECTS`) or just the primary? The mockup shows one; the spec text implies two. The plan currently keeps both. Say the word and it becomes one line of CSS in Task 5.

---

## Notes for the executor

**Read the v3 README's Mobile section before starting Task 5.** It is the only part of this plan not backed by paste-ready code.

**Things the handoff got wrong that are already corrected in this plan** — do not "fix" them back:

- The nav logo path `/assets/branding/logo/ggbytes-transparent-g.png` is **correct**. That directory exists and holds the full mark set. The spec README's asset table mentions `assets/imgs/ggbytes/` for the *footer* lockup, which is a different file.
- `code/README.md` opens with "Four edits. Nothing else in the repo needs to change" but then lists six steps including the status migration across seven files. The six steps are authoritative; the sentence is stale.
- `status_detail` is specified but **no template renders it yet**. That is expected in this scope — it lands with the project-detail page, which is out of scope here. Do not build a renderer for it.
- The v3 spec's Mobile section describes CSS that **`redesign.css` does not contain**. Pasting `redesign.css` does not deliver the mobile design; Task 5 does. Do not assume a `cp` covered it.
- `jekyll serve --detach` **crashes on this machine** (Windows). Use `script/preview.sh`, which serves the built `_site` statically. Do not spend time debugging `jekyll serve`.

**Out of scope** — the spec covers these but this plan does not. Do not start them:
`projects.html`, `csumb.html` → Coursework, `about.html`, `_layouts/project.html`, `_layouts/post.html`, `_layouts/course.html`, `archives.html`, `_layouts/tag.html`, `_includes/project-card.html` restyle, and content decision #2 (the GG Swarm capstone date-filter split).
