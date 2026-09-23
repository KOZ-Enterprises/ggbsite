---
layout: project
title: "HexMaster"
image: "/assets/imgs/project/hexmaster-logo.png"
description: "A powerful Discord bot and an intelligent logistics coordinator for Foxhole groups."
objective: "Enable seamless stockpile management and intelligent supply chain coordination for large-scale logistics operations."
status: "active"
status_detail: "Phase 4 · Guild Testing & Verification"
order: 2
project-tag: "hexmaster"
tools: 
  - name: "Python"
  - name: "PostgreSQL"
  - name: "Docker"
  - name: "SQLAlchemy"
  - name: "OCR"
  - name: "WarAPI"
resources:
  - name: "HexMaster Repository"
    link: "https://github.com/garykuepper/HexMaster"
    icon: "fa-brands fa-github"

reflection: "HexMaster bridges the gap between raw game data and strategic logistics, turning chaotic stockpiles into a searchable, actionable intelligence network."
---

## Project Overview

HexMaster is a powerful Discord bot designed for **Foxhole** logistics groups. It enables seamless stockpile management, cross-map item discovery, and intelligent supply chain comparison using OCR and real-time game data.

The bot follows a **snapshot-based storage** model, preserving full historical data of every stockpile update without ever overwriting.

### Roadmap & Development Phases

The project progresses through the following logistics and bot engineering milestones:

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-summary">
<span class="roadmap-summary-item"><strong>Phase 4</strong> In Progress</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">6 Development Milestones</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">Logistics Automation Track</span>
</div>

<div class="roadmap-track">
<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 1</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Foundation & Core Architecture</h4>
<p class="phase-details">Implemented snapshot-based storage model using PostgreSQL and SQLAlchemy for non-destructive historical tracking.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 2</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">OCR Ingestion & Stockpile Reporting</h4>
<p class="phase-details">Integrated computer vision OCR pipelines to transcribe in-game stockpile screenshots into structured records via <code>/report</code>.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 3</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Supply Chain Algorithms & Hex Math</h4>
<p class="phase-details">Developed requisition algorithms with 4x Seaport multipliers and custom Cartesian-Staggered hex math for accurate distance sorting.</p>
</div>

<div class="roadmap-phase is-active">
<div class="phase-header">
<span class="phase-badge">Phase 4 &middot; Active Target</span>
<span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
</div>
<h4 class="phase-title">Guild Testing & Verification</h4>
<p class="phase-details">Active live testing with Foxhole logistics regiments, verifying OCR edge cases, command response latency, and database concurrency.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 5</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Production Containerization</h4>
<p class="phase-details">Fully Dockerized cloud deployment with automated Postgres health checks, volume backups, and zero-downtime restarts.</p>
</div>

<div class="roadmap-phase is-stretch">
<div class="phase-header">
<span class="phase-badge">Phase 6</span>
<span class="status-tag" data-status="stretch"><span class="status-dot"></span>Stretch</span>
</div>
<h4 class="phase-title">Threat Mapping & WarAPI Live Alerts</h4>
<p class="phase-details">Live WarAPI dynamic map integration to overlay frontline contested roads, driver hazard routing, and automated supply drop pings.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Core Features

- **Intelligence Reporting**: Users file reports by uploading stockpile screenshots via `/report`. The bot uses OCR to transcribe item codes, quantities, and crate statuses. Every import creates a time-stamped record for trend analysis.
- **Requisition Orders**: Compare a Shipping Hub against a Receiving Town with automatic Seaport/Warehouse detection (4x multiplier), crate-standardized units, and priority sorting by mission-critical importance.
- **Strategic Reconnaissance**: Global item search across the entire World Conquest map using custom **Cartesian-Staggered** hex math for accurate distance sorting. Syncs 918+ town locations from WarAPI.

## Technical Architecture

- **Discord Bot**: Built with `discord.py` and `SQLAlchemy`
- **Database**: **PostgreSQL** with `asyncpg` for high-performance async queries
- **Sync Logic**: Standalone Python scripts for seeding regions and syncing with **WarAPI**
- **Deployment**: Fully **Dockerized** for consistent execution across environments
