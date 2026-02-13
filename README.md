# Gary Gigabytes: Engineering with a Side of Algorithmic Obsession

[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-CC0000?style=flat-square&logo=jekyll)](https://jekyllrb.com/)
[![Ruby](https://img.shields.io/badge/Ruby-3.1+-CC342D?style=flat-square&logo=ruby)](https://www.ruby-lang.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)

I spent a decade in Aerospace—focusing on aircraft hardware and wrestling with environmental control systems at Boeing—before I realized I didn't just want to build the hardware. I wanted to build the "brains." This site is my bridge between those two worlds. It’s where my Mechanical Engineering background meets my second degree in Computer Science at CSUMB to build tangible products, intelligent systems, and explore practical AI applications.

This isn't just a portfolio; it's a running log of what happens when machine logic gets applied to physical problems. I’m an engineer, builder, and lifelong tinkerer obsessed with complex systems—from decentralized drone swarms to autonomous navigation.

## The Build Architecture

I like my systems like I like my aircraft: modular, robust, and predictable. To achieve that, I've built this site with a stack that balances static speed with containerized agility.

- **Frontend Foundation (Jekyll 4.3):** I use Jekyll because it forces a structural discipline. Every post and project is handled with Liquid templates and clean Markdown, ensuring the technical logs stay readable.
- **Visual Logic (Vanilla CSS):** No bloated frameworks here. I’ve handwritten the CSS to keep the "vibe" precise—a clean, dark-mode-first aesthetic that feels like a modern cockpit.
- **Engine Room (Docker & GHCR):** The entire site is containerized. I use GitHub Actions to build and push images to GHCR on every `publish`, which then get pulled onto a DigitalOcean server.

## Where the Work Happens

The site is carved into a few distinct zones:

- **[Gary Gigabytes (Home)](/):** The entry point where I bridge the physical and digital worlds. Check here for the most recent log entries and featured work.
- **[About Me](/about/):** The backstory of a lifelong tinkerer. This section documents my transition from aerospace engineering to living at the intersection of hardware, software, and real-world impact.
- **[Hobby Projects](/projects/):** This is my attempt to track, showcase, and share the variety of personal projects I've built over the years. This is the workshop archive for documentation that was previously left in the vault.
- **[Academic Annex (CSUMB)](/csumb.html):** A dedicated area for my Computer Science journey. My goal here isn't just a degree—it's combining ME with CS to build intelligent autonomy and apply ML to real-world physical problems.

## Quality of Service

In engineering, if you can't verify it, it isn't finished. I apply that same mindset here:

- **RuboCop:** Rules are rules. I use RuboCop to keep the Ruby backbone consistent.
- **HTMLProofer:** I can't stand broken links in a lab notebook. This ensures the entire graph of the site remains connected.

## Current Maintenance & Progress

I’m currently focused on a full portfolio redesign and optimizing the deployment pipeline. I’ve moved the messy "build on the server" approach to a streamlined "build on GitHub" workflow. It means less time messing with VPS configs and more time writing logic.

---

### Want to talk shop?

If you're into robotics, autonomous systems, or just like talking architectural patterns, let's connect.

- **LinkedIn:** [Gary Kuepper](https://www.linkedin.com/in/garykuepper/)
- **Documentation:** For technical setup and deployment steps, see [DEPLOYMENT.md](file:///c:/Users/gkuep/RubymineProjects/ggbsite/DEPLOYMENT.md).

*Thanks for stopping by the lab.*
