---
layout: project
title: "Gary Gigabytes Website"
image: "/assets/imgs/ggbytes/ggbytes-page.png"
description: "A technical portfolio and a central hub for documenting my engineering journey."
objective: "Develop a high-performance, responsive workstation for documenting CS and Engineering projects with a focus on modularity and technical aesthetics."
status: "On-going"
project-tag: "gary-gigabytes"
order: 0
tools: 
  - name: "Jekyll"
  - name: "CSS"
  - name: "HTML5"
  - name: "Font Awesome"
  - name: "Google Fonts"
  - name: "Jekyll Paginate"
  - name: "Docker"
  - name: "Nginx"
  - name: "Google Cloud Run"
  - name: "GitHub Actions"
  - name: "Cloudflare"


timeline:

  - date: "Phase 1: Initial Bare HTML/CSS Design"
    phase: "Initial Design"
    details: "Create a basic HTML/CSS design for the portfolio."
    completed: true

  - date: "Phase 1.1: Nginx Setup"
    phase: "Initial Implementation"
    details: "Set up Nginx on DigitalOcean."
    completed: true

  - date: "Phase 2: Jekyll Integration"
    phase: "Blog Development"
    details: "Integrate Jekyll into the portfolio."
    completed: true

  - date: "Phase 3: Responsive Design"
    phase: "Design Improvement"
    details: "Make the portfolio responsive."
    completed: true

  - date: "Phase 4: Polish Design"
    phase: "Final Design Improvement"
    details: "Polish the portfolio design."
    completed: true

  - date: "Phase 5: Docker Setup"
    phase: "Implementation"
    details: "Set up Docker for the portfolio."
    completed: true

  - date: "Phase 6: Cloud Migration (DigitalOcean → GCP)"
    phase: "Infrastructure Upgrade"
    details: "Migrate from DigitalOcean droplet to Google Cloud Run with Global Load Balancer and CI/CD automation."
    completed: true

  - date: "Phase 7: Maintenance"
    phase: "Maintenance"
    details: "Maintain the portfolio."
    completed: false
---

## Project Overview

This portfolio site serves as a central hub for documenting
my engineering journey — from CS coursework at CSUMB to
personal robotics and trading projects. Built with Jekyll
and deployed on Google Cloud Run.

## Technical Architecture

- **Static Site Generator**: Jekyll with custom layouts
  for projects, posts, and course pages
- **Styling**: Custom CSS with a "blueprint grid" aesthetic
  and Engineering Amber accent palette
- **Deployment**: Dockerized Jekyll build, served via
  Google Cloud Run with a Global Load Balancer
- **CI/CD**: GitHub Actions triggers Cloud Build on push
- **DNS/CDN**: Cloudflare for caching and SSL

## Key Milestones

- **DigitalOcean → GCP Migration**: Moved from a $6/month
  always-on droplet to serverless Cloud Run, paying only
  for actual requests
- **Portfolio Overhaul**: Complete visual redesign with
  blueprint grid backgrounds, consistent spacing, and
  modular layout system
- **Project Showcase System**: Custom collections for
  projects and courses with auto-linked post feeds
