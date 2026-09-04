---
layout: project
title: "Drone"
image: "/assets/imgs/project/drone2.png"
description: "A quadcopter platform and a custom control logic testbed for swarm collaboration."
objective: "Build a simple drone n stuff yo"
status: "Conceptualization"
order: 10
project-tag: "drone"
tools: 
  - name: "Solidworks"
  - name: "Onshape"
  - name: "Arduino"
  - name: "C++"
  - name: "Clion"
  - name: "PlatformIO"

timeline:
  - date: "Phase 0: Conceptualization"
    phase: "Conceptualization"
    details: "Conceptualize the drone hardware and software architecture."
    completed: false

  - date: "Phase 1: Hardware Design"
    phase: "Design"
    details: "Design the drone chassis and electronics layout."
    completed: false

  - date: "Phase 1.5: Hardware Design of Remote Controller"
    phase: "Design"
    details: "Design the remote controller chassis and electronics layout."
    completed: false

  - date: "Phase 2: Software Bench Build"
    phase: "Software"
    details: "Build the software architecture for the drone."
    completed: false

  - date: "Phase 2.5: Software Bench Build of Remote Controller"
    phase: "Software"
    details: "Build the software architecture for the remote controller."
    completed: false

  - date: "Phase 3: Hardware Build"
    phase: "Hardware"
    details: "Build the drone hardware."
    completed: false

  - date: "Phase 3.5: Hardware Build of Remote Controller"
    phase: "Hardware"
    details: "Build the remote controller hardware."
    completed: false

  - date: "Phase 4: Testing"
    phase: "Testing"
    details: "Test the drone."
    completed: false

  - date: "Phase 4.5: Testing of Remote Controller"
    phase: "Testing"
    details: "Test the remote controller."
    completed: false

  - date: "Phase 5: Integration Testing"
    phase: "Testing"
    details: "Test the drone and remote controller together."
    completed: false

  - date: "Phase 6: Deployment"
    phase: "Deployment"
    details: "Deploy the drone and remote controller."
    completed: false

  - date: "Phase 7: Future"
    phase: "Future"
    details: "Apply algorithms learned from GG Swarm project to the drone."
    completed: false

---

## Project Overview

A custom-built quadcopter designed as a testbed for control
logic and eventually swarm collaboration. The goal is to go
from bare hardware design through flight controller software
to autonomous navigation — bridging the gap between the
simulated drones in GG Swarm and real-world flight.

## Technical Approach

- **Frame**: Custom chassis designed in SolidWorks/Onshape
- **Flight Controller**: Arduino-based with PlatformIO toolchain
- **Control Software**: C++ firmware for motor control,
  sensor fusion, and PID stabilization
- **Remote Controller**: Separate custom-built controller
  with its own hardware and software stack

## Connection to GG Swarm

This project is the physical counterpart to GG Swarm. Once
the simulated swarm coordination policies are validated in
Isaac Lab, the plan is to transfer those algorithms onto
real hardware starting with this drone platform.
