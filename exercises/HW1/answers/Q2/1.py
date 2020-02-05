import cv2
import numpy as np

window_name = "Grayscale"

cv2.namedWindow(window_name)

img = cv2.imread("flowers.png")

newimg = np.zeros(img.shape, dtype=np.uint8)

newimg[:,:,:] = np.repeat(np.average(a=img, axis=2, weights=(0.114, 0.587, 0.299)), 3, axis=1).reshape(img.shape)

cv2.imshow(window_name, newimg)

cv2.waitKey()
