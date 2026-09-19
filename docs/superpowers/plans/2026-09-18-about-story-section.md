# About Story Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one narrative coda to `/about/` telling the site's through-line, without rewriting a single existing block or adding a line of CSS.

**Architecture:** One new `<section class="about-wide">` appended to `about.html`, assembled from classes the page already uses (`.rule-header`, `.rule-title`, `.rule-line`, `.page-lead`). The only edit to existing markup is relocating the LinkedIn call-to-action paragraph, so the page still ends on an invitation rather than on the story. No Sass, no JavaScript, no layout change.

**Tech Stack:** Jekyll 4.4.1, Liquid, plain HTML. Verification uses the two Python gates already wired into CI and the local headless Chromium on `127.0.0.1:9222`.

**Spec:** No separate spec. This plan is the artifact; the design was settled in brainstorming on 2026-09-18 and the decisions are recorded under "Decisions" below.

## Global Constraints

- **No em dashes.** `vault/gary/voice.md` bans them as an AI tell. `about.html` contains zero today; it must still contain zero after this change.
- **Existing classes only, zero new CSS.** `python3 script/geometry.py --count` must stay `0`, and a hand-written `padding` or `border-radius` fails the build. This is why the new section reuses `.about-wide` / `.rule-header` / `.page-lead` rather than introducing a class.
- **Curated material only.** This page is read by recruiters. Out of bounds: childhood and kindergarten, the poker table at 15, the 2011 Greek festival, ADHD, drinking, and the strip-club thread. In bounds: the failed programming class, the decade as a mechanical engineer, the low-point job, solo travel, and the engineering.
- **The former employer is not named in the narrative.** `Experience` two blocks above still names Cunico Corporation, so the reader can connect the dots; what anonymity buys is that the prose attaches no editorial about a named company to it. Do not "helpfully" add the name back.
- **The copy is the deliverable, not a sketch.** The paragraphs in Task 1 are final. Do not rewrite them to taste. If they read wrong, stop and raise it rather than improving them in place.

## Decisions

Settled with Gary on 2026-09-18 before this plan was written. Do not revisit during execution.

| Decision | Choice | Why |
| --- | --- | --- |
| Surface | Public About page | It is the page a recruiter reads, and it was already part-narrative |
| Shape | Add one section; leave the existing blocks alone | Lowest-risk change to a page whose layout was just stabilised by the page-consistency work |
| Placement | **Coda**, after "Beyond the Code" | The through-line lands last, which is where an essay earns its thesis |
| Spine | "The gap between what people predict and what actually happens" | Already the site's stated through-line |
| Length / register | ~4 short paragraphs, dry and understated | Matches `voice.md`; the page's other narrative blocks run 80–110 words each |
| Low-point framing | Anonymous quality-control job, no bitterness | Names no employer, assigns no blame, keeps the beat |

**One deliberate exception to "leave everything alone":** the LinkedIn call-to-action currently closes "Beyond the Code", so appending a coda would strand it mid-page. It moves verbatim to the end of the new section. Nothing else in the existing 144 lines changes.

## File Structure

| File | Responsibility |
| --- | --- |
| `about.html` | The only file modified. Gains one section (lines 145+); loses the CTA paragraph from "Beyond the Code" (lines 139–143). |
| `_site/about/index.html` | Build output, regenerated. Read-only for verification. |

No other file is in scope. `_sass/`, `_includes/`, `_layouts/` and the two Python gates are untouched.

---

### Task 1: Add the "The Long Way Here" coda

**Files:**

- Modify: `about.html:139-144` (remove the CTA paragraph, append the new section)

**Interfaces:**

- Consumes: classes already defined in `_sass/_pages.scss` and `_sass/_components.scss` — `.about-wide`, `.rule-header`, `.rule-title`, `.rule-line`, `.page-lead`. All four appear elsewhere on this page.
- Produces: nothing other tasks consume. Task 2 reads `_site/about/index.html`.

**Baseline, measured before any edit** (re-confirm in Step 1, do not trust these numbers):

```text
em dashes in about.html : 0
<h1> count              : 1
<h2> count              : 5
<section> count         : 6
```

- [ ] **Step 1: Confirm the baseline**

```bash
cd ~/ggbsite
bundle exec jekyll build --quiet
grep -c '—' about.html          # expect 0
grep -c '<h2' about.html        # expect 5
grep -c '<section' about.html   # expect 6
```

- [ ] **Step 2: Remove the call-to-action paragraph from "Beyond the Code"**

It is the final `<p class="page-lead">` of that section. Delete exactly this, leaving the section's closing `</section>` in place:

```html
    <p class="page-lead">
        If you want to talk robotics, history, K-pop, or soccer, feel free to
        <a href="https://www.linkedin.com/in/garykuepper/" target="_blank" rel="noopener">connect with me on
            LinkedIn</a>.
    </p>
```

