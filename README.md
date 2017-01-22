# Vision Processing
This Python program, built with OpenCV, takes a picture using a webcam and sends the estimated distance (to the lift peg) to the roboRIO.

**Efficiency:** On a Raspberry Pi 2, the whole program, from taking the picture to sending the data, takes around 0.2 seconds.

# Requirements
- [ ] Raspberry Pi 2 (or 3) with Raspbian
- [ ] Microsoft Lifecam HD-3000 (or any other webcam)
- [ ] Ethernet cable

# Setup
1. Install OpenCV on the Raspberry Pi.
    - [Tutorial to install on Raspberry Pi 2](http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/)
    - [Tutorial to install on Raspberry Pi 3](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/)
2. Clone this repository
3. Calibrate the webcam so that it takes pictures with low brightness

## Connecting the Raspberry Pi and webcam
1. Connect the webcam to a USB port on the Raspberry Pi
2. Connect the Raspberry Pi to the router with an Ethernet cable

<!-- Include picture -->

# How it works
Each line is explained well in `vision-processing.py`, but here is a higher-level overview of the whole process:

1. Take a picture with the camera:

2. Using HSV, make a map of colors that are greenish:

3. Find all the contours:

4. Narrow down the list of contours to the two most likely to be the vision targets on either side of the lift peg:

5. Based on the schematics of the vision targets, use the formula \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ to find the distance from the camera to the vision target:
![Vision target dimensions for lift peg](https://cloud.githubusercontent.com/assets/14433542/22134282/c5881a6a-de7a-11e6-9057-a61954ca54b8.png)

6. Send the data (distance) to the roboRIO using NetworkTables

# Examples
TODO

<!-- Make a list of original pictures and their corresponding end contours. Also include difficult pictures with contours split by an obstruction -->
