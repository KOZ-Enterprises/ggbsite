---
layout: project
title: "Smart Mirror"
image: "/assets/imgs/smartmirror/magicmirror_final_cropped.jpg"
image_caption: "Final Build of the Smart Mirror"
description: "A functional smart mirror and a localized information hub for daily-use metrics."
objective: "Build a smart mirror for daily-use information at a glance."
status: "shipped"
status_detail: "Shipped · Production"
reflection: "This was one of my first DIY tech builds and helped me understand the basics of Linux, web-based UIs, and integrating hardware into a polished product."
resources:
  - name: "MagicMirror² Framework"
    link: "https://magicmirror.builders/"
    icon: "fas fa-link"
order: 1
project-tag: "smart-mirror"
tools:
  - name: "Raspberry Pi"
  - name: "MagicMirror²"
---

## Project Overview

A wall-mounted smart mirror built with a Raspberry Pi 4 and a
two-way acrylic mirror, running the MagicMirror² platform to
display time, weather, calendar, and news at a glance.

### Build Roadmap & Milestones

The project was engineered through the following build and stabilization milestones:

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-summary">
<span class="roadmap-summary-item"><strong>Shipped</strong> Complete</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">4 Build Milestones</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">Embedded IoT Track</span>
</div>

<div class="roadmap-track">
<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 1</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Concept & Optical Sourcing</h4>
<p class="phase-details">Evaluated two-way acrylic mirror transmittance, viewing angles, and frame dimensional tolerances.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 2</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Frame Assembly & Initial Build</h4>
<p class="phase-details">Built the custom wood chassis, fitted the 18.5" 1080p display, and set up the initial Raspberry Pi bench.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 3</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Circuit Isolation & Pi 4 Rebuild</h4>
<p class="phase-details">Redesigned the internal power wiring with isolated 110V power supplies and upgraded compute to a Raspberry Pi 4.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 4</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">MagicMirror² Customization & Wall Mount</h4>
<p class="phase-details">Configured localized calendar, weather, and news feeds on Linux with automatic startup and wall installation.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Build Details

- **Display**: 18.5" 1080p portable monitor behind a two-way
  acrylic mirror in an 11x17 frame
- **Compute**: Raspberry Pi 4 (1GB) — upgraded from a Pi 3
  after the original build shorted out
- **Software**: MagicMirror² with calendar, weather, and
  news modules

## Lessons Learned

This was one of my first DIY tech builds. It taught me the
basics of Linux, web-based UIs, embedded power management,
and integrating hardware into a polished product. The first
build ended with a fried monitor and Pi after accidentally
shorting the 110V circuit — so the rebuild was an exercise
in doing things right the second time.
