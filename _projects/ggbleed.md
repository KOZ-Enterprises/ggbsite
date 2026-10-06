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

## Project Overview

Aircraft ECS design is the work I know best, and I wanted something I could actually
show. So this is built only from public data: published papers, theses and government
reports, with every value cited. The models run in OpenModelica, which is open source, so
nothing here depends on a paid tool.

**ggBleed** models how an airliner's engines supply bleed air to the aircraft: hot,
high-pressure air taken from the engine compressor, regulated, and cooled before it goes
to air conditioning, anti-ice and pressurization. It feeds directly into
[ggPack](/projects/ggpack/), the air conditioning pack model.

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

## What It Models

- **Compressible gas dynamics:** ideal-gas properties, isentropic and choked/unchoked
  orifice flow, and the standard atmosphere.
- **Precooler:** ε-NTU crossflow heat exchanger with a lumped core thermal mass. The core
  time constant comes from an identified precooler model,[^b18] and the conductance is solved
  from two published flight-test cases.[^b13]
- **Valves and control:** high-stage valve, a pressure-regulating shutoff valve (PRSOV)
  holding a gauge setpoint, and a fan air valve driven by an outlet thermostat. The setpoint,
  control band, temperature limit and overheat trip come from an incident investigation
  report,[^b3] and the sensor and valve lags from a laboratory bleed rig.[^b10]
- **Flight mission:** ground, takeoff, climb, cruise with a wing anti-ice step, idle
  descent and approach, rebuilt from published engine port states,[^r1][^b16] a published
  cruise point[^p2] and the standard atmosphere.

## Technical Approach

The same system is built twice: a causal Python model and an acausal OpenModelica model,
so the two paradigms can be compared side by side. The OpenModelica cruise experiment
closes the plant with boundary sources and sinks and runs at the same published cruise
point as the Python mission.[^p2]

## Validation

So far the model is checked against published *limits*, not fitted to measured data:

- Through climb and cruise, the sensed precooler outlet stays inside the published control
  band,[^b3] the intermediate stage supplies cruise, the high stage takes over in descent, and
  nothing trips.
- The PRSOV regulates to the published setpoint, and the temperature limit and trip act at
  the published values.[^b3]
- The precooler's conductance is solved so the two flight-test cases land in that band.[^b13]

The OpenModelica cruise experiment settles on the same setpoint and band. Measured-data
validation cases are catalogued in the research library and are the next phase.

## Results

![Sensed precooler outlet temperature across the reference mission, against the published control band, temperature limit and overheat trip](/assets/imgs/project/ggbleed-mission.png)

The sensed outlet temperature holds the published 390–440 °F band through climb and
cruise[^b3] and dips below it at idle power in descent. It never reaches the temperature
limit or the overheat trip.

## Research

The parameters and validation cases come from a curated library of 28 public papers,
reports and theses on aircraft bleed and air conditioning systems, each read and filed
with a short summary and notes on where its data sits. Progress notes and research
findings are posted below as the work goes on.

## Sources & Disclaimer

This is an independent educational project. It is a 737-800-class reference architecture built
only from public sources: peer-reviewed papers, a doctoral dissertation, an FAA technical report and a government incident report. No manufacturer, maintenance, training or other
proprietary documents were used, and it is not a replica of any manufacturer's hardware. It is
not affiliated with or endorsed by Boeing, Airbus, or any equipment supplier.

Every model value in the code is tagged to one of the references below, to a derivation written
out from them, to textbook physics, or to a labelled generic modelling assumption. A provenance
checker runs with the test suite and fails the build on any untagged value.

## References

[^b18]: Shi, Dong, Liu, Luo (2024). "Study on Construction and Identification of Dynamic Model of Precooler in Aviation Bleed Air System". *Journal of Northwestern Polytechnical University* 42(6): 1089. Table 2, Eq. 19. [doi:10.1051/jnwpu/20244261089](https://doi.org/10.1051/jnwpu/20244261089)
[^b13]: Peng (2022). "Research and Verification on the Solution of Bleed Air Temperature Deviation of Civil Aircraft Pneumatic System". *Journal of Physics: Conference Series* 2410: 012009. Table 1. [doi:10.1088/1742-6596/2410/1/012009](https://doi.org/10.1088/1742-6596/2410/1/012009)
[^b3]: Air Accident Investigation Bureau Malaysia (2025). *Aircraft Serious Incident Final Report SI 04/24, Boeing 737-800 9M-LCM*. Ministry of Transport Malaysia. §1.6.2, §2.1.1, Figs. 9–10. [Report (PDF)](https://www.mot.gov.my/en/AAIB%20Statistic%20%20Accident%20Report%20Document/2024/5.%20Final%20Report%20SI%2004-24%209M-LCM%20.pdf)
[^b10]: Shang (2011). *Fault Detection and Isolation in an Aircraft Engine Bleed Air System*. PhD dissertation, Ryerson University. Ch. 2 and Ch. 5. [doi:10.32920/ryerson.14646084](https://doi.org/10.32920/ryerson.14646084)
[^r1]: Jones (2022). *Aircraft Air Quality and Bleed Air Contamination Detection*. FAA report DOT/FAA/TC-21/45. Table 56. [ROSA P](https://rosap.ntl.bts.gov/view/dot/62770)
[^b16]: Dai, Cui (2025). "Thermal Dynamic Simulation Study of the Aircraft ECS Laboratory Air Source". *Journal of Physics: Conference Series* 2992: 012049. §2, Tables 1–2. [doi:10.1088/1742-6596/2992/1/012049](https://doi.org/10.1088/1742-6596/2992/1/012049)
[^p2]: Jennions, Ali, Esperon-Miguez, Camacho Escobar (2020). "Simulation of an Aircraft Environmental Control System". *Applied Thermal Engineering* 172: 114925. Table 2. [doi:10.1016/j.applthermaleng.2020.114925](https://doi.org/10.1016/j.applthermaleng.2020.114925)
