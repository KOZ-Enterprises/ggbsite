---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "marl", "skrl", "csumb", "cst489", "cst499"]
title: "Week 12 — Phase 3 Complete, 9 Days Early"
description: "Rebuilt Phase 2 from scratch in one day, achieved formation control, then completed Phase 3 ahead of schedule."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
status: "In Progress"
date: 2026-03-31
project-tag: "ggswarm"
---

Rebuilt Phase 2 from scratch, achieved formation control in a single
session, then blew through Phase 3 — finishing 9 days ahead of schedule.

<!--more-->

## Milestones

- **Fresh start on Phase 2 — and finished in one day.** Archived the
  old codebase, rebuilt from the Isaac Lab quadcopter reference, and
  achieved working formation control all in a single session.
- **Phase 2A (hover):** Solved with `DirectRLEnv` + PPO shared policy
  (CTDE). 4 runs to reach ep_len 499/500.
- **Phase 2B (formation):** 8 runs with progressive fixes — from
  formation reward at zero (p2b-1) to stable triangle formation
  with zero crashes (p2b-8).
- **Phase 3: Complete.** MINCO trajectory optimization, CBF safety
  shields, and SwarmRaft consensus logic all integrated — 9 days
  ahead of the original Apr 7 target.

## Key Bugs Squashed

- SKRL bypasses gym wrappers — moved formation logic into the env
- `env_origins` subtraction missing from neighbor observations
- Episode timeout stagger caused drone "despawn" — synced within groups
- Corrected circumradius formula for formation offsets
- Group-aware goal sampling with shared centroid.

## Next Steps

- Begin **Phase 4: Stress Testing** — agent loss simulations,
  obstacle benchmarks, and scale testing

## Challenges

- The Phase 2 rebuild was a tough call but paid off immediately.
  Starting clean from the reference implementation eliminated
  accumulated technical debt from weeks of incremental patches.
