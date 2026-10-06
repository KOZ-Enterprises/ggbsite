---
layout: project
title: "ggPack"
image: "/assets/imgs/project/ggpack-pulldown.png"
description: "A 1-D multi-physics simulation of an airliner air conditioning pack built around a 3-wheel bootstrap air cycle machine."
objective: "Model air cycle machine dynamics, water separation and pack control, using only public sources, and validate the results against published cases."
status: "active"
status_detail: "Validation in progress"
order: 5
project-tag: "ggpack"
tools:
  - name: "Python"
  - name: "OpenModelica"
  - name: "uv"
  - name: "pytest"
---

## Overview

**ggPack** models an airliner air conditioning pack: the system that turns hot bleed air
into cool, dry air for the cabin. The heart of it is a three-wheel bootstrap air cycle
machine, with a compressor, turbine and ram fan on one shaft. It is a 737-800-class
reference architecture built only from public sources. Its inlet conditions come from
[ggBleed](/projects/ggbleed/).

## What It Models

- **Shaft dynamics:** a single rotor inertia balancing turbine, compressor and fan torques,
  with a published shaft mechanical efficiency.
- **High-pressure water separation:** primary and secondary heat exchangers, reheater,
  condenser and water extractor, with psychrometrics and evaporative spray of the extracted
  water into the ram duct.
- **Pack control:** flow control valve holding the pack-flow setpoint, temperature control
  valve bypass, and ram air doors.
- **ggBleed coupling:** runs directly on transient bleed outputs from ggBleed.

## Approach

As with ggBleed, the pack is built twice: a causal Python model and an acausal
OpenModelica model. The OpenModelica cruise experiment runs at a published cruise case;
it has no controller and models dry air, so it is a structural check, not a validation.

### Roadmap

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

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 1</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Public-Sources Audit</h4>
<p class="phase-details">Every parameter traced to a public source, derived, or labelled as an assumption, enforced by a checker in the test suite.</p>
</div>

<div class="roadmap-phase is-active">
<div class="phase-header">
<span class="phase-badge">Phase 2 &middot; Active Target</span>
<span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
</div>
<h4 class="phase-title">Validation</h4>
<p class="phase-details">Calibrate against the published ground and cruise cases, and add a wet heat-exchanger model for the condenser.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 3</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Write-Up</h4>
<p class="phase-details">Results, validation plots, and lessons learned.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Validation

A built-in `validate` command compares the model with three published cases: a ground
reference case and a second ground point from Li et al., and two cruise cases from
Chowdhury et al. Tolerances are the published mean deviations of an independent model.

Current state, stated plainly: **the pack is not yet calibrated.** Of 19 accuracy checks,
4 are within tolerance (including shaft speed in both ground cases), the cruise
controller reaches both published targets, and no physically impossible state occurs.
Known gaps, such as the condenser's missing wet heat-exchanger model and a water-mass
leak, are pinned as expected-failure tests so they stay visible.

## Research

The parameters and validation cases come from a curated library of 28 public papers,
reports and theses on aircraft bleed and air conditioning systems, each read and filed
with a short summary and notes on where its data sits. Progress notes and research
findings are posted below as the work goes on.

## Results

![ggPack ground reference case](/assets/imgs/project/ggpack-pulldown.png)

The published ground reference case run through the Python model: station temperatures,
pressures and shaft speed, moisture removal, and actuator positions.

## Sources & Disclaimer

This is an independent educational project. It is a 737-800-class reference architecture built
only from public sources: peer-reviewed journal papers and a government incident report. No manufacturer, maintenance, training or other proprietary documents
were used, and it is not a replica of any manufacturer's hardware. It is not affiliated with or
endorsed by Boeing, Airbus, or any equipment supplier.

Every model value is cited to one of the sources below, derived from them by a written calculation,
standard textbook physics, or a labelled generic modelling assumption. A provenance checker runs
with the test suite and fails the build on any untagged value.

- **P1:** Esperon-Miguez, Jennions, Camacho Escobar, Hanov, "Simulating faults in a Boeing
  737-200 Environmental Control System using a thermodynamic model", *Int. J. Prognostics and
  Health Management* 10(2) (2019).
- **P2:** Jennions, Ali, Esperon-Miguez, Camacho Escobar, "Simulation of an aircraft
  environmental control system", *Applied Thermal Engineering* 172, 114925 (2020).
- **P5:** Li, Hu, Sun, Wu, "Dynamic simulation model for three-wheel air-cycle refrigeration
  systems in civil aircrafts", *Int. J. Refrigeration* 145, 353–365 (2023).
- **P8:** Jennions, Ali, "Evaluation of Component Level Degradation in the Boeing 737-800 Air
  Cycle Machine", *J. Thermal Science and Engineering Applications* 15(3), 031014 (2023).
- **P9:** Chowdhury, Ali, Jennions, "Boeing 737-400 passenger air conditioner control system
  model for accurate fault simulation", *J. Thermal Science and Engineering Applications*
  14(9), 091008 (2022).
- **P18:** Li, Hu, Lei, "Performance simulation and diagnosis of faulty states in air-cycle
  refrigeration systems in civil aircrafts", *Int. J. Refrigeration* 156, 232–242 (2023).
- **P19:** Li, Hu, Wang, Shen, "Temperature control method optimization for dual-pack air
  cycle refrigeration system in civil aircraft based on dynamic system modelling",
  *Int. J. Refrigeration* 191, 107067 (2026).
- **B3:** Air Accident Investigation Bureau Malaysia, *Aircraft Serious Incident Final Report
  SI 04/24, Boeing 737-800 9M-LCM* (2025).
