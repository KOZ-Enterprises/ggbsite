---
layout: post
title: "Simulating Swarm Behavior in Gazebo"
date: 2026-02-01
tags: [drone-swarm, simulation, ros2]
description: "Initial tests of the flocking algorithm in a physics-based simulation environment."
---

Successfully implemented the Reynolds flocking algorithm (Alignment, Cohesion, Separation) within the Gazebo simulation.
The drones are able to maintain formation while navigating through a generated obstacle field.

Next steps involve tuning the PID controllers for smoother trajectory tracking and integrating the communication layer to simulate packet loss.
