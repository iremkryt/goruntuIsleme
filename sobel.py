# Sobel Edge Detection
import cv2

try:
    img = cv2.imread('picture1.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
except Exception as e:
    print(str(e))

img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

cv2.imshow('Sobel X', img_sobelx)
cv2.waitKey(0)

cv2.imshow('Sobel Y', img_sobely)
cv2.waitKey(0)

cv2.imshow('Sobel X Y using Sobel() function', img_sobel)
cv2.waitKey(0)