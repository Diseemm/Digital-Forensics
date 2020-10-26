import cv2 as cv
import sys
from matplotlib import pyplot as plt

forme3 = cv.imread(cv.samples.findFile("Resource/forme3.png"), cv.IMREAD_GRAYSCALE)
plt.hist(forme3.ravel(), 256, [0, 256])
plt.show()

ret, thresh_forme3 = cv.threshold(forme3, 90, 255, cv.THRESH_BINARY)
cv.imshow("Forme 3", thresh_forme3)

key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()