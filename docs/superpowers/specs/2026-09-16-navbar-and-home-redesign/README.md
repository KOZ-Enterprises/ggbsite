# Handoff: GGBytes site — navbar + layout redesign

## Overview

A full visual-system redesign of garygigabytes.com (Jekyll, repo
`KOZ-Enterprises/ggbsite`, branch `publish`). The brief: the navbar looked plain
and didn't match the logo's futuristic feel, and the home page's layout was
unbalanced with inconsistent spacing. The palette was to stay exactly as-is.

The work grew to cover every template on the site so nothing was left in the old
style. It also resolves two content-architecture decisions (see
**Content decisions**), which change routes and front matter, not just CSS.

## About the design files

`Home Redesign.dc.html` is a **design reference created in HTML** — a single
canvas holding every screen as a static mockup, newest iteration at the top. It
is not production code and should not be shipped. Implement the designs in the
target environment, which here is the existing Jekyll site: Liquid templates in
`_layouts/` and `_includes/`, one stylesheet at `assets/css/styles.css`, no build
step beyond Jekyll, no framework.

`code/` contains paste-ready Jekyll and CSS for the home page and navbar, already
written against the real repo structure. The remaining pages are specified in
this README and must be written to match.

## Fidelity

**High-fidelity.** Exact hex values, type sizes, letter-spacing, and spacing are
given below and are already in the mockup markup. Recreate them precisely. Every
value comes from the existing palette in `assets/css/styles.css` — no new colors
were invented.

## Target branch

Create a branch off `publish`:

```
git checkout publish && git pull
git checkout -b redesign/nav-and-layout
```

## Design tokens

### Colors (all pre-existing in the repo)

| Token | Hex | Use |
| --- | --- | --- |
| Page background | `#141818` | body, page ground |
| Surface | `#1a1e1e` | cards, navbar, sidebar modules |
| Surface deep | `#0f1111` | year-block headers, code blocks |
| Surface hover | `#1e2323` | card hover fill |
| Border | `#2e4c5b` | all 1px borders, module dividers |
| Border faint | `rgba(46,76,91,0.3)` | inner row dividers |
| Rule | `#1f2a2a` | section hairlines |
| Accent (teal) | `#64d5d2` | primary accent, active state, links |
| Accent hover | `#7fe3e0` | primary button hover |
| Amber | `#ffb300` | kickers, forward links, PLANNED status |
| Blue | `#5bc0de` | tech chips, SHIPPED/COMPLETE status |
| Ink | `#fafafa` | headings, primary text |
| Body | `#b9c4c4` | lead paragraphs |
| Body dim | `#9aa6a6` | excerpts, secondary copy |
| Muted | `#8a9696` | mono meta, dates, counts |
| Muted alt | `#8ba3a3` | inactive nav links, neutral status |
| Muted low | `#7d8a8a` | placeholder labels, separators |

Minimum contrast target is 4.5:1 on `#141818` and `#1a1e1e`. Do not go darker
than `#7d8a8a` for any text; the original draft used `#5f6b6b`/`#4e5a5a` and
failed.

### Typography

Two families must be added to `_includes/head.html`. The current link loads
Open Sans + Roboto Flex + Roboto only — **Roboto Mono is referenced throughout
`styles.css` but never loaded**, so all existing mono text is already falling
back to a system monospace, and Chakra Petch is new:

```html
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
```

| Role | Family | Size | Weight | Letter-spacing | Transform |
| --- | --- | --- | --- | --- | --- |
| Page title (h1) | Chakra Petch | 36–46px (`clamp(30px,4.4vw,46px)`) | 700 | -0.5px | none |
| Detail page title | Chakra Petch | 38–44px | 700 | -0.3px | none |
| Section rule title | Chakra Petch | 20–22px | 700 | 2.5px | uppercase |
| Card title | Chakra Petch | 20–24px | 700 | 0.5px | none |
| Log entry title | Chakra Petch | 19–21px | 600 | 0.3px | none |
| Nav link | Chakra Petch | 14.5px | 600 | 2px | uppercase |
| Wordmark | Chakra Petch | 21px | 700 | 4px | none |
| Button | Chakra Petch | 13.5px | 600 | 2px | uppercase |
| Lead paragraph | Roboto | 16–17px / 1.65 | 400 | — | none |
| Body copy | Roboto | 15.5–16.5px / 1.8 | 400 | — | none |
| Excerpt | Roboto | 14–14.5px / 1.6 | 400 | — | none |
| Kicker | Roboto Mono | 11px | 400 | 3px | uppercase |
| Meta / date | Roboto Mono | 10.5–11.5px | 400 | 1–2px | uppercase |
| Nav caption | Roboto Mono | 9.5px | 400 | 3.5px | uppercase |
| Status pill | Roboto Mono | 9.5–10px | 400 | 2–2.5px | uppercase |
| Module header | Roboto Mono | 10px | 400 | 2.5px | uppercase |

