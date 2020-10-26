import cv2 as cv
import sys
from matplotlib import pyplot as plt

cadastre2 = cv.imread(cv.samples.findFile("Resource/cadastre2.png"), cv.IMREAD_GRAYSCALE)

ret, thresh_arbi_cadastre2 = cv.threshold(cadastre2, 90, 255, cv.THRESH_BINARY)
plt.hist(cadastre2.ravel(), 256, [0, 256])
plt.show()
ret, thresh_otsu_cadastre2 = cv.threshold(cadastre2, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("Arbitrary", thresh_arbi_cadastre2)
cv.imshow("Otsu", thresh_otsu_cadastre2)

key = cv.waitKey(0)
if key == ord("q"):
    sys.exit()