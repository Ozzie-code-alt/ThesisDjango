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

#blurrds...
width, height = normal.shape[:2] #slice the flags
print(width)
print(height)
if width > 500:
    k=(50,50)
elif width > 200 and width <=500:
    k=(25,25)
else:
    k=(10,10)

blur = cv2.blur(normal,k)
get_image(blur)

# binary Imaged
v, binary = cv2.threshold(gray, 50,200, cv2.THRESH_BINARY)
get_image(binary,cmap='gray')


#inverted black and white
inverted = cv2.bitwise_not(binary)
get_image(inverted,cmap= 'gray')

