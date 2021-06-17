# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 19:01:55 2020

@author: a.a.carrion.almagro
"""

from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np


# load cv2 face detection model:
face_detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
face_detection_model = cv2.CascadeClassifier(face_detection_model_path)

# load emotion detection model
emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'
emotion_classifier = load_model(emotion_model_path, compile=False)

EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised", "neutral"]
FRAME_WIDTH = 800

cv2.namedWindow('your_face')
camera = cv2.VideoCapture(0)
while True:
    frame = camera.read()[1]
    #reading the frame
    frame = imutils.resize(frame,width=FRAME_WIDTH)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect faces in the captured frame
    faces = face_detection_model.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
    
    canvas = np.zeros((500, 600, 3), dtype="uint8")
    frameClone = frame.copy()
    if len(faces) > 0:
        faces = sorted(faces, reverse=True,
        key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
        # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
        # the ROI for classification via the CNN
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        label = EMOTIONS[preds.argmax()]
    else: continue

    # create PRobabilities bars.
    for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                # construct the label text
                text = "{}: {:.2f}%".format(emotion, prob * 100)

                # draw the label + probability bar on the canvas
                w = int(prob * 600)
                cv2.rectangle(canvas, (14, (i * 70) + 10),
                (w, (i * 70) + 70), (0, 255, 0), -1)                
                cv2.putText(canvas, text, (20, (i * 70) + 46),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (255, 255, 255), 2)
    
    # draw ROI and label
    cv2.putText(frameClone, label, (fX, fY - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                              (0, 255, 0), 2)


    cv2.imshow('your_face', frameClone)
    cv2.imshow("Probabilities", canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()