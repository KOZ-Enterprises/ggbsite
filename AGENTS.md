# Gary Gigabytes: AI Agent Context Guide

This file explains the project structure, conventions, and context for AI agents working on the ggbsite repository.

## Project Identity

- **Owner:** Gary Kuepper (Aerospace ME → CSUMB CS)
- **Purpose:** Personal portfolio + technical blog + academic documentation
- **Type:** Static site (Jekyll 4.3) hosted on Google Cloud Run
- **Audience:** Recruiters, collaborators, fellow engineers interested in robotics/autonomous systems/ML

## Site Purpose & Content Areas

### 1. Gary Gigabytes (Homepage)

- **URL:** `/`
- **Type:** Blog archive + featured projects
- **Content Source:** `_posts/` (Jekyll posts, front-matter: title, date, tags, excerpt)
- **Typical Posts:** Project updates, technical deep dives, research notes

### 2. About

- **URL:** `/about/`
- **Static Page:** `about.html`
- **Purpose:** Background, career transition narrative, skills summary

### 3. Hobby Projects

- **URL:** `/projects/`
- **Type:** Project showcase (custom collection)
- **Content Source:** `_projects/` (markdown files, one per project)
- **Fields:** title, date, description, tags, images, links to GitHub repos

### 4. Academic Annex (CSUMB)

- **URL:** `/csumb.html` or `/csumb/`
- **Type:** Course documentation + class projects
- **Content Source:** `_csumb/` (markdown per course, e.g., `cst300.md`, `cst499.md`)
- **Fields:** course number, semester, description, key learnings, links to portfolios

## Directory Structure

```text
ggbsite/
├── _posts/              # Blog posts (Markdown)
│   ├── YYYY-MM-DD-title.md
│   └── ... (sorted chronologically)
├── _projects/           # Project showcases (Markdown)
│   ├── project-name.md
│   └── ... (one file per project)
├── _csumb/              # Course documentation (Markdown)
│   ├── cstXXX.md
│   └── ... (one file per course)
├── _layouts/            # Jekyll templates (HTML/Liquid)
│   ├── default.html     # Base layout
│   ├── post.html        # Blog post layout
│   ├── project.html     # Project layout
│   ├── course.html      # CSUMB course layout
│   └── ...
├── _includes/           # Reusable Liquid components
│   ├── header.html
│   ├── footer.html
│   ├── nav.html
│   ├── project-card.html
│   └── post.html
├── assets/              # Static assets
│   ├── css/styles.css   # Vanilla CSS (dark-mode-first)
│   ├── js/scripts.js    # Minimal JavaScript
│   ├── imgs/            # Images (org by category)
│   └── docs/            # PDFs and presentations
├── _data/               # Data files (YAML)
│   └── tag_links.yml    # Tag taxonomy
├── _config.yml          # Jekyll configuration
├── Dockerfile           # Docker image definition
├── Gemfile              # Ruby dependencies
├── .github/workflows/   # GitHub Actions CI/CD
│   ├── deploy.yml       # Build & deploy pipeline
│   └── lint.yml         # Linting checks
├── DEPLOYMENT.md        # GCP Cloud Run operations guide
├── CLOUD_RUN_SETUP.md   # One-time infrastructure setup
└── README.md            # Project overview
```

## Front-Matter Conventions

### Blog Posts (`_posts/`)

```yaml
---
layout: post
title: "Post Title"
date: YYYY-MM-DD
tags: [tag1, tag2]
excerpt: |
  A brief summary that appears in blog archives.
  This is split by <!--more--> if longer content exists.
---
```

- **Required:** `layout`, `title`, `date`
- **Optional:** `tags` (comma-separated or array), `excerpt`
- **Excerpt Separator:** `<!--more-->` (marks where archive cutoff occurs)
- **Tags:** Used for categorization (see `_data/tag_links.yml` for taxonomy)

### Projects (`_projects/`)

```yaml
---
layout: project
title: "Project Name"
date: YYYY-MM-DD
description: "One-line summary"
tags: [category, technology]
image: /assets/imgs/project/project-name.png
github: "https://github.com/org/repo"
demo: "https://live-demo-url.com"
---
```

- **Required:** `layout`, `title`, `date`, `description`
- **Optional:** `tags`, `image`, `github`, `demo`, `paper`, `video`
- **Image:** Should be 400x300px or similar (used in cards)

### Courses (`_csumb/`)

```yaml
---
layout: course
title: "Course Title (CST XXX)"
course: "CSUMB CST XXX"
semester: "Fall 2025"
description: "Course summary and my key takeaways"
tags: [csumb, subject-matter]
---
```

