Title: Raspberry Pi Links
Author: SergeM
Date: 2016-12-31 21:30:00
Tags: links, raspberry, pi, servo, stepper, motor shield, pwm, raspberry pi, ssh


[Description of I2C interface](https://learn.sparkfun.com/tutorials/i2c)

[Raspberry Pi SPI and I2C Tutorial ](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)


Continuous deployment (Russian)
[Непрерывная кросс компиляция на Raspberry PI](https://m.habrahabr.ru/post/318840/)

## Controlling motors

### Brushless motor

[Control brushless motor with ESC](https://solenerotech1.wordpress.com/2013/09/09/tutorialhow-to-control-a-brushless-motor-with-raspberry-pi/). Without additional controllers

[With  PCA9685 PWM Board](http://raspberrypi.stackexchange.com/a/36317) (stackexchange thread)

[One more thread](https://www.raspberrypi.org/forums/viewtopic.php?t=46732)

### multiple servos 
[Controlling one servo](http://razzpisampler.oreilly.com/ch05.html). No additional controllers needed

[Adafruit 16 Channel Servo Driver with Raspberry Pi
Created by Kevin Townsend. pdf. (pca-9685)](https://cdn-learn.adafruit.com/downloads/pdf/adafruit-16-channel-servo-driver-with-raspberry-pi.pdf)

### Stepper motors / DC (brushed) motors
[with l293d](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-10-stepper-motors?view=all)

[[Raspberry] Stepper and dc motor using specializer HAT](https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi?view=all)  
Based on PC9865 PWM and TB6612 chipset. 1.2A per channel current capability (20ms long bursts of 3A peak)


[[Arduino] With adafruit motor schield v1](https://learn.adafruit.com/adafruit-motor-shield?view=all)  
Based on 74HC595N Serial to parallel output latch and L293D driver. 0.6A per bridge (1.2A peak) with thermal shutdown protection, 4.5V to 25V.  
[Library for motor control](https://github.com/adafruit/Adafruit-Motor-Shield-library)    
See also [about SN74HC595 shift register](/sn74hc595-shift-register.html)



[[Arduino] With adafruit motor shield v2](https://learn.adafruit.com/adafruit-motor-shield-v2-for-arduino?view=all)  
Based on PCA9685 and TB6612 MOSFET drivers with 1.2A per channel current capability ( up to 3A peak for approx 20ms at a time)

[[Raspberry] Drive a DC motor forward and in reverse with variable speed](https://learn.adafruit.com/adafruit-raspberry-pi-lesson-9-controlling-a-dc-motor?view=all) (with l293d, adafruit lesson 9)

[[Micropython board] Control  dc motor with pca9685](https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver?view=all) 

[[Raspberry] Video with just simple transistor scheme and with L293D controller](https://www.youtube.com/watch?v=W7cV9_W12sM)

[[Raspberry] using L293D and 4N35 opto isolator](https://medium.com/@seyoum14/using-a-dc-motor-to-run-a-propeller-with-raspberry-pi-e5a570864e6f#.q7qutomrv)

[[Arduino] 1 bidirectional DC motor using small DRV8871 motor driver](https://learn.adafruit.com/adafruit-drv8871-brushed-dc-motor-driver-breakout?view=all)   
Up to 45V and 3.6A of motor control

It is possible to have frequency controlled dc driver connected through Adafruit 16 Channel Servo Driver. 
See [post](https://www.raspberrypi.org/forums/viewtopic.php?t=12067&p=161140). [controller, ~100 Euro](http://www.robotshop.com/en/sabertooth-dual-regenerative-motor-driver.html), powerfull

[[Arduino] using drv8833 driver](https://ulrichbuschbaum.wordpress.com/2014/10/28/using-the-drv8833-motor-driver/), 

[[Arduino] using l293d](https://ulrichbuschbaum.wordpress.com/2014/09/17/the-l293d-motor-driver-and-makeblock/)


Using transistors: (1)[http://electronics.stackexchange.com/questions/7235/motor-driver-using-only-a-2n2222-transistor], very weak

## Connecting via ssh:
```
ssh -Y user@raspberrypi-url
```

## Access rasbberry Pi without monitor and ethernet 

Assuming we have an operating system (raspbian) installed.

1. Plug the SD-card into a computer. 

2. Automatic connection to wifi. Edit `/etc/wpa_supplicant/wpa_supplicant.conf` and add the following lines:

```
network={
    ssid="my-network-name"
    psk="my-network-pass"
    key_mgmt=WPA-PSK
}
```

3. Enable SSH access. Create an empty file `ssh` in `/boot/`.

4. Plug the card back into your raspberry, turn on. 

Now you can connect to raspberry via ssh:

    ssh pi@raspberrypi
    
or 

    ssh pi@<IP-OF-YOUR-RASPBERRY>




## Reading input (button) from GPIO
[without interrupts, raspi.tv](http://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs)

## RaspberryPi Zero pins Layout
![GPIO raspberry pins scheme]({filename}/2016/12/gpio.png)

![pins layout photo]({filename}/2016/12/gpio-raspberry-zero.png) [image source](http://pi4j.com/pins/model-zero-rev1.html)

## Other
[Example of using 545043 power supply](https://www.sunfounder.com/learn/Super_Kit_V2_for_RaspberryPi/lesson-7-how-to-drive-a-dc-motor-super-kit-for-raspberrypi.html)

[description of sn74hc595](http://www.ti.com/lit/ds/symlink/sn74hc595.pdf)

[blog about building security robot](https://seregus.wordpress.com/)

[h bridge using 2n2222 transistors for dc motor control. + reverse](http://www.instructables.com/id/H-Bridge-on-a-Breadboard/?ALLSTEPS); [another version](http://electronics.stackexchange.com/questions/7235/motor-driver-using-only-a-2n2222-transistor);
[another version of h bridge](http://www.electronicsteacher.com/robotics/robotics-tutorial/advanced-robotics/controlling-dc-motors.php)

[Build a Raspberry Pi Telepresence Rover ](http://www.bot-thoughts.com/2013/04/raspberry-pi-telepresence-rover.html) using [Pololu DRV8835](/motor-dirvers-controllers.html)
