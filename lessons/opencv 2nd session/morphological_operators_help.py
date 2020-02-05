import cv2

#cv2.erode(img, kernel, iterations:int, ...)
#cv2.dilate(img, kernel, iterations:int, ...)
#cv2.morphologyEx(img, operator, kernel=None)
#                      cv2.MORPH_OPEN -> erode + dilate
#                      cv2.MORPH_CLOSE -> dilate + erode
#                      cv2.MORPH_GRADIENT -> dilate - erode
#                                cv2.getStructuringElement(shape=(5, 5), ) -> creates a kernel

# conts, hierachy = cv2.findContours(binary input image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) --> returns the edges, and their connections
#                                    cv2.RETR_TREE -> 
#                                    cv2.RETR_EXTERNAL -> 
#                                                    cv2.CHAIN_APPROX_SIMPLE -> approximates the conts
#                                                    cv2.CHAIN_APPROX_NONE -> gives exact conts

# cv2.drawContours(img, cont, contourIDx, color, thickness)

# -- area --
# cv2.contourArea(cont) --> returns the area of the contour

# -- center --
#    M = cv2.moments(max_contour)
#    cX = int(M["m10"]/M["m00"])
#    cY = int(M["m01"]/M["m00"])

# -- length
#cv2.arcLength(contour, closed -> if the contour is closed or not -> the last point connects the first or not)


#    epsilone = 0.01 * cv2.arcLength(max_contour, True) # better be multipled by 0.01 ~ 0.05
#    approx = cv2.approxPolyDP()


# (x, y), r = cv2.minEnclosingCircle(max_contour)
