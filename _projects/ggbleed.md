---
layout: project
published: false
title: "ggBleed"
image: "/assets/imgs/project/ggbleed-mission.png"
description: "A 1-D multi-physics simulation of a turbofan engine's bleed air system, from bleed ports through pressure regulation to the precooler."
objective: "Model bleed air pressure regulation and precooler heat transfer across a full flight mission, using only public sources, and validate the results against published cases."
status: "active"
status_detail: "Draft"
order: 4
project-tag: "ggbleed"
tools:
  - name: "Python"
  - name: "OpenModelica"
  - name: "uv"
  - name: "pytest"
---

## Overview

<!-- TODO: why this project exists and who it is for. -->

**ggBleed** models how an airliner's engines supply bleed air to the aircraft: hot,
high-pressure air taken from the engine compressor, regulated, and cooled before it goes
to air conditioning, anti-ice and pressurization. The reference architecture is a
single-aisle airliner (737NG class). It feeds directly into [ggPack](/projects/ggpack/),
the air conditioning pack model.

## What It Models

- **Compressible gas dynamics:** isentropic nozzle relations, choked and unchoked orifice
  flow, and pressure drop.
- **Precooler heat transfer:** ε-NTU crossflow heat exchanger with transient core thermal mass.
- **Pneumatic valves:** pressure-regulating and high-pressure valves with diaphragm force
  balances, springs, travel limits and stiction.
- **Flight envelope:** takeoff, climb, cruise and idle descent, plus transient disturbances
  such as an anti-ice step demand.

## Approach

<!-- TODO: expand. -->

The same system is built twice: a causal Python ODE model and an acausal OpenModelica
model, so the two paradigms can be compared side by side.

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
<p class="phase-details">Python and OpenModelica bleed models with a pytest suite.</p>
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
Candidate cases include published engine-deck bleed extraction data and
precooler heat exchanger test data.

## Results

<!-- TODO: key plots and comparisons against the validation cases. -->

## Sources & Disclaimer

This is an independent educational project. It is built only from publicly available
material, cited below, and contains no proprietary data. It is not affiliated with or
endorsed by Boeing, Airbus, or any equipment supplier.

<!-- TODO: citation list from docs/VALIDATION_SOURCES.md. Do not publish until every
     parameter on this page traces to a source here. -->
