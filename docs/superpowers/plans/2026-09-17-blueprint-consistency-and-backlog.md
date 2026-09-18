# Blueprint Consistency & Backlog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the blueprint grid a deliberate, reusable page-header treatment instead of a one-off on the home page, and clear the backlog of verified defects and stale metadata left from the September 2026 redesign.

**Architecture:** The grid is three hand-copied `linear-gradient` pairs at two pitches. Task 1 extracts it into a `blueprint-grid()` mixin, proves that extraction changes no bytes, then bands the header elements that **already exist** — `.page-head`, `.detail-head`, `.intro-band` — rather than introducing a parallel wrapper class. Tasks 2-5 are independent of Task 1 and of each other.

**Tech Stack:** Jekyll 4.4.1, native Sass via `jekyll-sass-converter` 3.1.0 / `sass-embedded` 1.93.2, Playwright MCP for visual verification.

**Spec:** No separate spec. Every decision is recorded inline with the evidence behind it. Background on the CSS architecture is in `docs/css-architecture.md`.

**Revision note:** this plan was reviewed before execution and rewritten. The review found a verification step that the plan's own preceding step made impossible — the same defect that shipped in the previous plan — plus a script that corrupted a content file, a wrong filename, and a task with no executable content. All are fixed below. The review's structural recommendation (band the existing header elements instead of adding `.page-band`) was adopted; it removes five template edits, the dead-selector exposure, and a `margin` collision.

## Global Constraints

- **The palette is closed.** Sixteen tokens in `_sass/_tokens.scss`. Three literals are documented exceptions (`#f5f5f5`, `#c3cece`, `#8fd6d4`); do not add a fourth without a comment at the line.
- **Three breakpoints only**, reached solely through `@include respond-to(wide|nav|mobile)`. No bare `@media` outside `_tokens.scss`. Verify: `grep -rn "@media" _sass/ | grep -v _tokens.scss` must print nothing.
- **Dead selectors must stay at zero.** `python script/dead-css.py --count` → `0`. This is a build-failing CI gate. Note it reports **class** selectors; an attribute selector like `[data-status="x"]` is invisible to it.
- **`script/verify-redesign.sh` must report 26 PASS, exit 0.**
- **`docs/**` is linted by CI** (ignores cover `docs/superpowers/**`, not `docs/**`).
- **`CLAUDE.md` is a symlink to `AGENTS.md`** (mode `120000`, content exactly `AGENTS.md`, no trailing newline). Never write to it.
- **The Bash sandbox discards writes to the project directory between calls.** Use `dangerouslyDisableSandbox: true` for anything that builds or writes. Four agents have lost time to this.
- **Equal-specificity rules that set the same property need a `COLLISION SET` comment** (`docs/css-architecture.md`), including shorthand against longhand (`margin` against `margin-bottom`).
- **Deploy is `publish`.** `assets/css/styles.css` is generated, not committed.
- **Cloudflare caches assets 30 days** and there is no CLI or token on this machine. Changing an image means changing its filename.

---

### Task 1: Band every page header, and make the blueprint grid its signature

The grid currently reads as a design element on exactly one surface, which is why every other page looks unrelated to it.

**What exists today** (verified):

| Location | Pitch | Ever visible? |
| --- | --- | --- |
| `_sass/_pages.scss:18-19` `.intro-band` | 40px | Yes — home page only |
| `_sass/_components.scss:381-382` `.card-media` | 32px | No — backplate behind a thumbnail; all 7 projects have `image:`, and `card-noimg` appears in 0 built pages |
| `_sass/_components.scss:740-741` `.wide-card-media` | 32px | No — same reason |

**Six header shapes do the same job:**

| Page | Markup | Surface |
| --- | --- | --- |
| `index.html:7` | `.intro-band > .intro-inner` | framed + grid |
| `projects.html:7`, `csumb.html:10`, `archives.html:12` | `.page-head` | none (`max-width: 820px; margin: 0 0 28px`) |
| `_layouts/project.html:31`, `_layouts/tag.html:26` | `.detail-head` | none (`margin-bottom: 32px`) |
| `_layouts/course.html:44` | bare kicker/title/lead, **no wrapper**, inside `.detail-main` | none |
| `about.html:7-11` | `.bio-grid > .bio-main`, bare kicker/title/lead, **no wrapper** | none |
| `_layouts/post.html:26` | `.post-head` | none |