This is a relocation, not a deletion. Step 3 puts the same markup back at the end of the new section, byte for byte.

- [ ] **Step 3: Append the new section**

Append to the end of `about.html`, after the existing `</section>` that closes "Beyond the Code". The last paragraph is the relocated CTA, unchanged.

```html
<section class="about-wide">
    <div class="rule-header">
        <h2 class="rule-title">The Long Way Here</h2>
        <span class="rule-line"></span>
    </div>
    <p class="page-lead">
        I failed a programming class in high school and treated it as a verdict. It seemed reasonable at the
        time. I spent the next decade as a mechanical engineer, which is a perfectly good career for someone
        whose worst grade came from a programming class. I was good at it, and being good at it made it easy
        not to argue with the verdict.
    </p>
    <p class="page-lead">
        Then I took a quality control job I&rsquo;ll describe politely, certifying pipe fittings for submarine
        programs. It paid the bills. It was also narrow, with a ceiling low enough to touch, and I was good at
        that one too. Being good at something you don&rsquo;t want to spend a life on is its own kind of
        problem, and it took me about two years to name it.
    </p>
    <p class="page-lead">
        So I stopped treating the rest as optional. I went back to school for a computer science degree at
        CSU Monterey Bay, nights and weekends around a full-time job, and finished in 2026. The ambition was
        not new. Nobody had asked for it, and I had never given myself permission to act on it.
    </p>
    <p class="page-lead">
        The same instinct runs outside of work. I travel alone on purpose: no committee, no compromises, an
        itinerary I build as I go, and a standing rule that history is better confronted than skipped. Rigor
        and wanderlust aren&rsquo;t opposites. They&rsquo;re one trait pointed at different problems. Most of
        what I do comes down to closing the gap between what a model predicts and what actually happens, and
        I&rsquo;ve been doing that in one form or another since I decided a bad grade was not a verdict.
    </p>
    <p class="page-lead">
        If you want to talk robotics, history, K-pop, or soccer, feel free to
        <a href="https://www.linkedin.com/in/garykuepper/" target="_blank" rel="noopener">connect with me on
            LinkedIn</a>.
    </p>
</section>
```

Notes on the markup, so it is not "corrected" during review:

- Apostrophes are `&rsquo;` entities, matching every other paragraph on the page.
- P4 uses colons, periods and a comma splice rather than em dashes, per the constraint.
- 271 words across four paragraphs. P1 64, P2 67, P3 54, P4 86.

- [ ] **Step 4: Build and run both gates**

```bash
bundle exec jekyll build --quiet
python3 script/geometry.py --count   # expect 0
python3 script/dead-css.py --count   # expect 0
```

`geometry.py` is the guard that matters here: it rejects off-scale vertical `margin`/`padding`/`gap` and any unnamed `border-radius`. A `0` proves the new section added no geometry of its own. **If either count is non-zero, do not proceed and do not add an exemption** — the section was built from the wrong classes.

- [ ] **Step 5: Verify the structure changed and nothing else did**

```bash
grep -c '<h2' about.html          # expect 6  (was 5)
grep -c '<section' about.html     # expect 7  (was 6)
grep -c '—' about.html            # expect 0
grep -c 'linkedin.com/in/garykuepper' about.html   # expect 1, not 2
```

The last check is the one that catches a botched relocation: appending the section without deleting the original paragraph leaves two identical CTAs on the page, one of them buried mid-article.

Confirm the four pre-existing section titles survive:

```bash
grep -o '<h2 class="rule-title">[^<]*</h2>' about.html
```

Expected, in order: `Experience`, `Education`, `My Journey`, `What I&rsquo;m Building`, `Beyond the Code`, `The Long Way Here`.

- [ ] **Step 6: Verify the text is in the rendered DOM, not just the source**

Source-correct and page-correct are different claims. Serve the site and read the built page's text:

```bash
bundle exec jekyll serve --detach --port 4000
sleep 3
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:4000/about/   # expect 200
```

Then, against `http://127.0.0.1:4000/about/` in the local headless Chromium (CDP on `127.0.0.1:9222`), assert:

```js
// Scope every query to #main. The footer carries its own LinkedIn link and
// trailing text, so an unscoped body-level assertion fails against a correct page.
const main = document.querySelector('#main');
const s = [...main.querySelectorAll('section.about-wide')].pop();
s.querySelector('h2').textContent.trim();          // "The Long Way Here"
s.querySelectorAll('p.page-lead').length;          // 5
s.innerText.includes('closing the gap between what a model predicts and what actually happens'); // true
main.querySelectorAll('a[href*="linkedin.com/in/garykuepper"]').length;  // 1
main.innerText.trim().endsWith('LinkedIn.');       // true — the content still ends on the invitation
document.querySelectorAll('a[href*="linkedin.com/in/garykuepper"]').length; // 2 — the footer adds one
```

