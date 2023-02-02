import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/pic.jpg")
normal = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converted to BGR format.


def get_image(image, cmap =None):
    plt.imshow(image, cmap = cmap)
    plt.show()

#Colorized
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
get_image(hsv)


# grayscale

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
get_image(gray, cmap= "gray")

#blurred...