**The rule:** every page opens with one banded header carrying the blueprint grid, and nothing else on the page uses it.

**Blog posts are the one deliberate exclusion.** A post is a reading surface and the texture competes with body prose. Structurally this costs nothing: `.post-head` shares no class with the others, so excluding it requires no code.

**`/about/` is included.** An earlier draft omitted it while excluding posts with an argument — that asymmetry was an oversight, not a decision.

**Why band the existing elements instead of adding a `.page-band` wrapper:** `.page-head` and `.detail-head` already sit exactly where the band goes and already cover five of the six surfaces. Styling them directly removes five template edits, removes the risk of a new class tripping the dead-CSS gate, and removes a `margin` collision. The cost is that `.page-head`/`.detail-head` can no longer be used un-banded — which is precisely the rule being established.

**Alternative, if you want the opposite:** delete the grid from `.intro-band` so nothing has it. That is a two-line change and Steps 6-13 become unnecessary.

**Files:**

- Modify: `_sass/_tokens.scss` (pitch tokens + mixin)
- Modify: `_sass/_pages.scss:16-20`, `_sass/_components.scss:378-382`, `_sass/_components.scss:738-742` (replace literals)
- Modify: `_sass/_layout.scss:15-18` (`.page-head`), `:82-84` (`.detail-head`)
- Modify: `_layouts/course.html`, `about.html` (add the missing wrappers)
- Modify: `projects.html:17`, `archives.html:39`, `_layouts/tag.html:40` (remove the now-redundant rule)
- Modify: `docs/css-architecture.md`

- [ ] **Step 1: Add the tokens and the mixin**

In `_sass/_tokens.scss`, after the breakpoint block:

```scss
// ---- Blueprint grid --------------------------------------------------------
// The signature texture: faint accent-coloured graph paper. Two pitches, and
// only two. Bands are large surfaces and take the coarser grid; media
// backplates are small 4:3 boxes where 40px would show barely two lines.
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

- [ ] **Step 2: Snapshot the compiled CSS**

```bash
bundle exec jekyll build
cp _site/assets/css/styles.css "$SCRATCH/pre-mixin.css"
```

`$SCRATCH` is the session scratchpad, not the project directory.

- [ ] **Step 3: Replace the three literal copies**

At each of the three sites, replace the **three declarations spanning five lines** (`background-color`, the three-line `background-image`, and `background-size`) with a single `@include`, leaving every surrounding declaration in place and in order.

`_sass/_pages.scss` `.intro-band` (lines 16-20) and `_sass/_layout.scss` usage take the band pitch:

```scss
    @include blueprint-grid($grid-pitch-band);
```

`_sass/_components.scss` `.card-media` (378-382) and `.wide-card-media` (738-742):

```scss
    @include blueprint-grid($grid-pitch-media);
```

- [ ] **Step 4: Prove the extraction changed nothing**

```bash
bundle exec jekyll build
cmp "$SCRATCH/pre-mixin.css" _site/assets/css/styles.css && echo "IDENTICAL" || echo "DIFFERS"
```

Expected: `IDENTICAL`. **This check has been prototyped end to end and does pass** — all three call sites already emit `background-color` → `background-image` → `background-size` contiguously in that order, which is what the mixin emits, and `style: compressed` makes whitespace irrelevant. If it differs, the argument order or a default is wrong. Do not weaken this step.

- [ ] **Step 5: Commit the extraction on its own**

```bash
git add _sass/_tokens.scss _sass/_pages.scss _sass/_components.scss
git commit -m "refactor(css): extract the blueprint grid into a mixin

