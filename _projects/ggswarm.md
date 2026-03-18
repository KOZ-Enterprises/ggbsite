---
layout: project
title: "GG Swarm"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
description: "A decentralized coordination framework and an emergent behavior engine for UAV swarms."
objective: "Address bottlenecks in centralized drone control by implementing a scalable, fault-tolerant coordination framework using GATs and decentralized consensus logic."
status: "Research"
order: 1
project-tag: "ggswarm"
tools: 
  - name: "PyTorch"
  - name: "NVIDIA Isaac Lab"
  - name: "OpenUSD"
  - name: "Graph Neural Networks"
  - name: "Python"
  - name: "GPU Physics"

timeline:
  - date: "Weeks 1–4"
    phase: "Proposal and Plan"
    details: "Defining project scope, requirements, and theoretical research foundation."
    completed: true
  - date: "Weeks 5–6 (Feb 5 – Feb 17)"
    phase: "Foundation"
    details: "Install NVIDIA Isaac Lab; configure simulated multirotor assets; finalize graph connectivity logic."
    completed: true
  - date: "Weeks 7–8 (Feb 18 – Mar 3)"
    phase: "Brain Development"
    details: "Train the GATv2 policy using Multi-Agent PPO (MAPPO); test basic formation keeping in empty space. Milestone: M1 (Week 8): GNN policy training"
    completed: true
  - date: "Weeks 9–11 (Mar 4 – Mar 24)"
    phase: "Muscle Refinement"
    details: "Integrate MINCO trajectory optimization as a post-processing layer; implement SwarmRaft consensus logic. Milestone: M2 (Week 11, by 3/24): Logic integration"
    completed: false
  - date: "Weeks 12–13 (Mar 25 – Apr 7)"
    phase: "Stress Testing"
    details: "Conduct simulated agent loss tests; benchmark swarm navigation in high-density obstacle environments."
    completed: false
  - date: "Weeks 14–15 (Apr 8 – Apr 21)"
    phase: "Showcase Prep"
    details: "Finalize RTX Tiled Rendering; record HD demonstration; compile results into the final Testing Report. Milestone: M3 (Week 14, by 4/14): Mission success validation; M4 (Week 15, by 4/21): HD showcase + Testing Report + Presentation Draft"
    completed: false
  - date: "Week 16 (Apr 22 – Apr 24)"
    phase: "Delivery"
    details: "Present at Capstone Festival; submit Portfolio and Learning Journals. Milestone: Final Presentation due"
    completed: false

reflection: "This project pushes the boundaries of swarm intelligence by moving away from brittle husband-and-spoke models toward resilient, emergent behaviors."
---

## Project Overview

This capstone project addresses a critical bottleneck in the deployment of unmanned aerial vehicle swarms by tackling the inherent vulnerabilities found in centralized control architectures. Traditional hub and spoke models often suffer from single points of failure and prohibitive communication latencies as swarm sizes scale, making them a liability for high-stakes applications in disaster response, reconnaissance, and agriculture.

To solve this, the project proposes a fully decentralized coordination framework where global formation behavior emerges naturally from local agent interactions. By combining **Graph Neural Networks** for spatial reasoning with advanced **trajectory optimization** for flight dynamics, the system achieves a robust and fault-tolerant solution for complex aerial maneuvers.

## Technical Architecture

The technical architecture is split into two primary functional components described as the **brain** and the **muscles**:

* **The Brain**: Utilizes a Graph Attention Network to establish permutation invariance, allowing an individual drone to process information from an arbitrary number of neighbors without the need for retraining. This establishes a scalable coordination policy where drones maintain spatial awareness through local message passing.
* **The Muscles**: To translate neural network outputs into smooth flight, the project integrates **Minimum Control** trajectory optimization. This ensures that all maneuvers are dynamically feasible and significantly reduces the velocity jitter commonly found in raw reinforcement learning controllers.
* **The Heart/Nerves**: Incorporates **SwarmRaft**, a decentralized consensus logic that allows the swarm to automatically re-synchronize and fill gaps left by failing agents without human intervention.

## Simulation & Performance

The implementation leverages **NVIDIA Isaac Lab**, utilizing GPU-accelerated physics and high-fidelity rendering. This allows agents to learn complex behaviors in parallel across thousands of simulated environments before being tested in challenging scenarios such as cluttered forests and urban canyons.

**Performance Targets:**

* **Mean Formation Error**: < 0.1m during steady flight.
* **Re-sync Latency**: Fill gaps within 2.0s of drone failure.
* **Success Rate**: > 95% across randomized obstacle-dense environments.
* **Decision Latency**: End-to-end latency under 90ms.
