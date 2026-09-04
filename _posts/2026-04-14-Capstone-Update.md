---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "marl", "skrl", "csumb", "cst489", "cst499"]
title: "Week 14 — Phase 5 Complete, Phase 6 in Flight, Thesis Clarified"
description: "Phase 5 done 12 days ahead of the M4 gate. Cinematic trailer published, research question sharpened, 10 days to submission."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
status: "In Progress"
date: 2026-04-14
project-tag: "ggswarm"
---

Phase 5 done **12 days ahead of the M4 gate**, Phase 6 underway. The
cinematic trailer was edited from the 20 captured clips and published
to YouTube early in the week. The back half shifted to documentation
and framing — making the research question explicit: **coordination,
not stabilization**. 10 days remain to the Apr 24 deadline. No
training is planned; only editing, rehearsal, and submission remain.
<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/toPCBIbLLLM?si=Oy1DaxqxORCvJR57" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
<!--more-->

## Milestones

- **Cinematic trailer published (Apr 8).** Trailer cut in DaVinci /
  Premiere from the 20 clips captured in Phase 5 sub-A and uploaded
  to YouTube with a general-audience description (drones / AI / RL).
- **Phase 5 Testing Report compiled (Apr 8).** Results consolidated
  from Phase 4 M3 gate evidence — checkpoint, metrics, obstacle /
  dropout / scale claims with the corrected body-radius measurement.
- **README polish (Apr 8, Apr 13).** Project banner
  (`docs/assets/banner.jpg`) added; schedule table and status badge
  rolled forward to Phase 6. Followed on Apr 13 by a thesis +
  approach rewrite and a new concepts reference explaining ML / RL /
  GNN for the portfolio audience.
- **Scope clarification (Apr 13).** Added a "Coordination, Not
  Stabilization" section to `docs/design/architecture.md` and a
  matching scope note at the top of the proposal's executive summary.
  States the research question explicitly — *can a learned GNN policy
  replace hand-designed multi-agent coordination logic* — and the
  architectural consequence: the learned policy lives at Layer 2 and
  would feed a classical PID/LQR inner loop in any production
  deployment. Closes a recurring framing gap when explaining the
  project to non-RL audiences.
- **Phase 5 and Phase 6 docs updated** to reflect Phase 5 Complete
  and Phase 6 in progress.

## Next Steps (Week 15, Apr 15 – Apr 21)

- **Presentation narration.** Record voiceover against the
  already-cut cinematic clips — story beats: research question, GNN
  coordination layer, dropout / obstacle / scale results, what worked
  and what didn't. Cinematic videos are already done; this week is
  pure narration + edit pass.
- **Testing Report wrap-up.** Close out
  `docs/project/testing_report.md` — final metrics tables, figures,
  and the corrected body-radius obstacle claims. Written companion to
  the narrated video.
- **Portfolio + Learning Journal final pass** (submission Apr 24).
- **Clean-clone reproducibility check** against README only.
- **Final doc sweep:** changelog close-out, phase doc status sync,
  `v1.0.0-capstone` git tag.

## Challenges

- Framing, not engineering. The recurring gap when explaining the
  project to non-RL audiences was fixed this week by making the
  research question explicit in both the architecture doc and the
  proposal — coordination at Layer 2, not low-level stabilization.
- **10 days remain to the Apr 24 deadline** — Phase 5 finishing 12
  days ahead of the M4 gate leaves the runway clear for narration,
  rehearsal, and submission.