`h3` is globally `font-style: italic` in the current stylesheet — override it
wherever Chakra Petch headings are used, or the card and timeline titles will
render italic.

### Spacing, radius, borders

- Page padding: 44–48px horizontal, 36–52px vertical. Home sections separated by 40px.
- Card padding: 18–20px (grid cards), 22–28px (wide cards), 18px (sidebar modules).
- Grid gaps: 24px (card grids), 40–44px (page columns).
- Radius: 4px page shells, 6px cards and buttons, 8px nav mark (12px), 3px chips and pills.
- Borders: always 1px `#2e4c5b`. No shadows anywhere except the navbar mark's `inset 0 0 16px rgba(100,213,210,0.25)` and the active-underline glow.
- Blueprint grid fill: `linear-gradient(rgba(100,213,210,0.045) 1px, transparent 1px)` both axes, `background-size: 40px 40px` (32px inside cards).

## Components

### Navbar (`_includes/nav.html`)

Ready to paste: `code/_includes/nav.html`, CSS in `code/assets/css/redesign.css`.

- Height 86px, background `#1a1e1e`, `border-bottom: 1px solid #2e4c5b`, padding `0 5%`.
- A gradient hairline sits at `bottom: -1px`: teal at 35%, amber at 70%, transparent at both ends.
- Left: 52×52px mark — 2px `#64d5d2` border, 12px radius, inset teal glow, containing `ggbytes-transparent-g.png` at 26px tall. Then a two-line wordmark: `GARY` in `#fafafa` + `GIGABYTES` in `#64d5d2` (Chakra Petch 700, 21px, 4px tracking), and below it `ENGINEERING LOG & PORTFOLIO` (Roboto Mono 9.5px, 3.5px tracking, `#8a9696`).
- Right: four links — Home, Projects, Coursework, About. Inactive `#8ba3a3`; hover `#64d5d2` plus a 2px `#2e4c5b` bottom border.
- **Active state is the point of the redesign**: no filled block. `#fafafa` text, a 2px `#64d5d2` underline inset 14px from each side with `box-shadow: 0 0 10px rgba(100,213,210,0.8)`, plus 2px × 7px vertical bracket ticks at each end of the underline.
- Mobile (≤860px): existing `toggleNavbar()` and the `responsive` class still drive it — keep the JS untouched. Links stack, min-height 48px, and the active indicator rotates to a 2px left bar.

### Status vocabulary

Four values, used everywhere a project state appears. Set `status:` in project
front matter to exactly one:

| Value | Color | Border | Meaning |
| --- | --- | --- | --- |
| `active` | `#64d5d2` | `rgba(100,213,210,0.45)` | being worked on now |
| `planned` | `#ffb300` | `rgba(255,179,0,0.45)` | scoped, not started |
| `shipped` | `#5bc0de` | `rgba(91,192,222,0.45)` | done and running |
| `dormant` | `#8ba3a3` | `#2e4c5b` | paused, may return |

The seven `_projects/*.md` files currently carry prose values that predate this
vocabulary. Map them, and keep the descriptive phrase — it is useful — by moving
it to a new `status_detail:` field rendered in the mono meta line beside the
pill, not inside it:

| Current value | `status:` | `status_detail:` |
| --- | --- | --- |
| Active - Hardware Deployment | `active` | Hardware deployment |
| Optimization of Core Code | `active` | Core optimization |
| On-going | `active` | — |
| Testing | `active` | Testing |
| Conceptualization | `planned` | Conceptualization |
| Completed | `shipped` | — |

The pill shows only the four-value state; `status_detail` appears in the
`STARTED FEB 2026 · 8 LOG ENTRIES` meta row on detail pages (Roboto Mono 11px,
`#8a9696`). Cards show the pill alone.

