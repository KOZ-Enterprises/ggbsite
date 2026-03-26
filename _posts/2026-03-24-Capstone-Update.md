---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "marl", "skrl", "csumb", "cst489", "cst499"]
title: "Capstone Update: "
description: ""
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
status: "In Progress"
date: 2026-03-24
---


## 1. What project milestones did you accomplish this week?

- Phase 2 of my project which is stability and formation control.  Was able to train drones to remain stable and maintain distance from each other.

<!--more-->

## 2. What is your plan for next week?

- Begin Phase 3 which is to fine tune the swarm to add MINCO which helps filter out trajectories and incorporate SwarmRaft so the swarm can generate a consensus. 

## 3. What challenges, if any, are you currently facing in project development? Do you need instructor assistance?


I had to regress to basics and break up my basic formation control into 3 subphases.  I initially tried to go from a single hovering drone to a large swarm right away and I ended up just creating a mess.  

I am using quite a bit of my google cloud credit, and wonder if there was a way to get education credits? 

## Current Schedule

| Weeks | Dates                                | Phase                | Activity                                                                                              | Milestone                                        |
| ----- | ------------------------------------ | -------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| 5–6   | Feb 5 – Feb 17                       | 1. Foundation        | Install NVIDIA Isaac Lab; configure simulated multirotor assets; finalize graph connectivity logic.   | -                                                |
| 7–8   | ~~Feb 18 – Mar 3~~ → Feb 25 – Mar 24 | 2. Brain Development | Train GATv2 with MAPPO; test formation in empty space.                                                | ~~M1 Week 8~~ → M1 Week 11                       |
| 9–11  | ~~Mar 4 – Mar 24~~ → Mar 25 – Apr 7  | 3. Muscle Refinement | Integrate MINCO post-processing and SwarmRaft consensus logic.                                        | ~~M2 Week 11 (3/24)~~ → M2 Week 13 (4/7)         |
| 12–13 | Apr 8 – Apr 14                       | 4. Stress Testing    | Conduct simulated agent loss tests; benchmark swarm navigation in high-density obstacle environments. | M3 (Week 14, 4/14): Mission success validation   |
| 14–15 | Apr 14 – Apr 21                      | 5. Showcase Prep     | Finalize RTX tiled rendering; record HD demo; compile results.                                        | M4 (Week 15, 4/21): HD showcase + Testing Report |
| 16    | Apr 22 – Apr 24                      | 6. Delivery          | Present at Capstone Festival; submit Portfolio and Learning Journals.                                 | **Final Presentation due 4/24/26**               |