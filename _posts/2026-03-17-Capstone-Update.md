---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "marl", "skrl", "csumb", "cst489", "cst499"]
title: "Week 10 — MAPPO Training Pipeline and Environment Finalization"
description: "Finalized the MARL environment, set up MAPPO in SKRL, and replanned Phase 2."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
status: "In Progress"
date: 2026-03-17
project-tag: "ggswarm"
---

Finalized the MARL environment, set up the MAPPO training pipeline,
and replanned the schedule after falling ~2 weeks behind.

<!--more-->

## Milestones

- **Finalized `GGSwarmMarlEnv`** — multi-agent Crazyflie spawning,
  observation/action spaces, distance-based graph connectivity,
  and reward shaping
- **Set up MAPPO training pipeline** in SKRL,
  validated via `phase1_demo.py`
- **Replanned Phase 2** — ~2 weeks behind the original Mar 3
  target, but back on track to complete within days

## Next Steps

- Complete **Phase 2: Brain Development** by training
  the GATv2 coordination policy
- Transition into **Phase 3: Muscle Refinement** — MINCO
  trajectory optimization and SwarmRaft decentralized consensus

## Challenges

The sheer complexity of integrating Isaac Lab, PyTorch Geometric,
SKRL, and MARL — all while learning them from scratch.
Breaking through those integration hurdles has been tough
but rewarding.

<!-- markdownlint-disable MD033 -->
<div align="center">
  <iframe width="560" height="315"
    src="https://www.youtube.com/embed/W9Ezvd5NAVI?si=jbDCe6Alp3GBb8_Q"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write;
    encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen></iframe>
</div>
<!-- markdownlint-enable MD033 -->
