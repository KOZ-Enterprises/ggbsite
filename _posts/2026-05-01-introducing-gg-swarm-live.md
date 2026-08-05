---
layout: post
title: "Introducing GG Swarm Live: From Simulation to the Sky"
date: 2026-05-01
project-tag: "ggswarm"
tags: [robotics, drones, hardware, engineering]
image: "/assets/imgs/project/ggswarm-3-cropped.png"
---

With the ink finally dry on my Computer Science degree from CSUMB, I’m excited to officially announce the next chapter of my work in autonomous robotics: **GG Swarm Live**.

During my capstone, I focused heavily on the "brains" of the operation—developing a decentralized coordination framework using Graph Attention Networks (GATv2) and Reinforcement Learning (PPO). While the simulation results in NVIDIA Isaac Lab were promising, the ultimate goal has always been to see these algorithms control physical hardware in the real world.

## The Hardware Migration

**GG Swarm Live** is a dedicated program to transition my research from the "digital twin" to real-world airframes. This isn't just about porting code; it's about handling the messy realities of physics, communication latencies, and sensor noise that simulation can only approximate.

The technical stack for this phase is built on industry-standard foundations:

* **PX4 Autopilot**: The core flight stack for our physical airframes.
* **Skybrush**: We are integrating our RL-based execution layer with Skybrush to allow for expressive, choreographed drone light shows.
* **Crazyflie**: Initial sim-to-real baselining will take place on these micro-drones in a controlled indoor environment before scaling to larger outdoor platforms.

## Beyond the Capstone

The capstone gave us a v1.0.0 baseline. The roadmap for **GG Swarm Live** expands this into eight distinct phases, ranging from multi-drone shared-scene training to fully autonomous, obstacle-aware navigation in outdoor environments.

One of the most exciting commercial applications we're exploring is the "backyard light show" capability. By combining decentralized swarm logic with a user-friendly interface, we hope to make high-end aerial displays accessible for local events and creative displays. Crucially, the decentralized nature of the swarm adds a robust layer of safety; by removing single points of failure, we can ensure more reliable behavior around spectators and audience members.

## Follow the Journey

I’ve updated the [GG Swarm Project Page](/projects/ggswarm/) to serve as the central hub for this new phase. It now includes the full hardware roadmap and a section archiving the original academic research.

This degree wasn't a transition to becoming an engineer—I've been one since 2012—but rather a significant upgrade to my toolkit. The build is just beginning. Stay tuned for more logs as we take these swarms to the sky.

<em>Gary</em>
