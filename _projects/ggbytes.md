---
layout: project
title: "Gary Gigabytes Website"
image: "/assets/imgs/ggbytes/ggbytes-card-2026-09.png"
description: "A technical portfolio and a central hub for documenting my engineering journey."
objective: "Develop a high-performance, responsive workstation for documenting CS and Engineering projects with a focus on modularity and technical aesthetics."
status: "active"
status_detail: "Phase 8 · Workstation & Optimization"
project-tag: "gary-gigabytes"
order: 0
tools: 
  - name: "Jekyll"
  - name: "CSS"
  - name: "HTML5"
  - name: "Font Awesome"
  - name: "Google Fonts"
  - name: "Jekyll Paginate"
  - name: "Docker"
  - name: "Nginx"
  - name: "Google Cloud Run"
  - name: "GitHub Actions"
  - name: "Cloudflare"
---

## Project Overview

This portfolio site serves as a central hub for documenting
my engineering journey — from CS coursework at CSUMB to
personal robotics and trading projects. Built with Jekyll
and deployed on Google Cloud Run.

### Roadmap & Development Phases

The site's architecture has evolved through the following technical milestones:

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-summary">
<span class="roadmap-summary-item"><strong>Phase 8</strong> In Progress</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">8 Development Milestones</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">Platform Infrastructure Track</span>
</div>

<div class="roadmap-track">
<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 1</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Bare HTML/CSS & DigitalOcean Nginx</h4>
<p class="phase-details">Created the initial static site prototype running on a DigitalOcean droplet behind Nginx.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 2</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Jekyll Static Engine Integration</h4>
<p class="phase-details">Integrated Jekyll 4.3 with custom layouts for blog posts, project showcases, and CSUMB courses.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 3</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Responsive Design & Layout Flow</h4>
<p class="phase-details">Implemented fluid column layouts, card grids, and mobile-friendly navigation patterns.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 4</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Docker Containerization</h4>
<p class="phase-details">Containerized the Jekyll build environment for deterministic local preview and cloud deployments.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 5</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Cloud Run Migration & CI/CD</h4>
<p class="phase-details">Migrated from DigitalOcean to Google Cloud Run with Global Load Balancer, Cloudflare SSL, and automated GitHub Actions.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 6</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Sass Modularization & Token Architecture</h4>
<p class="phase-details">Deconstructed 3,356 lines of monolithic CSS into 8 Sass partials behind a closed 16-color palette and strict geometry rules.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 7</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">UI/UX Overhaul & Accessibility</h4>
<p class="phase-details">Engineered blueprint grid visuals, Chakra Petch / Roboto Mono type pairing, skip links, and WCAG AA contrast.</p>
</div>

<div class="roadmap-phase is-active">
<div class="phase-header">
<span class="phase-badge">Phase 8 &middot; Active Target</span>
<span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
</div>
<h4 class="phase-title">Continuous Maintenance & Technical Documentation</h4>
<p class="phase-details">Ongoing additions of interactive engineering components, quality gates (geometry, dead-CSS, htmlproofer), and research notes.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Technical Architecture

- **Static Site Generator**: Jekyll with custom layouts
  for projects, posts, and course pages
- **Styling**: Jekyll's native Sass — a token file plus eight
  documented partials, a closed sixteen-colour palette, and
  three breakpoints reached only through a `respond-to()` mixin
- **Deployment**: Dockerized Jekyll build, served via
  Google Cloud Run with a Global Load Balancer
- **CI/CD**: GitHub Actions triggers Cloud Build on push
- **DNS/CDN**: Cloudflare for caching and SSL

## Design History

Three visual generations so far. The old ones are kept on purpose: this project
exists to document the journey, and that includes what the site used to look
like. The order is inferred from the navigation labels — each generation's names
were renamed into the next — rather than from a dated record.

**First generation.** Centered wordmark over a horizontal nav reading
*Hobby Projects* and *BSCS Portfolio*, with a "Recent Updates" arrow list and
quote-styled post cards.

![First-generation site: a centered GGBYTES wordmark above a horizontal navigation bar](/assets/imgs/ggbytes/ggbytes-gen1.png)

**Second generation.** Same centered shape, tightened type and spacing; the nav
became *Projects* and *CSUMB*.

![Second-generation site: centered wordmark with a refined horizontal navigation bar](/assets/imgs/ggbytes/ggbytes-gen2.png)

**Current.** A left-aligned lockup with the G mark and a persistent navbar, an
introduction band carrying the role kicker and headline, and a featured project
hero. *CSUMB* became *Coursework*; the centered wordmark, the arrow list and the
quote cards are all gone.
