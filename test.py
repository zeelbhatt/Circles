import numpy as np
import cv2
import matplotlib.pyplot as plt

image  = cv2.imread("1.png")

trgb = np.sum(image, axis = 2)

a = trgb < 720

x = a.astype(int)

plt.imshow(x)

plt.show()
