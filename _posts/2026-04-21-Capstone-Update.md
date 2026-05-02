---
layout: post
tags: ["ggswarm", "capstone", "isaac-lab", "marl", "skrl", "csumb", "cst489", "cst499"]
title: "Week 15 — Project Wrapped, Testing Report Locked, Draft Presentation Cut"
description: "Project wrapped for the Capstone Festival. Testing Report closed, draft narration recorded, README polished. 3 days to submission."
project-title: "GG Swarm"
project-url: "/projects/ggswarm/"
image: "/assets/imgs/project/ggswarm-3-cropped.png"
status: "In Progress"
date: 2026-04-21
project-tag: "ggswarm"
---

Project wrapped for the Capstone Festival. Testing Report closed out,
draft presentation video recorded against the Phase 5 cinematic clips,
and the README got a final polish including an embedded 8-drone
highlight GIF. **3 days remain to the Apr 24 deadline** — remaining
work is rehearsal, portfolio/journal submission, and the
`v1.0.0-capstone` tag.

<!--more-->

## Milestones

- **Testing Report finalized** (`docs/project/testing_report.md`).
  Closed out with final metrics tables, figures, and the corrected
  body-radius obstacle claims promised in the Week 14 "Next" section.
  Written companion to the narrated presentation video.
- **Draft presentation video recorded.** Voiceover cut against the
  cinematic clips from Phase 5 sub-A — story beats: research question,
  GNN coordination layer, dropout / obstacle / scale results, what
  worked and what didn't. Draft status; one rehearsal/edit pass
  remains before the final lock.
- **README polish (Apr 21).** Embedded a 6s cinematic highlight GIF
  near the thesis block — source GIF was 19 MB, optimized to 8.7 MB
  via two-pass ffmpeg palette encode (640×432, 15 fps), clearing
  GitHub's 10 MB autoplay threshold so it loops inline without
  click-to-play. Table of Contents restructured, redundant title
  line removed.

## Next Steps (Week 16, Apr 22 – Apr 24)

- **Final presentation rehearsal + edit pass** against the draft
  video.
- **Portfolio + Learning Journal submission.**
- **Capstone Festival presentation** (Apr 24).
- **Post-festival:** `v1.0.0-capstone` git tag, changelog
  close-out, phase doc status sync to Phase 6 Complete.

## Challenges

- GIF size tuning was the only real friction this week — GitHub
  silently swaps autoplaying GIFs for click-to-play thumbnails above
  10 MB, which defeated the "loops inline under the thesis" intent.
  Fixed with a two-pass ffmpeg palette encode to land under the
  threshold without visible quality loss.
- **3 days remain to the Apr 24 deadline** — project itself is
  wrapped; remaining runway is rehearsal and submission, not code.