Rendered as a pill: `display:inline-flex`, gap 7–9px, a 5–6px dot in
`currentColor` (the `active` dot adds `box-shadow: 0 0 8px #64d5d2`), 3px radius,
4–5px × 9–11px padding. Both `.status-tag` (hero/detail) and `.status-badge`
(cards) key off `data-status`, so anything outside the four falls back to the
grey neutral. Replace **both** existing `.status-badge` rules in `styles.css`.

Course pages use a parallel set with the same pill component: `COMPLETE`
(`#5bc0de`), `IN PROGRESS` (`#64d5d2`), `PLANNED` (`#ffb300`).

### Section rule header

Used for every section divider sitewide, replacing `.section-header` with its
Font Awesome icon and teal underline. Flex row, 16px gap: Chakra Petch 700
20–22px uppercase 2.5px-tracked title, then `flex:1` 1px `#1f2a2a` line, then an
optional right-side Roboto Mono 10.5px `#8a9696` count (`8 ENTRIES`) or teal link
(`ARCHIVES →`). Drop the icons — the rule carries the hierarchy.

### Log row (date gutter)

The repeating list unit on home, project, course, tag, and post pages. CSS grid
`140px minmax(0,1fr)` (120px in narrower columns), 24–28px gap, 24px vertical
padding, `border-top: 1px solid rgba(46,76,91,0.35)`, hover
`rgba(100,213,210,0.04)`. Gutter holds the ISO date (`#8a9696`) with the first
tag beneath it in `#64d5d2`. Main column: Chakra Petch 600 21px title, then a
14.5px/1.65 `#9aa6a6` excerpt capped at 840px.

On ≤700px the grid collapses to one column and the gutter becomes a 12px-gap flex row.

### Card (grid)

`display:flex; flex-direction:column`, 1px `#2e4c5b`, 6px radius, `#1a1e1e`.
Hover: border `#64d5d2`, background `#1e2323`. Image wrapper is
`flex:0 0 auto; width:100%; aspect-ratio:4/3; position:relative` with the image
absolutely filling it — **required**, or flex resolves the wrapper from the
image's intrinsic ratio and card heights go ragged. Cards with no image show the
blueprint grid plus a centered `NO PREVIEW` label (Roboto Mono 10px, 2.5px
tracking, `#7d8a8a`).

Body: 18px/20px padding, `border-top: 1px solid #2e4c5b`, title row (title left,
status pill right), excerpt, then tech chips — Roboto Mono 10px, `#5bc0de`, 1px
`rgba(91,192,222,0.4)`, 3px radius — with a `+N` overflow count in `#7d8a8a`.

This replaces `.project-summary`'s hover slide-up overlay. Info is always
visible; the old `.overlay-details` `translateY(65%)` behavior goes away.

### Sidebar module

1px `#2e4c5b`, 6px radius, `#1a1e1e`, `overflow:hidden`. A header bar —
13px/18px padding, `border-bottom: 1px solid #2e4c5b`, Roboto Mono 10px 2.5px-
tracked `#64d5d2` label — then rows divided by `rgba(46,76,91,0.25)`. Replaces
`.sidebar-module`'s `h3` + icon pattern.

### Buttons

`.btn-primary`: `#64d5d2` fill, `#141818` text, 6px radius, 12px/22px padding,
Chakra Petch 600 13.5px uppercase 2px-tracked. Hover `#7fe3e0`.
`.btn-ghost`: transparent, `#64d5d2` text, 1px `#2e4c5b`. Hover border `#64d5d2`,
text `#fafafa`. These replace `.archive-btn` (italic) and `.post-project-btn`
(mono) — collapse both.

### Breadcrumb

On every detail page, above the title: Roboto Mono 10.5px, 2px tracking, 10px
gap, parent in `#64d5d2` linking up, separator and current page in `#8a9696`.
26px bottom margin. Example: `PROJECTS / GG SWARM`.

## Content decisions

These change routes and front matter. Both came from the client during review.

### 1. "Academic Projects" becomes "Coursework"

The CSUMB portfolio requirement is finished, so the page is no longer a second
project showcase. Nav label is **Coursework**.

