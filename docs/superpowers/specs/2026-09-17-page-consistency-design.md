# Page Consistency Design

**Status:** approved for planning
**Date:** 2026-09-17
**Scope:** page anatomy and geometry across every archetype on garygigabytes.com

**Revision note:** this spec has been reviewed twice and rewritten twice.

The first review found the geometry had been measured with a grep matching only shorthand `margin`, which under-reported the inventory. The second review found that the rewrite fixing that had introduced fresh contradictions: the band's concrete values in Section 2 disagreed with the remapping table in Section 3, the enforcement rule in Section 6 rejected the two exemptions Section 4 grants, and the in-scope total was still quoted three different ways.

Two structural changes prevent a third recurrence. **Every value is stated exactly once** — the band's own values live in Section 2 and nowhere else, and the remapping table explicitly does not govern them. And **every exemption is a named selector**, not a category, because a linter reading `_sass/*.scss` cannot infer that one `margin` is type-to-type and another is a block margin.

The page-anatomy findings have been correct and unchanged across both reviews. Every defect found so far has been in the spacing scale and its enforcement.

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

**Spacing has no scale.** 28 distinct px values appear in `margin*`/`padding*` declarations, and a further 19 in `gap`/`row-gap`/`column-gap`. Counting every untokenised declaration of `margin`, `padding` or `gap` that carries a px value — comments stripped, horizontal-only components ignored — there are **182 governed declarations, of which 100 carry an off-scale vertical value**:

| Value | Count | Value | Count | Value | Count |
| --- | --- | --- | --- | --- | --- |
| 7 | 2 | 14 | 16 | 26 | 3 |
| 9 | 1 | 15 | 1 | 28 | 11 |
| 10 | 18 | 18 | 9 | 36 | 2 |
| 12 | 12 | 20 | 10 | 44 | 6 |
| 13 | 4 | 22 | 4 | 52 | 1 |

By partial: `_components` 32, `_pages` 32, `_layout` 16, `_nav` 6, `_base` 5, `_content` 5, `_footer` 4.

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

`.page-head`, `.detail-head` and `.intro-band` become one shared rule.

**These are the band's values. They are set here, not derived from the remapping table in Section 3, and the table does not govern them.** The band is a new shared surface, so its geometry is chosen rather than migrated; `.page-head`'s current 28px margin and `.detail-head`'s 32px are both superseded.

| | Shared band | `.intro-band` override |
| --- | --- | --- |
| padding, desktop | `$space-4` (32px) | `$space-6` (48px) |
| padding, mobile | `$space-3 $space-2` (24px 16px) | `$space-4 $space-2` (32px 16px) |
| margin-bottom, desktop | `$space-4` (32px) | `$space-5` (40px) |
| margin-bottom, mobile | `$space-3` (24px) | `$space-3` (24px) |
| border | 1px `$c-border` | inherited |
| radius | `$radius-surface` | inherited |
| grid | `$grid-pitch-band` (40px) | inherited |

Surface padding uses scale values on **both** axes. This is a deliberate exception to the horizontal exemption in Section 3, which exists for inline and navbar insets, not for the padding of a bordered surface.

**Width:** the band spans the content column on every page. No `max-width` is set on the band itself. `.page-head`'s current `max-width: 820px` is removed; the reading measure is carried by `.page-lead`, which already sets its own `max-width: 820px`. `.page-kicker` and `.page-title` have no measure of their own and will run the full column — at 1280px that is a 1132px band and a 1066px text column. No current title or kicker is close to that length, so nothing reflows; what visibly changes is the band *surface*, which is the intent.

Every element inside `.page-head` and `.detail-head` also narrows by the band's padding: 64px at desktop, 32px at mobile. At 390px the text column becomes 318px, down from 350px.

**`.intro-inner` is deleted** — both the wrapper in `index.html` and the rule in `_sass/_pages.scss`. Its 780px measure would otherwise sit 40px inside `.page-lead`'s 820px and make the home lead narrower than every other page's. Nothing depends on it: no descendant selector references it, and `.intro-kicker`/`.intro-actions` are top-level rules. Deleting the rule without the markup, or the reverse, fails the dead-selector gate.

**`.intro-kicker` is unified into `.page-kicker`.** The home band is the one page that already had a band, and it uses `.intro-kicker` (`index.html:9`), so the kicker hierarchy in Section 3 would otherwise never reach it. The two rules are identical but for `text-transform: uppercase` — which is a no-op, since the home kicker text is already uppercase in the markup — and their margin. `index.html` switches class and the `.intro-kicker` rule is deleted. `script/verify-redesign.sh` asserts on the kicker's text, not its class, so the gate is unaffected.

