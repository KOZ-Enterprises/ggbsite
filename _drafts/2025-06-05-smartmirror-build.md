---
layout: post
tags: ["Smart Mirror"]
---

<img src="/assets/imgs/magicmirror_final_cropped.jpg" alt="Smart Mirror" class="project-image">

I recently built a smart mirror using a Raspberry Pi 4 and a two-way mirror. The project was inspired by the MagicMirror² platform, which provides a customizable interface for displaying information like time, weather, news, and more.

## Components Used
- [MagicMirror² software](https://magicmirror.builders/)
- Raspberry Pi 4
- Two-way mirror
- Monitor
- Frame

## Steps to Build
1. **Install MagicMirror²**: Follow the [installation guide](https://docs.magicmirror.builders/getting-started/installation.html) to set up the software on your Raspberry Pi.
2. **Configure Modules**: Customize the modules you want to display, such as weather, calendar, and news. You can find a list of available modules [here](https://docs.magicmirror.builders/modules/).
3. **Set Up the Hardware**: Assemble the two-way mirror with the monitor and frame. Ensure the monitor is positioned behind the mirror for optimal visibility.
4. **Connect the Raspberry Pi**: Connect the Raspberry Pi to the monitor and power it on. Make sure it boots into the MagicMirror² interface.
5. **Final Adjustments**: Adjust the settings in the `config.js` file to customize the appearance and functionality of your smart mirror.

## Tips
- Use a high-quality two-way mirror for better visibility.
- Consider adding voice control capabilities using a microphone and a voice assistant like Google Assistant or Alexa.
- Explore additional modules to enhance functionality, such as traffic updates or smart home controls.