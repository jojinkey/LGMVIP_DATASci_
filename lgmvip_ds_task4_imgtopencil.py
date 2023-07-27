# -*- coding: utf-8 -*-
"""LGMVIP_DS_TASK4_imgtopencil.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eNIoC0ON1Dd-8eZnykxTABpBaj8UFHDw

<center><h1>TASK 4</h1></center>
<center><h1>IMAGE TO PENCIL SKETCH WITH PYTHON</h1></center>
<center> </h2>
    <h3> by -Jalaj Singh </h3></center>
    <center><h1><b><font color="blue"> Let's Grow More </b></h1>

1. IMPORTING LIBRARIES
"""

import cv2
import matplotlib.pyplot as plt

"""2. LOADING A IMAGE IN RGB FORMAT"""

img = cv2.imread("image.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.axis("off")
plt.title("Original image")
plt.show()

"""3. CONVERTING THE IMAGE INTO GRAYSCALE (BLACK & WHITE)"""

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray,cmap="gray")
plt.axis("off")
plt.title("Grayscale Image")
plt.show()

"""4. INVERTING THE IMAGE"""

inverted_gray_image = 255 - img_gray
plt.imshow(inverted_gray_image,cmap="gray")
plt.axis("off")
plt.title("Inverted Image")
plt.show()

"""5.BLURRING THE IMAGE"""

blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)
plt.imshow(blurred_img, cmap="gray")
plt.axis("off")
plt.title("Blurred Image")
plt.show()

"""5. GENERATING THE SKETCH IMAGE"""

final = cv2.divide(img_gray, 255 - blurred_img, scale = 255)
plt.imshow(final, cmap="gray")
plt.axis("off")
plt.title("Sketch Image")
plt.show()

"""7. ALL TRANSITION AT ONCE"""

plt.figure(figsize=(20,20))
plt.subplot(1,5,1)
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.subplot(1,5,2)
plt.imshow(img_gray,cmap="gray")
plt.axis("off")
plt.title("GrayScale Image")
plt.subplot(1,5,3)
plt.imshow(inverted_gray_image,cmap="gray")
plt.axis("off")
plt.title("Inverted Image")
plt.subplot(1,5,4)
plt.imshow(blurred_img,cmap="gray")
plt.axis("off")
plt.title("Blurred Image")
plt.subplot(1,5,5)
plt.imshow(final,cmap="gray")
plt.axis("off")
plt.title("Sketch Image")
plt.show()