- Page scope is stated up front: kicker `CSU MONTEREY BAY · BS COMPUTER SCIENCE · APRIL 2026`, h1 `Coursework`.
- Order is capstone first (most interesting), then the course registry, then prior degrees.
- Every course row keeps its link to its `_csumb/` page — there is still work worth reading there.
- The old Project Showcase grid is removed; it duplicated `/projects/`.
- A prior-degrees strip closes the page: MS Mechanical Engineering (CSU Long Beach, 2015) and BS Mechanical Engineering (Cal Poly SLO, 2012) on one line, with a `See About →` ghost button. This is how the mechanical side gets acknowledged without the page pretending to cover it.
- Keep the URL at `/csumb/` or move to `/coursework/`; if moved, add `jekyll-redirect-from` `redirect_from: /csumb/` (the plugin is already in `_config.yml`).

### 2. Capstone snapshot vs. live project

GG Swarm exists twice on purpose, split by time:

- **Coursework → capstone card**: the project **as submitted**, frozen at April 2026. Pill reads `AS SUBMITTED · APR 2026` in the grey neutral (not `ACTIVE`). Copy describes scope, results, and write-up at submission. Forward link: `CONTINUED AS AN ACTIVE BUILD →`.
- **Projects → GG Swarm**: the living build, `status: active`, accruing log entries. Its sidebar carries an `ORIGIN` module: "Began as my CST 499 capstone at CSUMB, submitted April 2026" + `SEE THE SUBMITTED SNAPSHOT →`.

Implement the split as a **date filter, not duplicated content**. Capstone posts
already carry `project-tag: ggswarm` and the `csumb` tag. The snapshot view shows
only entries dated on or before the submission date; the project page shows all
of them. Nothing is maintained twice, and new work can only land in one place.

### 3. Files to remove

- `flowchart.html` — archive it. `_config.yml` already has an `exclude:` block (`template/`, `test.html`), so this is a one-line addition to that list. It was a one-off roadmap, is entirely off-system (nested `<head>`, Segoe UI, `#27e3ff`, gold banners, emoji), and overlaps the GG Swarm timeline.
- `_layouts/tags.html` — delete. The tag index styles a `.tag-list` class that does not exist in the stylesheet, and the Archives tag strip is a better entry point. **Keep `_layouts/tag.html`** — individual tag pages are linked from every post.
- `_includes/header.html` — delete. Orphaned, and points at a logo file that is not in the repo.

### 4. Logo placement

The navbar uses the G mark plus a type wordmark, so the full lockup
(`ggbytes-transparent-cropped.png`) now lives in the **footer**, once per page:
26px tall, `opacity: 0.85`, 16px gap, beside
`© <year> · BUILT IN LONG BEACH, CA · 33.77°N 118.19°W` in Roboto Mono 10.5px
`#8a9696`. "GARY GIGABYTES" is dropped from that line since the logo says it.

## Screens

Each screen below maps to a mockup id in `Home Redesign.dc.html`. Open it and
search for `id="2a"` etc. Newest turns are at the top of the file.

### Home — `2a` (chosen) — `index.html`

Paste-ready: `code/index.html`.

Order: intro band → featured project hero → project logs → pagination.

1. **Intro band** — blueprint-grid fill, 1px border, 4px radius, 52px/48px padding, content capped at 780px. Amber kicker `GARY KUEPPER // ECS ANALYSIS ENGINEER @ BOEING`, h1 `Bridging the physical / and digital worlds` (explicit `<br>`), 16.5px lead with `<strong>` in `#fafafa`, then Browse Projects (primary) + About Me (ghost).
2. **Featured hero** — min-height 430px, image absolutely filling, gradient overlay `90deg, rgba(20,24,24,0.97) 0%, rgba(20,24,24,0.85) 42%, rgba(20,24,24,0.25) 100%`. Body max 660px: status pill, 50px Chakra Petch title, 17px description, Open Project + All N Projects. Reads `image`/`status`/`description`/`title` from the `ggswarm` project front matter using the same Liquid lookup as before.
3. **Project logs** — rule header (`Project Logs` + `ARCHIVES →`), then paginated log rows, then pagination with ghost buttons and a Roboto Mono page count.

Replaced: the `.hero-card` quote block with its Font Awesome quote marks, and the
unbalanced `.grid-container` two-column block (Recent Log Entries beside Featured
Project). The rejected alternative `2b` put the hero first — keep `2a`.

### Projects — `3a` — `projects.html`

Page head (kicker `HOBBY PROJECTS`, h1 `Things I'm building`, existing lead copy
verbatim), a 1px `#1f2a2a` rule, then a three-column card grid (`repeat(3, minmax(0,1fr))`, 24px gap) of all `_projects/` entries sorted by `order`.
Update `_includes/project-card.html` to the static card described above.

