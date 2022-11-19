from keras.models import load_model
from keras_preprocessing.image import img_to_array
import cv2
import numpy as np
import os


class EmotionDetector:
    def __init__(self):
        self.absolute_path = os.path.dirname(__file__)

        self.face_classifier = cv2.CascadeClassifier(os.path.join
                                                     (self.absolute_path, "haarcascade_frontalface_default.xml"))
        self.classifier = load_model(os.path.join(self.absolute_path, "EmotionDetectionModel.h5"))

        self.class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']
        self.labels = []
        self.cap = cv2.VideoCapture(0)

    def main_loop(self):
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = self.classifier.predict(roi)[0]
                label = self.class_labels[prediction.argmax()]
                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, 'No Face Found', (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            break

        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()
