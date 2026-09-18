# Blueprint Consistency & Backlog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the blueprint grid a deliberate, reusable page-header treatment instead of a one-off on the home page, and clear the backlog of verified defects and stale metadata left from the September 2026 redesign.

**Architecture:** The grid is currently three hand-copied `linear-gradient` pairs at two different pitches. Task 1 extracts it into a `blueprint-grid()` mixin in `_tokens.scss`, proves that refactor changes no bytes, and only then introduces a shared `.page-band` header surface that every index and detail page uses. Tasks 2-5 are independent and can run in any order.

**Tech Stack:** Jekyll 4.4.1, native Sass via `jekyll-sass-converter` 3.1.0 / `sass-embedded` 1.93.2, Playwright MCP for visual verification.

**Spec:** No separate spec. This plan is self-contained; every decision is recorded inline with the evidence behind it. Background on the CSS architecture lives in `docs/css-architecture.md`.

## Global Constraints

- **The palette is closed.** Sixteen tokens in `_sass/_tokens.scss`. Three literals are documented exceptions (`#f5f5f5`, `#c3cece`, `#8fd6d4`); do not add a fourth without a comment at the line.
- **Three breakpoints only**, reached solely through `@include respond-to(wide|nav|mobile)`. No bare `@media` outside `_tokens.scss`. Verify: `grep -rn "@media" _sass/ | grep -v _tokens.scss` must print nothing.
- **Dead selectors must stay at zero.** `python script/dead-css.py --count` → `0`. This is a build-failing CI gate; a new class that no template uses will fail the Lint workflow.
- **`script/verify-redesign.sh` must report 26 PASS, exit 0.**
- **`docs/**` is linted by CI** (the markdownlint ignores cover `docs/superpowers/**`, not `docs/**`). Any new guide must pass `npx markdownlint-cli2 --config .markdownlint-cli2.yaml`.
- **`CLAUDE.md` is a symlink to `AGENTS.md`** (git mode `120000`, content exactly `AGENTS.md`, no trailing newline). Never write to it. Never "fix" a trailing-newline warning on it.
- **The Bash tool's sandbox discards writes to the project directory between calls.** Use `dangerouslyDisableSandbox: true` for anything that builds, writes, or must persist. Three agents lost time to this.
- **`_config.yml` excludes `docs/`**, so plans and guides are not published.
- **Deploy is `publish`.** Pushing there builds a Docker image via Cloud Build and deploys to Cloud Run. `assets/css/styles.css` is generated, not committed.
- **Cloudflare caches assets for 30 days** (`max-age=2592000`) and there is no CLI or API token on this machine. Changing an image means changing its filename.

---

### Task 1: Make the blueprint grid a real page-header treatment

The main event. Currently the grid reads as a design element on exactly one surface — the home page intro band — which is why every page after it feels unrelated.

**What is actually there today** (verified, not assumed):

| Location | Pitch | Visible? |
| --- | --- | --- |
| `_sass/_pages.scss:15` `.intro-band` | 40px | Yes — home page only |
| `_sass/_components.scss:373` `.card-media` | 32px | No — it is a backplate behind a project thumbnail, and all 7 projects have images |
| `_sass/_components.scss:~736` `.wide-card-media` | 32px | No — same reason |

So the grid exists three times, at two pitches, and is only ever *seen* in one place.

**And the header markup is five different shapes** doing the same job:

| Page | Markup | Surface |
| --- | --- | --- |
| `index.html:7` | `.intro-band > .intro-inner` | framed + grid |
| `projects.html:7`, `csumb.html:10`, `archives.html:12` | `.page-head` | none (just `max-width` + margin) |
| `_layouts/project.html:31`, `_layouts/tag.html:26` | `.detail-head` | none |
| `_layouts/course.html:43` | bare `.page-kicker`/`.page-title`/`.page-lead`, no wrapper at all | none |
| `_layouts/post.html:26` | `.post-head` | none |

**The rule this task establishes:** every page opens with one banded header carrying the blueprint grid, and nothing else on the page uses it. One blueprint surface per page, at the top.

**Deliberate exception — blog posts keep their plain header.** A post is a reading surface; a textured band directly above body prose competes with it, and `.post-head` already solved its own problem (left-aligned, measured column). If you disagree, adding `.page-band` to `_layouts/post.html` is a one-line change — but make it a decision, not a default.

**Alternative direction, if you'd rather go the other way:** delete the grid from `.intro-band` so nothing has it, and keep it purely as a media backplate. That is a two-line change and Tasks 1.4-1.8 become unnecessary. This plan assumes you want the grid promoted, because you said you liked it.

