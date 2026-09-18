---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "marl", "skrl", "csumb", "cst489", "cst499"]
title: "Week 11 — Phase 2 Complete, Formation Control Achieved"
description: "Trained drones to maintain stability and formation distance, completing Phase 2."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
status: "In Progress"
date: 2026-03-24
project-tag: "ggswarm"
---

Completed Phase 2 — drones can now maintain stability
and hold formation distance from each other.

<!--more-->

## Milestones

- **Completed Phase 2: Brain Development** — trained drones
  to remain stable and maintain distance from each other
- **Broke formation control into 3 subphases** — going from
  a single hovering drone straight to a large swarm
  created a mess, so I took a more incremental approach

## Next Steps

- Begin **Phase 3: Muscle Refinement** — integrate MINCO
  trajectory optimization and SwarmRaft consensus logic

## Challenges

- Had to regress to basics and decompose formation control
  into smaller subphases. Jumping straight from one drone
  to a full swarm didn't work — incremental scaling was key.
- Google Cloud credit usage is adding up. Looking into
  education credits as an option.
