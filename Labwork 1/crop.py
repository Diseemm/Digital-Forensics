import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("football.jpeg"))
print(img.shape)

imgCropped = img[70:259,70:359]

cv.imshow("Cropped", imgCropped)
cv.waitKey(0)