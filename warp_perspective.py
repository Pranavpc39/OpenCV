import cv2
import numpy as np
from numpy.matrixlib.defmatrix import matrix

img = cv2.imread("images/cards.jpg")

width, height = 250, 350

pts1 = np.float32([[273, 62], [407, 123], [184, 259], [325, 322]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

img_op = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Original", img)
cv2.imshow("Output", img_op)

cv2.waitKey(0)
