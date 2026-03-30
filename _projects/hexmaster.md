---
layout: project
title: "HexMaster"
image: "/assets/imgs/project/HexMaster-cropped.png"
description: "A powerful Discord bot and an intelligent logistics coordinator for Foxhole groups."
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
resources:
  - name: "HexMaster Repository"
    link: "https://github.com/garykuepper/HexMaster"
    icon: "fa-brands fa-github"

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

## Project Overview

HexMaster is a powerful Discord bot designed for **Foxhole** logistics groups. It enables seamless stockpile management, cross-map item discovery, and intelligent supply chain comparison using OCR and real-time game data.

The bot follows a **snapshot-based storage** model, preserving full historical data of every stockpile update without ever overwriting.

## Core Features

- **Intelligence Reporting**: Users file reports by uploading stockpile screenshots via `/report`. The bot uses OCR to transcribe item codes, quantities, and crate statuses. Every import creates a time-stamped record for trend analysis.
- **Requisition Orders**: Compare a Shipping Hub against a Receiving Town with automatic Seaport/Warehouse detection (4x multiplier), crate-standardized units, and priority sorting by mission-critical importance.
- **Strategic Reconnaissance**: Global item search across the entire World Conquest map using custom **Cartesian-Staggered** hex math for accurate distance sorting. Syncs 918+ town locations from WarAPI.

## Technical Architecture

- **Discord Bot**: Built with `discord.py` and `SQLAlchemy`
- **Database**: **PostgreSQL** with `asyncpg` for high-performance async queries
- **Sync Logic**: Standalone Python scripts for seeding regions and syncing with **WarAPI**
- **Deployment**: Fully **Dockerized** for consistent execution across environments

## Future Roadmap

- **Logistics Threat Mapping**: Overlay "Front Line" map data to warn drivers about contested territory
- **Supply Drop Alerts**: Automated pings when frontline bases run low on critical supplies
- **Trend Charts**: Visual graphs of stockpile changes over time for strategic planning
