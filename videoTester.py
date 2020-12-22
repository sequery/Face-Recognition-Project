import os
import cv2
import numpy as npq
import faceRecognition as fr

# This module captures images via webcam and performs face recognition
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')  # Load saved training data

name = {1: "Dwayne Johnson", 2: "Ulanyjy", 3: "Ulanyjy"}

cap = cv2.VideoCapture(0)

while True:
    ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
    faces_detected, gray_img = fr.faceDetection(test_img)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)

    for face in faces_detected:
        (x, y, w, h) = face
        roi_gray = gray_img[y:y + w, x:x + h]
        label, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
        print("confidence:", confidence)
        print("label:", label)
        fr.draw_rect(test_img, face)
        predicted_name = name[label]
        if confidence < 30:  # If confidence less than 30 then don't print predicted face text on screen
            fr.put_text(test_img, predicted_name, x, y)
        else:
            fr.put_text(test_img, "Tanamok", x, y)
    resized_img = cv2.resize(test_img, (720, 480))
    cv2.imshow('face recognition tutorial ', resized_img)
    if cv2.waitKey(1) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows()