- **Required:** `layout`, `title`, `course`, `semester`, `description`
- **Optional:** `tags`, `skills`, `projects`, `gpa` (if relevant)

## Content Conventions

### Writing Style

- **Tone:** Authentic, analytical, conversational
- **Markers:** Use light descriptors and relatable asides (e.g., "Not my proudest moment...")
- **Structure:** Mix dense technical blocks with light, punchy sentences
- **Vocabulary:** Active verbs, focus on "vibe" and energy

### Technical Precision

- Use bullet points for mechanical explanations
- Code blocks for examples
- Links to external repos/papers
- Avoid corporate speak

### Tagging Guidelines

**Common Tags:** See `_data/tag_links.yml` for full taxonomy

- Course codes: `cst300`, `cst499`, `csumb`
- Project categories: `hobby-projects`, `capstone`, `research`
- Technical: `robotics`, `marl`, `autonomous-systems`, `ml`
- Specific projects: `ggswarm`, `hexmaster`, `smart-mirror`

### Citations & References

Any fact, value, method or result taken from published work is cited the way a wiki does
it: a numbered inline marker that links to a reference list at the bottom, which links back.
Live examples: `_projects/ggbleed.md`, `_projects/ggpack.md`, `_projects/ggswarm.md`.

- **Inline:** a kramdown footnote, `[^key]`, placed after the punctuation (`...a lab rig.[^b10]`).
  It renders as `[n]`. Reuse the same key for every citation of the same source; kramdown
  numbers by first use and adds one back-link per citation. Never hand-write `<sup>` markup.
- **Key:** a short lowercase slug, either the source's ID where one exists (ggResearch IDs
  such as `b3` and `p5` on ggBleed/ggPack, which must match that repo's `docs/SOURCES.md`) or
  the method name (`gatv2`, `ppo`).
- **List:** every definition goes at the very end of the file, under a final `## References`
  heading, which must be the page's last heading. Keep the definitions in first-citation order.
- **Format:** `Surname, Surname (Year). "Article Title". *Venue* vol(issue): pages. Location. [link](url)`
  - Surnames only. Up to four authors; beyond that, the first four, then "et al.".
  - Books, theses and reports: italic title, no quotes.
  - Location is the table, figure or section the material came from, when the page relies
    on a specific value.
  - Link preference: DOI (`[doi:10.x/y](https://doi.org/10.x/y)`), then arXiv, then the
    publisher's or agency's official URL. Never link a paywalled copy, a local path, or the
    tailnet-only ggResearch site.
- **Verify before publishing:** resolve every DOI or URL and check the title, authors, year,
  volume and pages against the record (`curl -sLH 'Accept: application/vnd.citationstyles.csl+json' https://doi.org/<doi>`).
  Never cite from memory.
- **Excerpts:** no citations above `<!--more-->`, because archive cards would show markers
  whose references are missing.
- **Not citations:** links to tools, products, docs and repositories stay ordinary inline links.
- **Styling:** lives in the citations block of `_sass/_content.scss`. The back-link glyph
  is `kramdown.footnote_backlink` in `_config.yml`.

## Deployment Pipeline

```text
1. Local Development
   └─> Write markdown, test locally with `bundle exec jekyll serve`

2. Push to GitHub
   └─> `git push origin feature-branch`

3. Merge to `publish` Branch
   └─> Triggers GitHub Actions workflow

4. Build & Deploy (GitHub Actions)
   ├─> Build Docker image (via Dockerfile)
   ├─> Push to Google Container Registry (GCR)
   ├─> Deploy to Google Cloud Run (us-central1)
   └─> Load Balancer routes traffic from garygigabytes.com

5. Live
   └─> Accessible via HTTPS (Cloudflare + GCP SSL cert)
```

**Workflow File:** `.github/workflows/deploy.yml`
**Status Checks:** Lint (RuboCop, HTMLProofer, yamllint, markdownlint, actionlint, hadolint, dead-CSS)

## Key Files for AI Agents

