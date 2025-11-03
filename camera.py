import cv2
import numpy as np

# Load pre-trained models from OpenCV's GitHub
AGE_MODEL = "https://github.com/spmallick/learnopencv/raw/master/AgeGender/opencv_face_detector_uint8.pb"
AGE_PROTO = "https://github.com/spmallick/learnopencv/raw/master/AgeGender/opencv_face_detector.pbtxt"
AGE_NET = "https://github.com/spmallick/learnopencv/raw/master/AgeGender/age_net.caffemodel"
AGE_DEPLOY = "https://github.com/spmallick/learnopencv/raw/master/AgeGender/age_deploy.prototxt"

# Download files if not present
import os
import urllib.request

def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)

download_file(AGE_MODEL, "opencv_face_detector_uint8.pb")
download_file(AGE_PROTO, "opencv_face_detector.pbtxt")
download_file(AGE_NET, "age_net.caffemodel")
download_file(AGE_DEPLOY, "age_deploy.prototxt")

# Load models
face_net = cv2.dnn.readNet("opencv_face_detector_uint8.pb", "opencv_face_detector.pbtxt")
age_net = cv2.dnn.readNet("age_net.caffemodel", "age_deploy.prototxt")

# Age categories
AGE_BUCKETS = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], False, False)
    face_net.setInput(blob)
    detections = face_net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.6:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")
            face = frame[y1:y2, x1:x2]

            if face.size == 0:
                continue

            face_blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
            age_net.setInput(face_blob)
            age_preds = age_net.forward()
            age = AGE_BUCKETS[age_preds[0].argmax()]

            label = f"Age: {age}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("Age Estimation", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()