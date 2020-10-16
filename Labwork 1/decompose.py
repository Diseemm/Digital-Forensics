import cv2 as cv
import sys
import glob
import os

img = cv.imread(cv.samples.findFile("Resource/logo-usth.png"))

b, g, r = cv.split(img)
cv.imshow('image_blue', b)
cv.waitKey(0)
cv.imshow('image_green', g)
cv.waitKey(0)
cv.imshow('image_red', r)
cv.waitKey(0)

cv.destroyAllWindows()
