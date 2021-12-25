import cv2
import numpy as np


def sketch(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(img_gray, (7, 7), 1)
    canny_img = cv2.Canny(blur_img, 20, 50)
    ret, mask = cv2.threshold(canny_img, 30, 175, cv2.THRESH_BINARY_INV)
    return canny_img, mask


cap = cv2.VideoCapture(0)
while True:

    ret, frame = cap.read()
    sketch_img, canny_img = sketch(frame)
    cv2.imshow("Normal", frame)
    cv2.imshow("sketch", sketch_img)
    cv2.imshow("Canny", canny_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
