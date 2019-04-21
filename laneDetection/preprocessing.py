import cv2
import numpy as np

image = cv2.imread("./base_imagenes/bd_10.jpg")
(h, w, d) = image.shape
print("alto: {}, ancho: {}, profundidad: {}".format(h, w, d))
cv2.imshow("Imagen", image)
cv2.waitKey(0)

# (B, G, R) = image[19, 89]
# print("Blue: {}, Green: {}, Red: {}".format(B, G, R))

roi = image[h//2:h-20, 0:w]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resized = cv2.resize(image, (200, 200))
# cv2.imshow("Resized", resized)
# cv2.waitKey(0)

gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.waitKey(0)

thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

edged = cv2.Canny(gray, 50, 150)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

edged2 = cv2.Canny(thresh, 50, 150)
cv2.imshow("Edged2", edged2)
cv2.waitKey(0)

lines = cv2.HoughLinesP(edged2, 1, np.pi/100, 40, minLineLength=50, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(roi, (x1, y1), (x2, y2), (255, 0, 0), 3)
cv2.imshow("Hough", roi)
cv2.waitKey(0)