---
layout: project
title: "GG Swarm"
image: "/assets/imgs/project/ggswarm-2.png"
description: "A fully decentralized coordination framework for UAV swarms where global behavior emerges from local agent interactions using Graph Neural Networks and Minimum Control trajectory optimization."
objective: "Address bottlenecks in centralized drone control by implementing a scalable, fault-tolerant coordination framework using GATs and decentralized consensus logic."
status: "In Progress"
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

  - date: "Phase 0"
    phase: "The Setup"
    details: "Setting up the development environment on Google Cloud."
    completed: false
  - date: "Phase 1"
    phase: "Research & Architecture"
    details: "Developing the decentralized coordination framework and spatial reasoning strategy."
    completed: false
  - date: "Phase 2"
    phase: "Brain (GAT) Implementation"
    details: "Training Graph Attention Networks for permutation-invariant local message passing."
    completed: false
  - date: "Phase 3"
    phase: "Muscles & Nerves"
    details: "Integrating Minimum Control optimization and SwarmRaft decentralized consensus."
    completed: false
  - date: "Phase 4"
    phase: "Simulation & Training"
    details: "GPU-accelerated training in Isaac Lab across thousands of parallel environments."
    completed: false

reflection: "This project pushes the boundaries of swarm intelligence by moving away from brittle husband-and-spoke models toward resilient, emergent behaviors."
---

### Project Overview

This capstone project addresses a critical bottleneck in the deployment of unmanned aerial vehicle swarms by tackling the inherent vulnerabilities found in centralized control architectures. Traditional hub and spoke models often suffer from single points of failure and prohibitive communication latencies as swarm sizes scale, making them a liability for high-stakes applications in disaster response, reconnaissance, and agriculture.

To solve this, the project proposes a fully decentralized coordination framework where global formation behavior emerges naturally from local agent interactions. By combining **Graph Neural Networks** for spatial reasoning with advanced **trajectory optimization** for flight dynamics, the system achieves a robust and fault-tolerant solution for complex aerial maneuvers.

### Technical Architecture

The technical architecture is split into two primary functional components described as the **brain** and the **muscles**:

* **The Brain**: Utilizes a Graph Attention Network to establish permutation invariance, allowing an individual drone to process information from an arbitrary number of neighbors without the need for retraining. This establishes a scalable coordination policy where drones maintain spatial awareness through local message passing.
* **The Muscles**: To translate neural network outputs into smooth flight, the project integrates **Minimum Control** trajectory optimization. This ensures that all maneuvers are dynamically feasible and significantly reduces the velocity jitter commonly found in raw reinforcement learning controllers.
* **The Heart/Nerves**: Incorporates **SwarmRaft**, a decentralized consensus logic that allows the swarm to automatically re-synchronize and fill gaps left by failing agents without human intervention.

### Simulation & Performance

The implementation leverages **NVIDIA Isaac Lab**, utilizing GPU-accelerated physics and high-fidelity rendering. This allows agents to learn complex behaviors in parallel across thousands of simulated environments before being tested in challenging scenarios such as cluttered forests and urban canyons.

**Performance Targets:**

* **Mean Formation Error**: < 0.1m during steady flight.
* **Re-sync Latency**: Fill gaps within 2.0s of drone failure.
* **Success Rate**: > 95% across randomized obstacle-dense environments.
* **Decision Latency**: End-to-end latency under 90ms.
