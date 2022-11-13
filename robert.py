#robert
import cv2
import  numpy as np
from  scipy import ndimage
import matplotlib.pyplot as plt

robert_v = np.array([
    [1,0],[0,-1]
])

robert_h = np.array([
    [0,1],[-1,0]
])

img = cv2.imread('picture1.jpg', 0).astype('float64')
img /= 255.0

vertical = ndimage.convolve(img, robert_v)
horizontal= ndimage.convolve(img, robert_h)
edged_img= np.sqrt(np.square(horizontal)+np.square(vertical))
edged_img *= 255
plt.subplot(1,2,1), plt.imshow(img)
plt.title('original')
plt.subplot(1,2,2), plt.imshow(edged_img)
plt.title('robert')
plt.show()