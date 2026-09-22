---
layout: project
title: "ggTrader"
image: "/assets/imgs/project/ggtrader-logo.png"
description: "An algorithmic trading bot and a research framework for professional strategy development."
objective: "Create a reproducible and scalable trading research and execution framework for professional traders."
status: "active"
status_detail: "Phase 4 · Analytics & Optimization"
order: 3
project-tag: "ggtrader"
tools: 
  - name: "Python"
  - name: "Pandas/NumPy"
  - name: "Kraken API"
  - name: "Jupyter"
  - name: "SQLAlchemy"
  - name: "VectorBT"
resources:
  - name: "ggTrader Repository"
    link: "https://github.com/garykuepper/ggTrader"
    icon: "fa-brands fa-github"

timeline:
  - date: "Phase 1"
    phase: "Core Engine"
    details: "Modular simulation framework & vectorized patterns"
    completed: true

  - date: "Phase 2"
    phase: "Exchanges & Adapters"
    details: "Kraken API integration & Parquet storage pipelines"
    completed: true

  - date: "Phase 3"
    phase: "Optimization Suite"
    details: "Walk-Forward Optimization & sensitivity analysis"
    completed: true

  - date: "Phase 4"
    phase: "Professional Insights"
    details: "Jupyter visualization & ResultsManager audit trails"
    completed: false

  - date: "Phase 5"
    phase: "Execution Architecture"
    details: "Position sizing algorithms & risk shields"
    completed: false

  - date: "Phase 6"
    phase: "Live Paper Validation"
    details: "Shadow order execution & latency tracking"
    completed: false

  - date: "Phase 7"
    phase: "Production Deployment"
    details: "Multi-strategy cloud execution nodes"
    completed: false

reflection: "ggTrader turns individual trading scripts into a professional research lab, ensuring every trade is backed by rigorous statistical validation."
---

## Project Overview

**ggTrader** is a professional algorithmic trading framework designed
for high-performance research and execution. It moves away from
monolithic scripts toward a modular, scalable architecture that
supports complex strategy validation and multi-exchange connectivity.

### Roadmap & Development Phases

The framework progresses through the following research and execution milestones:

<!-- markdownlint-disable MD033 MD046 -->
<div class="roadmap-summary">
<span class="roadmap-summary-item"><strong>Phase 4</strong> In Progress</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">7 Development Milestones</span>
<span class="roadmap-summary-sep">&middot;</span>
<span class="roadmap-summary-item">Quant Strategy Track</span>
</div>

<div class="roadmap-track">
<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 1</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Foundation & Core Engine</h4>
<p class="phase-details">Built the modular trading engine and reproducible simulation logic using VectorBT patterns.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 2</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Data Ingestion & Exchange Adapters</h4>
<p class="phase-details">Kraken REST/WebSocket exchange adapters and high-speed partitioned Parquet data stores.</p>
</div>

<div class="roadmap-phase is-complete">
<div class="phase-header">
<span class="phase-badge">Phase 3</span>
<span class="status-tag" data-status="complete"><span class="status-dot"></span>Complete</span>
</div>
<h4 class="phase-title">Optimization & Walk-Forward Testing</h4>
<p class="phase-details">Implemented Walk-Forward Optimization (WFO) and multi-dimensional parameter sensitivity analysis.</p>
</div>

<div class="roadmap-phase is-active">
<div class="phase-header">
<span class="phase-badge">Phase 4 &middot; Active Target</span>
<span class="status-tag" data-status="active"><span class="status-dot"></span>Active</span>
</div>
<h4 class="phase-title">Interactive Analytics & Audit Trails</h4>
<p class="phase-details">Deep Jupyter Notebook visual tooling and ResultsManager timestamped run archives.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 5</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Execution & Risk Architecture</h4>
<p class="phase-details">Dynamic position sizing algorithms, drawdown guards, and order-book impact simulations.</p>
</div>

<div class="roadmap-phase">
<div class="phase-header">
<span class="phase-badge">Phase 6</span>
<span class="status-tag" data-status="planned"><span class="status-dot"></span>Planned</span>
</div>
<h4 class="phase-title">Live Paper Validation</h4>
<p class="phase-details">Real-time shadow execution against live order books with execution slippage tracking.</p>
</div>

<div class="roadmap-phase is-stretch">
<div class="phase-header">
<span class="phase-badge">Phase 7</span>
<span class="status-tag" data-status="stretch"><span class="status-dot"></span>Stretch</span>
</div>
<h4 class="phase-title">Production Cloud Deployment</h4>
<p class="phase-details">Containerized multi-strategy execution nodes with automated failover and telemetry pings.</p>
</div>
</div>
<!-- markdownlint-enable MD033 MD046 -->

## Core Features

- **Modular Architecture**: Clean separation between core engine
  logic, portfolio management, signal indicators, and exchange
  adapters (Kraken).
- **Reproducible Research**: A dedicated `ResultsManager` and
  timestamped results folders ensure that every backtest and
  optimization run is tracked and auditable.
- **Walk-Forward Optimization (WFO)**: Finds stable parameters
  over sliding time windows to reduce overfitting.
- **Sensitivity Analysis**: Tests how strategy performance reacts
  to parameter drift, ensuring robustness in changing markets.
- **Professional Analytics**: Deep integration with **Jupyter
  Notebooks** for interactive visualization and performance
  deep-dives.

## Technical Architecture

- **Core**: Python, NumPy, Pandas
- **Backtesting**: High-performance simulation logic
  (integrated with VectorBT patterns)
- **Data**: Parquet local storage, Kraken API adapters
- **Optimization**: Custom WFO and sensitivity analysis pipelines
