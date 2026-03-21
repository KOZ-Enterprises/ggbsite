---
layout: post
title: "Infrastructure Upgrade: Migrating from DigitalOcean to Google Cloud Run"
date: 2026-03-21
tags: ["gary-gigabytes", "hobby-projects", "docker", "google-cloud"]
description: "The site has moved from a DigitalOcean droplet to Google Cloud Run with a Global Load Balancer, cutting costs while improving reliability and scalability."
project-title: "Gary Gigabytes Website"
project-url: "/projects/ggbytes/"
---

After running on a DigitalOcean droplet for some time, I made the decision to migrate this portfolio site to Google Cloud Run. This wasn't just a technical exercise—it was driven by practical considerations around cost, scalability, and operational simplicity.

<!--more-->

## Why Migrate?

The DigitalOcean droplet, while reliable, was running 24/7 even during periods of low traffic. A static Jekyll site doesn't need constant resources; it's request-driven and naturally bursty. Google Cloud Run's serverless model meant paying only for actual requests, which aligned much better with typical portfolio traffic patterns.

## What Changed

### Before: DigitalOcean Droplet
- Single $4–$6/month droplet (Ubuntu 20.04)
- Nginx reverse proxy + Jekyll-built static content
- Manual deployments (git pull + rebuild)
- Single domain on the droplet IP

### After: Google Cloud Run + Global Load Balancer

The new architecture:

1. **Cloud Run Services** — Two containerized applications:
   - `ggbsite` (port 80): Jekyll site rebuilt on every push to `publish` branch
   - `culinaryotter` (port 3000): Companion project site, patched to run without external database dependencies

2. **Global Load Balancer** — Routes traffic and provides:
   - Static external IP (`34.36.126.59`)
   - Host-based routing: `garygigabytes.com` → ggbsite; `culinaryotter.garygigabytes.com` → culinaryotter
   - HTTP (port 80) and HTTPS (port 443) forwarding

3. **Cloudflare DNS** — Already in place, now points to the GCP static IP instead of DigitalOcean

4. **SSL/TLS** — Cloudflare handles visitor-facing HTTPS (Full mode); origin cert validates between Cloudflare and GCP

## Automated Deployments

The migration includes end-to-end CI/CD:

- **GitHub Actions** (`deploy.yml`): Triggers on push to `publish` branch
- **Workload Identity Federation** (WIF): Securely authenticates GitHub Actions to GCP without storing long-lived credentials
- **Cloud Build**: Builds the Docker image directly into Google Container Registry (`gcr.io`)
- **Automatic deployment**: `gcloud run deploy` updates the service with the new image

No more manual deployments. Every push to `publish` rebuilds and deploys the site in under 2 minutes.

## CulinaryOtter Integration

As part of the migration, my class project [CulinaryOtter](https://culinaryotter.garygigabytes.com/) was also containerized and deployed to Cloud Run. It runs on port 3000 and routes through the same load balancer via the `culinaryotter.garygigabytes.com` subdomain.

The app originally had a hardcoded database connection at startup that would crash if the database was unavailable. I patched it to use lazy database connection initialization, allowing the service to start cleanly and serve non-database routes (homepage, recipe search, about pages) even when the database isn't configured. This makes it resilient and deployment-friendly.

## Cost & Performance

- **Compute**: Cloud Run charges for CPU and memory during request execution. For a low-traffic portfolio, this typically runs $0–$2/month.
- **Load Balancer**: ~$18/month for the global load balancer with static IP (the primary recurring cost).
- **Storage**: Minimal (source code in GitHub, container images in GCR).
- **Total**: ~$20–$25/month (vs. ~$60–$72/year for the DigitalOcean droplet alone).

More importantly, there's no overhead for idle droplets, automatic scaling if traffic spikes, and the deployment pipeline is now transparent and audit-able in GitHub Actions logs.

## Lessons Learned

- **Workload Identity Federation** is the right way to authenticate CI/CD pipelines to cloud providers—no stored secrets, and rotation is automatic.
- **Serverless architectures shine for low-traffic sites**; pay-per-request models eliminate the "always-on" tax.
- **Containerization clarity**: The move to Docker forced me to be explicit about dependencies and startup processes, which paid off during the CulinaryOtter patch.

The site is now leaner, faster-to-deploy, and cheaper to run. The technical debt has been converted into operational leverage.
