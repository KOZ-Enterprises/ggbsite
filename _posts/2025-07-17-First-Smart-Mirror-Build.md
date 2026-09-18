---
layout: post
title: "First Smart Mirror Build"
tags: ["smart-mirror", "hobby-projects"]
---

I built my first [smart mirror](/projects/smartmirror/) using a Raspberry Pi 3+ and an old monitor I have lying around a year ago.  After the PI stopped working I opened it back up to figure out why it stopped working.  In process of doing so I accidentally shorted the 110V circuit and the circuit breaker in my apartment tripped.  So I basically fried the monitor and PI so opted to start over with a newer monitor.
<!--more-->
<div class="image-container">
<a href="/assets/imgs/smartmirror/magicmirrorbuildfinal_cropped.jpg" target="_blank">
    <img src="/assets/imgs/smartmirror/magicmirrorbuildfinal_cropped.jpg" alt="Smart Mirror" class="project-image" style="width: 600px">
</a> <p class="caption"> The original build using an old 720p monitor, which fit perfectly in the frame!</p>
</div>

I'll be posting the new monitor build soon, but wanted to share my original build for funsies.  I do miss how the old monitor fit perfectly in the frame I had, but the viewing angle was terrible.  

<div class="image-container">
<a href="/assets/imgs/smartmirror/magicmirror_annotated.png" target="_blank">
    <img src="/assets/imgs/smartmirror/magicmirror_annotated.png" alt="Smart Mirror" class="project-image" style="width: 600px">
</a>
<p class="caption">The 3 monitor PCBs are visible.  I was able to find where the AC power gets convert to ~18VDC, where I soldered in the 5V DC-DC converter to power the pi.  Also note a PI Zero is shown which DOES NOT WORK btw.  From experience it's best to use a PI4 and above. </p>
</div>

## Components

- [MagicMirror² software](https://magicmirror.builders/)
- [Raspberry Pi 3 1GB](https://www.pishop.us/product/raspberry-pi-3-model-b-plus/)
- [11x17 Frame](https://a.co/d/7LMuKS5)

## MagicMirror² Modules

### Core Modules

- [Calendar](https://docs.magicmirror.builders/modules/calendar.html)
- [Clock](https://docs.magicmirror.builders/modules/clock.html)
- [Weather](https://docs.magicmirror.builders/modules/weather.html)

### Third-Party Modules

- [MMM-GoogleCalendar](https://github.com/MichMich/MagicMirror/tree/master/modules/MMM-GoogleCalendar)
- [MMM-MonthyCalendar](https://github.com/kolbyjack/MMM-MonthlyCalendar)
- [MMM-CloneWarsQuotes](https://github.com/macd2point0/MMM-CloneWarsQuotes)

## Steps to Build

1. **Install MagicMirror²**: Follow the [installation guide](https://docs.magicmirror.builders/getting-started/installation.html) to set up the software on your Raspberry Pi.
2. **Configure Modules**: Customize the modules you want to display, such as weather, calendar, and news. You can find the [list of available modules](https://docs.magicmirror.builders/modules/) in the MagicMirror² docs.
3. **Set Up the Hardware**: Assemble the two-way mirror with the monitor and frame. Ensure the monitor is positioned behind the mirror for optimal visibility.
4. **Connect the Raspberry Pi**: Connect the Raspberry Pi to the monitor and power it on. Make sure it boots into the MagicMirror² interface.
5. **Final Adjustments**: Adjust the settings in the `config.js` file to customize the appearance and functionality of your smart mirror.

## Key Takeaways

- This was a fun project that uses a Raspberry PI to create a functional smart mirror that I use daily.
- Using a modern Portable Monitor I think is the way to go, since it's already low voltage and excellent viewing angle compared to older screens.

Want to thank the MagicMirror² community for their extensive documentation that made this project possible. If you're interested in building your own smart mirror, I highly recommend checking out their resources and getting involved in the community.

I'll be posting the new and improved build soon!!!