**Files:**

- Modify: `_sass/_tokens.scss` (add pitch tokens + mixin)
- Modify: `_sass/_pages.scss:15-21`, `_sass/_components.scss:373-384`, `_sass/_components.scss:736-744` (replace literals)
- Modify: `_sass/_layout.scss` (add `.page-band`)
- Modify: `projects.html`, `csumb.html`, `archives.html`, `_layouts/project.html`, `_layouts/tag.html`, `_layouts/course.html`

- [ ] **Step 1: Add the tokens and the mixin**

In `_sass/_tokens.scss`, after the breakpoint block. A mixin emits nothing until it is used, so `_tokens.scss` still compiles to zero CSS and the guide's claim stays true.

```scss
// ---- Blueprint grid --------------------------------------------------------
// The signature texture: a faint accent-coloured graph paper. Two pitches, and
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

- [ ] **Step 2: Snapshot the compiled CSS before touching anything**

```bash
bundle exec jekyll build
cp _site/assets/css/styles.css "$SCRATCH/pre-mixin.css"
```

Use the session scratchpad for `$SCRATCH`, not the project directory.

- [ ] **Step 3: Replace all three literal copies with the mixin**

`_sass/_pages.scss` `.intro-band` — replace the four background lines with:

```scss
    @include blueprint-grid($grid-pitch-band);
```

`_sass/_components.scss` `.card-media` and `.wide-card-media` — replace the four background lines in each with:

```scss
    @include blueprint-grid($grid-pitch-media);
```

- [ ] **Step 4: Prove that refactor changed nothing**

```bash
bundle exec jekyll build
cmp "$SCRATCH/pre-mixin.css" _site/assets/css/styles.css && echo "IDENTICAL" || echo "DIFFERS"
```

Expected: `IDENTICAL`. This is a pure extraction — three call sites producing the bytes they produced before. If it differs, the mixin's argument order or default is wrong. Fix before continuing.

- [ ] **Step 5: Commit the extraction on its own**

```bash
git add _sass/_tokens.scss _sass/_pages.scss _sass/_components.scss
git commit -m "refactor(css): extract the blueprint grid into a mixin

Three hand-copied gradient pairs at two pitches become one mixin with named
pitch tokens. Compiled CSS is byte-identical; this is extraction only, so the
behaviour change that follows lands on top of a proven-neutral base."
```

Keeping this separate matters: if the visual change in Step 8 looks wrong, this commit is still good and can stay.

- [ ] **Step 6: Add the shared band surface**

In `_sass/_layout.scss`, next to `.page-head`:

```scss
// The page's opening surface. One per page, always at the top - this is the
// only place the blueprint grid is allowed to show. `.intro-band` on the home
// page is the same treatment with a taller inner padding.
.page-band {
    @include blueprint-grid($grid-pitch-band);
    border: 1px solid $c-border;
    border-radius: 4px;
    padding: 32px 36px;
    margin: 0 0 28px;

    @include respond-to(mobile) {
        padding: 24px 20px;
    }
}

.page-band .page-head {
    margin-bottom: 0;
}
```

- [ ] **Step 7: Wrap the three index-page headers**

In `projects.html`, `csumb.html` and `archives.html`, wrap the existing `<section class="page-head">…</section>` in the band. `projects.html` becomes:

```html
<div class="page-band">
    <section class="page-head">
        <p class="page-kicker">Hobby Projects</p>
        <h1 class="page-title">Things I'm building</h1>
        <p class="page-lead">
            Over the years, I've worked on a variety of personal and academic projects — but I haven't always done the best
            job documenting them. That changes here. This site is my attempt to track, showcase, and share the things I'm
            building and learning.
        </p>
    </section>
</div>
```

Apply the same wrapper in `csumb.html:10` and `archives.html:12`, leaving their inner content untouched.

- [ ] **Step 8: Wrap the detail headers**

`_layouts/project.html:31` and `_layouts/tag.html:26` already have `<header class="detail-head">`. Add the band class to it rather than nesting another element:

```html
<header class="detail-head page-band">
```

`_layouts/course.html` has no header wrapper at all — its kicker, title and lead sit bare inside `.detail-main`. Give it one, wrapping only those three elements and leaving `.page-body` and everything after it outside:

```html
        <header class="detail-head page-band">
            <p class="page-kicker">
                {{ page.course_code }}{% if page.term %} &middot; {{ page.term }}{% endif %}
            </p>
            <h1 class="page-title">{{ course_name }}</h1>
            {% if page.note %}
            <p class="page-lead">{{ page.note }}</p>
            {% endif %}
        </header>
