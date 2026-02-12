# Gary Gigabytes Website

[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-CC0000?style=flat-square&logo=jekyll)](https://jekyllrb.com/)
[![Ruby](https://img.shields.io/badge/Ruby-3.1+-CC342D?style=flat-square&logo=ruby)](https://www.ruby-lang.org/)
[![License](https://img.shields.io/github/license/KOZ-Enterprises/ggbsite?style=flat-square)](LICENSE)
[![Commit](https://img.shields.io/github/last-commit/KOZ-Enterprises/ggbsite?style=flat-square)](https://github.com/KOZ-Enterprises/ggbsite/commits/main)
[![Size](https://img.shields.io/github/repo-size/KOZ-Enterprises/ggbsite?style=flat-square)](https://github.com/KOZ-Enterprises/ggbsite)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/garykuepper/)

Welcome to my personal website, where I showcase my projects and academic work as I bridge the gap between engineering and computer science. This Jekyll-powered website serves as a portfolio for my work, a platform to document my journey in technology, and features an integrated blog.

## Table of Contents

- [About Me](#about-me)
- [Features](#features)
- [Website Structure](#website-structure)
- [Technologies Used](#technologies-used)
- [Code Quality](#code-quality)
- [License](#license)
- [Contact](#contact)

## About Me

I hold a Bachelor's degree in Mechanical Engineering and am currently pursuing a Bachelor's degree in Computer Science at California State University, Monterey Bay (CSUMB). My passion for technology and innovation drives me to explore the exciting world of artificial intelligence and machine learning.

## Features

- **Portfolio Showcase**: Displays my hobby and academic projects including autonomous Arduino rovers, Raspberry Pi clusters, quantum computing simulations, and full-stack web apps
- **Academic Work**: Dedicated section for my Computer Science coursework and projects from CSUMB
- **Integrated Blog**: Jekyll-powered blog to document my projects, insights, and experiences
- **Responsive Design**: Clean, modern layout that works across devices
- **Tag System**: Organized content categorization for easy navigation

## Website Structure

The site is organized into several key sections:

- **Home** (`index.html`) - Introduction and overview
- **About** (`about.html`) - Detailed background information
- **Projects** (`projects.html`) - Portfolio of personal and hobby projects
- **CSUMB** (`csumb.html`) - Academic coursework and university projects
- **Blog Posts** - Regular updates and project documentation

### Collections

The site uses Jekyll collections to organize content:

- **`_projects/`** - Personal and hobby projects
- **`_csumb/`** - Academic work from California State University, Monterey Bay
- **`_posts/`** - Blog posts and project updates

## Technologies Used

- **Jekyll 4.3** - Static site generator
- **HTML5 & CSS3** - Frontend markup and styling
- **Liquid** - Templating language
- **Markdown** - Content authoring
- **Ruby** - Development environment
- **Git** - Version control

## Code Quality

To ensure the quality of the codebase, we use the following tools:

- **RuboCop**: A Ruby static code analyzer and formatter.

  ```bash
  bundle exec rubocop
  ```

- **HTMLProofer**: A set of tests to validate your HTML output.

  ```bash
  bundle exec jekyll build
  bundle exec htmlproofer ./_site
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Feel free to reach out if you have any questions or would like to collaborate!

- [LinkedIn Profile](https://www.linkedin.com/in/garykuepper/)

Thank you for visiting my page!
