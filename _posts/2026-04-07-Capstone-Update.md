---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "marl", "skrl", "csumb", "cst489", "cst499"]
title: "Week 13 — Phase 4 Complete, Showcase Prep Begins 7 Days Early"
description: "Walked back three compounding bugs and a failed experiment to land clean forest navigation. Phase 4 done; Phase 5 starts ahead of schedule."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
status: "In Progress"
date: 2026-04-07
project-tag: "ggswarm"
---

Forest navigation now works cleanly — **0 body penetrations** in 700-step
play with 8 drones weaving through 40cm tree trunks. Phase 4 is complete
and Phase 5 (Showcase Prep) starts 7 days early.

<!--more-->

## Milestones

- **Phase 4 COMPLETE.** All seven M3 criteria pass (with the corrected
  body-radius obstacle metric). Production checkpoint locked in at
  `logs/skrl/ggswarm/p4/2026-04-06_21-09-24_ppo_torch/`.
- **Clean forest run.** p4-revert-4 checkpoint (reward 66.83 / ep_len
  307.74) trains slightly *better* than the Mar 31 baseline. 0 body
  penetrations, +0.037m min body clearance, 0 stuck drones — vs 128
  penetrations and piled-up drones at the start of the week.
- **Reverted the learned-obstacle-avoidance experiment.** Six commits of
  obstacle penalties, obs columns, and curriculum gave zero measurable
  benefit across six GCE runs. Archived to
  `experimental/learned-obstacle-avoidance`; main is back on goal deflection.
- **Boids-style flock alignment for deflection.** Replaced pure radial
  deflection with a 70/30 lateral/radial blend, side picked from mean
  K-nearest neighbor velocity. Drones now coordinate which side of a
  cylinder to dodge.
- **Forest cylinders widened to 40cm diameter** for visual realism (young
  tree trunks); bumped `cbf_obstacle_d_safe` to 0.60m to compensate.

## Forest Play Results (p4-revert-4, 700 steps × 8 drones)

| Metric | broken (start of week) | after fixes |
| :--- | :--- | :--- |
| Body penetrations | 128 (and stuck at start) | **0** |
| Min body clearance | -0.049m | **+0.037m (positive)** |
| Min pair distance | 0.100m | 0.177m |
| Final mean X | -0.28 (didn't traverse) | +6.22 |
| Final min X | -0.88 (drones piled up) | +5.39 (no stuck drones) |
| Stuck drones | 1+ | **0** |

## Key Bugs Squashed

- **Cfg drift regression.** Two retrains collapsed to reward 24/7 vs the
  63 baseline. Env code was character-identical to Mar 31 — culprit was
  100% drift in `cbf_d_safe`, `cbf_max_correction`, `collision_radius`,
  and `dropout_enabled`. A bad recovery attempt also reproduced the p3-16
  unclamped-CBF flip by raising `cbf_max_correction` to 0.50 (true Mar 31
  value was hardcoded `_MAX_CORRECTION = 0.15` in `cbf.py`).
- **Deflection used goal position, not drone position** — drones whose
  slots landed just outside the deflection radius drifted into cylinders
  under formation pressure and were never protected.
- **Base goal advanced unconditionally** — stuck drones had their goal
  run away up to 4.12m ahead, drowning out lateral deflection. Fix:
  cap with new `forest_max_goal_lead = 0.5m`.
- **Historical "0 hits" was a measurement bug.** p4-forest-14/15/16 and
  the M3 gate never included the 0.10m drone radius. Re-measured every
  historical forest run — all grazed cylinders by ~5cm. Re-stated in
  `phase4_stress_testing.md` § 4 and § 5.5.

## Next Steps

- **Phase 5A:** add `--tron` flag to `play.py` that calls
  `setup_tron_environment()` after `gym.make()`. ~30 lines, enables the
  first Tron-styled forest video same session.
- **HD demo capture** with the trees2 forest config and the production
  checkpoint.
- **Phases 5B–D:** Tron visual debug, formation morphing scene sequencer,
  full cinematic trailer (~2:30 at 1080p 60fps).
- **Post-capstone:** downwash penalty for vertical-stacking at spawn
  (real-world fidelity, not on critical path).

## Challenges

- A week of debugging that, on paper, produced one reverted experiment
  and one cfg fix. The real lesson: hardcoded constants in module files
  (`_MAX_CORRECTION` in `cbf.py`) silently became part of the baseline
  and weren't visible in cfg diffs. Promoted them to function parameters
  per the project's "no magic numbers" rule.
- **17 days remain to the Apr 24 deadline** — Phase 5 starting 7 days
  early gives real headroom for the cinematic showcase work.
