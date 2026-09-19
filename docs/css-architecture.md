# CSS architecture

Source lives in `_sass/`. `assets/css/styles.scss` is a manifest of `@use` rules compiling to `/assets/css/styles.css`, the one path `_includes/head.html` links. Jekyll compiles it natively — no gems, no npm, no build step.

## The palette is closed

Every colour is a variable in `_sass/_tokens.scss`. There are sixteen.

| Token | Hex | Use |
| --- | --- | --- |
| `$c-bg` | `#141818` | body, page ground |
| `$c-surface` | `#1a1e1e` | cards, navbar, sidebar modules |
| `$c-surface-deep` | `#0f1111` | year-block headers, code blocks |
| `$c-surface-hover` | `#1e2323` | card hover fill |
| `$c-border` | `#2e4c5b` | every 1px border |
| `$c-rule` | `#1f2a2a` | section hairlines |
| `$c-accent` | `#64d5d2` | primary accent, active state, links |
| `$c-accent-hover` | `#7fe3e0` | primary button hover |
| `$c-amber` | `#ffb300` | kickers, forward links, PLANNED |
| `$c-blue` | `#5bc0de` | tech chips, SHIPPED/COMPLETE |
| `$c-ink` | `#fafafa` | headings, primary text |
| `$c-body` | `#b9c4c4` | lead paragraphs, body copy |
| `$c-body-dim` | `#9aa6a6` | excerpts, secondary copy |
| `$c-muted` | `#8a9696` | mono meta, dates, counts |
| `$c-muted-alt` | `#8ba3a3` | inactive nav links, neutral status |
| `$c-muted-low` | `#7d8a8a` | placeholder labels, darkest allowed text |

All 41 `rgba()` values resolve from these tokens too, so the palette is the whole colour surface. Never use a text colour darker than `$c-muted-low`.

**If a colour you need is not in the table**, it is a design decision, not a commit. Three literals predate the closed palette, each commented at the line: `#f5f5f5` in `_footer.scss`, and `#c3cece` / `#8fd6d4` in `_pages.scss` / `_content.scss`. Adding a fourth without a comment is what this stops.

## Three breakpoints, and why only three

Defined in `_tokens.scss` and reached only through `respond-to()`:

| Mixin | Width | Meaning |
| --- | --- | --- |
| `respond-to(wide)` | 1024px | multi-column page layouts collapse below this |
| `respond-to(nav)` | 860px | navbar switches to the toggle (spec-mandated) |
| `respond-to(mobile)` | 700px | single column, mobile type, 44px touch targets |

These replaced nine media queries at six widths that left real gaps. No partial contains a bare `@media`; verify with `grep -rn "@media" _sass/ | grep -v _tokens.scss`.

## The page skeleton

Every page resolves to the same three parts, in order:

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

`.page-head`, `.detail-head` and `.intro-band` share one rule in `_layout.scss`; `.intro-band` overrides only its larger padding and margin, in `_pages.scss`. Blog posts are the one deliberate exclusion: a textured band above body prose would compete with it rather than frame it.

## The partials

Listed in manifest order: broad to specific, and load-bearing.

| File | Owns |
| --- | --- |
| `_tokens.scss` | variables, the spacing/radius/grid-pitch scales and `blueprint-grid()` — emits no CSS of its own; a mixin emits only where used |
| `_base.scss` | element defaults — selectors naming no class, plus `#main` |
| `_layout.scss` | page shells and grids: the header band, `.detail-grid`, `.bio-grid` |
| `_nav.scss` | `.nav-shell` and everything inside it |
| `_components.scss` | reused on 2+ pages: `.card`, `.log-row`, `.btn-*`, `.side-*` |
| `_pages.scss` | used on exactly one page: `.registry`, `.xp-list`, and `.intro-band`'s override of the shared band |
| `_content.scss` | Markdown prose — `.page-body` descendants, `.mermaid` |
| `_footer.scss` | `footer`, `.social-icons`, `.footer-mark` |
| `_utilities.scss` | standalone helpers, loaded last so they can override |

Responsive rules live **with** their component, nested via `respond-to()`: a single mobile block at a 3,000-line file's end is what let the 768px gap hide.

## Two geometry scales

`_tokens.scss` also holds the geometry that used to accumulate per component.

**Spacing:** six steps on 8px, `$space-1`…`$space-6` (8px–48px), plus `$space-half` (4px), legal **only** in the compound `$space-1 + $space-half` and **only** on `.page-kicker`'s margin — so the kicker binds tighter to the title than the title does to the lead.

**Radius:** `$radius-surface` (6px, cards/bands/media), `$radius-chip` (3px, chips/pills/markers), `$radius-mark` (12px, the nav logo frame), plus exactly two `// OPTICAL`-marked px literals in `_nav.scss` where the value tracks a sibling dimension instead — `grep -rn "border-radius:[^;]*px" _sass/` finds exactly these two.

**Grid:** `blueprint-grid()` appears in exactly three places, the header band (`$grid-pitch-band`, 40px) and the two media backplates `.card-media` / `.wide-card-media` (`$grid-pitch-media`, 32px), and nowhere else.

Both scales are enforced mechanically (see Enforcement below), not by a list of exempt selectors — an earlier spec draft named ten by hand, and the mechanical rules subsumed all ten plus nine it had missed. Full rules: `docs/superpowers/specs/2026-09-17-page-consistency-design.md`.

## Where does a new rule go?

Work down the list, stop at the first match: a colour or size literal → add a token; selector names no class → `_base.scss`; navbar → `_nav.scss`, footer → `_footer.scss`; positions blocks on the page → `_layout.scss`; used on 2+ pages → `_components.scss`; used on exactly one page → `_pages.scss`; styles Markdown output → `_content.scss`; a hand-applied helper belonging to no component → `_utilities.scss`.

**Then check the cascade — it can override the answer.** Tied specificity is broken by source order (the `@use` order): `.detail-grid-narrow` ties `.detail-grid` on specificity, so it stays in `_layout.scss` rather than `_pages.scss` purely to load later. If specificity decides the winner, follow the list; if source order decides it, the rule is pinned where it is.

Seven places carry a `COLLISION SET` comment: two tied rules touch the same property (shorthand against longhand counts, e.g. `margin` vs. `margin-bottom`) and reordering would change the render — `grep -rn "COLLISION SET" _sass/`. Comment a new one the same way, immediately above the rule that must stay second.

## Naming

- `.page-*` for page shells, `.detail-*` for the two-column detail layout, and `.card` / `.wide-card` / `.log-row` / `.side-*` / `.btn-*` for components.
- State is a `data-status` attribute, never a class: `active`, `planned`, `shipped`, `dormant`, plus `completed` / `in-progress` on course pages.

## Enforcement

Two build-failing scripts, both wired into the Lint workflow on every pull request.

**`script/dead-css.py`** reports class selectors defined in `_sass/` that appear in no built page (`_site` is the oracle, so build first). Two sets exempt live-but-invisible selectors: `RUNTIME` (added by `assets/js/scripts.js`) and `TEMPLATE_FALLBACK` (a template branch current content never takes) — comment any addition.

```bash
bundle exec jekyll build
python script/dead-css.py --count    # must be 0
```

**`script/geometry.py`** rejects geometry that bypasses the two scales above, applying three mechanical rules to every `margin`/`padding`/`gap` and `border-radius` declaration in `_sass/`: only the vertical axis is inspected; 6px or less is optical and always allowed; negatives are offsets and skipped. A violation the scale should legitimately allow is a spec change — edit the design spec's rules and this doc, not the script's constants.

```bash
python script/geometry.py --count    # must be 0
```
