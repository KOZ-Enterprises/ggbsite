# CSS architecture

Source lives in `_sass/`. `assets/css/styles.scss` is a manifest of `@use` rules compiling to
`/assets/css/styles.css`, the one path `_includes/head.html` links. Jekyll compiles it natively — no gems, no npm, no build step.

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

All 45 `rgba()` values resolve from these tokens too, gradient stops included, so
the palette is the whole colour surface. Never use a text colour darker than
`$c-muted-low`; the type scale is fixed at three roles (`.page-title`,
`.page-lead`, `.page-body`); the status vocabulary is exactly `active`, `planned`,
`shipped`, `dormant`, plus `completed` / `in-progress` on course pages.

**If a colour you need is not in the table**, it is a design decision, not a
commit. Pick the nearest token, or get the palette extended deliberately. Three
literals predate the closed palette, each commented at the line — adding a fourth
without a comment is what this section exists to stop:

- `#f5f5f5` — `.social-icons a` in `_footer.scss`. Close to `$c-ink`, not equal.
- `#c3cece` — `.feature-hero-desc` in `_pages.scss`; and `#8fd6d4` —
  `.page-body pre, .page-body code` in `_content.scss`.

## Three breakpoints, and why only three

Defined in `_tokens.scss` and reached only through `respond-to()`:

| Mixin | Width | Meaning |
| --- | --- | --- |
| `respond-to(wide)` | 1024px | multi-column page layouts collapse below this |
| `respond-to(nav)` | 860px | navbar switches to the toggle (spec-mandated) |
| `respond-to(mobile)` | 700px | single column, mobile type, 44px touch targets |

The stylesheet used to have nine media queries at six widths, and the gap
between them was a real bug: the navbar switched to the hamburger at 860px but
`.detail-grid` did not collapse until 700px, so **701–860px rendered a mobile
navbar above a desktop two-column body**, and at 768px the 320px sidebar was
wider than the 318px main column. The 1024px tier closes that band.

No partial contains a bare `@media` — verify with
`grep -rn "@media" _sass/ | grep -v _tokens.scss`.

## The partials

Listed in manifest order: broad to specific, and load-bearing.

| File | Owns |
| --- | --- |
| `_tokens.scss` | variables only; emits no CSS |
| `_base.scss` | element defaults — selectors naming no class, plus `#main` |
| `_layout.scss` | page shells and grids: `.page-head`, `.detail-grid`, `.bio-grid` |
| `_nav.scss` | `.nav-shell` and everything inside it |
| `_components.scss` | reused on 2+ pages: `.card`, `.log-row`, `.btn-*`, `.side-*` |
| `_pages.scss` | used on exactly one page: `.intro-band`, `.registry`, `.xp-list` |
| `_content.scss` | Markdown prose — `.page-body` descendants, `.mermaid` |
| `_footer.scss` | `footer`, `.social-icons`, `.footer-mark` |
| `_utilities.scss` | standalone helpers, loaded last so they can override |

Responsive rules live **with** their component, nested via `respond-to()`: a
single mobile block at a 3,000-line file's end is what let the 768px gap hide.

## Where does a new rule go?

Work down the list and stop at the first match:

1. A colour or size literal → add a token, then reference it.
2. Selector names no class → `_base.scss`.
3. It is the navbar → `_nav.scss`. The footer → `_footer.scss`.
4. It positions blocks on the page → `_layout.scss`.
5. Two or more pages use it → `_components.scss`.
6. Exactly one page uses it → `_pages.scss`.
7. It styles Markdown output → `_content.scss`.
8. It is a hand-applied helper belonging to no component → `_utilities.scss`.

**Then check the cascade, because it can override the answer.** When two rules
tie on specificity, source order decides — and source order is the `@use` order.

The worked example is `.detail-grid-narrow`, which lives in `_layout.scss`
although rule 6 would send it to `_pages.scss`. It ships as
`class="detail-grid detail-grid-narrow"` and sets `grid-template-columns` at the
same (0,1,0) specificity as `.detail-grid`, so it wins purely on being later,
and must sit after the base rule and before the responsive collapse.
`_pages.scss` loads after `_layout.scss`, so a copy there would re-apply the
two-column track *below* both media queries and course detail pages would never
collapse — the main column measures 22px wide at 390px.

The opposite case: `.intro-actions .btn-primary` is (0,2,0) and beats the
(0,1,0) mobile `.btn-primary` rule in `_components.scss` on specificity, so
source order cannot touch it and `_pages.scss` is safe. Four similar rules rely
on the same reasoning. **If specificity decides the winner, follow the list; if
source order decides it, the rule is pinned where it is.**

## Collision sets

Six places in the partials carry a `COLLISION SET` comment — two or more rules
at equal specificity setting the same property, where reordering changes the
rendering. Find them with `grep -rn "COLLISION SET" _sass/`. Each states which
rules collide, at what specificity, and what breaks if they are swapped.

You have found a new one when two rules match the same element, tie on
specificity, and touch the same property — including shorthand against longhand
(`margin` against `margin-bottom` counts). Write the comment in the same shape,
immediately above the rule that must stay second.

## Naming

- `.page-*` for page shells, `.detail-*` for the two-column detail layout, and
  `.card` / `.wide-card` / `.log-row` / `.side-*` / `.btn-*` for components.
- State is a `data-status` attribute, never a class — see the vocabulary above.

## The dead-selector audit

`script/dead-css.py` reports class selectors defined in `_sass/` that appear in
no built page. `_site` is the oracle, so build first.

```bash
bundle exec jekyll build
python script/dead-css.py            # list them
python script/dead-css.py --count    # just the number
```

The count must be zero. The Lint workflow runs it on every pull request and
fails otherwise, so a dead selector is caught in the commit that creates it
rather than accumulating for a year. Two sets exempt live-but-invisible selectors:
`RUNTIME` (added by `assets/js/scripts.js`) and `TEMPLATE_FALLBACK` (a template
branch current content never takes). Comment any addition.
