---
layout: project
title: "HexMaster"
image: "/assets/imgs/project/HexMaster-cropped.png"
description: "A powerful Discord bot for Foxhole logistics groups featuring snapshot-based stockpile management, OCR-driven intelligence reporting, and automated requisition gap analysis."
objective: "Enable seamless stockpile management and intelligent supply chain coordination for large-scale logistics operations."
status: "Testing"
order: 2
project-tag: "hexmaster"
tools: 
  - name: "Python"
  - name: "PostgreSQL"
  - name: "Docker"
  - name: "SQLAlchemy"
  - name: "OCR"
  - name: "WarAPI"

timeline:
  - date: "Phase 1: Foundation"
    phase: "Core Architecture"
    details: "Implemented snapshot-based storage model using PostgreSQL and SQLAlchemy for historical data tracking."
    completed: true
    
  - date: "Phase 2: Intelligence"
    phase: "OCR & Reporting"
    details: "Integrated OCR services to transcribe stockpile screenshots into structured data via /report commands."
    completed: true

  - date: "Phase 3: Logistics"
    phase: "Supply Chain Logic"
    details: "Developed requisition algorithms with 4x hub multipliers and Cartesian-Staggered hex math for distance sorting."
    completed: true

  - date: "Phase 4: Testing"
    phase: "Bot Testing"
    details: "Deployed the trading bot to a production environment."
    completed: false

  - date: "Phase 5: Deployment"
    phase: "Bot Deployment"
    details: "Deployed the trading bot to a production environment."
    completed: false

  - date: "Phase 6: Future"
    phase: "Threat Mapping"
    details: "Planned integration with live WarAPI map data to overlay logistics threat levels and automated alerts."
    completed: false

reflection: "HexMaster bridges the gap between raw game data and strategic logistics, turning chaotic stockpiles into a searchable, actionable intelligence network."
---

HexMaster is a powerful Discord bot designed for **Foxhole** logistics groups. It enables seamless stockpile management, cross-map item discovery, and intelligent supply chain comparison using OCR and real-time game data.

The bot follows a **snapshot-based storage** model, preserving full historical data of every stockpile update without ever overwriting.

### Core Features (MVP)

#### 1. Intelligence Reporting

- **Filing Reports**: Users file intelligence reports by uploading screenshots of stockpiles via the `/report` slash command.
- **Deep Processing**: The bot uses an OCR service to transcribe item codes, names, total quantities, and crate statuses.
- **Historical snapshots**: Every import creates a new time-stamped record for trend analysis.

#### 2. Requisition Orders

- **Supply Chain Decisioning**: Compare a "Shipping Hub" (e.g., Seaport/Warehouse) against a "Receiving Town/Base".
- **Hub Detection**: Automatically detects Seaports and Storage Warehouses to apply a **4x requirement multiplier**.
- **Crate-First Units**: All quantities are standardized to "Crates" for easy logistics math.
- **Priority Logic**: Sorts items by mission-critical importance and highlights shortages.

#### 3. Strategic Reconnaissance

- **Global Search**: Find which stockpiles currently hold a specific item across the entire World Conquest map.
- **Accurate Hex Math**: Uses a custom **Cartesian-Staggered** coordinate system to calculate distances in physical hex units.
- **Proximity Sorting**: Results are sorted by distance from your reference town.
- **Sync with WarAPI**: Automatically fetches 918+ town locations and marker types (Major/Minor) from the official Foxhole servers.

### Architecture & Tech Stack

- **Discord Bot**: Built with `discord.py` and `SQLAlchemy`.
- **Database**: **PostgreSQL** with `asyncpg` for high-performance async queries.
- **Sync Logic**: Standalone Python scripts for seeding regions and syncing with **WarAPI**.
- **Deployment**: Fully **Dockerized** for consistent execution across environments.

### Future Roadmap

- **Logistics Threat Mapping**: Overlay current "Front Line" map data to warn logistics drivers if a `/locate` result requires driving through contested or enemy-held territory.
- **Supply Drop Alerts**: Automated pings when a critical frontline base is low on Soldier Supplies or AT weapons.
- **Trend Charts**: Visual graphs of stockpile changes over time for strategic planning.
