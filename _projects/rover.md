---
layout: project
title: "ggGridRunner"
image: "/assets/imgs/project/rover-sil.png"
image_caption: "Rover Prototype"
description: "A 4-wheel-steering ground rover: where I learn embedded hardware and firmware before anything flies."
objective: "Build an STM32 rover driven by a PS4 controller over XBee radios, with a safe, checksummed remote link, then heading hold."
status: "active"
status_detail: "Primary project · Milestone 1: Motors spin"
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
  - name: "STM32 (Blue Pill)"
  - name: "Arduino Pro Micro"
  - name: "XBee"
  - name: "PS4 Controller"
  - name: "C++"
  - name: "PlatformIO"
  - name: "3D Printing"
---

## Project Overview

A ground rover with four independently steered wheels (Ackermann, crab and
spin-in-place modes). An STM32 Blue Pill runs the rover; an Arduino Pro
Micro reads a PS4 controller and talks to it over XBee radios. It is the
first rung of my drone projects: learn firmware, IMU drift, motor control
and a failsafe radio link where a mistake doesn't crash.

### Roadmap & Development Phases

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-summary">
<span class="roadmap-summary-item"><strong>Milestone 1</strong> In Progress</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">4 Milestones</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">Ground → Air</span>
</div>

<div class="roadmap-track">
<div class="roadmap-phase is-active">
<div class="phase-header">
<span class="phase-badge">Milestone 1 &middot; Active Target</span>
<span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
</div>
<h4 class="phase-title">Motors spin</h4>
<p class="phase-details">STM32 flashed; motors run forward and reverse with correct throttle scaling, wheels in the air.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Milestone 2</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Safe remote link</h4>
<p class="phase-details">PS4 → XBee → motors, with framed, CRC-checked packets and a dead-man's switch.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">In parallel</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Chassis build</h4>
<p class="phase-details">Suspension designed, printed and assembled, in parallel with the bench milestones.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Milestone 3</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Drives on remote</h4>
<p class="phase-details">Electronics in the chassis, driven around on the remote.</p>
</div>

<div class="roadmap-phase is-stretch">
<div class="phase-header">
<span class="phase-badge">Milestone 4</span>
<span class="status-tag" data-status="stretch"><span class="status-dot"></span>Stretch</span>
</div>
<h4 class="phase-title">Heading hold</h4>
<p class="phase-details">Encoders plus IMU hold a straight line.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Technical Approach

- **Compute**: STM32 Blue Pill on the rover, Arduino Pro Micro in the
  remote, linked by XBee radios
- **Input**: PS4 controller for manual driving
- **Drive**: four driven wheels, each steered by its own servo
  (motor driver still being chosen)
- **Chassis**: 3D-printed custom frame
- **Software**: C++ firmware for motor control and
  wireless command parsing

## Connection to GG Swarm

Like ggSkybit, my hobby drone, this rover is a stepping stone toward
real-world autonomous coordination. The plan is to apply
navigation and consensus algorithms developed in simulation
to physical ground-based platforms.
