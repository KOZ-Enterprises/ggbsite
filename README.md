# Gary Gigabytes Website

Welcome to my personal website, where I showcase my projects and academic work as I bridge the gap between engineering and computer science. This website serves as a portfolio for my work and a platform to document my journey in technology.

## Table of Contents

- [About Me](#about-me)
- [Projects](#projects)
- [Future Enhancements](#future-enhancements)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Local Development](#local-development)

## About Me

I hold a Bachelor's degree in Mechanical Engineering and am currently pursuing a Bachelor's degree in Computer Science at California State University, Monterey Bay (CSUMB). My passion for technology and innovation drives me to explore the exciting world of artificial intelligence and machine learning.

## Projects

Here are some of the projects I'm currently working on:

1. **Rover** - *in-progress*
   - **Objective**: Develop a smart RC car with semi-autonomous and ultimately autonomous features.
   - **Requirements**:
     - The rover should be controlled using a PS4 controller with extended range since Bluetooth range is fairly short.
     - The rover should be able to drive in a straight line or any other basic patterns.

2. **Drone** - *on-hold*
   - **Objective**: Develop a small-medium sized drone with swarm technology.
   - **Note**: On hold as I will be learning the foundations of good software design and hardware design with the Rover project first.

3. **Gary Gigabytes Website** - *in-progress*
   - **Objective**: Showcase my personal and academic projects! Oh, and by the way, welcome!

4. **Smart Mirror** - *completed*
   - **Objective**: Develop a smart mirror that displays useful information such as time, weather, and notifications.

## Future Enhancements

- **Blog Integration**: Plans to introduce a blog feature on the main page to document my projects, insights, and experiences in more detail.

## Technologies Used

- HTML
- CSS
- JavaScript (future plans)
- Any other relevant technologies or libraries used in your projects.

## Local Development

For local development, consider the following:

- `Chocolatey` Package Manager ([Windows install directions](https://phoenixnap.com/kb/chocolatey-windows))

- `Node.js` and `NPM` ([Install via Chocolatey](https://phoenixnap.com/kb/install-node-js-npm-on-windows#ftoc-heading-5:~:text=Step%201%3A%20Install%20Node.js%20and%20NPM))

- `CORS` security proceedures can prevent `JavaScript` from executing on the page, resulting in the website failing to load some elements when tested via localhost. `Serve`([source](https://github.com/vercel/serve)) helps you serve a static site and provides an interface for listing a directory's contents (i.e. the HTML pages of this website).

```bash
> npm install --global serve
```

Once that's done, you can run this command inside your project's directory...

```bash
> serve
```

...or specify which folder you want to serve:

```bash
> serve folder-name/
```

Finally, run this command to see a list of all available options:

```bash
> serve --help
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Feel free to reach out if you have any questions or would like to collaborate!

- [LinkedIn Profile](https://www.linkedin.com/in/garykuepper/)


Thank you for visiting my page!