---
layout: project
title: "ggPack"
image: "/assets/imgs/project/ggpack-logo.png"
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

## Project Overview

Same reason as [ggBleed](/projects/ggbleed/): aircraft ECS design is the work I know best,
and I wanted something I could actually show. Everything here comes from public data
(published papers and government reports, every value cited), and the models run in
OpenModelica, which is open source, so nothing here depends on a paid tool.

**ggPack** models an airliner air conditioning pack: the system that turns hot bleed air
into cool, dry air for the cabin. The heart of it is a three-wheel bootstrap air cycle
machine, with a compressor, turbine and ram fan on one shaft. Its inlet conditions come
from [ggBleed](/projects/ggbleed/).

### Roadmap & Development Phases

The model progresses through the following milestones:

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-summary">
<span class="roadmap-summary-item"><strong>Phase 2</strong> In Progress</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">4 Development Milestones</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">ECS Simulation Track</span>
</div>

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

## What It Models

- **Shaft dynamics:** a single rotor inertia balancing turbine, compressor and fan torques.
  The inertia is fitted to a published start-up simulation,[^p5] and the shaft mechanical
  efficiency comes from a published component study.[^p8]
- **High-pressure water separation:** primary and secondary heat exchangers, reheater,
  condenser and water extractor, with psychrometrics and evaporative spray of the extracted
  water into the ram duct. Heat-exchanger conductances are derived from published
  effectiveness values.[^p2]
- **Pack control:** flow control valve holding the pack-flow setpoint,[^p18] temperature
  control valve bypass, and ram air doors. Ground ambient inputs follow a published
  fault-simulation study.[^p1]
- **ggBleed coupling:** runs directly on transient bleed outputs from ggBleed, with the
  same published regulation setpoint and precooler band.[^b3]

## Technical Approach

As with ggBleed, the pack is built twice: a causal Python model and an acausal
OpenModelica model. The OpenModelica cruise experiment runs at a published cruise
case.[^p9] It has no controller and models dry air, so it is a structural check, not a
validation.

## Validation

A built-in `validate` command compares the model with three published cases: a ground
reference case,[^p5] a second ground point,[^p18] and two cruise cases.[^p9] Tolerances are
the published mean deviations of an independent model of the same system.[^p19]

Current state, stated plainly: **the pack is not yet calibrated.** Of 19 accuracy checks,
4 are within tolerance (including shaft speed in both ground cases), the cruise
controller reaches both published targets, and no physically impossible state occurs.
Known gaps, such as the condenser's missing wet heat-exchanger model and a water-mass
leak, are pinned as expected-failure tests so they stay visible.

## Results

![Model deviation from the published ground cases, in multiples of the published tolerance, for each pack station](/assets/imgs/project/ggpack-validation.png)

Each point is one published measurement, plotted as the model's deviation in multiples
of the published tolerance.[^p19] Most stations run cold, some by more than ten
tolerances, which is the calibration work ahead.

## Research

The parameters and validation cases come from a curated library of 28 public papers,
reports and theses on aircraft bleed and air conditioning systems, each read and filed
with a short summary and notes on where its data sits. Progress notes and research
findings are posted below as the work goes on.

## Sources & Disclaimer

This is an independent educational project. It is a 737-800-class reference architecture built
only from public sources: peer-reviewed journal papers and a government incident report. No manufacturer, maintenance, training or other
proprietary documents were used, and it is not a replica of any manufacturer's hardware. It is
not affiliated with or endorsed by Boeing, Airbus, or any equipment supplier.

Every model value in the code is tagged to one of the references below, to a derivation written
out from them, to textbook physics, or to a labelled generic modelling assumption. A provenance
checker runs with the test suite and fails the build on any untagged value.

## References

[^p5]: Li, Hu, Sun, Wu (2023). "Dynamic Simulation Model for Three-Wheel Air-Cycle Refrigeration Systems in Civil Aircrafts". *International Journal of Refrigeration* 145: 353–365. §4, Table 1. [doi:10.1016/j.ijrefrig.2022.08.026](https://doi.org/10.1016/j.ijrefrig.2022.08.026)
[^p8]: Jennions, Ali (2023). "Evaluation of Component Level Degradation in the Boeing 737-800 Air Cycle Machine". *Journal of Thermal Science and Engineering Applications* 15(3): 031014. Fig. 3. [doi:10.1115/1.4056510](https://doi.org/10.1115/1.4056510)
[^p2]: Jennions, Ali, Esperon-Miguez, Camacho Escobar (2020). "Simulation of an Aircraft Environmental Control System". *Applied Thermal Engineering* 172: 114925. Table 2. [doi:10.1016/j.applthermaleng.2020.114925](https://doi.org/10.1016/j.applthermaleng.2020.114925)
[^p18]: Li, Hu, Lei (2023). "Performance Simulation and Diagnosis of Faulty States in Air-Cycle Refrigeration Systems in Civil Aircrafts". *International Journal of Refrigeration* 156: 232–242. Table 3. [doi:10.1016/j.ijrefrig.2023.10.006](https://doi.org/10.1016/j.ijrefrig.2023.10.006)
[^p1]: Esperon-Miguez, Jennions, Camacho Escobar, Hanov (2019). "Simulating Faults in a Boeing 737-200 Environmental Control System Using a Thermodynamic Model". *International Journal of Prognostics and Health Management* 10(2). Table 7. [doi:10.36001/ijphm.2019.v10i2.2731](https://doi.org/10.36001/ijphm.2019.v10i2.2731)
[^b3]: Air Accident Investigation Bureau Malaysia (2025). *Aircraft Serious Incident Final Report SI 04/24, Boeing 737-800 9M-LCM*. Ministry of Transport Malaysia. §1.6.2, §2.1.1, Figs. 9–10. [Report (PDF)](https://www.mot.gov.my/en/AAIB%20Statistic%20%20Accident%20Report%20Document/2024/5.%20Final%20Report%20SI%2004-24%209M-LCM%20.pdf)
[^p9]: Chowdhury, Ali, Jennions (2022). "Boeing 737-400 Passenger Air Conditioner Control System Model for Accurate Fault Simulation". *Journal of Thermal Science and Engineering Applications* 14(9): 091008. Table 4. [doi:10.1115/1.4053740](https://doi.org/10.1115/1.4053740)
[^p19]: Li, Hu, Wang, Shen (2026). "Temperature Control Method Optimization for Dual-Pack Air Cycle Refrigeration System in Civil Aircraft Based on Dynamic System Modelling". *International Journal of Refrigeration* 191: 107067. Table 3. [doi:10.1016/j.ijrefrig.2026.107067](https://doi.org/10.1016/j.ijrefrig.2026.107067)
