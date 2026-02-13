---
layout: post
tags: ["hexmaster", "foxhole", "logistics"]
title: "HexMaster: Entering the Testing Phase"
description: "A powerful Discord bot and a logistics tool for Foxhole groups moving into testing."
project-title: "HexMaster"
project-url: "/projects/hexmaster/"
image: "/assets/imgs/project/HexMaster-cropped.png"
project-tag: "hexmaster"
status: "Testing"
tools:
  - name: "Python"
  - name: "PostgreSQL"
  - name: "OCR"
  - name: "WarAPI"
---

I am excited to announce that **HexMaster** has officially entered its active testing phase!

HexMaster is a powerful Discord bot designed for **Foxhole** logistics groups, enabling seamless stockpile management, cross-map item discovery, and intelligent supply chain comparison. Using a snapshot-based storage model, it preserves full historical data of every stockpile update, ensuring no information is ever lost.

<!--more-->

## What HexMaster Does

* **Intelligence Reporting**: File reports by uploading screenshots of stockpiles via OCR.
* **Requisition Orders**: Compare "Shipping Hubs" against "Receiving Bases" to identify supply gaps.
* **Strategic Reconnaissance**: Find specific items across the entire World Conquest map with proximity sorting.
* **Priority Management**: Track mission-critical items through customizable priority lists.

## Quick Command Reference 🚀

| Category | Command | Description |
| :--- | :--- | :--- |
| **Players** | `/report` | Upload a screenshot to update stockpile data. |
| | `/locate` | Find the nearest source of a specific item. |
| | `/inventory` | View items currently held in a town or base. |
| | `/requisition` | Calculate missing supplies for a destination. |
| **Admins** | `/setup config` | Set server faction and shard. |
| | `/setup priorities` | Load standard priority templates. |

## Future Roadmap

My goal is to make logistics as frictionless as possible. Upcoming features include:

* **Dynamic Inventory Cleanup**: Automatically handling destroyed towns via WarAPI.
* **Logistics Threat Mapping**: Warning drivers if routes pass through contested territory.
* **Trend Charts**: Visualizing stockpile changes over time.

## Acknowledgements

HexMaster relies on critical community-maintained tools including **Foxhole Stockpiles (FS)** for OCR logic, and the official **WarAPI** for real-time map status.

Stay tuned for more updates as testing progresses!
