import cv2
import numpy as np


def empty(a):
    pass


# Create a new cv2 window for trackbar
cv2.namedWindow("Trackbar")

cv2.resizeWindow("Trackbar", 670, 240)
# Create a trackbar
cv2.createTrackbar("Hue Min", "Trackbar", 10, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 18, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 85, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 197, 255, empty)
cv2.createTrackbar("Val Max", "Trackbar", 255, 255, empty)


while True:
    img = cv2.imread("images/lambo.jpg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbar")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    cv2.imshow("Normal", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    cv2.waitKey(1)
