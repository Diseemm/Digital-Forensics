import cv2 as cv
import sys

forme1 = cv.imread(cv.samples.findFile("Resource/forme1.png"), cv.IMREAD_GRAYSCALE)
lena = cv.imread(cv.samples.findFile("Resource/lena.png"), cv.IMREAD_GRAYSCALE)
forme3 = cv.imread(cv.samples.findFile("Resource/forme3.png"), cv.IMREAD_GRAYSCALE)

ret, thresh_forme1 = cv.threshold(forme1, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
ret, thresh_lena = cv.threshold(lena, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
ret, thresh_forme3 = cv.threshold(forme3, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("Otsu Binary with Forme 1", thresh_forme1)
cv.imshow("Otsu Binary with Lena", thresh_lena)
cv.imshow("Otsu Binary with Forme 3", thresh_forme3)

key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()