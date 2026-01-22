---
layout: post
title: "Improved Smart Mirror Build"
tags: ["smart-mirror","hobby-projects"]
---
<div class="image-container">
<a href="/assets/imgs/magicmirror_final_cropped.jpg" target="_blank">
    <img src="/assets/imgs/magicmirror_final_cropped.jpg" alt="Smart Mirror" class="project-image" style="width: 600px">
</a>
</div>

I recently built a smart mirror using a Raspberry Pi 4 and a two-way mirror. The project is uses MagicMirror² software, which provides a customizable interface for displaying information like time, weather, news. 
<!--more-->
### Components
- [MagicMirror² software](https://magicmirror.builders/)
- [Raspberry Pi 4 1GB](https://www.pishop.us/product/raspberry-pi-4-model-b-1gb/)
- [Two-way Acrylic mirror](https://a.co/d/21ZsVwt)
- [18.5" 1920x1080 Portable Monitor](https://www.newegg.com/p/2NY-0094-00021?item=9SIBMMWK9P5965&utm_source=transactional&utm_medium=email&cm_mmc=TEMC-Shipping-Notice-USA-_-101929&utm_campaign=TEMC-Shipping-Notice-USA-_-101929)
- [11x17 Frame](https://a.co/d/7LMuKS5)
- [HDMI to Micro HDMI Cable](https://a.co/d/aOiFJnA)

### MagicMirror² Modules

#### Core Modules
- [Calendar](https://docs.magicmirror.builders/modules/calendar.html)
- [Clock](https://docs.magicmirror.builders/modules/clock.html)
- [Weather](https://docs.magicmirror.builders/modules/weather.html)

#### Third-Party Modules
- [MMM-GoogleCalendar](https://github.com/MichMich/MagicMirror/tree/master/modules/MMM-GoogleCalendar)
- [MMM-MonthyCalendar](https://github.com/kolbyjack/MMM-MonthlyCalendar)
- [MMM-CloneWarsQuotes](https://github.com/macd2point0/MMM-CloneWarsQuotes)


### Steps to Build
1. **Install MagicMirror²**: Follow the [installation guide](https://docs.magicmirror.builders/getting-started/installation.html) to set up the software on your Raspberry Pi.
2. **Configure Modules**: Customize the modules you want to display, such as weather, calendar, and news. You can find a list of available modules [here](https://docs.magicmirror.builders/modules/).
3. **Set Up the Hardware**: Assemble the two-way mirror with the monitor and frame. Ensure the monitor is positioned behind the mirror for optimal visibility.
4. **Connect the Raspberry Pi**: Connect the Raspberry Pi to the monitor and power it on. Make sure it boots into the MagicMirror² interface.
5. **Final Adjustments**: Adjust the settings in the `config.js` file to customize the appearance and functionality of your smart mirror.

<div class="image-grid"> 
    <div class="image-container">
        <a href="/assets/imgs/mm-final-overview.jpg">
            <img src="/assets/imgs/mm-final-overview.jpg" alt="Smart Mirror Overview" class="project-image" >
        </a>
        <p class="caption">The insides</p>
</div>
    <div class="image-container">
      <a href="/assets/imgs/mm-final-usb-fail.jpg"> 
        <img src="/assets/imgs/mm-final-usb-fail.jpg" alt="Mirror fail" class="project-image">
       </a> <p class="caption">Soo... was hoping to use these right angle usb connectors to keep all the cables inside but that didn't go as planned. </p>
</div>
    <div class="image-container">
      <a href="/assets/imgs/mm-final-micro-hdmi-final2.jpg">  
        <img src="/assets/imgs/mm-final-micro-hdmi-final2.jpg" alt="Mirror fail" class="project-image">
       </a> <p class="caption">Did not realize the micro hdmi was in the opposite orientation as on the RPI4... whoops. </p>
</div>
    <div class="image-container">
      <a href="/assets/imgs/mm-final-mirror-border.jpg"> 
        <img src="/assets/imgs/mm-final-mirror-border.jpg" alt="Mirror fail" class="project-image">
       </a> <p class="caption">Mirror Border to fill the empty space and add support for the 2 way mirror.</p>
</div>
    <div class="image-container">
      <a href="/assets/imgs/mm-final-packing-spacers.jpg"> 
        <img src="/assets/imgs/mm-final-packing-spacers.jpg" alt="Mirror fail" class="project-image">
       </a> <p class="caption">I put these white packing material around the monitor to help center it in the frame.</p>
</div>
    <div class="image-container">
      <a href="/assets/imgs/mm-final-sealing-up.jpg">  
        <img src="/assets/imgs/mm-final-sealing-up.jpg" alt="Mirror fail" class="project-image">
       </a> <p class="caption">Sealing the whole thing up with nails.  I wish I had a better way but oh well! It works ¯\_(ツ)_/¯
    </p>
</div>
    <div class="image-container">
      <a href="/assets/imgs/mm-finaljpg">  
        <img src="/assets/imgs/mm-final.jpg" alt="Mirror fail" class="project-image">
       </a> <p class="caption"> Still came out clean! :)
    </p>
</div>
</div>



### Key Takeaways
- This was a fun project that uses a Raspberry PI to create a functional smart mirror that I use daily.
- Using a modern Portable Monitor, I think is the way to go, since it's already low-voltage and excellent viewing angle compared to older screens.
- Using actual glass would have been better, since the acrylic has a slight clown mirror effect, but that would have been much more expensive.

