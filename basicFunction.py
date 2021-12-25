import cv2
import numpy as np

img = cv2.imread("images/kl_rahul.jpg")

# To convert image to gray image
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# To convert into blur image, (7,7) - numbers should be odd numbers (kernal size), 1 - sigma number
blurImg = cv2.GaussianBlur(grayImg, (7, 7), 1)

# To detect edges - (Canny Image)
# 100,100 - threshhold values for edges
cannyImg = cv2.Canny(img, 100, 100)

# Dialation image
kernal = np.ones((5, 5), np.uint8)
#iternations - width
dialationImg = cv2.dilate(cannyImg, kernal, iterations=1)

# Eroded image
erodedImg = cv2.erode(dialationImg, kernal, iterations=1)

cv2.imshow("Gray Image", grayImg)
cv2.imshow("BLur Image", blurImg)
cv2.imshow("Canny Image", cannyImg)
cv2.imshow("Dialate Image", dialationImg)
cv2.imshow("Eroded Image", erodedImg)


cv2.waitKey(0)
