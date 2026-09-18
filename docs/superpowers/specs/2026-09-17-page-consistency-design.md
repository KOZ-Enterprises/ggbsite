# Page Consistency Design

**Status:** approved for planning
**Date:** 2026-09-17
**Scope:** page anatomy and geometry across every archetype on garygigabytes.com

## The problem

The site's colour and type layers are tokenised, documented and working. Nothing below them was ever decided, so page structure and geometry accumulated per component instead of being designed. Three separate fixes in one session each surfaced another instance of the same underlying gap, which is the signal that the gap is systemic rather than cosmetic.

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

**Twelve block-spacing values with no scale:** 8, 10, 14, 16, 18, 24, 28, 32, 36, 40, 44, 48.

**Five corner radii, three of which bypass the tokens:** `$radius-card` 6px and `$radius-chip` 3px are defined, but `12px`, `4px` and `2px` appear as raw literals. `.tech-chip` is the clearest symptom — it renders as a 12px pill in its base rule and a 3px near-square under `.card-chips` and `.side-chips`. One component, two shapes, depending where it lands.

**The blueprint grid appears three times and is visible once.** `.card-media` and `.wide-card-media` carry it at 32px, but both are backplates behind project thumbnails; all seven projects have an `image:`, and `card-noimg` appears in zero built pages. Only `.intro-band` on the home page ever shows it, which is why the texture reads as a home-page quirk rather than a site signature.

**Two separator mechanisms.** `.rule-header` (title + hairline + optional count) is used by seven templates. `.page-rule` is used by three, and in every case sits immediately below the header.

## Scope

**In:** the page skeleton every archetype follows; which surfaces take a border, a grid and a radius; a spacing scale; a radius scale; the separator rule; enforcement.

**Out:** the colour palette and the type scale. Both were refactored in September 2026, are documented in `docs/css-architecture.md`, and work. Re-opening them would churn correct work.

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

Two templates gain the wrapper they never had: `_layouts/course.html` and `about.html`. In both, the header is placed **above** the grid rather than inside a column, so the band spans the full content width on every page. Today the course header sits inside `.detail-main` and the about header inside `.bio-main`; left there, their bands would be column-width while every other band is full width.

### 2. The band

`.page-head`, `.detail-head` and `.intro-band` become one shared rule:

- blueprint grid at `$grid-pitch-band` (40px)
- 1px `$c-border`
- `$radius-surface`
- padding and margin from the spacing scale

`.intro-band` keeps only what differs — its larger padding and margin. It does not restate the border or the grid.

**The grid appears on the band and nowhere else.** The two 32px media backplates stay as they are: they are fallbacks behind images, not decoration, and they are never seen while every project has an image.

**Blog posts are the one exclusion.** A post is a reading surface and a textured, bordered band directly above body prose competes with it. `.post-head` shares no class with the others, so the exclusion costs nothing structurally. The post header also carries date and read-time metadata, which suits a plain treatment.

This exclusion is a decision, not an oversight. `/about/` was excluded in an earlier draft without an argument; that was the oversight, and `/about/` is included here.

### 3. Spacing scale

Six steps on an 8px rhythm. The 40px blueprint pitch is five steps, so the texture and the spacing share a grid.

```scss
$space-1:  8px;
$space-2: 16px;
$space-3: 24px;
$space-4: 32px;
$space-5: 40px;
$space-6: 48px;
```

Remapping of the twelve current values. Nothing moves more than 4px.

| Current | New | Current | New |
| --- | --- | --- | --- |
| 8 | `$space-1` 8 | 28 | `$space-3` 24 |
| 10 | `$space-1` 8 | 32 | `$space-4` 32 |
| 14 | `$space-2` 16 | 36 | `$space-4` 32 |
| 16 | `$space-2` 16 | 40 | `$space-5` 40 |
| 18 | `$space-2` 16 | 44 | `$space-5` 40 |
| 24 | `$space-3` 24 | 48 | `$space-6` 48 |