```

- [ ] **Step 9: Check `.detail-head` does not now double up**

`.detail-head` may already carry its own margin or border that fights the band.

```bash
sed -n "/^\.detail-head/,/^}/p" _sass/_layout.scss
```

If it sets `border`, `border-radius`, `padding` or `background`, reconcile it — the band owns those now. Leave its `max-width` alone.

- [ ] **Step 10: Build and run the gates**

```bash
bundle exec jekyll build
bash script/verify-redesign.sh          # 26 PASS
python script/dead-css.py --count       # 0
grep -rn "@media" _sass/ | grep -v _tokens.scss || echo ok
```

`.page-band` is a new class — if the count is not 0, a template is not using it and the CI gate will fail the build.

- [ ] **Step 11: Verify visually, at every breakpoint**

Serve with `bash script/preview.sh 4325` (`jekyll serve --detach` crashes on Windows), then with Playwright check `/`, `/projects/`, `/csumb/`, `/archives/`, `/projects/ggswarm/`, `/csumb/cst363/`, `/tags/ggswarm/` at **390, 768, 861, 1280**:

```js
() => ({
  overflow: document.documentElement.scrollWidth > window.innerWidth,
  bands: [...document.querySelectorAll('.page-band, .intro-band')].length,
  bandBg: getComputedStyle(document.querySelector('.page-band, .intro-band')).backgroundImage.slice(0, 60)
})
```

Assert: no horizontal overflow anywhere, exactly **one** band per page, and the grid actually painting. A page with two bands means a wrapper was nested wrongly.

- [ ] **Step 12: Confirm the grid did not cost any text contrast**

The grid is `rgba($c-accent, 0.045)` over `$c-bg`, so the luminance shift should be negligible — but the site just had an AA failure from stacked transparency, so measure rather than assume. On `/projects/` at 1280, check `.page-kicker`, `.page-title` and `.page-lead` compute to at least 4.5:1 against `$c-bg` (`rgb(20,24,24)`).

- [ ] **Step 13: Commit**

```bash
git add -A
git commit -m "feat(css): one banded, blueprint-gridded header on every page

The grid previously read as a design element on exactly one surface, the home
intro band, so every other page looked unrelated to it. Five different header
shapes now share one .page-band treatment, and the grid appears there and
nowhere else.

