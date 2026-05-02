# Gary Gigabytes: Engineering with a Side of Algorithmic Obsession

[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-CC0000?style=flat-square&logo=jekyll)](https://jekyllrb.com/)
[![Ruby](https://img.shields.io/badge/Ruby-3.1+-CC342D?style=flat-square&logo=ruby)](https://www.ruby-lang.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)

I've spent over a decade in Aerospace. Today, I work day-to-day as an ECS Analysis Engineer at Boeing, resolving in-service safety problems to keep airplanes flying (and making sure everyone can actually keep breathing onboard!). But I didn't just want to build the hardware; I wanted to build the "brains." This site is my bridge between those two worlds. It's where my Mechanical Engineering background meets my degree in Computer Science from CSUMB (Class of 2026) to build tangible products, intelligent systems, and explore practical AI applications.

This isn't just a portfolio; it's a running log of what happens when machine logic gets applied to physical problems. I'm an engineer, builder, and lifelong tinkerer obsessed with complex systems—from decentralized drone swarms to autonomous navigation.

## The Build Architecture

I like my systems like I like my aircraft: modular, robust, and predictable. To achieve that, I've built this site with a stack that balances static speed with containerized agility.

- **Frontend Foundation (Jekyll 4.3):** I use Jekyll because it forces a structural discipline. Every post and project is handled with Liquid templates and clean Markdown, ensuring the technical logs stay readable.
- **Visual Logic (Vanilla CSS):** No bloated frameworks here. I've handwritten the CSS to keep the "vibe" precise—a clean, dark-mode-first aesthetic that feels like a modern cockpit.
- **Engine Room (Docker & Cloud Run):** The entire site is containerized. GitHub Actions build and push images on every `publish` branch, which deploy directly to Google Cloud Run. A Global Load Balancer handles SSL termination and static IP management. Cloudflare sits in front for DNS and additional caching.

## Where the Work Happens

The site is carved into a few distinct zones:

- **[Gary Gigabytes (Home)](/):** The entry point where I bridge the physical and digital worlds. Check here for the most recent log entries and featured work.
- **[About Me](/about/):** The backstory of a lifelong tinkerer. This section documents my journey of adding Computer Science to my aerospace foundation, living at the intersection of hardware, software, and real-world impact.
- **[Hobby Projects](/projects/):** This is my attempt to track, showcase, and share the variety of personal projects I've built over the years. This is the workshop archive for documentation that was previously left in the vault.
- **[Academic Annex (CSUMB)](/csumb.html):** A dedicated area documenting my Computer Science journey. This degree combined my ME background with CS to build intelligent autonomy and apply ML to real-world physical problems.

## Quality of Service

In engineering, if you can't verify it, it isn't finished. I apply that same mindset here:

- **RuboCop:** Rules are rules. I use RuboCop to keep the Ruby backbone consistent.
- **HTMLProofer:** I can't stand broken links in a lab notebook. This ensures the entire graph of the site remains connected.
- **YAML/Markdown/Docker linting (CI):** The repo also runs lightweight checks for YAML, Markdown, GitHub Actions, and the Dockerfile.

## Local linting (same checks as CI)

Ruby/Jekyll checks:

```bash
bundle exec rubocop
bundle exec jekyll build
bundle exec htmlproofer ./_site --disable-external --allow-hash-href --assume-extension --enforce-https=false
```

Docker-based checks (no Node required in this repo):

```bash
docker run --rm -v "$PWD:/work" -w /work cytopia/yamllint:latest -c .yamllint.yml .
docker run --rm -v "$PWD:/work" -w /work ghcr.io/davidanson/markdownlint-cli2:latest -c .markdownlint-cli2.yaml
docker run --rm -v "$PWD:/repo" -w /repo rhysd/actionlint:latest -color
docker run --rm -v "$PWD:/work" -w /work hadolint/hadolint:latest hadolint -c .hadolint.yaml Dockerfile
```

## Deployment & Infrastructure

**Current Setup:**
- Hosting: Google Cloud Run (us-central1)
- Load Balancing: GCP Global Load Balancer with static IP
- DNS: Cloudflare (garygigabytes.com)
- SSL: Google-managed certificates + Cloudflare proxying

**Documentation:**
- [DEPLOYMENT.md](DEPLOYMENT.md) - Day-to-day operational guide
- [CLOUD_RUN_SETUP.md](CLOUD_RUN_SETUP.md) - One-time GCP project bootstrap
- [AGENTS.md](AGENTS.md) - AI agent context and project structure

---

### Want to talk shop?

If you're into robotics, autonomous systems, or just like talking architectural patterns, let's connect.

- **LinkedIn:** [Gary Kuepper](https://www.linkedin.com/in/garykuepper/)
- **GitHub:** [koz-enterprises](https://github.com/koz-enterprises)
- **Portfolio Projects:** [View Projects](/projects/)

*Thanks for stopping by the lab.*