### Coursework — `3b` — `csumb.html`

Kicker, h1 `Coursework`, lead. Then:

1. **Capstone card** — grid `300px 1fr`, image left (min-height 200px), body right with 24px title, `AS SUBMITTED · APR 2026` pill, description, amber `CONTINUED AS AN ACTIVE BUILD →`.
2. **Course registry** — rule header with `12 COURSES`, then one bordered container of linked rows: grid `110px 1.1fr 1.4fr auto`, 24px gap, 16px/22px padding. Columns are course code (Roboto Mono 12px `#64d5d2`), title (Chakra Petch 600 16px), one-line note (Roboto Mono 11.5px `#8a9696`), state pill. Hover `rgba(100,213,210,0.05)`. Replaces the 2-up `.course-item` grid — far better at 12 rows.
3. **Prior degrees strip** — top rule, mono label, one-line degree list, `See About →`.

### About — `3c` — `about.html`

1. **Bio + portrait** — grid `1.6fr 1fr`. Left: kicker `GARY KUEPPER // LONG BEACH, CA`, h1, two 16px/1.7 paragraphs (existing copy, verbatim). Right: framed panel — 14px padding, 1px border, 6px radius, square `aspect-ratio:1/1` headshot inside a 4px-radius inner frame, mono caption below. Replaces `.headshot.featured-img`'s 4px teal border and centered placement.
2. **Experience / Education** — two columns, 44px gap. Experience is a timeline: each role a 2px left border (`#64d5d2` for current, `#2e4c5b` for past), 18px left padding, Chakra Petch 700 17px company, mono role + date range, 14px detail line. Education is a bordered list: degree + school left, year right in `#64d5d2` for the most recent, `#8ba3a3` for older. All three degrees live here.
3. **My Journey / What I'm Building** — two columns, rule headers, 15px/1.7 `#9aa6a6` copy. Existing text verbatim.

Note: "Beyond the Code" from the current page was not in the mockup — carry it
over as a full-width section using the same rule header and body treatment.

### Project detail — `4a` — `_layouts/project.html`

Breadcrumb, status pill + mono meta (`STARTED FEB 2026 · 8 LOG ENTRIES`), 44px
h1, 17px description capped at 820px. Then grid `minmax(0,1fr) 320px`, 40px gap:

- **Main**: 16:9 bordered hero image; objective block (2px `#64d5d2` left border, `rgba(46,76,91,0.18)` fill, `0 6px 6px 0` radius, mono `OBJECTIVE` label, 15.5px/1.7 copy) replacing `.objective-box`; body content at 15.5px/1.8; then `Project Log` rule header and log rows.
- **Sidebar**: four modules — `TECH STACK` (chips, 7px gap, 18px padding), `RESOURCES` (rows with a teal `↗`, hover tint), `TIMELINE` (rows of an 11px squared marker — 2px border, filled `#64d5d2` with glow when complete — beside mono date, Chakra Petch phase, 13px detail), `ORIGIN` (the capstone cross-link).

Keep the existing programmatic-timeline Liquid; only the markup and styling change.

### Blog post — `4b` — `_layouts/post.html` (+ `_includes/post.html`)

Header goes **left-aligned**, not centered. Breadcrumb `LOG / <date>`, then a
measured 800px column: mono meta row (date · read time · project link, separated
by `#7d8a8a` dots), 42px h1, 18px description, tag links (Roboto Mono 11px, teal,
`rgba(100,213,210,0.35)` border, 3px radius) above a 1px `#1f2a2a` rule.

Content at 16.5px/1.85 `#c3cece`. `h2` inside content: Chakra Petch 700 26px,
10px bottom padding, 1px `#1f2a2a` bottom border. Code/terminal blocks:
`#0f1111`, 1px `#2e4c5b`, 6px radius, Roboto Mono 13px/1.7, `#8fd6d4` text with
`#8a9696` prompts and `#ffb300` warnings. Footer: `More from this project` rule
header, related log rows, then primary + ghost buttons.

The existing `.post-content` card (40px padding, heavy shadow) is dropped in
favor of the measured column; keep `.post-list .post-content` overrides for
excerpts.

### Course page — `4c` — `_layouts/course.html`

