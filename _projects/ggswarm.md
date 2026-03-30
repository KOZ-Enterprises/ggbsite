---
layout: project
title: "GG Swarm"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
description: "A decentralized coordination framework and an emergent behavior engine for UAV swarms."
objective: "Address bottlenecks in centralized drone control by implementing a scalable, fault-tolerant coordination framework using GATs and decentralized consensus logic."
status: "Testing"
order: 1
project-tag: "ggswarm"
tools:
  - name: "Python"
  - name: "PyTorch"
  - name: "NVIDIA Isaac Lab"
  - name: "PyTorch Geometric"
  - name: "SKRL"
  - name: "Google Cloud"
  - name: "GATv2"
  - name: "PPO"
resources:
  - name: "GG Swarm Repository"
    link: "https://github.com/garykuepper/ggSwarm"
    icon: "fa-brands fa-github"

timeline:
  - date: "Weeks 1–4"
    phase: "Proposal and Plan"
    details: "Defining project scope, requirements, and theoretical research foundation."
    completed: true
  - date: "Weeks 5–6 (Feb 5 – Feb 17)"
    phase: "Foundation"
    details: "Install NVIDIA Isaac Lab; configure simulated multirotor assets; finalize graph connectivity logic."
    completed: true
  - date: "Weeks 7–8 (Feb 25 – Mar 24)"
    phase: "Brain Development"
    details: "PPO hover stability and formation control via shared policy (CTDE)."
    completed: true
  - date: "Weeks 9–11 (Mar 25 – Mar 29)"
    phase: "Muscle Refinement"
    details: "MINCO trajectory optimization, CBF safety shields, and SwarmRaft consensus logic. Completed 9 days early."
    completed: true
  - date: "Weeks 12–13 (Mar 30 – Apr 13)"
    phase: "Stress Testing"
    details: "Agent loss simulations, obstacle benchmarks, and scale testing."
    completed: false
  - date: "Weeks 14–15 (Apr 14 – Apr 20)"
    phase: "Showcase Prep"
    details: "RTX tiled rendering, HD demo recording, and final Testing Report."
    completed: false
  - date: "Week 16 (Apr 22 – Apr 24)"
    phase: "Delivery"
    details: "Capstone Festival presentation and portfolio submission."
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

## GNSC 5-Layer Architecture

```mermaid
flowchart BT
    L1["<b>Layer 1: Local Sensing</b><br/>12D body-frame + K×3 neighbor rel_pos"]
    L2["<b>Layer 2: GNN Message Passing</b><br/>2-layer GATv2, K=2 sparse edges, edge cache"]
    L3["<b>Layer 3: Distributed Consensus</b><br/>MINCO min-jerk filter (T=0.04s) + SwarmRaft dropout"]
    L4["<b>Layer 4: Runtime Safety Shields</b><br/>CBF barrier constraints, clamped corrections, MINCO sync"]
    L5["<b>Layer 5: Mission Execution</b><br/>Thrust/moment mapping → physics"]

    L1 --> L2 --> L3 --> L4 --> L5

    style L1 fill:#3498db,color:#fff
    style L2 fill:#2ecc71,color:#fff
    style L3 fill:#f39c12,color:#fff
    style L4 fill:#e74c3c,color:#fff
    style L5 fill:#8e44ad,color:#fff
```

## Action Pipeline

```mermaid
flowchart TD
    A["GNN Policy (L2)<br/>raw actions [N, 4]"] --> B["MINCO min-jerk filter (L3)<br/>smooth C2-continuous actions"]
    B --> C["CBF Safety Filter (L4)<br/>safe actions (barrier-constrained)"]
    C -->|"sync _minco_pos"| B
    C --> D["Thrust/Moment Mapping (L5)<br/>physics forces/torques"]
    D --> E["Isaac Sim Physics"]

    style A fill:#4a90d9,color:#fff
    style B fill:#50b86c,color:#fff
    style C fill:#e74c3c,color:#fff
    style D fill:#8e44ad,color:#fff
    style E fill:#555,color:#fff
```

## Simulation & Performance

The implementation leverages **NVIDIA Isaac Lab**, utilizing GPU-accelerated physics and high-fidelity rendering. This allows agents to learn complex behaviors in parallel across thousands of simulated environments before being tested in challenging scenarios such as cluttered forests and urban canyons.

**Performance Targets:**

* **Mean Formation Error**: < 0.1m during steady flight.
* **Re-sync Latency**: Fill gaps within 2.0s of drone failure.
* **Success Rate**: > 95% across randomized obstacle-dense environments.
* **Decision Latency**: End-to-end latency under 90ms.

## Demo

<!-- markdownlint-disable MD033 -->
<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/mPHrrt0b45c?si=BKt7HmGNt-22kJGY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
<!-- markdownlint-enable MD033 -->
