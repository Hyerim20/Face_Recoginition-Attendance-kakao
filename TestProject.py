import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# 동적 경로 설정
base_path = os.path.dirname(__file__)
elon_path = os.path.join(base_path, 'FaceFile', 'Elon Musk.jpg')
kang_path = os.path.join(base_path, 'FaceFile', 'kanghyerim.jpg')

# 등록된 얼굴 이미지와 인코딩
imgElon = face_recognition.load_image_file(elon_path)
imgElon_rgb = cv2.cvtColor(imgElon, cv2.COLOR_RGB2BGR)
encodeElon = face_recognition.face_encodings(imgElon)[0]

imgKang = face_recognition.load_image_file(kang_path)
imgKang_rgb = cv2.cvtColor(imgKang, cv2.COLOR_RGB2BGR)
encodeKang = face_recognition.face_encodings(imgKang)[0]

# 저장된 얼굴 데이터
known_face_encodings = [encodeElon, encodeKang]
known_face_names = ["Elon Musk", "Kang Hyerim"]

# 등록된 얼굴 이미지 표시
imgElon_resized = cv2.resize(imgElon_rgb, (200, 200))
imgKang_resized = cv2.resize(imgKang_rgb, (200, 200))
cv2.imshow("Registered - Elon Musk", imgElon_resized)
cv2.imshow("Registered - Kang Hyerim", imgKang_resized)

# 카메라 연결
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("카메라에서 프레임을 읽을 수 없습니다.")
        break

    # 얼굴 감지
    imgS = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = imgS[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    print(f"Face locations: {face_locations}")

    # 얼굴 인코딩
    face_encodings = []
    if len(face_locations) > 0:
        try:
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        except Exception as e:
            print(f"Error during face encoding: {e}")
            face_encodings = []

    # 얼굴 이름 비교 및 표시
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    # 얼굴 위치와 이름을 비디오 프레임에 표시
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