**The grid appears on the band and on the two media backplates, and nowhere else.** The backplates stay: they are fallbacks behind images, not decoration.

**Blog posts are the one exclusion.** A post is a reading surface and a textured, bordered band directly above body prose competes with it. `.post-head` shares no class with the others, so the exclusion costs nothing structurally. This is a decision, not an oversight — `/about/` was excluded from an earlier draft without an argument, and is included here.

### 3. Spacing scale

Six steps on an 8px rhythm, plus one tightly-scoped half-step. The 40px blueprint pitch is five steps, so texture and spacing share a grid.

```scss
$space-half:  4px;   // legal ONLY in the compound below, on the named selector
$space-1:     8px;
$space-2:    16px;
$space-3:    24px;
$space-4:    32px;
$space-5:    40px;
$space-6:    48px;
```

**What the scale governs:** the vertical axis of `margin`, `padding` and `gap`. The counts are in The Problem above and are not restated here. The band's own geometry is set in Section 2 and is not part of this.

**Exemptions are mechanical rules, not a list.** An earlier draft named individual selectors, on the reasoning that a linter cannot infer intent from source text. Testing a real checker against the tree showed that is true but unnecessary: three axis-and-magnitude rules subsume every selector that list named, and several it had missed. A rule a script applies uniformly beats a list someone has to maintain.

1. **Only the vertical axis is inspected.** For a shorthand, that is the first component (and the third, in the four-value form); for `gap` and `row-gap`, all of it; for `column-gap`, `-left` and `-right`, nothing. This alone exempts every horizontal inset — `padding: 0 20px` on the navbar has a vertical component of `0`, which carries no px literal at all.
2. **Values of 6px or less are optical and always allowed.** Chips, badges, hairline gaps and icon spacing live here, tuned against 10-11px type where an 8px floor would visibly fatten them. Every selector the earlier draft exempted by name — `.tech-chip`, `.status-tag`, `.status-badge`, `.side-timeline`, `.post-tagchip` and the rest — falls under this rule, as do nine more it had missed, including `ol`, `#main`, `.card-chips`, `.tl-content`, `.nav-wordmark`, `.post-page h2` and `.year-row`.
3. **Negative values are offsets, not rhythm**, and are skipped. The only one is `_sass/_pages.scss:124 margin-top: -96px`, a deliberate overlap.

Properties other than `margin`, `padding` and `gap` are never inspected: `border`, `letter-spacing` and gradient stops are not spacing.

For `border-radius` the rule is simpler still — no px literal at all, unless the line carries an `// OPTICAL` comment. Exactly two lines qualify, both named in Section 4.

**`$space-half` is legal in exactly one place.** It exists because `.page-kicker` sits 14px above the title while `.page-title` sits 18px above the lead — the kicker is bound tighter on purpose, and a flat 8px scale erases that distinction on the three elements this spec is most about.

The rule a script can apply: **`$space-half` may appear only inside the compound `$space-1 + $space-half` (12px), and only on `.page-kicker`'s `margin-bottom`.** A bare `12px` is rejected everywhere, including there. Anything else that wants a half-step is a spec change, not a judgement call at the call site.

That yields kicker→title 12px and title→lead 16px.

**Remapping.** Every off-scale value and its target. The band's values are excluded — see Section 2.

| Current | Count | New |
| --- | --- | --- |
| 7 | 2 | `$space-1` 8 |
| 9 | 1 | `$space-1` 8 |
| 10 | 18 | `$space-1` 8 |
| 12 | 12 | `$space-2` 16 |
| 13 | 4 | `$space-2` 16 — `.side-head`, `.side-row`, `.side-kv`, `.year-row`; these are sidebar rows, not chips, so the optical exemption does not reach them |
| 14 | 16 | `$space-2` 16, except `.page-kicker`'s `margin-bottom` → `$space-1 + $space-half` 12 |
| 15 | 1 | `$space-2` 16 |
| 18 | 9 | `$space-2` 16 |
| 20 | 10 | `$space-3` 24 where vertical; the horizontal-only cases are exempt above |
| 22 | 4 | `$space-3` 24 |
| 26 | 3 | `$space-3` 24 |
| 28 | 11 | `$space-3` 24 |
| 36 | 2 | `$space-4` 32 |
| 44 | 6 | `$space-5` 40 |
| 52 | 1 | the sole occurrence is `.intro-band`'s padding, set in Section 2 |

