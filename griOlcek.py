import cv2
from PIL import Image

img = cv2.imread('picture1.jpg', 2)

ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def pixelate(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    image.save("picture1.jpg")

pixelate("picture1.jpg",8)