Blog posts keep their plain header on purpose: a post is a reading surface and
the texture competes with body prose."
```

---

### Task 2: Reformat the GG Swarm roadmap

Deferred deliberately during the emoji removal. The roadmap is an 8-row markdown table (`_projects/ggswarm.md:33-41`) whose Status column is now bare words (`Complete`, `Active`, `Planned`, `Stretch`) after the emoji were stripped.

The site already has a status vocabulary and a component for exactly this: `data-status` attributes rendered as `.status-badge` / `.status-tag`, with the vocabulary `active`, `planned`, `shipped`, `dormant`, plus `completed` / `in-progress` on course pages. The roadmap reinvents it as plain text in a table cell.

**Files:**

- Modify: `_projects/ggswarm.md:30-41`
- Possibly modify: `_sass/_components.scss` (if the badge needs a table-cell variant)

- [ ] **Step 1: Decide the target shape**

Two options; pick one before writing any markup.

1. **Keep the table, style the status cell.** Requires rendering raw HTML in the markdown table so each status becomes `<span class="status-badge" data-status="planned">Planned</span>`. Cheapest, keeps the scannable grid.
2. **Replace the table with a phase list**, matching the `.timeline` component the project layout already renders from front matter. Most consistent with the rest of the site, but the roadmap is *page body* content and the timeline is *front matter* — so this means moving eight rows into `_projects/ggswarm.md` front matter and letting the layout render them.

Option 2 is the more consistent answer and removes hand-formatted markup entirely. Option 1 is a twenty-minute change. Choose deliberately.

- [ ] **Step 2: Check the status vocabulary actually covers it**

```bash
grep -rn "data-status" _sass/_components.scss | head
grep -rn "status-badge\|status-tag" _includes _layouts | head
```

The roadmap uses `Stretch`, which is **not** in the vocabulary. Either map it onto an existing value or add it to the palette and the guide's vocabulary list deliberately — do not invent an undocumented status.

- [ ] **Step 3: Implement, build, verify**

```bash
bundle exec jekyll build
python script/dead-css.py --count    # 0 - a new status class with no template use fails CI
npx --yes markdownlint-cli2 --config .markdownlint-cli2.yaml
```

- [ ] **Step 4: Check mobile**

Tables are the most common source of horizontal overflow. At 390px confirm `document.documentElement.scrollWidth <= window.innerWidth` on `/projects/ggswarm/`.

- [ ] **Step 5: Commit**

---

### Task 3: Make a project appear on its own tag page

A verified defect, and a much smaller one than it looks. The machinery already works — it is one missing key.

`_plugins/tag_generator.rb:30` already indexes non-post collection docs, and `_layouts/tag.html:11` already renders them as project cards. But `tag_names` (`_plugins/tag_generator.rb:55-63`) harvests tags from `tech_stack`, `tools` and `tags` only. A project declares its own identity in **`project-tag`**, which is not in that list.

The result, measured on the current build:

```
/tags/python/    links to /projects/ggswarm/ = 1     <- works
/tags/pytorch/   links to /projects/ggswarm/ = 1     <- works
/tags/ggswarm/   links to /projects/ggswarm/ = 0     <- broken
```

So GG Swarm appears on the tag page for *Python*, but not on the tag page for *itself*. `/tags/ggswarm/` shows ten log entries about the project and no way to reach it.

**Files:**

- Modify: `_plugins/tag_generator.rb:55-63`

- [ ] **Step 1: Add `project-tag` to the harvested keys**

In `tag_names`, add one line:

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

Update the comment block at the top of the class (lines 6-12) to say three sources, not two — it currently enumerates them explicitly and will otherwise be wrong.

- [ ] **Step 2: Understand the blast radius before building**

`tag_names` is shared by posts and collection docs, so this also indexes posts by their `project-tag`. That is harmless — a post carrying `project-tag: "ggswarm"` already lists `ggswarm` in its `tags:`, and `add_all` dedupes with `list << doc unless list.include?(doc)`. Confirm rather than assume:

```bash
grep -l '^project-tag:' _posts/*.md | head -3 | xargs grep -l '^tags:.*ggswarm' | wc -l
```

- [ ] **Step 3: Build and check the page count first**

```bash
bundle exec jekyll build
find _site -name "*.html" | wc -l
```

Was 153. A `project-tag` value with no existing tag page **creates a new page** — for example `_projects/ggbytes.md` declares `project-tag: "gary-gigabytes"`. An increase is expected and correct; note the new number and confirm each new page is one you want.

- [ ] **Step 4: Verify the fix and that nothing regressed**

```bash
grep -c "/projects/ggswarm/" _site/tags/ggswarm/index.html    # expect >= 1, was 0
grep -c "log-row" _site/tags/ggswarm/index.html               # expect 10, unchanged
grep -c "/projects/ggswarm/" _site/tags/python/index.html     # expect 1, unchanged
bash script/verify-redesign.sh                                # 26 PASS
python script/dead-css.py --count                             # 0
bundle exec rubocop                                           # the plugin is linted
```

- [ ] **Step 5: Check a tag that has posts but no project**

`_layouts/tag.html:11` filters `tagged_docs` through `project_urls contains d.url`, which exists because course pages once rendered as empty project cards. Confirm that filter still holds: pick a tag with posts and no owning project and verify it renders no empty card and no Liquid error.

- [ ] **Step 6: Commit**

---

### Task 4: Content metadata and copy fixes

Small, independent, verified. Some need your input; those are marked.

**Files:** `about.md`, `_posts/2026-02-09-HexMaster-Testing.md`, `_csumb/*.md` (12 files), `_posts/*.md` (18 files)

- [ ] **Step 1: Give `/about/` a real description**

`about.md` has no `description:` front matter, so it falls back to the site-wide blurb. Confirmed: `grep -c "^description:" about.md` → `0`.

Add a `description:` of **at least 100 characters** — below that, `_includes/head.html` appends the site blurb to satisfy LinkedIn, which reads fine but is generic. Write one that describes the page.

- [ ] **Step 2: Remove the last emoji**

`_posts/2026-02-09-HexMaster-Testing.md` contains one U+1F680 (rocket).

```bash
python - <<'PY'
import io, re
p = "_posts/2026-02-09-HexMaster-Testing.md"
s = io.open(p, encoding="utf-8").read()
s = re.sub("[\U0001F000-\U0001FAFF]\\s*", "", s)
io.open(p, "w", encoding="utf-8", newline="").write(s)
PY
```

Check the line still reads correctly afterwards — if the emoji carried meaning, replace it with a word rather than deleting it.

- [ ] **Step 3 (NEEDS YOUR DATA): `term:` and `skills:` on the 12 course files**

`_layouts/course.html:13-16` documents both as optional front matter, and renders a Term row and a Skills module when present. Coverage is currently **0 of 12** for each, so both features are dead code in practice.

This needs the actual terms ("Spring 2025") and skill lists per course — it cannot be inferred from the repo. Supply them and this becomes mechanical.

- [ ] **Step 4 (NEEDS YOUR DATA): `project-tag:` on the remaining posts**

12 of 30 posts carry `project-tag:`. The other 18 do not, so they never appear in a project's related-entries feed and `_layouts/post.html:96`'s fallback link cannot resolve.

List them and decide which belong to which project:

```bash
grep -L '^project-tag:' _posts/*.md
```

Some genuinely belong to no project; those are correct as they are.

- [ ] **Step 5: Verify and commit**

```bash
bundle exec jekyll build
python - <<'PY'
import glob, re, io
bad = [f for f in glob.glob("_site/**/*.html", recursive=True)
       if (m := re.search(r'<meta property="og:description" content="(.*?)">', io.open(f, encoding="utf-8", errors="ignore").read(), re.S))
       and len(m.group(1)) < 100]
