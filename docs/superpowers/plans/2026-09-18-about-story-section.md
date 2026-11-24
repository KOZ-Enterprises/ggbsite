# About Story Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one closing narrative section to `/about/` that states the site's through-line, without rewriting a single existing block or adding a line of CSS.

**Architecture:** One new `<section class="about-wide">` appended to `about.html`, assembled from classes the page already uses (`.rule-header`, `.rule-title`, `.rule-line`, `.page-lead`). The heading is deliberately a different job from the "How I Got Here" heading that Gary's separate in-flight work adds over the bio paragraph: that one carries chronology, this one carries the argument. The only edit to existing markup is relocating the LinkedIn call-to-action paragraph, so the page still ends on an invitation rather than on the story. No Sass, no JavaScript, no layout change.

**Tech Stack:** Jekyll 4.4.1, Liquid, plain HTML. Verification uses the two Python gates already wired into CI and the local headless Chromium on `127.0.0.1:9222`.

**Spec:** No separate spec. This plan is the artifact; the design was settled in brainstorming on 2026-09-18 and the decisions are recorded under "Decisions" below.

## Global Constraints

- **No em dashes.** `vault/gary/voice.md` bans them as an AI tell. `about.html` contains zero today; it must still contain zero after this change.
- **Existing classes only, zero new CSS.** `python3 script/geometry.py --count` must stay `0`, and a hand-written `padding` or `border-radius` fails the build. This is why the new section reuses `.about-wide` / `.rule-header` / `.page-lead` rather than introducing a class.
- **Curated material only.** This page is read by recruiters. Out of bounds: childhood and kindergarten, the poker table at 15, the 2011 Greek festival, ADHD, drinking, and the strip-club thread. In bounds: the failed programming class, the decade as a mechanical engineer, the low-point job, solo travel, and the engineering.
- **The former employer is not named in the narrative.** `Experience` two blocks above still names Cunico Corporation, so the reader can connect the dots; what anonymity buys is that the prose attaches no editorial about a named company to it. Do not "helpfully" add the name back.
- **Do not re-tell the bio.** The bio paragraph carries the chronology (failed class, the decade, nights-and-weekends degree, 2026). This section's copy references that arc only in passing and spends its words on what the bio does not say. If the "How I Got Here" heading has landed when you execute, this constraint is already satisfied by the copy below. Do not "round it out" by restoring the retelling.
- **The copy is the deliverable, not a sketch.** The paragraphs in Task 1 are final. Do not rewrite them to taste. If they read wrong, stop and raise it rather than improving them in place.

## Decisions

Settled with Gary on 2026-09-18 before this plan was written. Do not revisit during execution.

| Decision | Choice | Why |
| --- | --- | --- |
| Surface | Public About page | It is the page a recruiter reads, and it was already part-narrative |
| Shape | Add one section; leave the existing blocks alone | Lowest-risk change to a page whose layout was just stabilised by the page-consistency work |
| Placement | Closing section, after "Beyond the Code" | The through-line lands last, which is where an essay earns its thesis |
| Heading | **"What It Adds Up To"** | Gary's in-flight work adds "How I Got Here" over the bio. The two headings must read as different jobs: one is history, one is meaning |
| Spine | "The gap between what people predict and what actually happens" | Already the site's stated through-line |
| Length / register | ~4 short paragraphs, dry and understated | Matches `voice.md`; the page's other narrative blocks run 80 to 110 words each |
| Low-point framing | Anonymous quality-control job, no bitterness | Names no employer, assigns no blame, keeps the beat |
| Call-to-action | **Moved** below the new section | Confirmed 2026-09-18: the page should still end by inviting people to reach out |

**One deliberate exception to "leave everything alone":** the LinkedIn call-to-action currently closes "Beyond the Code", so appending a section would strand it mid-page. It moves verbatim to the end of the new section. Nothing else in the existing 144 lines changes.

## File Structure

| File | Responsibility |
| --- | --- |
| `about.html` | The only file modified. Loses the CTA paragraph from "Beyond the Code" (lines 139 to 143) and gains one section at the end. |
| `_site/about/index.html` | Build output, regenerated. Read-only for verification. |

No other file is in scope. `_sass/`, `_includes/`, `_layouts/` and the two Python gates are untouched.

---

### Task 1: Add the "What It Adds Up To" section

**Files:**

- Modify: `about.html:139-144` (remove the CTA paragraph, append the new section)

**Interfaces:**

- Consumes: classes already defined in `_sass/_pages.scss` and `_sass/_components.scss` — `.about-wide`, `.rule-header`, `.rule-title`, `.rule-line`, `.page-lead`. All of them appear elsewhere on this page.
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

If `<h2` already reads `6`, Gary's "How I Got Here" heading has landed. That does not change this task; continue, and note the new total in Step 5 instead.

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
        <h2 class="rule-title">What It Adds Up To</h2>
        <span class="rule-line"></span>
    </div>
    <p class="page-lead">
        Most of the work I have done comes down to the same thing: closing the gap between what a model predicts
        and what actually happens. A simulation is confident, a test result is true, and the distance between
        them is where I&rsquo;ve spent my career. It&rsquo;s also, roughly, the shape of my life.
    </p>
    <p class="page-lead">
        That wasn&rsquo;t a plan. A failed programming class told me programming wasn&rsquo;t for me, and I
        believed it for about ten years, which is easy when you&rsquo;re already good at something else. Then I
        took a quality control job I&rsquo;ll describe politely, certifying pipe fittings for submarine
        programs, and that was the floor of my own chart. Narrow work, a low ceiling, and enough competence in
        it to stay forever. Being good at something you don&rsquo;t want a life of is its own kind of problem.
    </p>
    <p class="page-lead">
        I stopped waiting for permission somewhere in there. The ambition wasn&rsquo;t new. What changed was
        that I started treating the years as something I was spending rather than something that was happening
        to me.
    </p>
    <p class="page-lead">
        The same instinct runs outside of work. I travel alone on purpose: no committee, no compromises, an
        itinerary I build as I go, and a standing rule that history is better confronted than skipped. Rigor and
        wanderlust aren&rsquo;t opposites. They&rsquo;re one trait pointed at different problems, and both are
        ways of finding out what&rsquo;s actually there instead of what you expected.
    </p>
    <p class="page-lead">
        If you want to talk robotics, history, K-pop, or soccer, feel free to
        <a href="https://www.linkedin.com/in/garykuepper/" target="_blank" rel="noopener">connect with me on
            LinkedIn</a>.
    </p>
