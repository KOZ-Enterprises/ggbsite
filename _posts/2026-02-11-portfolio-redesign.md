---
layout: post
title: "Portfolio Overhaul: Engineering Aesthetic & Structural Integrity"
date: 2026-02-10
tags: ["gary-gigabytes", "hobby-projects"]

---

It was time for a structural evaluation. While this site has always served its purpose as a digital lab notebook, the underlying "codebase" (the CSS and HTML) had become a bit of a patchwork. Over the last few days, I've performed a complete overhaul of the site's architecture and visual language.

<!--more-->

## Core Objectives

The mission was simple: improve **consistency**, **alignment**, and **visual impact** without sacrificing the "Technical Workshop" feel.

## 1. The "Blueprint" Backdrop

I wanted the site to feel like an engineer's workstation. I implemented a custom `blueprint-grid` utility that uses CSS linear gradients to create a subtle grid pattern. This provides a structured backdrop for project showcases, reinforcing the idea that everything here is a "work in progress" or a "technical draft."

## 2. Engineering Amber Accent

While the previous teal (`#64d5d2`) and midnight palette was clean, it lacked a certain "pop." I introduced **Engineering Amber** (`#ffb300`). This high-visibility accent is used sparingly on critical icons and links, mimicking the status lights on a control panel.

## 3. Structural Alignment & Spacing

A major focus was on horizontal alignment. I moved section headers into shared rows above grid containers to ensure that "Recent Log Entries" and "Featured Project" sit on the same line, regardless of screen size. I also developed spacing utility classes to "sandwich" elements more tightly, removing the excessive gaps that often plague modular layouts.

## 4. Better Content Delivery

- **Project Log Style**: Homepage excerpts now match the structured list style of my project pages, including the terminal icon.
- **Image Intelligence**: I've suppressed images in excerpts to keep the list focused, and implemented an `invert-white` CSS filter to turn black university logos into high-contrast white assets.
- **Centering for Impact**: Post tags are now centered on full-page views for a cinematic look, while staying left-aligned in lists for readability.

This redesign wasn't just about looks—it was about making the system easier to maintain and more satisfying to use. The lab is now organized. Ready for the next build.
