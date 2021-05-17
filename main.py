import cv2
from random import randrange

##### For Pictures
# #load pretrained data
# trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# #import image
# img = cv2.imread("avengers.jpeg")
#
# #must convert to grayscale
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #detect faces
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#
# #print(face_coordinates)
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y) , (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 3)
#
# #show briefly
# cv2.imshow("Face Detector", img)
# #waits for a pressed key
# cv2.waitKey()
# print("code completed")
################################################
##### Video
#load pretrained data
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#capture video
webcam = cv2.VideoCapture(0)
while True:
    successful_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("Face Detector", frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break
#  release webcam
webcam.release()

print("Code completed")