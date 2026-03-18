---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "marl", "skrl", "csumb", "cst489", "cst499"]
title: "Capstone Update: MAPPO Training Pipeline and Environment Finalization"
description: "Progress update on finalizing the Isaac Lab MARL environment, MAPPO training pipeline in SKRL, and replanning Phase 2."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
status: "In Progress"
date: 2026-03-17
---


### 1. What project milestones did you accomplish this week? If you're working in a team, please list what you personally contributed, not the project status overall

I finalized the foundational Isaac Lab MARL environment (`GGSwarmMarlEnv`), including multi-agent Crazyflie spawning, observation/action spaces, distance-based graph connectivity, and reward shaping. I also set up the MAPPO training pipeline in SKRL and validated it via `phase1_demo.py`. While I fell behind in getting the initial environment setup and running—meaning Phase 2 completion is roughly two weeks behind my original March 3rd target—I have replanned my schedule and am back on track to complete Phase 2 in the next 2 days. Since this is a solo project, I individually contributed all architecture and codebase development.

<!--more-->

### 2. What is your plan for next week?

My plan is to fully complete Phase 2 (Brain Development) in the next 2 days by successfully training the GATv2 coordination policy. After that, I will transition into Phase 3, which focuses on MINCO trajectory optimization and SwarmRaft decentralized consensus. I know Phase 3 will represent the bulk of the project's work, but my replanned timeline still leaves me sufficient time to complete that task before the final showcase.

### 3. What challenges, if any, are you currently facing in project development? Do you need instructor assistance?

My primary challenge has been the sheer complexity of combining many advanced topics and ideas (Isaac Lab, PyTorch Geometric, SKRL, MARL) while simultaneously having to learn them from scratch. While falling behind on the environment setup was tough, breaking through those integration hurdles has already proven to be a very rewarding experience. At this time, I do not need instructor assistance.

<div align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/W9Ezvd5NAVI?si=jbDCe6Alp3GBb8_Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
