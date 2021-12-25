import cv2

# TO read image
img = cv2.imread("images/lambo.jpg")
print(img.shape)

# To resize image
resizedImg = cv2.resize(img, (300, 300))

# To Crop image
croppedImg = img[100:600, 400:]

# to display image
cv2.imshow("Output", img)
cv2.imshow("Resized", resizedImg)
cv2.imshow("Cropped", croppedImg)


# TO add delay while showing image, 0 - means infinite
cv2.waitKey(0)
