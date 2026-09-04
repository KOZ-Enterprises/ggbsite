---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "drone", "csumb", "cst489", "cst499"]
title: "Week 9 — Isaac Lab Integration and Brain Development"
description: "Set up Isaac Sim/Lab locally and ran the first Crazyflie drone in simulation."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3.png"
status: "In Progress"
date: 2026-03-10
project-tag: "ggswarm"
---

Set up the Isaac Lab development environment locally and got my first Crazyflie drone running in simulation — laying the groundwork for multi-agent training.

<!--more-->

## Milestones

- **Installed NVIDIA Isaac Sim and Isaac Lab** on my local machine, verified hardware can handle the development phase. Large-scale sims (many drones) will run on Google Cloud.
- **Ran the Crazyflie drone model** in Isaac Sim successfully. First attempt at manual flight control ended in a crash — the learning starts!

## Next Steps

- Get familiar with the Isaac Lab API for drone control and training workflows
- Begin **Phase 2: Brain Development** — start training the GATv2 coordination policy using PPO

## Challenges

The main hurdle is the Isaac Lab API learning curve. Working through tutorials to build familiarity before jumping into the training pipeline.
