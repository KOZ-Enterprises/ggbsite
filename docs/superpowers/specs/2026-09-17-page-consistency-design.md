# Page Consistency Design

**Status:** approved for planning
**Date:** 2026-09-17
**Scope:** page anatomy and geometry across every archetype on garygigabytes.com

**Revision note:** the first draft of this spec measured the geometry with a grep that matched only `margin: 0 0 Npx` and `margin-bottom: Npx`. It therefore reported 12 spacing values when there are 28, estimated the blast radius at "around eight rules" when it is 53 declarations, and omitted `gap` entirely — 55 declarations, 19 distinct values. The page-anatomy findings were correct and survive unchanged; every number in the geometry sections below has been re-measured. Two Success Criteria were self-defeating and are rewritten.

## The problem

The site's colour and type layers are tokenised, documented and working. Nothing below them was ever decided, so page structure and geometry accumulated per component. Three separate fixes in one session each surfaced another instance of the same gap, which is the signal that it is systemic rather than cosmetic.

Measured on the current build:

**Six header shapes do one job.**

| Page | Markup | Surface |
| --- | --- | --- |
| `index.html:7` | `.intro-band > .intro-inner` | bordered, blueprint grid, 52/48 padding |
| `projects.html:7`, `csumb.html:10`, `archives.html:12` | `.page-head` | none — `max-width: 820px; margin: 0 0 28px` |
| `_layouts/project.html:31`, `_layouts/tag.html:26` | `.detail-head` | none — `margin-bottom: 32px` |
| `_layouts/course.html:44` | bare kicker/title/lead, no wrapper, inside `.detail-main` | none |
| `about.html:7-11` | bare kicker/title/lead, no wrapper, inside `.bio-grid > .bio-main` | none |
| `_layouts/post.html:26` | `.post-head` | none |

**Spacing has no scale.** 28 distinct px values appear in `margin*`/`padding*` declarations: 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 28, 30, 32, 36, 40, 44, 48, 52, 96. A further 19 distinct values appear in `gap`/`row-gap`/`column-gap` across 55 declarations, 39 of them off any rhythm — including the structural ones (`.bio-grid` at 44px, the responsive collapses at 28px).

**Seven corner radii, five bypassing the tokens.** `$radius-card` 6px and `$radius-chip` 3px are defined. Raw literals in use: 12px (`.tech-chip`, `.nav-mark`), 10px (`.nav-mark` at mobile), 4px (`.intro-band`, `.feature-hero`, `.portrait-frame img`), 2px (`.tl-marker`), 1px (`.nav-icon-bar`). Plus `border-radius: 50%` on `.status-dot`.

`.tech-chip` carries dead geometry: its base rule sets 12px, but all four usages sit inside `.card-chips` or `.side-chips`, whose (0,2,0) rules set `$radius-chip`. The base rule never applies, so the site renders one shape while the source claims two. Removing it changes nothing visually — it deletes a value that misleads the next reader.

**The blueprint grid appears three times and is visible once.** `.card-media` and `.wide-card-media` carry it at 32px, but both are backplates behind project thumbnails; all seven projects have an `image:`, and `card-noimg` appears in zero built HTML pages. Only `.intro-band` ever shows it.

**Two separator mechanisms.** `.rule-header` (title + hairline + optional count) is used by seven templates. `.page-rule` by three.

## Scope

**In:** the page skeleton every archetype follows; which surfaces take a border, a grid and a radius; a spacing scale for structural rhythm; a radius scale; the separator rule; enforcement.

**Out:** the colour palette and the type scale. Both were refactored in September 2026, are documented in `docs/css-architecture.md`, and work.

## Decisions

### 1. The page skeleton

Every page resolves to the same three parts:

```text
HEADER BAND     kicker · title · lead          (+ actions on the home page)
BODY            archetype-specific
PAGE ACTIONS    back-link / primary action     (detail pages)
```

| Archetype | Header | Body | Actions |
| --- | --- | --- | --- |
| Home | band, large padding | featured hero + log list | — |
| Projects / Coursework / Archives | band | card grid or list | — |
| About | band | `.bio-grid` | — |
| Project / Course / Tag | band | `.detail-grid` (main + side) | yes |
| Blog post | **plain** `.post-head` | `.page-body` + related entries | yes |

`_layouts/course.html` and `about.html` gain the wrapper they never had. In both, the header goes **above** the grid, not inside a column, so the band spans the full content width on every page.

### 2. The band

`.page-head`, `.detail-head` and `.intro-band` become one shared rule:

- blueprint grid at `$grid-pitch-band` (40px)
- 1px `$c-border`
- `$radius-surface`
- `padding: $space-4` (32px); at mobile `$space-3 $space-2` (24px 16px)
- `margin: 0 0 $space-4` (32px)

`.intro-band` keeps only what differs: `padding: $space-6` (48px, from 52/48); at mobile `$space-4 $space-2` (32px 16px, from 28/20); `margin: 0 0 $space-5` (40px, unchanged).

**Width:** the band spans the content column on every page. No `max-width` is set on the band itself. `.page-head`'s current `max-width: 820px` is removed; the reading measure is carried by `.page-lead`, which already sets its own `max-width: 820px`. Index-page headers therefore widen; nothing narrows.