| File | Purpose | When to Edit |
| ------ | --------- | -------------- |
| `_config.yml` | Jekyll config (collections, plugins) | Adding new collection type |
| `_layouts/*.html` | HTML templates | Changing page structure |
| `_includes/*.html` | Reusable components | Updating navigation, footers, cards |
| `_sass/*.scss` | Sass partials (the stylesheet source) | Visual updates (dark mode first!) |
| `assets/css/styles.scss` | Manifest; compiles to `/assets/css/styles.css` | Adding a partial |
| `.rubocop.yml` | Ruby linting rules | Adjusting code standards |
| `.github/workflows/*.yml` | CI/CD automation | Changing build/deploy process |
| `Dockerfile` | Container definition | Changing base image or build steps |
| `DEPLOYMENT.md` | Ops docs | Recording deployment procedures |
| `.agent/rules/.cursorrules` | AI agent context | Improving agent understanding |

## How to Add Content

### New Blog Post

1. Create file: `_posts/YYYY-MM-DD-slug-title.md`
2. Add front-matter (see Front-Matter Conventions above)
3. Write markdown content (cite published sources per Citations & References)
4. Use `<!--more-->` to mark archive cutoff
5. Commit & push to `publish` branch → Auto-deploys

### New Project

1. Create file: `_projects/slug-name.md`
2. Add front-matter with required fields
3. Write description (markdown)
4. Include image (300-400px recommended)
5. Link to GitHub repo
6. Commit & push → Auto-deploys

### New CSUMB Course

1. Create file: `_csumb/cstXXX.md`
2. Add front-matter with course details
3. List key learnings, projects, technologies
4. Include links to relevant work
5. Commit & push → Auto-deploys

## Portfolio Project: CulinaryOtter

**Location:** [TerraBit-Apex-Solutions/CulinaryOtter](https://github.com/TerraBit-Apex-Solutions/CulinaryOtter) (separate repo)

**Featured on:** This site as example portfolio work

**Tech Stack:** Node.js/Express, MySQL, EJS templates, Docker

**Role:** Portfolio showcase of group project capabilities

**Related Page:** `/projects/` may link to CulinaryOtter documentation or live instance

## Code Standards

- **Python:** Strict PEP 8 (Black/Ruff style, 88-100 char line length, snake_case filenames)
- **Ruby:** RuboCop enforced (see `.rubocop.yml`)
- **YAML:** yamllint enforced (see `.yamllint.yml`)
- **Markdown:** markdownlint enforced (see `.markdownlint-cli2.yaml`)
- **Dockerfile:** hadolint enforced (see `.hadolint.yaml`)
- **CSS:** Sass partials in `_sass/`, no frameworks, dark-mode-first
- **JavaScript:** Minimal, vanilla (no jQuery required)

### CSS

Read `docs/css-architecture.md` before touching the stylesheet. Three rules
carry most of the weight:

- **The palette is closed.** Every colour is a token in `_sass/_tokens.scss`.
  Four documented literals sit outside it; do not add a fifth silently.
- **Three breakpoints only** — `respond-to(wide|nav|mobile)` at 1024 / 860 /
  700px. A fourth width re-creates the 701-860px bug this replaced.
- **Responsive rules live with their component**, nested via `respond-to()`.
  No partial contains a bare `@media`.

`script/dead-css.py --count` must report `0`; CI fails the build otherwise.

## Style Persona (for Content)

**Voice:** Authentic, Analytical, Visually Descriptive

**Technical Precision:** Use bullet points and clear headings for code/mechanical explanations. Stay accurate but conversational.

**The 'Casual Shift':** Use light markers and relatable asides.

**Vibrant Vocabulary:** Use active verbs and focus on the "vibe" or energy of the work. Avoid corporate speak.

**Formatting:** Mix dense technical blocks with light, punchy sentences. No long, academic paragraphs.

## Useful Commands

```bash
# Local development
bundle exec jekyll serve    # Start dev server at http://localhost:4000

# Linting
bundle exec rubocop         # Check Ruby code
bundle exec jekyll build    # Build site & check for errors
bundle exec htmlproofer ./_site --disable-external

# Deployment
git push origin publish     # Trigger GitHub Actions workflow
```

## Resources & Links

- **Jekyll Docs:** <https://jekyllrb.com/>
- **Liquid Templates:** <https://shopify.github.io/liquid/>
- **Markdown:** <https://www.markdownguide.org/>
- **GitHub Actions:** <https://docs.github.com/en/actions>
- **Google Cloud Run:** <https://cloud.google.com/run/docs>
- **Cloudflare:** <https://dash.cloudflare.com/>

## Contact & Support

- **Primary Contact:** Gary Kuepper
- **Email:** [LinkedIn Profile](https://www.linkedin.com/in/garykuepper/)
- **Issues:** GitHub repo issues for bugs/feature requests
- **Deployment Questions:** See DEPLOYMENT.md and CLOUD_RUN_SETUP.md