Three hand-copied gradient pairs at two pitches become one mixin with named
pitch tokens. Compiled CSS is byte-identical, so the appearance change that
follows lands on a proven-neutral base."
```

- [ ] **Step 6: Band the existing header elements**

Replace the current `.page-head` rule in `_sass/_layout.scss:15-18` with the shared band, and **delete the standalone `.detail-head` rule at `:82-84`** — the band owns its margin now.

```scss
// The page's opening surface: one per page, always at the top, and the only
// place the blueprint grid is allowed to show. Blog posts are deliberately
// excluded - .post-head is a reading surface and the texture fights body prose.
//
// max-width is deliberately NOT set here. It used to sit on .page-head, but a
// band has to span the content column or index pages and detail pages get
// visibly different widths. The text measure is carried by .page-lead, which
// sets its own max-width: 820px.
.page-head,
.detail-head,
.intro-band {
    @include blueprint-grid($grid-pitch-band);
    border: 1px solid $c-border;
    border-radius: 4px;
    padding: 32px 36px;
    margin: 0 0 28px;

    @include respond-to(mobile) {
        padding: 24px 20px;
    }
}
```

- [ ] **Step 7: Reduce `.intro-band` to its overrides**

`.intro-band` in `_sass/_pages.scss` now inherits the band. Delete its `background-*`, `border`, `border-radius` declarations and keep only what differs — the larger padding and margin. Add the collision comment the architecture doc requires:

```scss
// COLLISION SET - the home band is the shared treatment from _layout.scss,
// scaled up. Both rules are (0,1,0) and both set padding and margin, so this
// wins only because _pages.scss loads after _layout.scss. Do not move it
// earlier, and do not restate the border or the grid here.
.intro-band {
    padding: 52px 48px;
    margin: 0 0 40px;

    @include respond-to(mobile) {
        padding: 28px 20px;
    }
}
```

Confirm the existing mobile padding value before writing it; match what is there rather than what is shown here if they differ.

- [ ] **Step 8: Give `course.html` the header it never had**

`_layouts/course.html` has no wrapper, and its kicker/title/lead sit **inside** `.detail-main` — a grid column. `project.html` puts `.detail-head` **above** `.detail-grid` at full width. Match that, so the band is the same width on every detail page.

Move the three elements out of `.detail-main` to just above `<div class="detail-grid detail-grid-narrow">`:

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

Leave `.page-body` and everything after it inside `.detail-main`.

- [ ] **Step 9: Give `about.html` the same treatment**

`about.html:7-11` has bare kicker/title/lead inside `.bio-grid > .bio-main`. Move those three elements out of `.bio-grid` entirely, into a `<header class="detail-head">` above it, so the band spans full width like every other page. The portrait and prose stay in `.bio-grid`.

Check afterwards that `.bio-grid`'s two-column layout still resolves with the heading removed — it may have been relying on `.bio-main` having that content.

- [ ] **Step 10: Remove the now-redundant hairlines**

`projects.html:17`, `archives.html:39` and `_layouts/tag.html:40` each place `<div class="page-rule"></div>` immediately after the header. With a bordered band directly above, that is one separator too many. Delete those three lines.

Then check whether `.page-rule` is still used anywhere:

```bash
grep -rn "page-rule" --include=*.html --include=*.md . | grep -v _site
```

If nothing uses it, remove the rule from the Sass too — otherwise the dead-CSS gate fails the build.

- [ ] **Step 11: Build and run the gates**

```bash
bundle exec jekyll build
bash script/verify-redesign.sh          # 26 PASS
python script/dead-css.py --count       # 0
grep -rn "@media" _sass/ | grep -v _tokens.scss || echo ok
find _site -name "*.html" | wc -l       # 153
```

- [ ] **Step 12: Verify visually at every breakpoint**

Serve with `bash script/preview.sh 4325` (`jekyll serve --detach` crashes on Windows). With Playwright, check `/`, `/about/`, `/projects/`, `/csumb/`, `/archives/`, `/projects/ggswarm/`, `/csumb/cst363/`, `/tags/ggswarm/` at **390, 768, 861, 1280**:

```js
() => {
  const band = document.querySelector('.page-head, .detail-head, .intro-band');
  return {
    overflow: document.documentElement.scrollWidth > window.innerWidth,
    bandCount: document.querySelectorAll('.page-head, .detail-head, .intro-band').length,
    bandImage: band ? getComputedStyle(band).backgroundImage.slice(0, 48) : 'NO BAND',
    bandWidth: band ? Math.round(band.getBoundingClientRect().width) : null
  };
}
```

Assert on every page: no horizontal overflow, `bandCount === 1`, `bandImage` contains `linear-gradient`, and `bandWidth` is the same on `/projects/` and `/projects/ggswarm/` at a given viewport. The null guard matters — a page with no band must report `NO BAND`, not throw.

Then load a blog post and confirm `bandCount === 0` there, as intended.

- [ ] **Step 13: Confirm no text lost contrast**

The grid is `rgba($c-accent, 0.045)` over `$c-bg`, so the shift should be negligible — but this site just had an AA failure from stacked transparency, so measure. On `/projects/` at 1280, check `.page-kicker`, `.page-title` and `.page-lead` compute to at least 4.5:1 against `rgb(20,24,24)`.

- [ ] **Step 14: Update the architecture guide**

`docs/css-architecture.md` is the normative reference and two of its claims are now stale:

- The partial table says `_tokens.scss` holds "variables only; emits no CSS". Still true (a mixin emits only where used), but it now also holds the `blueprint-grid()` mixin — say so.
- The `_layout.scss` row lists what it owns; add the band.
- Add the blueprint grid to the guide as a named treatment: what it is, the two pitch tokens, and the rule that it appears on the page band and nowhere else.

Keep the file under 150 lines and passing markdownlint.

- [ ] **Step 15: Commit**

```bash
git add -A
git commit -m "feat(css): one banded, blueprint-gridded header on every page

