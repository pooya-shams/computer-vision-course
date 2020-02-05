import cv2

circle = cv2.imread("circle.png")
rectangle = cv2.imread("rectangle.png")

And = cv2.bitwise_and(circle, rectangle) # -> (image 1, image 2, mask which means part(optional)) --> returns bitwise gate of any pixel in two images(they should be the same size)
Or = cv2.bitwise_or(circle, rectangle)
Xor = cv2.bitwise_xor(circle, rectangle)
Not = cv2.bitwise_not(circle, rectangle)

cv2.imshow("and", And)
cv2.imshow("or", Or)
cv2.imshow("xor", Xor)
cv2.imshow("not", Not)
cv2.waitKey(0)
cv2.destroyAllWindows()