Breadcrumb `COURSEWORK / CST 363`, grid `minmax(0,1fr) 300px`. Left: kicker
`CST 363 · SPRING 2025`, 38px h1, lead, body with a bordered `h2`, then
`Work from this course` rule header + log rows. Right: `COURSE` module
(label/value rows for code, term, state pill), `SKILLS` chips, `NAVIGATE` module
with prev/next course links and an amber `ALL 12 COURSES`. The current layout
surfaces none of this metadata.

### Archives — `5a` — `archives.html`

Kicker `30 ENTRIES · 2024 — 2026`, h1 `Archives`, lead, then a tag filter strip
(all tags as chips, 8px gap) above a 1px rule. Then one block per year: 1px
border, 6px radius, a `#0f1111` header bar (Chakra Petch 700 22px 3px-tracked
`#64d5d2` year, right-side mono entry count), then rows.

Row markup matters: a **`<div>`** grid `100px minmax(0,1fr) auto`, 22px gap, 13px/20px
padding, `border-top: 1px solid rgba(46,76,91,0.28)`, hover tint. Date left,
**title as the only `<a>`**, tag chips right as sibling links. Do not wrap the row
in an anchor — nested `<a>` is invalid and the parser hoists the chips out of the
grid.

Replaces the `fa-ul` bulleted list with terminal icons.

### Tag page — `5b` — `_layouts/tag.html`

Breadcrumb `ARCHIVES / TAG`, kicker `N PROJECTS · N LOG ENTRIES`, h1 with a teal
`#` prefix. Then a `Projects` rule header with wide project cards (grid
`220px 1fr`, image left), a `Log Entries` rule header with count, log rows, and a
`← Back to archives` ghost button. Uses `page.tagged_docs` / `page.tagged_posts`
as today.

## Interactions & behavior

- **Nav active state** is route-derived. Use `page.url == '/'` for Home and `page.url contains '/projects/'` (likewise `/csumb/`) so detail pages keep their section highlighted — the current include only matches exact index URLs.
- **Mobile nav** keeps `toggleNavbar()` and the `responsive` class; do not rewrite the JS.
- **Transitions**: 0.25s ease on nav link color and border, button fills, and card border/background. 0.2s on row hover tints. No transforms — the old `translateX(5px)` row slide and `translateY(-5px)` card lift are both dropped.
- **No hover-dependent content.** Card details are always visible, so touch users get the same information.
- **Responsive**: nav switches to the toggle at 860px, layout collapses at 700px. See **Mobile** below for the full specification — several elements change treatment rather than just reflowing.

## Mobile (≤700px, verified at 390px)

Mockups: `6a` home, `6b` menu open, `6c` Coursework, `6d` project detail.
Minimum touch target is 44px; minimum type is 9.5px (mono meta) and 14px (body).

### Navbar

- Bar height 68px (from 86px), padding `0 20px`.
- Mark shrinks to 42×42px with a 10px radius, logo image 21px.
- Wordmark drops to 16px with 2.5px tracking. Caption becomes `ENGINEERING LOG` at **10px / 1.5px tracking** — do not go below 10px; if it will not fit, drop the caption rather than shrink it.
- Toggle is a 22×2px three-bar icon in `#8ba3a3`, turning `#64d5d2` when open, with 10px vertical padding for reach.
- Open menu: links stack at `min-height: 48px`, divided by `rgba(46,76,91,0.5)`. The active indicator rotates from a bottom underline to a **2px left bar** inset 10px top and 11px bottom, keeping the same `0 0 10px rgba(100,213,210,0.8)` glow.

### Layout

- All multi-column grids collapse to one column: page columns, card grids, Experience/Education, and the project/course sidebars. Sidebar modules move **below** the main content, not beside it.
- Page padding drops to 20px horizontal, 28px vertical.
- Buttons go full-width and stack with a 10px gap, 14px vertical padding.
- Type steps down: page h1 30px, detail h1 32px, section rule titles 18px, lead 15px, body 15px/1.75.

### Featured hero

The desktop side gradient does not work at 390px. Instead: a 4:3 image, a
bottom-up overlay (`to top, rgba(20,24,24,0.96) 22%, rgba(20,24,24,0.3) 75%`),
and the text block pulled up over the image bottom with `margin-top: -96px`.
Status pill gets a `rgba(15,17,17,0.7)` backing so it stays legible over
whatever the image is doing.

### Log rows

The date gutter is dropped entirely. Rows become a vertical stack: an inline
date + tag row (10.5px mono, 12px gap), then the title, then the excerpt. 18px
vertical padding, same `rgba(46,76,91,0.35)` top border.

