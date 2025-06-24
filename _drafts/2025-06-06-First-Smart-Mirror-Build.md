---
layout: post
title: "First Smart Mirror Build"
tags: ["Smart Mirror"]
---
<div class="image-container">
<a href="/assets/imgs/magicmirrorbuildfinal_cropped.jpg" target="_blank">
    <img src="/assets/imgs/magicmirrorbuildfinal_cropped.jpg" alt="Smart Mirror" class="project-image" style="width: 600px">
</a>
</div>

I built my first smart mirror using a Raspberry Pi 3+ and an old monitor I have lying around a year ago.  After the PI stopped working I opened it back up to figure out why it stopped working.  In process of doing so I accidentally shorted the 110V circuit and the circuit breaker in my apartment tripped.  So I basically fried the monitor and PI so opted to start over with a newer monitor.  

I'll be posting the new monitor build soon, but wanted to share my original build for funsies.  I do miss how the old monitor fit perfectly in the frame I had, but the viewing angle was terrible.  

## Components
- [MagicMirror² software](https://magicmirror.builders/)
- [Raspberry Pi 3 1GB](https://www.pishop.us/product/raspberry-pi-3-model-b-plus/)
- [11x17 Frame](https://a.co/d/7LMuKS5)

### MagicMirror² Modules
- [MMM-GoogleCalendar](https://github.com/MichMich/MagicMirror/tree/master/modules/MMM-GoogleCalendar)
- [MMM-GoogleCalendar](https://github.com/MichMich/MagicMirror/tree/master/modules/MMM-GoogleCalendar)
- [MMM-GoogleCalendar](https://github.com/MichMich/MagicMirror/tree/master/modules/MMM-GoogleCalendar)

## Steps to Build
1. **Install MagicMirror²**: Follow the [installation guide](https://docs.magicmirror.builders/getting-started/installation.html) to set up the software on your Raspberry Pi.
2. **Configure Modules**: Customize the modules you want to display, such as weather, calendar, and news. You can find a list of available modules [here](https://docs.magicmirror.builders/modules/).
3. **Set Up the Hardware**: Assemble the two-way mirror with the monitor and frame. Ensure the monitor is positioned behind the mirror for optimal visibility.
4. **Connect the Raspberry Pi**: Connect the Raspberry Pi to the monitor and power it on. Make sure it boots into the MagicMirror² interface.
5. **Final Adjustments**: Adjust the settings in the `config.js` file to customize the appearance and functionality of your smart mirror.

## Key Takeaways
- This was a fun project that uses a Raspberry PI to create a functional smart mirror that I use daily.
- Using a modern Portable Monitor I think is the way to go, since it's already low voltage and excellent viewing angle compared to older screens.
- Using actual glass would have been better, since the acrylic has a slight clown mirror effect, but that would have been much more expensive.

Want to thank the MagicMirror² community for their support and the extensive documentation that made this project possible. If you're interested in building your own smart mirror, I highly recommend checking out their resources and getting involved in the community.