print(f"pages under 100 chars: {len(bad)}")
PY
```

Expected: `0`.

---

### Task 5: Sync `main` with `publish`

`main` is the default branch; `publish` is what deploys. PR #55 merged `publish` into `main`, but captured the state before the last several pushes.

Current: `main` is **28 commits behind** and 1 ahead (its own merge commit). Dependabot alerts are at **0 open**, so this is housekeeping, not a security issue.

- [ ] **Step 1: Confirm the gap before acting**

```bash
git fetch origin
git log --oneline origin/main -1
git log --oneline origin/publish -1
git rev-list --count origin/main..origin/publish
git rev-list --count origin/publish..origin/main
```

- [ ] **Step 2: Open a PR rather than pushing to `main`**

`main` is protected by the Lint workflow. Open `publish` → `main` as a pull request so the checks run, exactly as PR #55 did. Do not force-push and do not fast-forward locally.

- [ ] **Step 3: Confirm the merge kept `publish` deployable**

`main` merging does not redeploy — only pushes to `publish` do. After the merge, confirm `publish` is unchanged and the live site still responds:

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
find _site -name "*.html" | wc -l           # 153, unless Task 3 intentionally changes it
grep -rn "@media" _sass/ | grep -v _tokens.scss || echo ok
git ls-files -s CLAUDE.md                   # mode 120000, blob 47dc3e3d...
```

- [ ] **Four viewports, no regressions**

390, 768, 861, 1280 on `/`, `/projects/`, `/about/`, `/projects/ggswarm/`, `/csumb/cst363/`, `/tags/ggswarm/`: no horizontal overflow, single-column below 1024px, one band per page, 44px touch targets at mobile.

- [ ] **Shipping**

Merge to `publish` and push. If any image changed, **its filename must change too** — Cloudflare caches for 30 days and there is no purge tooling on this machine.

## Deferred, not scheduled

Recorded so they are not lost, but not worth a task yet:

- **A small-format GG Swarm mark.** HexMaster has `assets/branding/logo/hexmaster.svg`; GG Swarm has only a 1024px PNG. Worth generating if the swarm logo ever needs to render small, the way the HexMaster one did.
- **A committed cascade-equivalence tool.** Task 3 of the previous plan used a throwaway script to prove a CSS refactor changed no rendering. It was never committed, and its review found two real flaws: it compared literal property names, so it missed shorthand-versus-longhand collisions (`margin` against `margin-bottom`), and its ancestor-subset heuristic wrongly rejected genuine collisions. If a future refactor needs it, rebuild it shorthand-aware and ancestor-agnostic, and settle flagged pairs against the real DOM rather than a heuristic. Do not resurrect the original.
- **`.ai-disclaimer` sizing.** Now passes AA at 5.01:1, but it renders at 10.88px, which is small for body copy. A size bump is a design call, not a fix.

## Notes for the executor

- Task 1 is the only task with a visual outcome; it is deliberately split so the mixin extraction (provably byte-neutral) commits separately from the appearance change.
- Tasks 2-5 are independent of Task 1 and of each other.
- Task 4 Steps 3 and 4 are blocked on information only the author has. Do the rest of Task 4 and report those two as outstanding rather than guessing at course terms or project ownership.
- The previous plan in this directory shipped with a self-contradiction between two of its steps that three agents had to work around. If a step here cannot be satisfied as written, say so and stop — do not quietly substitute a weaker check.
