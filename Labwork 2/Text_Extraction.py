import cv2 as cv
import sys
from matplotlib import pyplot as plt

cadastre1 = cv.imread(cv.samples.findFile("Resource/cadastre1.png"), cv.IMREAD_GRAYSCALE)

ret, thresh_cadastre1 = cv.threshold(cadastre1, 120, 255, cv.THRESH_BINARY) #To compare with Otsu method
ret, thresh_cadastre1_otsu = cv.threshold(cadastre1, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
plt.hist(cadastre1.ravel(), 256, [0, 256]) #To plot a histogram to determine the method
plt.show()

cv.imshow("Arbitrary", thresh_cadastre1)
cv.imshow("Otsu", thresh_cadastre1_otsu)

key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()