The scale governs **block-level vertical rhythm** — margins between blocks and padding on surfaces. It does not govern padding inside small components such as chips and status pills, whose 2-5px values are optical rather than structural.

### 4. Radius scale

Three named tokens, replacing five values.

```scss
$radius-surface:  6px;   // cards, bands, modules, heroes, code blocks, media
$radius-chip:     3px;   // chips, status pills, timeline markers
$radius-mark:    12px;   // the nav logo frame, and only that
```

| Rule | Current | New |
| --- | --- | --- |
| `.tech-chip` | 12px | `$radius-chip` 3px |
| `.intro-band` | 4px | `$radius-surface` 6px |
| `.feature-hero` | 4px | `$radius-surface` 6px |
| `.portrait-frame img` | 4px | `$radius-surface` 6px |
| `.tl-marker` | 2px | `$radius-chip` 3px |
| `.nav-mark` | 12px | `$radius-mark` 12px (unchanged, now named) |

`.tech-chip` moving to 3px resolves the contradiction with `.card-chips .tech-chip` and `.side-chips .tech-chip`, which already use `$radius-chip`. `$radius-mark` exists so the nav logo frame keeps its shape: the G mark was drawn to sit in that frame, and flattening it to 6px would change the brand mark on every page.

### 5. Separators

`.rule-header` is the only separator. It carries a title, a hairline and an optional count, and seven templates already use it.

`.page-rule` is removed from `projects.html`, `archives.html` and `_layouts/tag.html`, and from the Sass. All three of its uses sit directly beneath the header; once that header is a bordered band, the hairline is a second line doing the same job about thirty pixels below the first.

### 6. Enforcement

Tokens, documentation, and a build-failing check.

A script scans `_sass/*.scss` and fails the build on:

- a `margin` or `padding` px literal that is not on the 8px scale
- any `border-radius` px literal

It reports `file:line` for each violation and carries an exemption list for genuine one-offs, following the shape of `script/dead-css.py`, which is already wired into `.github/workflows/lint.yml` as a build-failing gate.

Enforcement is the point rather than an extra. Twelve margins and five radii accumulated precisely because the surrounding code always looked like documentation and nothing rejected a new value.

## Success criteria

1. Every page has exactly one header band, except blog posts, which have none.
2. Band width is identical across archetypes at a given viewport.
3. `grep -rnE "(margin|padding):[^;]*[0-9]+px" _sass/` returns only values on the 8px scale or listed exemptions.
4. `grep -rn "border-radius:[^;]*px" _sass/` returns nothing outside `_tokens.scss`.
5. The blueprint grid appears on the band and on the two media backplates, nowhere else.
6. `.page-rule` does not exist in templates or Sass.
7. The existing gates still pass: 26 build assertions, 0 dead selectors, no bare `@media` outside `_tokens.scss`, markdownlint clean.
8. No horizontal overflow at 390, 768, 861 or 1280 on any archetype.

## Deliberately not addressed

- **Colour and type.** Out of scope, as above.
- **Component inventory and interaction states.** Hover, focus and visited styling is consistent enough not to be the complaint; revisiting it would widen this into a full design-system rewrite.
- **The GG Swarm roadmap table.** Formatting is tracked separately in the implementation plan; it is content presentation, not page anatomy.
- **Small-component padding.** Chips and pills use 2-5px optical padding that the 8px scale would coarsen for no gain.

## Risks

- **The spacing remap is a visible change.** Around eight rules shift by 2-4px. Individually imperceptible, collectively a real diff, and it cannot be verified by the byte-identical comparison used for pure refactors. Verification is visual and per-viewport.
- **The enforcement script needs an exemption list from day one.** 1px borders, `letter-spacing`, and the blueprint grid's own 1px gradient stops are legitimate literals. An over-strict first version will fail the build on correct code and erode trust in the gate.
- **`about.html` restructuring touches a two-column layout.** Moving the heading out of `.bio-main` may affect how `.bio-grid` resolves; it needs checking rather than assuming.
