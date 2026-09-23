---
layout: project
title: "ggSkybit"
image: "/assets/imgs/project/drone2.png"
description: "A quadcopter platform and a custom control logic testbed for swarm collaboration."
objective: "Develop a custom quadcopter platform and flight control testbed for autonomous navigation and swarm algorithms."
status: "planned"
status_detail: "Phase 0 · Conceptualization"
order: 10
project-tag: "drone"
tools: 
  - name: "Solidworks"
  - name: "Onshape"
  - name: "Arduino"
  - name: "C++"
  - name: "Clion"
  - name: "PlatformIO"
---

## Project Overview

A custom-built quadcopter designed as a testbed for control
logic and eventually swarm collaboration. The goal is to go
from bare hardware design through flight controller software
to autonomous navigation — bridging the gap between the
simulated drones in GG Swarm and real-world flight.

The name is a *Tron* nod: Bit is Flynn's little hovering
companion, and one Bit is where a swarm starts. It is part
of ggSkyGrid, my drone projects alongside ggSkylight (light
shows) and GG Swarm.

### Roadmap & Development Phases

The project is currently progressing through the following hardware-focused roadmap:

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-summary">
<span class="roadmap-summary-item"><strong>Phase 0</strong> In Progress</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">8 Development Milestones</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">Avionics & Swarm Track</span>
</div>

<div class="roadmap-track">
<div class="roadmap-phase is-active">
<div class="phase-header">
<span class="phase-badge">Phase 0 &middot; Active Target</span>
<span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
</div>
<h4 class="phase-title">Conceptualization & Architecture</h4>
<p class="phase-details">Avionics layout, power distribution budgeting, and PlatformIO toolchain selection.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 1</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Airframe CAD & Structural Design</h4>
<p class="phase-details">3D-printed and carbon-fiber frame design in SolidWorks/Onshape with optimized thrust-to-weight ratio.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 1.5</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Remote Controller Hardware</h4>
<p class="phase-details">Custom handheld transmitter enclosure, dual-axis hall effect gimbals, and battery integration.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 2</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Flight Controller Bench Build</h4>
<p class="phase-details">Arduino/ESP32 sensor fusion (IMU, barometer) and real-time PID attitude stabilization firmware.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 2.5</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Controller Firmware</h4>
<p class="phase-details">Low-latency telemetry communications, channel calibration, and failsafe watchdog logic.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 3</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Chassis Assembly & Wiring</h4>
<p class="phase-details">ESC wiring, brushless motor mounting, vibration isolation, and physical hardware assembly.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 4</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Hover & Flight Verification</h4>
<p class="phase-details">Tethered thrust tests, dynamic PID tuning, telemetry logging, and autonomous return-to-home.</p>
</div>

<div class="roadmap-phase is-stretch">
<div class="phase-header">
<span class="phase-badge">Phase 5</span>
<span class="status-tag" data-status="stretch"><span class="status-dot"></span>Stretch</span>
</div>
<h4 class="phase-title">Swarm Sim-to-Real Transfer</h4>
<p class="phase-details">Deploying decentralized GATv2/MINCO swarm navigation policies directly onto the physical drone.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Technical Approach

- **Frame**: Custom chassis designed in SolidWorks/Onshape
- **Flight Controller**: Arduino-based with PlatformIO toolchain
- **Control Software**: C++ firmware for motor control,
  sensor fusion, and PID stabilization
- **Remote Controller**: Separate custom-built controller
  with its own hardware and software stack

## Connection to GG Swarm

This project is the physical counterpart to GG Swarm. Once
the simulated swarm coordination policies are validated in
Isaac Lab, the plan is to transfer those algorithms onto
real hardware starting with this drone platform.
