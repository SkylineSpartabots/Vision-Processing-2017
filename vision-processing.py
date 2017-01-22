import numpy as np
import cv2
from math import tan, pi

# return an image from the USB webcamera
def getPictureFromCamera(portNum = 0):
	cam = cv2.VideoCapture(0)
	cam.set(cv2.CAP_PROP_BRIGHTNESS, 0.1)
	cam.set(cv2.CAP_PROP_CONTRAST, 0.9)
	retval, picture = cam.read()
	return picture

# import source image, mainly used for testing
def getTestPicture(fileName = "source"):
	return cv2.imread("images/" + fileName + ".jpg", cv2.IMREAD_COLOR)

def findContours(image):
	# find contours
	im2, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	# put the two largest contours into an array bigContours
	largestContour, largestContourSize, secondLargestContour, secondLargestContourSize = 0, 0, 0, 0
	for contour in contours:
		contourSize = cv2.contourArea(contour)
		if contourSize > largestContourSize:
			secondLargestContour, largestContour = largestContour, contour
			secondLargestContourSize, largestContourSize = largestContourSize, contourSize
		elif contourSize > secondLargestContourSize:
			secondLargestContour = contour
			secondLargestContourSize = contourSize
	return [largestContour, secondLargestContour]

# start timer to test efficiency
startTime = cv2.getTickCount()

img = getPictureFromCamera()

cv2.imwrite("camera-pic.jpg", img)

# convert BGR format to HSV
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# make an array of numbers 0 or 225 for the areas that are greenish
img = cv2.inRange(img, (60, 170, 40), (150, 255, 255))

bigContours = findContours(img)

# convert HSV format to BGR in order to draw contours in color
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# outline all big contours (-1)
# cv2.drawContours(img, bigContours, -1, (20,240,50), 1)

# draw boxes over the big contours
for contour in bigContours:
	rect = cv2.minAreaRect(contour)
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	cv2.drawContours(img, [box], 0, (5,40,255), 1)

# export processed image
cv2.imwrite("processed.jpg", img)

# find dimensions of the first contour
x, y, pixelWidth, pixelHeight = cv2.boundingRect(bigContours[0])

distance = 5 / 12 * 480 / (pixelHeight * tan(34.3 / 180 * pi))

print("Distance is " + str(distance * 12) + " in.")

# print time taken
print("Completed in " + str(round(((cv2.getTickCount() - startTime)/cv2.getTickFrequency())*1000, 3)) + " ms")