**`.intro-inner` is deleted** — both the wrapper in `index.html` and the rule in `_sass/_pages.scss`. Its 780px measure would otherwise sit 40px inside `.page-lead`'s 820px and make the home lead narrower than every other page's. Deleting the rule without deleting the markup, or the reverse, fails the dead-selector gate.

**The grid appears on the band and on the two media backplates, and nowhere else.** The backplates stay: they are fallbacks behind images, not decoration.

**Blog posts are the one exclusion.** A post is a reading surface and a textured, bordered band directly above body prose competes with it. `.post-head` shares no class with the others, so the exclusion costs nothing structurally. This is a decision, not an oversight — `/about/` was excluded from an earlier draft without an argument, and is included here.

### 3. Spacing scale

Six steps on an 8px rhythm, plus one tightly-scoped half-step. The 40px blueprint pitch is five steps, so texture and spacing share a grid.

```scss
$space-half:  4px;   // type-to-type inside a band or card ONLY
$space-1:     8px;
$space-2:    16px;
$space-3:    24px;
$space-4:    32px;
$space-5:    40px;
$space-6:    48px;
```

**What the scale governs:** block margins, padding on surfaces, and layout `gap`. Roughly 57 declarations.

**What it does not govern, stated as categories rather than a line list:**

- **Small-component optical padding** — chips, status pills and badges use 2-5px padding tuned to a 13px type size. An 8px floor would visibly fatten them. (~9-11 declarations)
- **Horizontal-only values** — the scale is vertical rhythm. `padding: 0 20px` on the navbar is horizontal inset, not rhythm. (~15 declarations)
- **Negative offsets** — `_sass/_pages.scss:124 margin-top: -96px` is a deliberate overlap, not spacing.
- **Properties other than margin, padding and gap** — `border`, `letter-spacing` and gradient stops are not spacing and are never inspected.

`$space-half` exists for one purpose: spacing between type elements inside a band or a card, where the 8px floor destroys deliberate hierarchy. Today `.page-kicker` sits 14px above the title and `.page-title` 18px above the lead — the kicker is bound tighter on purpose. Flattening both to 16px would remove that distinction on the three elements this spec is most about. It becomes kicker→title 12px (`$space-1 + $space-half`), title→lead 16px (`$space-2`). `$space-half` is not valid for block margins, surface padding or layout gap.

**Remapping.** Every value that moves, with its new token:

| Current | New | Current | New |
| --- | --- | --- | --- |
| 10 | `$space-1` 8 | 30 | `$space-4` 32 |
| 12 | `$space-1 + $space-half` 12 (type) / `$space-2` 16 (block) | 36 | `$space-4` 32 |
| 13 | exempt (optical) | 44 | `$space-5` 40 |
| 14 | 12 (type) / `$space-2` 16 (block) | 52 | `$space-6` 48 |
| 15 | `$space-2` 16 | 96 | exempt (negative offset) |
| 18 | `$space-2` 16 | 20 | `$space-3` 24 (vertical) / exempt (horizontal) |
| 22 | `$space-3` 24 | 26 | `$space-3` 24 |
| 28 | `$space-3` 24 | | |

Values already on the scale (8, 16, 24, 32, 40, 48) are unchanged. Values at or below 6px are optical and exempt.

### 4. Radius scale

Three named tokens plus two documented exemptions.

```scss
$radius-surface:  6px;   // cards, bands, modules, heroes, code blocks, media
$radius-chip:     3px;   // chips, status pills, timeline markers
$radius-mark:    12px;   // the nav logo frame at desktop
```

`$radius-card` is **renamed** to `$radius-surface`. It is referenced at 16 call sites — 5 in `_components.scss`, 5 in `_pages.scss`, 4 in `_content.scss`, 2 in `_layout.scss` — plus its definition in `_tokens.scss`. All are updated in the same change and the old name is retired, not aliased.

| Rule | Current | New |
| --- | --- | --- |
| `.tech-chip` | 12px | `$radius-chip` 3px — dead geometry, zero visual change |
| `.intro-band` | 4px | `$radius-surface` 6px |
| `.feature-hero` | 4px | `$radius-surface` 6px |
| `.portrait-frame img` | 4px | `$radius-surface` 6px |
| `.tl-marker` | 2px | `$radius-chip` 3px |
| `.nav-mark` | 12px | `$radius-mark` 12px — unchanged, now named |
| `.nav-mark` at mobile (`_sass/_nav.scss:84`) | 10px | **exempt** |
| `.nav-icon-bar` (`_sass/_nav.scss:263`) | 1px | **exempt** |
| `.status-dot` | `50%` | **exempt** — not a px literal |

The two exemptions are optical and tied to their own box sizes. The mobile mark steps 12px→10px alongside a 52px→42px box; forcing `$radius-mark` there would reshape the brand mark on phones, which is the outcome that token exists to prevent. `.nav-icon-bar` is a 22×2px hamburger bar — `$radius-chip` exceeds half its height.

### 5. Separators

