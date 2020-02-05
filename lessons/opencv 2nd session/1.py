""" indirect way of getting binary image
colored image -> gray -> binary """

import cv2

img = cv2.imread("ball.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converts the color to other types -> (image matrix, type of convertion)

T, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY) # -> (gray input image matrix, range:int, maximum -> what will be the balck color, range type) --> returns 
#                                         cv2.THRESH_BINARY -> just thresh binary
#                                         cv2.THRESH_BINARY_INV -> inverses the thresh binary
cv2.imshow("window", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
