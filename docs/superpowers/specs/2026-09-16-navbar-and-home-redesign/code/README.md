# Paste-in guide — 2a layout + new navbar

Four edits. Nothing else in the repo needs to change.

## 1. Font — `_includes/head.html`

The design uses Chakra Petch AND Roboto Mono. Neither is currently loaded —
the existing link is Open Sans + Roboto Flex + Roboto, so every mono meta line
is falling back to a system monospace. Add both:

```html
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap" rel="stylesheet">
```

## 2. `_includes/nav.html`

Replace the whole file with `code/_includes/nav.html`.

The mobile toggle still calls `toggleNavbar()` and still toggles `responsive` on
`#myNavbar`, so `assets/js/scripts.js` keeps working as-is.

## 3. `index.html`

Replace the whole file with `code/index.html`. It drops the quote hero card and
the unbalanced two-column block, and uses: intro band → featured project hero →
project log list → pagination.

The featured hero reads `image`, `status`, `description`, and `title` from the
`ggswarm` project front matter, same lookup you had.

## 4. `assets/css/styles.css`

Append all of `code/assets/css/redesign.css`, then delete these now-dead blocks
from the top part of the file so nothing fights it:

- `.navbar`, `.navbar .nav-links`, `.navbar a`, `.navbar a.active, .navbar a:hover`,
  `.navbar .icon`, the `@media (max-width:700px)` navbar block, `.navbar .logo`,
  `.navbar .logo img`
- `.hero-card`, `.hero-card p`, `.hero-quote`
- both old `.status-badge` rules (there are two; the new file has one)

`nav { position: sticky }` stays — the new bar is sticky too.

## 5. Status tags

Vocabulary is now fixed at four values. Set `status:` in each project's front
matter to exactly one of:

| value | meaning |
| --- | --- |
| `active` | being worked on now (teal) |
| `planned` | scoped, not started (amber) |
| `shipped` | done and running (blue) |
| `dormant` | paused, may return (grey) |

Both `.status-tag` (hero) and `.status-badge` (project cards) style off
`data-status`, so they stay identical everywhere. Anything outside the four
values falls back to the grey neutral.

## 6. Footer — full logo + coordinates

The navbar uses the G mark plus a type wordmark, so the full lockup lives in the
footer instead (one appearance per page). In `_includes/footer.html`, replace the
copyright line with:

```html
<div class="footer-mark">
  <img src="/assets/imgs/ggbytes/ggbytes-transparent-cropped.png" alt="Gary Gigabytes" />
  <p>&#169; {{ 'now' | date: "%Y" }} &middot; BUILT IN LONG BEACH, CA &middot; 33.77&deg;N 118.19&deg;W</p>
</div>
```

CSS for it is in `redesign.css` (`.footer-mark`).
