import cv2

img = cv2.imread("1.png")

font = cv2.FONT_HERSHEY_PLAIN

cv2.line(img, (100, 50), (300, 400), (0, 0, 255), 5) # draws a line, positions are (x, y), color is bgr -> (image matrix, start pos, end pos, color, width)
cv2.rectangle(img, (200, 500), (800, 900), (0, 132, 195), 10) # draws a rectangle, positions are (x, y), color is bgr -> (image matrix, up left pos, down right pos, color, width)
cv2.circle(img, (400, 600), 400, (0, 255, 0), 3) # draws a circle
cv2.ellipse(img, (300, 300), (400, 200) , 10, 45, 275, (0, 255, 0), 10) # draws an ellipse (image matrix, center, (width, height) , angle, start angle, end angle, color, thickness)
cv2.putText(img, "Detected", (250, 220), font, 10, (0, 255, 0), 5) # writes something -> (image matrix, text, start pos, font, size, color, thickness)


cv2.imshow("image window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