### Course registry rows

The four-column grid restacks per row: code + state pill on one line
(`justify-content: space-between`), then the title, then the note. 16px/18px
padding, 7px gap. State pills at 9.5px minimum.

### Footer

Stacks and centers: logo (24px), then a two-line meta block (9.5px mono,
`line-height: 1.7`), then social links. **The social links need
`min-height: 44px; display: flex; align-items: center; padding: 0 14px`** — as
bare inline anchors they measure 13px tall and fail touch sizing. Same applies
to breadcrumb links on detail pages.

## State management

None. Static Jekyll output. The only client-side state is the mobile nav's
`responsive` class, which already exists.

## Assets

All already in the repo — nothing new to create.

| File | Use |
| --- | --- |
| `assets/branding/logo/ggbytes-transparent-g.png` | navbar mark (26px in a 52px frame) — `assets/branding/logo/` holds the full mark set; this is the path the shipped nav include uses |
| `assets/imgs/ggbytes/ggbytes-transparent-cropped.png` | footer lockup (26px tall) |
| `assets/imgs/project/*.png` | project cards and heroes |
| `assets/imgs/headshot.jpg` | About portrait |
| `assets/imgs/CSU_Monterey_Bay_seal.png`, `CSU-Longbeach_seal.png`, `CalPoly_Seal.png` | currently in the Education list; the redesigned list is text-only — keep or drop, your call |

Copies of the ones used in the mockup are in `assets/` inside this bundle so the
HTML renders offline.

Font Awesome stays loaded for the mobile menu icon and any in-content icons, but
the redesign removes it from every section header.

## Files

### In this bundle

| Path | What it is |
| --- | --- |
| `Home Redesign.dc.html` | the mockup canvas — every screen, all iterations |
| `code/_includes/nav.html` | paste-ready navbar |
| `code/index.html` | paste-ready home page |
| `code/assets/css/redesign.css` | paste-ready CSS block (append to `styles.css`) |
| `code/README.md` | the four paste steps for home + navbar |
| `assets/` | images the mockup references |
| `screenshots/` | rendered PNG of every screen (see table below) |

### Screenshots

| File | Screen | Mockup id |
| --- | --- | --- |
| `01-home.png` | Home | `2a` |
| `02-projects.png` | Projects | `3a` |
| `03-coursework.png` | Coursework | `3b` |
| `04-about.png` | About | `3c` |
| `05-project-detail.png` | Project detail | `4a` |
| `06-blog-post.png` | Blog post | `4b` |
| `07-course-page.png` | Course page | `4c` |
| `08-archives.png` | Archives | `5a` |
| `09-tag-page.png` | Tag page | `5b` |
| `10-mobile-home.png` | Home, 390px | `6a` |
| `11-mobile-menu.png` | Menu open, 390px | `6b` |
| `12-mobile-coursework.png` | Coursework, 390px | `6c` |
| `13-mobile-project-detail.png` | Project detail, 390px | `6d` |

Desktop shots are 1280px wide at 1×; mobile shots are 390px wide at 2×. They are
references for layout and color — take exact values from the token tables above,
not from the pixels.

### To change in the repo

| Path | Action |
| --- | --- |
| `_includes/head.html` | add the Chakra Petch link |
| `_includes/nav.html` | replace with `code/_includes/nav.html` |
| `index.html` | replace with `code/index.html` |
| `assets/css/styles.css` | append `redesign.css`; delete the old `.navbar*`, `.hero-card*`, `.hero-quote`, and both `.status-badge` blocks |
| `_includes/footer.html` | full-logo lockup + coordinates |
| `_includes/project-card.html` | static card |
| `projects.html` | page head + card grid |
| `csumb.html` | Coursework page, new order |
| `about.html` | bio/portrait, timeline, education list |
| `_layouts/project.html` | detail page markup |
| `_layouts/post.html` | left-aligned header, measured column |
| `_layouts/course.html` | course meta sidebar |
| `archives.html` | year blocks |
| `_layouts/tag.html` | tag page |
| `_config.yml` | add `flowchart.html` to the existing `exclude:` list |
| `_layouts/tags.html`, `_includes/header.html` | delete |
| `_projects/*.md` | normalize `status:` to active/planned/shipped/dormant |

Course codes, titles, and notes shown in the Coursework registry mockup are
placeholders from the CSUMB catalog — the real `_csumb/` collection data
replaces them.