- [ ] **Step 7: Check overflow at the four widths**

The page-consistency spec makes this a standing success criterion. At viewport widths 390, 768, 861 and 1280, assert no horizontal overflow:

```js
document.documentElement.scrollWidth <= window.innerWidth; // true at all four
```

Also confirm the new section renders its heading at the same size and rule length as `Beyond the Code` immediately above it. If the two section headers differ visually, a class was mistyped.

- [ ] **Step 8: Stop the server**

```bash
kill %1 2>/dev/null || pkill -f 'jekyll serve'
```

- [ ] **Step 9: Commit**

```bash
git add about.html
git commit -m "content(about): add the long way here coda"
```

---

### Task 2: Publish and verify the live page

**Files:**

- No file changes. This task ships the previous one and verifies the result.

**Interfaces:**

- Consumes: the commit from Task 1.
- Produces: a verified live `/about/`.

- [ ] **Step 1: Confirm the local branch is green before publishing**

```bash
git status --short            # expect only '?? assets/imgs/cyrus/' — untracked, unrelated, leave it
git log --oneline -1
python3 script/geometry.py --count   # expect 0
python3 script/dead-css.py --count   # expect 0
```

Do **not** commit or delete `assets/imgs/cyrus/` as part of this work. It is a separate, untracked asset drop.

- [ ] **Step 2: Publish**

`deploy.yml` triggers on push to `publish`. That is a production deploy to Cloud Run, so confirm with Gary before running it.

```bash
git push origin HEAD:publish
```

- [ ] **Step 3: Wait for the deploy to finish**

```bash
gh run list --branch publish --limit 3
gh run watch "$(gh run list --branch publish --limit 1 --json databaseId --jq '.[0].databaseId')"
```

Expected: the `Deploy` workflow concludes `success`. A `failure` here leaves the previous revision serving; check `gh run view --log-failed` before retrying.

- [ ] **Step 4: Verify live, cache-busted**

Cloudflare has served stale HTML on this site before, which is why an earlier commit had to re-point screenshot URLs. Fetch with a cache-busting query first:

```bash
curl -s "https://garygigabytes.com/about/?cb=$(date +%s)" | grep -c 'The Long Way Here'   # expect 1
```

Then confirm the rendered page, not just the markup:

```text
https://garygigabytes.com/about/?cb=<timestamp>
```

Assert: the section heading reads "The Long Way Here"; the phrase "closing the gap between what a model predicts and what actually happens" is present; exactly one LinkedIn link sits inside the main content (the footer adds its own, so a page-wide count of 2 is correct); the main content's final visible text is the invitation sentence; `Experience`, `Education`, `My Journey`, `What I&rsquo;m Building` and `Beyond the Code` all survive with their content unchanged.

If the live page still shows the old version after a successful deploy, the cause is the CDN cache, not the build. Re-fetch with a fresh `cb` value before investigating anything else.

- [ ] **Step 5: Confirm the sharing card is unaffected**

`about.html` sets no front matter `description`, so `_includes/head.html` falls back to `default_desc` (103 characters, already over LinkedIn's 100-character floor). Verify the page's `og:description` is unchanged from before this change rather than rewritten.

---

## Deliberately not addressed

- **A page-specific `description` for the sharing card.** The About page ships the generic site description to LinkedIn. A narrative description is a small, separate change; bundling it here would widen a content review into a metadata review.
- **The travel paragraph in "Beyond the Code".** It overlaps thematically with P4 but makes a different claim (how he travels versus the solo-travel instinct). Left alone.
- **The vault's story canon.** `vault/stories/entities/people/cunico-captain.md` frames the Cunico chapter as ego-versus-outcome, where he taught a process and someone else took the credit. This section frames it as rock bottom and resolve. Both are now on the record and they are not the same beat. Reconciling them is a vault edit under the vault's contradiction policy, not a site edit, and it needs Gary's call.
- **`assets/imgs/cyrus/`.** Untracked, unrelated to this plan.
- **Any other page.** Home, Projects, Coursework, Archives and the blog are untouched.

## Risks

- **Tone drift during review.** The copy is dry and self-deprecating by design, and a reviewer who finds P2's "describe politely" insufficiently apologetic may want to soften it. That softness is the thing being avoided. Take changes to Gary, not to the draft.
- **The relocation is easy to half-do.** Appending the section without removing the original paragraph produces two LinkedIn CTAs, and nothing in CI catches it. Step 5's single-match check exists for exactly this.
- **Anonymity is partial by construction.** Because `Experience` names Cunico two blocks above, a careful reader can connect the low-point job to the company. This was a decision, not an oversight: the goal is that the prose itself passes no judgement on a named employer.
