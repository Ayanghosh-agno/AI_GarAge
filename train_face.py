import cv2
import os
import face_recognition

donface=face_recognition.load_image_file("Training_image_2.jpg")
donEncode=face_recognition.face_encodings(donface)[0]

nancyface=face_recognition.load_image_file("Training_image_1.jpg")
nancyEncode=face_recognition.face_encodings(nancyface)[0]