</section>
```

Notes on the markup, so it is not "corrected" during review:

- Apostrophes are `&rsquo;` entities, matching every other paragraph on the page. There are 11 of them.
- No em dashes. P1 and P2 use a colon; P1 uses parentheses-equivalent commas.
- 234 words across four paragraphs. P1 53, P2 86, P3 34, P4 61. The fifth paragraph is the relocated CTA and is not counted.

- [ ] **Step 4: Build and run both gates**

```bash
bundle exec jekyll build --quiet
python3 script/geometry.py --count   # expect 0
python3 script/dead-css.py --count   # expect 0
```

`geometry.py` is the guard that matters here: it rejects off-scale vertical `margin`/`padding`/`gap` and any unnamed `border-radius`. A `0` proves the new section added no geometry of its own. **If either count is non-zero, do not proceed and do not add an exemption** — the section was built from the wrong classes.

- [ ] **Step 5: Verify the structure changed and nothing else did**

```bash
grep -c '<h2' about.html          # expect 6, or 7 if "How I Got Here" has landed
grep -c '<section' about.html     # expect 7
grep -c '—' about.html            # expect 0
grep -c 'linkedin.com/in/garykuepper' about.html   # expect 1, not 2
```

The last check is the one that catches a botched relocation: appending the section without deleting the original paragraph leaves two identical CTAs on the page, one of them buried mid-article.

Confirm the pre-existing section titles survive:

```bash
grep -o '<h2 class="rule-title">[^<]*</h2>' about.html
```

Expected, in order: `Experience`, `Education`, `My Journey`, `What I&rsquo;m Building`, `Beyond the Code`, `What It Adds Up To`.

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
s.querySelector('h2').textContent.trim();          // "What It Adds Up To"
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
git commit -m "content(about): add the what it adds up to section"
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
curl -s "https://garygigabytes.com/about/?cb=$(date +%s)" | grep -c 'What It Adds Up To'   # expect 1
```

Then confirm the rendered page, not just the markup:

```text
https://garygigabytes.com/about/?cb=<timestamp>
```

Assert: the section heading reads "What It Adds Up To"; the phrase "closing the gap between what a model predicts and what actually happens" is present; exactly one LinkedIn link sits inside the main content (the footer adds its own, so a page-wide count of 2 is correct); the main content's final visible text is the invitation sentence; `Experience`, `Education`, `My Journey`, `What I&rsquo;m Building` and `Beyond the Code` all survive with their content unchanged.

If the live page still shows the old version after a successful deploy, the cause is the CDN cache, not the build. Re-fetch with a fresh `cb` value before investigating anything else.

- [ ] **Step 5: Confirm the sharing card is unaffected**

`about.html` sets no front matter `description`, so `_includes/head.html` falls back to `default_desc` (103 characters, already over LinkedIn's 100-character floor). Verify the page's `og:description` is unchanged from before this change rather than rewritten.

---

## Deliberately not addressed

- **A page-specific `description` for the sharing card.** The About page ships the generic site description to LinkedIn. A narrative description is a small, separate change; bundling it here would widen a content review into a metadata review.
- **The travel paragraph in "Beyond the Code".** It overlaps thematically with P4 but makes a different claim (how he travels versus the solo-travel instinct). Left alone.
- **Gary's "How I Got Here" heading over the bio.** Separate in-flight work. It adds a heading and does not change the paragraph's content, so it does not conflict with this plan and needs no rebase. Whichever lands second is a clean merge.
- **`assets/imgs/cyrus/`.** Untracked, unrelated to this plan.
- **Any other page.** Home, Projects, Coursework, Archives and the blog are untouched.

## Resolved outside this plan

The vault's Cunico entry carried only one reading of that chapter: ego versus outcome, where he taught a process and someone else took the credit. Gary confirmed on 2026-09-18 that the floor-and-resolve reading is true as well. Both now sit on the record in `vault/stories/entities/people/cunico-captain.md` under "Two beats in one chapter". No site change follows from it, and nothing was overwritten.

## Risks

- **Tone drift during review.** The copy is dry and self-deprecating by design, and a reviewer may find P2's "describe politely" insufficiently apologetic, or want P1's closing line softened. That flatness is the thing being avoided. Take changes to Gary, not to the draft.
- **The relocation is easy to half-do.** Appending the section without removing the original paragraph produces two LinkedIn CTAs, and nothing in CI catches it. Step 5's single-match check exists for exactly this.
- **Two headings can still look like one job.** "How I Got Here" and "What It Adds Up To" sit on the same page and both concern the same decade. The copy is written so the second does not repeat the first; a reviewer who adds the chronology back into the new section has broken the separation, not improved it.
- **Anonymity is partial by construction.** Because `Experience` names Cunico two blocks above, a careful reader can connect the low-point job to the company. This was a decision, not an oversight: the goal is that the prose itself passes no judgement on a named employer.
