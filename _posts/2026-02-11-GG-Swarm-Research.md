---
layout: post
tags: ["ggswarm", "capstone", "csumb","cst489","cst499"]
title: "Project Launch: GG Swarm - Decentralized UAV Coordination"
description: "A research overview and a project launch for decentralized UAV coordination."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3.png"
project-tag: "ggswarm"
status: "In Progress"
tools:
  - name: "NVIDIA Isaac Lab"
  - name: "PyTorch"
  - name: "Graph Neural Networks"
  - name: "Google Cloud"
---

This post introduces the [**GG Swarm**]({{ page.project-url }}) capstone project, a decentralized coordination framework designed to overcome the single point of failure and high latency of centralized control in large UAV swarms. By integrating Graph Neural Networks (GNNs) for spatial reasoning with advanced Minimum Control (MINCO) trajectory optimization, the system achieves robust, fault-tolerant behavior for high-stakes applications.

<!--more-->

## Executive Summary

The GG Swarm architecture comprises the **"brain,"** a Graph Attention Network (GATv2) that enables scalable, permutation-invariant spatial awareness via local message passing, and the **"muscles,"** which use trajectory optimization to ensure dynamically feasible maneuvers with reduced velocity jitter. To ensure high-fidelity testing and training, implementation occurs in **NVIDIA Isaac Lab**, utilizing GPU-accelerated simulation on **Google Cloud** to perform high-scale training across thousands of environments.

## Project Goals and Objectives

Our mission is to build a swarm that is not just smart, but resilient.

### Key Goals

- **G1**: Establish a scalable coordination policy using graph-based learning.
- **G2**: Achieve mathematically optimal flight paths for swarm agents.
- **G3**: Ensure mission continuity despite individual drone failures or signal loss.
- **G4**: Create a professional-grade visual validation of swarm autonomy.

### Key Objectives

- **O1**: Implement a GATv2 control policy in Isaac Lab maintaining a mean formation error < 0.1m.
- **O2**: Integrate MINCO trajectory optimization to reduce velocity jitter by at least 20%.
- **O3**: Implement **SwarmRaft** consensus logic to automatically re-sync the swarm within 2.0s of a failure.
- **O4**: Produce a high-definition demonstration video of 20+ agents navigating cluttered environments.

## Approach & Methodology

The project employs a **"Centralized Training, Decentralized Execution" (CTDE)** reinforcement learning workflow within a 5-layer architecture:

1. **Local Sensing**: Simulated LiDAR/IMU data collection in Isaac Lab.
2. **GNN Message Passing**: Information aggregation via GATv2 for spatial awareness.
3. **Distributed Consensus**: Agents align on global objectives through local interactions.
4. **Runtime Safety Shields**: Control Barrier Functions (CBFs) to ensure zero inter-agent collisions.
5. **Mission Execution**: Execution of high-level commands like "Change Formation Shape."

## Timeline & Milestones

| Phase | Activity | Weeks |
| :--- | :--- | :--- |
| **Proposal & Plan** | Defining project scope, requirements, and research foundation. | 1–4 |
| **Foundation** | Install Isaac Lab; configure assets; finalize connectivity logic. | 5–6 |
| **Brain Development** | Train GATv2 policy using PPO; test basic formation keeping. | 7–8 |
| **Muscle Refinement** | Integrate MINCO optimization; implement SwarmRaft consensus. | 9–10 |
| **Stress Testing** | Conduct agent loss tests; benchmark in high-density obstacles. | 11–12 |
| **Showcase Prep** | Finalize RTX Tiled Rendering; record HD demonstration. | 13–15 |
| **Delivery** | Present at Capstone Festival; submit Portfolio. | 16 |

**Key Milestones:**

- **M1 (Week 8):** Successful training of GNN coordination policy.
- **M2 (Week 10):** Integration of trajectory refinement and fault-tolerant consensus.
- **M3 (Week 14):** Validation of mission success rates (>95%) in cluttered environments.
- **M4 (Week 15):** Completion of high-fidelity 1080p visual showcase.

## Resources & Platform

Due to the massive hardware requirements for parallel training, we are utilizing **Google Cloud** (Brev or AWS Batch) for high-environment-count training and 4K rendering. The development stack includes:

- **Platform**: NVIDIA Isaac Sim 5.1 / Isaac Lab 2.3
- **Deep Learning**: PyTorch 2.5+
- **Hardware**: Local RTX 3070 for development, Cloud GPUs for training.

Stay tuned for updates as we progress through Brain Development!
