import cv2

# # TO read image
# img = cv2.imread("images/goku.jpg")

# # to display image
# cv2.imshow("Output", img)
# # TO add delay while showing image, 0 - means infinite
# cv2.waitKey(0)

###################################

# # TO capture video

# # reading video file
# cap = cv2.VideoCapture("video/goku_Vs_jiren.mp4")

# while True:
#     # video = images frames, will store all frames and display with img
#     # success - boolean var if video captured succefully or not
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     # if q is pressed video will be stopped
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
###################################

# TO capture video from webcam

#0- means default webcam ID
cap = cv2.VideoCapture(0)
# setting height
cap.set(3,640)
# setting width
cap.set(4,480)

while True:
    # video = images frames, will store all frames and display with img
    # success - boolean var if video captured succefully or not
    success, img = cap.read()
    cv2.imshow("Video", img)
    # if q is pressed video will be stopped
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

###################################