---
layout: project
published: false
title: "ggPack"
image: "/assets/imgs/project/ggpack-pulldown.png"
description: "A 1-D multi-physics simulation of an airliner air conditioning pack built around a 3-wheel bootstrap air cycle machine."
objective: "Model air cycle machine dynamics, water separation and pack control, using only public sources, and validate the results against published cases."
status: "active"
status_detail: "Draft"
order: 5
project-tag: "ggpack"
tools:
  - name: "Python"
  - name: "OpenModelica"
  - name: "uv"
  - name: "pytest"
---

## Overview

<!-- TODO: why this project exists and who it is for. -->

**ggPack** models an airliner air conditioning pack: the system that turns hot bleed air
into cool, dry air for the cabin. The heart of it is a 3-wheel bootstrap air cycle machine,
with a compressor, turbine and fan on one shaft. The reference architecture is a
single-aisle airliner (737NG class). Its inlet conditions come from
[ggBleed](/projects/ggbleed/).

## What It Models

- **Shaft dynamics:** a rotor inertia balance between turbine, compressor, fan and bearing torques.
- **High-pressure water separation:** reheater, condenser and centrifugal water extractor,
  with phase-change psychrometrics and ram air water spray.
- **Pack control:** flow control valve scheduling, temperature control valve bypass, and
  modulating ram air doors.
- **ggBleed coupling:** runs directly on transient bleed outputs from ggBleed.

## Approach

<!-- TODO: expand. -->

As with ggBleed, the pack is built twice: a causal Python model and an acausal
OpenModelica model.

### Roadmap

<!-- TODO: confirm phases and status before publishing. -->

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-track">
<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 0</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Core Models</h4>
<p class="phase-details">Python and OpenModelica pack models, coupled to ggBleed.</p>
</div>

<div class="roadmap-phase is-active">
<div class="phase-header">
<span class="phase-badge">Phase 1 &middot; Active Target</span>
<span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
</div>
<h4 class="phase-title">Public Sourcing &amp; Validation</h4>
<p class="phase-details">Trace every parameter to a public source and validate against published cases.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 2</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Write-Up</h4>
<p class="phase-details">Results, validation plots, and lessons learned.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Validation

<!-- TODO: fill from docs/VALIDATION_SOURCES.md once the research pass is done. -->
First target: reproduce the bootstrap pack baseline from Pérez-Grande &amp; Leo
(2002), widely reused in later ECS literature.

## Results

<!-- TODO: key plots and comparisons against the validation cases. -->

## Sources & Disclaimer

This is an independent educational project. It is built only from publicly available
material, cited below, and contains no proprietary data. It is not affiliated with or
endorsed by Boeing, Airbus, or any equipment supplier.

<!-- TODO: citation list from docs/VALIDATION_SOURCES.md. Do not publish until every
     parameter on this page traces to a source here. -->
