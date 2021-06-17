
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
FRAME_WIDTH = 1000

cv2.namedWindow('your_face')
camera = cv2.VideoCapture(0)
try:
    
    while True:
        frame = camera.read()[1]
        cv2.namedWindow('your_face',cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('your_face',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        #reading the frame
        frame = imutils.resize(frame,width=1500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detection_model.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
        for (x,y,w,h) in faces:
            roi = gray[y:y + h, x:x + w]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            
            
            preds = emotion_classifier.predict(roi)[0]
            emotion_probability = np.max(preds)
            label = EMOTIONS[preds.argmax()]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                    cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255 ), 2)
            
            
        cv2.imshow('your_face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
