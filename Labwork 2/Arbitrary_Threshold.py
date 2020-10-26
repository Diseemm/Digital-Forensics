import cv2 as cv
import sys

forme1= cv.imread(cv.samples.findFile("Resource/forme1.png"), cv.IMREAD_GRAYSCALE)
house8 = cv.imread(cv.samples.findFile("Resource/house8.png"), cv.IMREAD_GRAYSCALE)
woman = cv.imread(cv.samples.findFile("Resource/femme.png"), cv.IMREAD_GRAYSCALE)

ret, thresh_forme1 = cv.threshold(forme1, 120, 255, cv.THRESH_BINARY)
ret, thresh_house8 = cv.threshold(house8, 120, 255, cv.THRESH_BINARY)
ret, thresh_woman = cv.threshold(woman, 120, 255, cv.THRESH_BINARY)

cv.imshow("Binary Threshold Forme 1", thresh_forme1)
cv.imshow("Binary Threshold House 8", thresh_house8)
cv.imshow("Binary Threshold Woman", thresh_woman)

key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()
