import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# 이미지 가져올 목록 생성
path = 'FaceFile'
images = []
classNames = []
myList = os.listdir(path)  # 폴더의 이미지 목록을 가져오기
print("Loaded images:", myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')  # 이미지 읽기
    images.append(curImg)  # 현재 이미지 추가
    classNames.append(os.path.splitext(cl)[0])  # 이미지 이름 추가
print("Class names:", classNames)

# 인코딩 계산하는 함수
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if encode:  # 인코딩 결과가 있는 경우만 추가
            encodeList.append(encode[0])
        else:
            print("No face detected in an image.")
    return encodeList

# 출석 기록 함수
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            current_date = now.strftime("%Y:%m:%d")
            f.writelines(f'\n{name},{dtString},{current_date}')

# 이미지 인코딩
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# IP Webcam 주소 입력
cap = cv2.VideoCapture("http://192.168.x.x:8080/video")  # IP Webcam 주소 입력

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read from webcam. Check the IP address and network.")
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(f"Detected Face: {name}")
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
