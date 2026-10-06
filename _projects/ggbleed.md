---
layout: project
title: "ggBleed"
image: "/assets/imgs/project/ggbleed-logo.png"
description: "A 1-D multi-physics simulation of a turbofan engine's bleed air system, from bleed ports through pressure regulation to the precooler."
objective: "Model bleed air pressure regulation and precooler heat transfer across a full flight mission, using only public sources, and validate the results against published cases."
status: "active"
status_detail: "Validation in progress"
order: 4
project-tag: "ggbleed"
tools:
  - name: "Python"
  - name: "OpenModelica"
  - name: "uv"
  - name: "pytest"
---

## Overview

**ggBleed** models how an airliner's engines supply bleed air to the aircraft: hot,
high-pressure air taken from the engine compressor, regulated, and cooled before it goes
to air conditioning, anti-ice and pressurization. It is a 737-800-class reference
architecture built only from public sources. It feeds directly into
[ggPack](/projects/ggpack/), the air conditioning pack model.

## What It Models

- **Compressible gas dynamics:** ideal-gas properties, isentropic and choked/unchoked
  orifice flow, and the standard atmosphere.
- **Precooler:** ε-NTU crossflow heat exchanger with a lumped core thermal mass.
- **Valves and control:** high-stage valve, a pressure-regulating shutoff valve (PRSOV)
  holding a gauge setpoint, and a fan air valve driven by an outlet thermostat, with sensor
  and valve lags, a temperature limit and an overheat trip.
- **Flight mission:** ground, takeoff, climb, cruise with a wing anti-ice step, idle
  descent and approach, rebuilt from published engine port states, a published cruise
  point and the standard atmosphere.

## Approach

The same system is built twice: a causal Python model and an acausal OpenModelica model,
so the two paradigms can be compared side by side. The OpenModelica cruise experiment
closes the plant with boundary sources and sinks and runs at the same cited cruise point
as the Python mission.

### Roadmap

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
<p class="phase-details">Compare against published measured and simulated cases from the research library.</p>
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

So far the model is checked against published *limits*, not fitted to measured data:

- Through the whole mission, the precooler outlet stays inside the control band published
  in the AAIB Malaysia incident report, the intermediate stage supplies cruise, the high
  stage takes over in descent, and nothing trips.
- The PRSOV regulates to the published setpoint, and the temperature limit and trip act
  at the published values.
- The precooler's conductance is solved so two published flight-test cases land in that band.

The OpenModelica cruise experiment settles on the same setpoint and band. Measured-data
validation cases are catalogued in the research library and are the next phase.

## Research

The parameters and validation cases come from a curated library of 28 public papers,
reports and theses on aircraft bleed and air conditioning systems, each read and filed
with a short summary and notes on where its data sits. Progress notes and research
findings are posted below as the work goes on.

## Results

![ggBleed mission profile](/assets/imgs/project/ggbleed-mission.png)

Mission profile from the Python model: temperatures, pressures, valve positions and flows
from ground idle to landing.

## Sources & Disclaimer

This is an independent educational project. It is a 737-800-class reference architecture built
only from public sources: peer-reviewed papers, a doctoral dissertation, an FAA technical report and
a government incident report. No manufacturer, maintenance, training or other proprietary documents
were used, and it is not a replica of any manufacturer's hardware. It is not affiliated with or
endorsed by Boeing, Airbus, or any equipment supplier.

Every model value is cited to one of the sources below, derived from them by a written calculation,
standard textbook physics, or a labelled generic modelling assumption. A provenance checker runs
with the test suite and fails the build on any untagged value.

- **B3:** Air Accident Investigation Bureau Malaysia, *Aircraft Serious Incident Final Report
  SI 04/24, Boeing 737-800 9M-LCM* (2025).
- **B10:** Shang, *Fault detection and isolation in an aircraft engine bleed air system*,
  PhD dissertation, Ryerson University (2011).
- **B13:** Peng, "Research and Verification on the Solution of Bleed Air Temperature Deviation
  of Civil Aircraft Pneumatic System", *J. Phys.: Conf. Ser.* 2410, 012009 (2022).
- **B16:** Dai, Cui, "Thermal dynamic simulation study of the aircraft ECS laboratory air
  source", *J. Phys.: Conf. Ser.* 2992, 012049 (2025).
- **B18:** Shi, Dong, Liu, Luo, "Study on construction and identification of dynamic model of
  precooler in aviation bleed air system", *J. Northwestern Polytechnical University* 42(6)
  (2024).
- **R1:** Jones, *Aircraft Air Quality and Bleed Air Contamination Detection*, FAA report
  DOT/FAA/TC-21/45 (2022).
- **P2:** Jennions, Ali, Esperon-Miguez, Camacho Escobar, "Simulation of an aircraft
  environmental control system", *Applied Thermal Engineering* 172, 114925 (2020).