Values already on the scale (8, 16, 24, 32, 40, 48) do not move. Values of 6px or less are optical; the only ones in the governed set are the named exemptions above.

### 4. Radius scale

Three named tokens plus two documented px exemptions. (`.status-dot`'s `border-radius: 50%` is not a px literal and is outside the rule entirely.)

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
- reject any `border-radius` px literal, **except** the two exemptions named in Section 4, which are recognised by an `// OPTICAL` comment marker on the line rather than by line number

It reports `file:line` for each violation.

Enforcement is the point rather than an extra. 28 spacing values and seven radii accumulated precisely because the surrounding code always looked like documentation and nothing rejected a new value.

### 7. Documentation

`docs/css-architecture.md` is the normative reference and is updated in the same change. Specifically:

- the `_tokens.scss` row gains the spacing scale, the radius scale, the `$grid-pitch-band` / `$grid-pitch-media` tokens and the `blueprint-grid()` mixin
- the `_layout.scss` row gains the band
- the `_pages.scss` row loses `.intro-band` as a one-page component
- a new section states the page skeleton, the band rule, the two scales and their exemptions
- the enforcement gate is listed alongside the dead-selector audit

Merging `.page-head, .detail-head, .intro-band` into one rule in `_layout.scss` while `.intro-band` keeps padding and margin overrides in `_pages.scss` creates an equal-specificity shorthand collision resolved only by `@use` order. `docs/css-architecture.md` requires a `COLLISION SET` comment for exactly this, and one is written at the override.

## Success criteria

1. Every page has exactly one header band, except blog posts, which have none. (13 pages currently have no header element at all: `/about/` and the 12 course pages.)
2. Band width is identical across archetypes at a given viewport, and no band sets `max-width`.
3. The enforcement check reports zero violations, where a violation is an off-scale vertical `margin`/`padding`/`gap` value on a selector not in Section 3's exemption tables. Every currently off-scale declaration is either remapped by Section 3's table or named in one of its exemption tables; none is left to an implementer's judgement.
4. `grep -rn "border-radius:[^;]*px" _sass/` returns nothing but the two documented nav exemptions.
5. The blueprint grid appears on the band and on the two media backplates, nowhere else.
6. `.page-rule` and `.intro-inner` exist in neither templates nor Sass.
7. Text in the band meets AA against `$c-bg`: `.page-kicker`, `.page-title` and `.page-lead` at 4.5:1 or better, measured on `/` and on one index and one detail page. (`.page-kicker` exists on all three once `.intro-kicker` is unified per Section 2.) The grid is `rgba($c-accent, 0.045)` and should be negligible, but this site has already shipped one AA failure from stacked transparency.
8. The existing gates still pass: 26 build assertions, 0 dead selectors, no bare `@media` outside `_tokens.scss`, markdownlint clean, `bundle exec rubocop` clean.
9. No horizontal overflow at 390, 768, 861 or 1280 on any archetype.

## Deliberately not addressed

- **Colour and type.** Out of scope, as above.
- **Component inventory and interaction states.** Hover, focus and visited styling is consistent enough not to be the complaint.
- **The GG Swarm roadmap table.** Content presentation, tracked separately.
- **Small-component padding, horizontal insets, negative offsets.** Exempt by category, per Section 3.

## Risks

- **The spacing remap is a large visible change** — see the inventory in The Problem for the count and its distribution across partials. Both earlier drafts of this spec under-reported it, the first by a factor of two and the second by nearly half. It cannot be verified by the byte-identical comparison used for pure refactors. Verification is visual, per archetype, per viewport.
- **The enforcement check is the hard part of this work.** A naive implementation is over-inclusive (flagging chip padding and horizontal insets the spec calls correct) and simultaneously under-inclusive (blind to longhand, where most violations are). Both failure modes were present in the first draft of this spec. Budget for the check being harder than the remap, and test it against the known-correct exemptions before wiring it into CI.
- **Removing `.page-head`'s `max-width` widens three index headers.** Intended, but it is the change most likely to look wrong at first glance.
- **`about.html` restructuring touches a two-column layout.** Moving the heading out of `.bio-main` may affect how `.bio-grid` resolves.

## Supersedes

`docs/superpowers/plans/2026-09-17-blueprint-consistency-and-backlog.md` Task 1 predates this spec and conflicts with it on the band's radius (4px vs `$radius-surface`), padding (32/36 and 24/20, both off-scale), margin (28, off-scale), and `.intro-band`'s preserved 52/48. That plan's Task 1 must be rewritten against this spec before execution; its Tasks 2-5 are unaffected.
