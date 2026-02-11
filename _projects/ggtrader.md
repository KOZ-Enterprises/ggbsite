---
layout: project
title: "ggTrader"
image: "/assets/imgs/project/tradingbot.png"
description: "A professional algorithmic trading bot built with a modular design, featuring Walk-Forward Optimization (WFO), sensitivity analysis, and high-performance Kraken data adapters."
objective: "Create a reproducible and scalable trading research and execution framework for professional traders."
status: "Completed"
order: 3
project-tag: "ggtrader"
tools: 
  - name: "Python"
  - name: "Pandas/NumPy"
  - name: "Kraken API"
  - name: "Jupyter"
  - name: "SQLAlchemy"
  - name: "VectorBT"

timeline:
  - date: "Phase 1: Foundation"
    phase: "Core Engine"
    details: "Built the modular trading engine and simulation logic with a focus on reproducibility."
    completed: true
  - date: "Phase 2: Data & Connectivity"
    phase: "Exchanges & Adapters"
    details: "Implemented Kraken exchange adapters and structured data management for raw/parquet formats."
    completed: true
  - date: "Phase 3: Intelligence"
    phase: "Optimization Suite"
    details: "Developed Walk-Forward Optimization (WFO) and sensitivity analysis scripts for strategy validation."
    completed: true
  - date: "Phase 4: Analytics"
    phase: "Professional Insights"
    details: "Integrated Jupyter Notebooks and ResultsManager for deep-dive visualization and parameter tracking."
    completed: true

reflection: "ggTrader turns individual trading scripts into a professional research lab, ensuring every trade is backed by rigorous statistical validation."
---

### Project Overview

**ggTrader** is a professional algorithmic trading framework designed for high-performance research and execution. It moves away from monolithic scripts toward a modular, scalable architecture that supports complex strategy validation and multi-exchange connectivity.

### Key Features

* **Modular Architecture**: Clean separation between core engine logic, portfolio management, signal indicators, and exchange adapters (Kraken).
* **Reproducible Research**: A dedicated `ResultsManager` and timestamped results folders ensure that every backtest and optimization run is tracked and auditable.
* **Advanced Optimization**:
  * **Walk-Forward Optimization (WFO)**: Finds stable parameters over sliding time windows to reduce overfitting.
  * **Sensitivity Analysis**: Tests how strategy performance reacts to parameter drift, ensuring robustness in changing markets.
* **Professional Analytics**: Deep integration with **Jupyter Notebooks** for interactive visualization and performance deep-dives.

### Directory Structure

The project is organized into a professional package structure:

* `src/ggTrader/`: Core logic including the engine, indicators, and data adapters.
* `scripts/`: Operational runners for standard backtests, WFO, and sensitivity analysis.
* `notebooks/`: For visualization and strategy research.
* `results/`: Structured output storage for all experiments.

### Technical Stack

* **Core**: Python, NumPy, Pandas
* **Backtesting**: High-performance simulation logic (integrated with VectorBT patterns).
* **Data**: Parquet local storage, Kraken API adapters.
* **Optimization**: Custom WFO and sensitivity analysis pipelines.
