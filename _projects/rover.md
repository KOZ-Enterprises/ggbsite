---
layout: project
title: "ggGridRunner"
image: "/assets/imgs/project/rover-sil.png"
image_caption: "Rover Prototype"
description: "A smart RC car and a foundational platform for autonomous navigation experiments."
objective: "Develop a ground rover with wireless telemetry and progressive autonomous navigation capabilities."
status: "planned"
status_detail: "Phase 0 · Conceptualization"
reflection: "Rover has taught me about wireless communication, embedded motor control, and practical hardware debugging. It's also helping lay the foundation for future robotics projects."
resources:
  - name: "GitHub Project Page"
    link: "https://github.com/users/garykuepper/projects/2/"
    icon: "fas fa-code"
  - name: "ggGridRunner Repository"
    link: "https://github.com/garykuepper/ggGridRunner"
    icon: "fa-brands fa-github"
order: 9
project-tag: "rover"
tools: 
  - name: "Arduino"
  - name: "XBee"
  - name: "PS4 Controller" 
  - name: "DRV8871 Motor Drivers"
  - name: "C++"
  - name: "3D Printing"
---

## Project Overview

A smart RC car built as a foundational platform for autonomous
navigation experiments. Starting with wireless joystick control
and working toward self-driving capabilities using lessons
from the GG Swarm project.

### Roadmap & Development Phases

The project is currently progressing through the following hardware-focused roadmap:

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-summary">
<span class="roadmap-summary-item"><strong>Phase 0</strong> In Progress</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">8 Development Milestones</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">UGV & Robotics Track</span>
</div>

<div class="roadmap-track">
<div class="roadmap-phase is-active">
<div class="phase-header">
<span class="phase-badge">Phase 0 &middot; Active Target</span>
<span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
</div>
<h4 class="phase-title">Conceptualization & Architecture</h4>
<p class="phase-details">Kinematics modeling, differential drive power budgeting, and embedded controller architecture.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 1</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Chassis CAD & Mechanical Layout</h4>
<p class="phase-details">3D-printed modular chassis, dual DRV8871 H-bridge motor driver brackets, and LiPo battery bay.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 1.5</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Remote Controller Hardware</h4>
<p class="phase-details">Custom handheld wireless transmitter enclosure with dual analog joysticks and mode switches.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 2</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Firmware Bench Build</h4>
<p class="phase-details">Arduino C++ command parsing, differential drive steering curves, and failsafe watchdog timer.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 2.5</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Wireless Telemetry Pipeline</h4>
<p class="phase-details">Bidirectional XBee serial packet transmission, signal quality monitoring, and control latency testing.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 3</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Prototype Assembly & Road Testing</h4>
<p class="phase-details">Physical assembly, motor driver heat dissipation verification, and outdoor rough-terrain drive tests.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 4</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Obstacle Ranging & Reactive Steering</h4>
<p class="phase-details">Integrating ultrasonic and Time-of-Flight (ToF) distance sensors for collision avoidance.</p>
</div>

<div class="roadmap-phase is-stretch">
<div class="phase-header">
<span class="phase-badge">Phase 5</span>
<span class="status-tag" data-status="stretch"><span class="status-dot"></span>Stretch</span>
</div>
<h4 class="phase-title">Ground Swarm Coordination</h4>
<p class="phase-details">Porting multi-agent consensus and decentralized path-following algorithms from GG Swarm research.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Technical Approach

- **Compute**: Arduino-based control with XBee wireless
  communication
- **Input**: PS4 controller for manual driving
- **Drive**: DRV8871 motor drivers for differential steering
- **Chassis**: 3D-printed custom frame
- **Software**: C++ firmware for motor control and
  wireless command parsing

## Connection to GG Swarm

Like ggSkybit, my hobby drone, this rover is a stepping stone toward
real-world autonomous coordination. The plan is to apply
navigation and consensus algorithms developed in simulation
to physical ground-based platforms.
