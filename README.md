# Vision Processing
This Python program, built with OpenCV, takes a picture using a webcam and sends the estimated distance (to the lift peg) to the roboRIO.

**Efficiency:** On a Raspberry Pi 2, the whole program takes around 0.3 seconds.

# Requirements
- [ ] Raspberry Pi 2 (or 3) with Raspbian
- [ ] Microsoft Lifecam HD-3000 (or any other webcam)
- [ ] Ethernet cable

# Setup
1. Install OpenCV on the Raspberry Pi
    - [How to install OpenCV on RasPi 2](http://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/)
    - [How to install OpenCV on RasPi 3](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/)
2. Install [pynetworktables](http://robotpy.readthedocs.io/en/stable/install/pynetworktables.html) with `pip3 install pynetworktables`
3. Clone this repository
4. Calibrate the webcam so that it takes pictures with low brightness

## Connecting the Raspberry Pi and webcam
1. Connect the webcam to a USB port on the Raspberry Pi
2. Connect the Raspberry Pi to the router with an Ethernet cable

<!-- Include picture -->

# How it works
Each line is explained well in `vision-processing.py`, but here is a higher-level overview of the whole process:

1. Take a picture with the camera:
<!-- include picture -->

2. Using HSV, make a map of colors that are greenish:
<!-- include picture -->

3. Find all the contours:
<!-- include picture -->

4. Narrow down the list of contours to the two most likely to be the vision targets on either side of the lift peg:
<!-- include picture -->

5. Based on the schematics of the vision targets, use this formula to find the distance from the camera to the vision target:
    - `distance = targetHeight * resY / (pixelHeight * tan(viewAngleY))`
        - `targetHeight = 5` (in inches)
        - `resY = 480` (the Microsoft Lifecam is 640x480)
        - `pixelHeight` is the height of an LED peg vision target contour
        - `viewAngleY = 34.3°` (for the Microsoft Lifecam)
            - If you are using a different webcam, you can check [this page](http://vrguy.blogspot.com/2013/04/converting-diagonal-field-of-view-and.html) to find your webcam's vertical FOV from its diagonal FOV and aspect ratio (usually found in the webcam's specifications)
    - ![Vision target dimensions for lift peg](https://cloud.githubusercontent.com/assets/14433542/22134282/c5881a6a-de7a-11e6-9057-a61954ca54b8.png)

6. Send the data (distance) to the roboRIO using NetworkTables (TODO)

## Examples
![Example picture 1](https://cloud.githubusercontent.com/assets/14433542/22178727/1d2c05cc-dff4-11e6-82d9-3527add7bf7c.png)
![Example processed picture 1](https://cloud.githubusercontent.com/assets/14433542/22178730/2f0e8b98-dff4-11e6-97de-bc0ca39eed1e.png)
Pixel height: 152px, 23.2 in., Actual distance: 23.6 in

<!-- Make a list of original pictures and their corresponding end contours. Also include difficult pictures with contours split by an obstruction -->

# TODO
- [ ] Send the distance data to the roboRIO using NetworkTables
- [ ] **Make vision still be accurate with a tilted viewpoint**
- [ ] Make everything more efficient
- [ ] Make everything more readable
- [ ] Add more explanation and images to this README
- [ ] Add more examples to README