`.rule-header` is the only separator. It carries a title, a hairline and an optional count, and seven templates already use it.

`.page-rule` is removed from `projects.html:17`, `_layouts/tag.html:40` and `archives.html:39`, and from the Sass.

Two of those three sit directly beneath the header, where a bordered band makes the hairline a second line doing the same job. **`archives.html` is different and is decided on its own terms:** there the rule separates the tag strip from the year list, not the header from the body. It is removed because `.tag-strip` already carries `margin-bottom: 24px` and `.year-block` is itself bordered, so the boundary survives without a dedicated line. If that proves too quiet in review, the correct replacement is a titled `.rule-header`, not a bare rule.

### 6. Enforcement

Tokens, documentation, and a build-failing check, following the shape of `script/dead-css.py`, which is already wired into `.github/workflows/lint.yml`.

The check must be **axis-aware, longhand-aware and comment-skipping**, or it is worse than nothing. Specifically it must:

- inspect `margin`, `padding` and `gap` in **both** shorthand and longhand forms — a check matching only `margin:` is blind to `margin-bottom:`, which is where most off-scale values live
- evaluate only the **vertical** axis of shorthand values, since horizontal insets are out of scope
- skip comments, so prose like `` // `margin: 0 auto; padding: 20px` `` is not a violation
- skip the exempt categories in Section 3 by rule, not by a hand-maintained list of line numbers
- reject any `border-radius` px literal outside the token definitions

It reports `file:line` for each violation.

Enforcement is the point rather than an extra. 28 spacing values and seven radii accumulated precisely because the surrounding code always looked like documentation and nothing rejected a new value.

### 7. Documentation

`docs/css-architecture.md` is the normative reference and is updated in the same change. Specifically:

- the `_tokens.scss` row gains the spacing scale, the radius scale and the `blueprint-grid()` mixin
- the `_layout.scss` row gains the band
- the `_pages.scss` row loses `.intro-band` as a one-page component
- a new section states the page skeleton, the band rule, the two scales and their exemptions
- the enforcement gate is listed alongside the dead-selector audit

Merging `.page-head, .detail-head, .intro-band` into one rule in `_layout.scss` while `.intro-band` keeps padding and margin overrides in `_pages.scss` creates an equal-specificity shorthand collision resolved only by `@use` order. `docs/css-architecture.md` requires a `COLLISION SET` comment for exactly this, and one is written at the override.

## Success criteria

1. Every page has exactly one header band, except blog posts, which have none. (13 pages currently have no header element at all: `/about/` and the 12 course pages.)
2. Band width is identical across archetypes at a given viewport, and no band sets `max-width`.
3. The enforcement check reports zero violations, where a violation is an off-scale vertical `margin`/`padding`/`gap` value outside the Section 3 exemption categories.
4. `grep -rn "border-radius:[^;]*px" _sass/` returns nothing but the two documented nav exemptions.
5. The blueprint grid appears on the band and on the two media backplates, nowhere else.
6. `.page-rule` and `.intro-inner` exist in neither templates nor Sass.
7. Text in the band meets AA against `$c-bg`: `.page-kicker`, `.page-title` and `.page-lead` at 4.5:1 or better, measured on a banded page. The grid is `rgba($c-accent, 0.045)` and should be negligible, but this site has already shipped one AA failure from stacked transparency.
8. The existing gates still pass: 26 build assertions, 0 dead selectors, no bare `@media` outside `_tokens.scss`, markdownlint clean, `bundle exec rubocop` clean.
9. No horizontal overflow at 390, 768, 861 or 1280 on any archetype.

## Deliberately not addressed

- **Colour and type.** Out of scope, as above.
- **Component inventory and interaction states.** Hover, focus and visited styling is consistent enough not to be the complaint.
- **The GG Swarm roadmap table.** Content presentation, tracked separately.
- **Small-component padding, horizontal insets, negative offsets.** Exempt by category, per Section 3.

## Risks

- **The spacing remap is a large visible change** — roughly 57 declarations, not the handful the first draft claimed. It cannot be verified by the byte-identical comparison used for pure refactors. Verification is visual, per archetype, per viewport.
- **The enforcement check is the hard part of this work.** A naive implementation is over-inclusive (flagging chip padding and horizontal insets the spec calls correct) and simultaneously under-inclusive (blind to longhand, where most violations are). Both failure modes were present in the first draft of this spec. Budget for the check being harder than the remap, and test it against the known-correct exemptions before wiring it into CI.
- **Removing `.page-head`'s `max-width` widens three index headers.** Intended, but it is the change most likely to look wrong at first glance.
- **`about.html` restructuring touches a two-column layout.** Moving the heading out of `.bio-main` may affect how `.bio-grid` resolves.

## Supersedes

`docs/superpowers/plans/2026-09-17-blueprint-consistency-and-backlog.md` Task 1 predates this spec and conflicts with it on the band's radius (4px vs `$radius-surface`), padding (32/36 and 24/20, both off-scale), margin (28, off-scale), and `.intro-band`'s preserved 52/48. That plan's Task 1 must be rewritten against this spec before execution; its Tasks 2-5 are unaffected.
