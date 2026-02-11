# Gary Gigabytes Website

![Jekyll](https://img.shields.io/badge/Jekyll-4.3-CC0000?style=flat&logo=jekyll)
![Ruby](https://img.shields.io/badge/Ruby-3.1+-CC342D?style=flat&logo=ruby)
![License](https://img.shields.io/github/license/GICodeWarrior/ggbsite?style=flat)

Welcome to my personal website, where I showcase my projects and academic work as I bridge the gap between engineering and computer science. This Jekyll-powered website serves as a portfolio for my work, a platform to document my journey in technology, and features an integrated blog.

## Table of Contents

- [About Me](#about-me)
- [Features](#features)
- [Website Structure](#website-structure)
- [Technologies Used](#technologies-used)
- [Code Quality](#code-quality)
- [Local Development](#local-development)
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

## Local Development

For local development with Jekyll, follow these steps:

### Prerequisites

1. **Install Ruby**: Jekyll requires Ruby to run. Install Ruby using a package manager like `Chocolatey` ([Windows install directions](https://phoenixnap.com/kb/chocolatey-windows)) or download it directly from [Ruby's official website](https://www.ruby-lang.org/en/downloads/).

2. **Install Bundler**: Once Ruby is installed, install Bundler:

    ```bash
    gem install bundler
    ```

### Setup

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd ggbsite
    ```

2. **Install Dependencies**: Run Bundler to install the required gems:

    ```bash
    bundle install
    ```

3. **Serve the Site Locally**: Use the following command to serve your Jekyll site locally:

    ```bash
    bundle exec jekyll serve
    ```

    By default, the site will be available at `http://localhost:4000`.

4. **For Windows Users**: The site includes the `wdm` gem for improved file watching performance on Windows systems.

### Development Workflow

- **Adding Blog Posts**: Create new Markdown files in the `_posts/` directory with the naming convention `YYYY-MM-DD-title.md`
- **Adding Projects**: Create new files in the `_projects/` collection directory
- **Adding Academic Work**: Create new files in the `_csumb/` collection directory
- **Customizing Layouts**: Edit files in the `_layouts/` directory
- **Modifying Styles**: Update CSS files in the `assets/` directory

### Stop the Server

To stop the local server, press `Ctrl+C` in the terminal.

For more details, refer to the [Jekyll documentation](https://jekyllrb.com/docs/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Feel free to reach out if you have any questions or would like to collaborate!

- [LinkedIn Profile](https://www.linkedin.com/in/garykuepper/)

Thank you for visiting my page!
