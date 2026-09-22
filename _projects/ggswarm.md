---
layout: project
title: "GG Swarm"
image: "/assets/imgs/project/ggswarm-logo.png"
description: "A decentralized coordination framework transitioning from simulation to real-world drone light shows."
objective: "Deploy an adaptive RL-based execution layer onto physical PX4-based drone swarms for commercial light shows and complex formation maneuvers."
status: "active"
status_detail: "Hardware deployment"
order: 1
project-tag: "ggswarm"
tools:
  - name: "Python"
  - name: "PyTorch"
  - name: "PX4 Autopilot"
  - name: "Skybrush"
  - name: "NVIDIA Isaac Lab"
  - name: "GATv2"
  - name: "PPO"
  - name: "Crazyflie"
resources:
  - name: "GG Swarm Repository"
    link: "https://github.com/garykuepper/ggSwarm"
    icon: "fa-brands fa-github"

timeline:
  - date: "Phase 0"
    phase: "Capstone Baseline"
    details: "Simulation baseline in Isaac Lab"
    completed: true
  - date: "Phase 1"
    phase: "Shared-Scene Training"
    details: "Multi-drone policy convergence"
    completed: false
  - date: "Phase 2"
    phase: "Sim-to-Real Baseline"
    details: "Crazyflie deployment with LPS"
    completed: false
  - date: "Phase 3"
    phase: "Decentralized Assignment"
    details: "P2P ranging & consensus logic"
    completed: false
  - date: "Phase 4"
    phase: "Drone Show Capability"
    details: "Skybrush integration for light shows"
    completed: false
  - date: "Phase 5"
    phase: "Outdoor Deployment"
    details: "Fault tolerance & RTK-GPS integration"
    completed: false
  - date: "Phase 6"
    phase: "Onboard Compute"
    details: "Edge inference & obstacle avoidance"
    completed: false
  - date: "Phase 7"
    phase: "Hardware-Agnostic"
    details: "General-purpose adaptive swarm layer"
    completed: false
---

## Current Phase: GG Swarm Live (Post-Capstone)

Following the successful completion of the academic capstone, the project has transitioned into **GG Swarm Live**, a real-hardware deployment program. The focus is now on taking the decentralized GATv2/PPO policies developed in simulation and deploying them onto physical PX4-based airframes. This creates an adaptive execution layer that can handle formation stability, obstacle avoidance, and decentralized coordination for commercial drone light shows.

### Cinematic Trailer

Cut from twenty clips captured in Phase 5 of the capstone: decentralized
GATv2/PPO policies holding formation, avoiding obstacles and coordinating
in simulation.

<!-- markdownlint-disable MD033 -->
<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/toPCBIbLLLM?si=Oy1DaxqxORCvJR57" title="GG Swarm cinematic trailer" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
<!-- markdownlint-enable MD033 -->

### Roadmap & Development Phases

The project is currently progressing through the following hardware-focused roadmap:

<div class="roadmap-summary">
    <span class="roadmap-summary-item"><strong>Phase 1</strong> In Progress</span>
    <span class="roadmap-summary-sep">&middot;</span>
    <span class="roadmap-summary-item">8 Development Milestones</span>
    <span class="roadmap-summary-sep">&middot;</span>
    <span class="roadmap-summary-item">Hardware Deployment Track</span>
</div>

<div class="roadmap-track">
    <div class="roadmap-phase is-complete">
        <div class="phase-header">
            <span class="phase-badge">Phase 0</span>
            <span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
        </div>
        <h4 class="phase-title">Capstone Baseline</h4>
        <p class="phase-details">v1.0.0-capstone simulation baseline in Isaac Lab.</p>
    </div>

    <div class="roadmap-phase is-active">
        <div class="phase-header">
            <span class="phase-badge">Phase 1 &middot; Active Target</span>
            <span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
        </div>
        <h4 class="phase-title">Shared-Scene Training</h4>
        <p class="phase-details">Multi-drone training in complex shared simulation scenes.</p>
    </div>

    <div class="roadmap-phase">
        <div class="phase-header">
            <span class="phase-badge">Phase 2</span>
            <span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
        </div>
        <h4 class="phase-title">Sim-to-Real Baseline</h4>
        <p class="phase-details">Initial deployment to Crazyflie drones with LPS.</p>
    </div>

    <div class="roadmap-phase">
        <div class="phase-header">
            <span class="phase-badge">Phase 3</span>
            <span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
        </div>
        <h4 class="phase-title">Decentralized Assignment</h4>
        <p class="phase-details">Transitioning to peer-to-peer ranging and consensus logic.</p>
    </div>

    <div class="roadmap-phase">
        <div class="phase-header">
            <span class="phase-badge">Phase 4</span>
            <span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
        </div>
        <h4 class="phase-title">Drone Show Capability</h4>
        <p class="phase-details">Integration with <strong>Skybrush</strong> for expressive shapes and light shows.</p>
    </div>

    <div class="roadmap-phase">
        <div class="phase-header">
            <span class="phase-badge">Phase 5</span>
            <span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
        </div>
        <h4 class="phase-title">Outdoor Deployment</h4>
        <p class="phase-details">Extended fault tolerance and RTK-GPS integration.</p>
    </div>

    <div class="roadmap-phase">
        <div class="phase-header">
            <span class="phase-badge">Phase 6</span>
            <span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
        </div>
        <h4 class="phase-title">Onboard Compute</h4>
        <p class="phase-details">Moving all inference and obstacle avoidance to onboard chips.</p>
    </div>

    <div class="roadmap-phase is-stretch">
        <div class="phase-header">
            <span class="phase-badge">Phase 7</span>
            <span class="status-tag" data-status="stretch"><span class="status-dot"></span>Stretch</span>
        </div>
        <h4 class="phase-title">Hardware-Agnostic</h4>
        <p class="phase-details">General-purpose adaptive swarm execution layer.</p>
    </div>
</div>

---

## Archived Milestone: Academic Capstone (v1.0.0)

This section preserves the original research and simulation work completed for my Computer Science Capstone at CSUMB.

### Project Overview

The capstone addressed a critical bottleneck in the deployment of unmanned aerial vehicle swarms by tackling the inherent vulnerabilities found in centralized control architectures. The project proposed a fully decentralized coordination framework where global formation behavior emerges naturally from local agent interactions.

### Technical Architecture

The architecture was split into the **Brain** (GATv2 spatial reasoning) and the **Muscles** (MINCO trajectory optimization), unified by a GNSC 5-Layer model.

#### GNSC 5-Layer Architecture

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

### Capstone Timeline & Simulation Performance

The simulation phase leveraged **NVIDIA Isaac Lab** for GPU-accelerated physics, achieving high-fidelity results in formation stability and obstacle avoidance.

* **Mean Formation Error**: < 0.1m during steady flight.
* **Success Rate**: > 95% across randomized obstacle-dense environments.

#### Capstone Timeline

* **Weeks 1–4**: Proposal and Plan (Completed)
* **Weeks 5–11**: Core Development (Brain/Muscles) (Completed)
* **Weeks 12–15**: Stress Testing and Showcase Prep (Completed)
* **Week 16**: Capstone Festival Delivery (Completed April 2026)
