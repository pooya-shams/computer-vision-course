from __future__ import print_function

import cv2 as cv

alpha = 0.5

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

print(''' Simple Linear Blender
-----------------------
* Enter alpha [0.0-1.0]: ''')
input_alpha = float(raw_input().strip())
if 0 <= alpha <= 1:
    alpha = input_alpha
# [load]
src1 = cv.imread('LinuxLogo.jpeg')
src2 = cv.imread('WindowsLogo.png')
# [load]
if src1 is None:
    print("Error loading src1")
    exit(-1)
elif src2 is None:
    print("Error loading src2")
    exit(-1)
# [blend_images]
beta = (1.0 - alpha)
dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
# [blend_images]
# [display]
cv2.imshow('dst', dst)
cv2.waitKey(0)
# [display]
cv2.destroyAllWindows()