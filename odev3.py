#ÖDEV 3/ contrast

import cv2
import numpy as np
import matplotlib.pyplot as plt

try:
    img = cv2.imread('foti.png')
    img = cv2.resize(img, (500, 600))
except Exception as e:
    print(str(e))

img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=5)
final_image = clahe.apply(img_bw) + 30

_, ordinary_img = cv2.threshold(img_bw, 155, 255, cv2.THRESH_BINARY)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('orijinal resim'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(ordinary_img, cmap='gray')
plt.title('ordinary threshold'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(final_image, cmap='gray')
plt.title('clahe resim'), plt.xticks([]), plt.yticks([])

plt.show()