The grid read as a design element on exactly one surface, the home intro band,
so every other page looked unrelated to it. The six header shapes now share one
band treatment applied to the elements that already existed, and the grid
appears there and nowhere else.

course.html and about.html gain the header wrapper they never had, both placed
above their grid so the band is full width everywhere. Blog posts keep their
plain header: a post is a reading surface and the texture fights body prose."
```

---

### Task 2: Style the GG Swarm roadmap status column

Deferred during the emoji removal. The roadmap is an 8-row table at `_projects/ggswarm.md:46-55` (heading at `:44`) whose Status column is now bare words after the emoji were stripped.

The site already has a component for this: `.status-badge` with a `data-status` attribute (`_sass/_components.scss:105-131`). The roadmap reinvents it as plain text.

**The decision, made:** keep the table and style the status cell. The alternative — moving the roadmap into front matter to reuse the timeline — was rejected on inspection: that component is `.side-timeline`, a **sidebar** module (`_layouts/project.html:120-134`), and its item schema uses `completed:` as a **boolean**, which cannot carry four states. Moving an 8-row main-column table into a narrow sidebar is a relocation, not a formatting fix.

**Status vocabulary:** the defined values are `active`, `planned`, `shipped`, `dormant`, `completed`, `in-progress`. The roadmap's `Stretch` is not among them. Map it to `dormant` — both mean "not committed, not in progress" — and keep the visible label "Stretch". Do **not** invent an undocumented status. If you want Stretch to read distinctly, add it to `_sass/_components.scss` **and** to the vocabulary list in `docs/css-architecture.md` in the same commit.

**Files:**

- Modify: `_projects/ggswarm.md:46-55`

- [ ] **Step 1: Confirm kramdown renders inline HTML inside a table cell**

There is no precedent for this in the content — no `<span>` appears in any `_projects/*.md` or `_posts/*.md`. Prove it before rewriting eight rows. Change one row, build, and check the output:

```bash
bundle exec jekyll build
grep -o 'status-badge[^<]*' _site/projects/ggswarm/index.html | head -3
```

If the span is escaped rather than rendered, stop and use the alternative below.

- [ ] **Step 2: Rewrite the status cells**

```markdown
| **0** | **Capstone Baseline** | <span class="status-badge" data-status="completed">Complete</span> | v1.0.0-capstone simulation baseline. |
| **1** | **Shared-Scene Training** | <span class="status-badge" data-status="active">Active</span> | Multi-drone training in complex shared simulation scenes. |
| **2** | **Sim-to-Real Baseline** | <span class="status-badge" data-status="planned">Planned</span> | Initial deployment to Crazyflie drones with LPS. |
```

Apply the same shape to rows 3-6 (`planned`) and row 7 (`dormant`, label `Stretch`). Keep the Phase, Title and Details columns exactly as they are.

Add `<!-- markdownlint-disable MD033 -->` / `<!-- markdownlint-enable MD033 -->` around the table if the config does not already allow inline HTML — check `.markdownlint-cli2.yaml`, which currently sets `MD033: false`, meaning it is already permitted.

- [ ] **Step 3: If Step 1 showed the HTML is escaped**

Fall back to a definition-style list instead of a table, using the same badge markup outside a table cell. Do not leave the status column as bare text — that is the state this task exists to improve.

- [ ] **Step 4: Verify**

```bash
bundle exec jekyll build
grep -c 'status-badge' _site/projects/ggswarm/index.html   # expect 8
python script/dead-css.py --count                          # 0
npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml
```

`dead-css.py` reports class selectors, and `.status-badge` is already used elsewhere, so this cannot newly fail — run it as a regression check, not as the gate for this change.

- [ ] **Step 5: Check mobile**

Tables are the most common source of horizontal overflow. At 390px on `/projects/ggswarm/`, confirm `document.documentElement.scrollWidth <= window.innerWidth`. The badge adds padding and a border to a cell that previously held bare text.

- [ ] **Step 6: Commit**

```bash
git add _projects/ggswarm.md
git commit -m "content(ggswarm): render roadmap status as the shared badge

The Status column was bare text after the emoji were removed, reinventing a
component the site already has. Stretch maps to dormant - both mean not
committed, not in progress - rather than inventing an undocumented status."
```

---

### Task 3: Make a project appear on its own tag page

A verified defect, and one line to fix. The machinery already works.

`_plugins/tag_generator.rb:30` already indexes non-post collection docs, and `_layouts/tag.html` already renders them as project cards. But `tag_names` (`:55-63`) harvests tags from `tech_stack`, `tools` and `tags` only. A project declares its identity in **`project-tag`**, which is not in that list.

Measured on the current build:

```
/tags/python/    links to /projects/ggswarm/ = 1     <- works
/tags/pytorch/   links to /projects/ggswarm/ = 1     <- works
/tags/ggswarm/   links to /projects/ggswarm/ = 0     <- broken
```

GG Swarm appears on the tag page for *Python* but not on the tag page for *itself*.

**Files:**

- Modify: `_plugins/tag_generator.rb:6-12` (comment), `:55-63` (`tag_names`)

- [ ] **Step 1: Add `project-tag` to the harvested keys**

```ruby
    def tag_names(doc)
      values = TECH_KEYS.flat_map { |key| Array(doc.data[key]) }
      values += Array(doc.data['tags'])
      values += Array(doc.data['project-tag'])
      values.filter_map do |value|
        name = value.is_a?(Hash) ? value['name'] : value
        stripped = name.to_s.strip
        stripped unless stripped.empty?
      end
    end
```

Update the class comment at `:6-12`, which enumerates the tag sources explicitly and will otherwise be wrong.

- [ ] **Step 2: Know the blast radius before building**

`tag_names` is shared by posts and collection docs, so posts are now also indexed by their `project-tag`. For **11 of the 12** posts that carry one, this is a no-op — they already list the same value in `tags:` and `add_all` dedupes with `list << doc unless list.include?(doc)`.

**One post is not a no-op:** `_posts/2026-05-01-introducing-gg-swarm-live.md` has `project-tag: ggswarm` but `tags: [robotics, drones, hardware, engineering]`. It will correctly start appearing on `/tags/ggswarm/`, taking that page from 10 log rows to 11.

Confirm the set yourself before building — note that `tags:` is a YAML **block** list in most posts and an inline list in others, so a naive `grep '^tags:.*ggswarm'` matches nothing and proves nothing:

```bash
python - <<'PY'
import glob, re, io
for p in sorted(glob.glob("_posts/*.md")):
    s = io.open(p, encoding="utf-8").read(2500)
    pt = re.search(r'^project-tag:\s*["\']?([\w-]+)', s, re.M)
    if not pt:
        continue
    tg = re.search(r'^tags:\s*(\[.*?\]|(?:\n\s*-\s*.*)+)', s, re.M)
    if pt.group(1) not in (tg.group(1) if tg else ""):
        print("will newly appear:", p, pt.group(1))
PY
```

- [ ] **Step 3: Build and check the page count**

```bash
bundle exec jekyll build
find _site -name "*.html" | wc -l
```

Was **153**, expect **155**. Two tag pages are created because their `project-tag` values had no page: **`ggtrader`** and **`rover`**. (`/tags/gary-gigabytes/` already exists, so `_projects/ggbytes.md` adds nothing.) Confirm those two are pages you want; if not, the fix is front matter, not the plugin.

- [ ] **Step 4: Verify the fix, and that nothing regressed**

```bash
grep -c "/projects/ggswarm/" _site/tags/ggswarm/index.html    # expect >= 1, was 0
grep -c "log-row" _site/tags/ggswarm/index.html               # expect 11, was 10 (see Step 2)
grep -c "/projects/ggswarm/" _site/tags/python/index.html     # expect 1, unchanged
bash script/verify-redesign.sh                                # 26 PASS
python script/dead-css.py --count                             # 0
bundle exec rubocop                                           # the plugin is linted
```

- [ ] **Step 5: Check a tag with posts but no project**

`_layouts/tag.html` filters `tagged_docs` through `project_urls contains d.url`, which exists because course pages once rendered as empty project cards. Pick a tag with posts and no owning project and confirm it renders no empty card and no Liquid error.

- [ ] **Step 6: Commit**

```bash
git add _plugins/tag_generator.rb
git commit -m "fix(tags): index projects by their own project-tag

The generator already indexed collection docs and the layout already rendered
them, but tag_names harvested only tech_stack, tools and tags - so GG Swarm
appeared on /tags/python/ and not on /tags/ggswarm/.

Adds two tag pages (ggtrader, rover) whose project-tag had no page, and one log
entry to /tags/ggswarm/ from a post that carries project-tag: ggswarm without
listing it in tags:."
```

---

### Task 4: Content metadata and copy fixes

Small, independent, verified. Two steps need your input and are marked.

**Files:** `about.html`, `_posts/2026-02-09-HexMaster-Testing.md`, `_csumb/*.md` (12), `_posts/*.md` (18)

- [ ] **Step 1: Give `/about/` a real description**

The file is **`about.html`**, not `about.md`. Its front matter has no `description:`, so it falls back to the site-wide blurb:

```bash
grep -c "^description:" about.html    # 0
```

Add a `description:` of **at least 100 characters** describing the page. Below 100, `_includes/head.html` appends the generic site blurb to satisfy LinkedIn — which validates but reads generically.

- [ ] **Step 2: Remove the last emoji**

`_posts/2026-02-09-HexMaster-Testing.md:31` ends a heading with U+1F680: `## Quick Command Reference 🚀`.

Strip the **preceding** whitespace, not the following. A greedy trailing `\s*` eats the newline and pulls the next markdown table row up into the heading, which silently stops the table rendering:

```bash
python - <<'PY'
import io, re
p = "_posts/2026-02-09-HexMaster-Testing.md"
s = io.open(p, encoding="utf-8").read()
s = re.sub(r"\s*[\U0001F000-\U0001FAFF]", "", s)
io.open(p, "w", encoding="utf-8", newline="").write(s)
PY
sed -n '29,34p' _posts/2026-02-09-HexMaster-Testing.md
```

Confirm the heading still reads correctly and the table below it still starts on its own line.

- [ ] **Step 3 (NEEDS YOUR DATA): `term:` and `skills:` on the 12 course files**

`_layouts/course.html:14-15` documents both as optional front matter and renders a Term row and a Skills module when present. Coverage is **0 of 12** for each, so both features are dead in practice.

This needs the real terms ("Spring 2025") and skill lists per course. It cannot be inferred from the repo. Supply them and this is mechanical.

- [ ] **Step 4 (NEEDS YOUR DATA): `project-tag:` on the remaining posts**

12 of 30 posts carry `project-tag:`. The other 18 never appear in a project's related-entries feed, and `_layouts/post.html:96`'s fallback link cannot resolve for them.

```bash
grep -L '^project-tag:' _posts/*.md
```

Some genuinely belong to no project; those are correct as they are. Decide per post.

- [ ] **Step 5: Verify at the source, not the output**

Do **not** verify Step 1 by checking built `og:description` lengths — `_includes/head.html` pads anything under 100 characters, so that assertion passes before and after and can never detect whether the step was done. Assert on the front matter instead:

```bash
bundle exec jekyll build
python - <<'PY'
import io, re
s = io.open("about.html", encoding="utf-8").read(1200)
m = re.search(r'^description:\s*["\']?(.*?)["\']?\s*$', s, re.M)
print("about.html description:", len(m.group(1)) if m else "MISSING", "chars")
PY
python - <<'PY'
import io, re
s = io.open("_posts/2026-02-09-HexMaster-Testing.md", encoding="utf-8").read()
print("emoji remaining:", len(re.findall("[\U0001F000-\U0001FAFF]", s)))
PY
```

Expected: a length of 100 or more, and 0 emoji.

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "content: about description, last emoji removed"
```

---

### Task 5: Sync `main` with `publish`

`main` is the default branch; `publish` deploys. PR #55 merged `publish` into `main` but captured the state before the last several pushes.

Current: `main` is **28 behind**, 1 ahead (its own merge commit). Dependabot open alerts: **0**. This is housekeeping, not security.

- [ ] **Step 1: Confirm the gap**

```bash
git fetch origin
git log --oneline origin/main -1
git log --oneline origin/publish -1
git rev-list --count origin/main..origin/publish
git rev-list --count origin/publish..origin/main
```

- [ ] **Step 2: Open a PR rather than pushing to `main`**

`.github/workflows/lint.yml` runs on `pull_request`, so opening `publish` → `main` as a PR runs the checks, exactly as PR #55 did. Do not force-push and do not fast-forward locally.

- [ ] **Step 3: Confirm `publish` still deploys**

Merging to `main` does not redeploy — only pushes to `publish` do. Afterwards:

```bash
curl -sI https://garygigabytes.com/ | head -1
```

---

## Final verification

- [ ] **Everything green**

```bash
bundle exec jekyll build && echo "build=$?"
bash script/verify-redesign.sh              # 26 PASS
python script/dead-css.py --count           # 0
bundle exec rubocop
npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml
find _site -name "*.html" | wc -l           # 153, or 155 after Task 3
grep -rn "@media" _sass/ | grep -v _tokens.scss || echo ok
git ls-files -s CLAUDE.md                   # mode 120000, blob 47dc3e3d...
```

- [ ] **Four viewports, no regressions**

390, 768, 861, 1280 on `/`, `/about/`, `/projects/`, `/projects/ggswarm/`, `/csumb/cst363/`, `/tags/ggswarm/`: no horizontal overflow, single column below 1024px, exactly one band per page, zero bands on a blog post, 44px touch targets at mobile.

- [ ] **Shipping**

Merge to `publish` and push. If any image changed, **its filename must change too** — Cloudflare caches 30 days and there is no purge tooling here.

## Deferred, not scheduled

- **A small-format GG Swarm mark.** HexMaster has `assets/branding/logo/hexmaster.svg`; GG Swarm has only a 1024px PNG.
- **A committed cascade-equivalence tool.** The previous plan used a throwaway script to prove a CSS refactor changed no rendering. Its review found two real flaws: it compared literal property names, missing shorthand-versus-longhand collisions, and its ancestor-subset heuristic wrongly rejected genuine collisions. If a future refactor needs one, rebuild it shorthand-aware and ancestor-agnostic and settle flagged pairs against the real DOM. Do not resurrect the original.
- **`.ai-disclaimer` sizing.** Passes AA at 5.01:1 but renders at 10.88px. A size bump is a design call, not a fix.
- **UTF-8 BOM on compiled `styles.css`.** Noted as minor and deferred during the Sass migration; harmless, and recorded here so the decision is not rediscovered as a bug.

## Notes for the executor

- Task 1 is the only task with a visual outcome, and is deliberately split so the provably byte-neutral mixin extraction commits separately from the appearance change.
- Tasks 2-5 are independent of Task 1 and of each other.
- Task 4 Steps 3 and 4 are blocked on information only the author has. Do the rest and report those two outstanding rather than guessing at course terms or project ownership.
- This plan's first draft contained a verification step that its own preceding step made impossible, and the plan before it shipped with the same defect. If a step here cannot be satisfied as written, **say so and stop** — do not quietly substitute a weaker check.
