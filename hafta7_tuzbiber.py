import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('picture1.jpg') # read image
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.04
    noisy = np.copy(image)

    num_salt = int(np.ceil(amount * image.size * s_vs_p))
    corrds = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy[corrds] = 1

    num_pep = int(np.ceil(amount * image.size * s_vs_p))
    corrds = [np.random.randint(0, i - 1, num_pep) for i in image.shape]
    noisy[corrds] = 0

    return noisy


img = cv2.imread("picture1.jpg")
img = img / 255
noise_img = saltPepperNoise(img)
cv2.imshow("Gaussian Noise", noise_img)
cv2.waitKey(0)

size_y = img.shape[0]
size_x = img.shape[1]

flattened = img.reshape([size_x*size_y])

rhist,_ ,_ = plt.hist(flattened, bins=256)
plt.show()

rhist,_ ,_ = plt.hist(flattened, bins=32)
plt.show()

rhist,_ ,_ = plt.hist(flattened, bins=8)
plt.show()