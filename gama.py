#ÖDEV 2

import cv2
import numpy as np


def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread('picture1.jpg')
gammaImg = gammaCorrection(img, 3)

cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('picture1.jpg')
gammaImg = gammaCorrection(img, 4)

cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('picture1.jpg')
gammaImg = gammaCorrection(img, 5)

cv2.imshow('Original image', img)
cv2.imshow('Gamma corrected image', gammaImg)
cv2.waitKey(0)
cv2.destroyAllWindows()