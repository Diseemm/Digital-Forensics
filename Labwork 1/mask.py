import cv2 as cv
import numpy as np
import sys

img = cv.imread("usthlogo.jpeg")
if img is None:
    sys.exit("No image!!")

b, g, r = cv.split(img)
ret, maskRed = cv.threshold(r, 127, 255, cv.THRESH_BINARY)
logoRed = cv.resize(maskRed, (960,540))
cv.imshow("Red Logo", logoRed)
ret, maskBlue = cv.threshold(b, 127, 255, cv.THRESH_BINARY)
logoBlue = cv.resize(maskBlue, (960,540))
cv.imshow("Blue Logo", logoBlue)

key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()
