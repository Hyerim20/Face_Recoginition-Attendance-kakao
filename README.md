# Face Recognition Attendance System

## 소개
이 프로젝트는 학교에서 출석체크 시 대리출석 방지를 목표로 개발된 **얼굴 인식 기반 출석 관리 시스템**입니다.  
등록된 얼굴 이미지를 기반으로 카메라에서 실시간으로 감지된 얼굴과 비교하여 출석 여부를 확인합니다.  
또한, 출석 기록은 자동으로 저장되며, 이를 **카카오톡 API**를 통해 실시간으로 공유할 수 있습니다.

---

## 프로젝트 주요 기능

1. **얼굴 인식 기반 출석 확인**
   - 등록된 얼굴 데이터와 웹캠으로 실시간 감지된 얼굴을 비교하여 일치 여부를 판단합니다.
   - 얼굴 일치 여부를 바탕으로 사용자의 이름을 확인하고 출석 시간을 기록합니다.

2. **카카오톡 API를 통한 데이터 공유**
   - 출석 기록(출석 시간 및 사용자 이름)을 카카오톡 '나와의 채팅' 기능을 통해 실시간으로 전송할 수 있습니다.
   - 토큰 갱신 및 메시지 전송 자동화 기능 포함.

3. **테스트 모듈**
   - 등록된 얼굴 이미지와 테스트 이미지를 비교하여 얼굴 일치 확률을 확인합니다.
   - 웹캠을 통해 실시간으로 얼굴을 감지하고 등록된 인물과의 일치 여부를 판단합니다.

4. **출석 데이터 관리**
   - 출석 시간과 이름을 `CSV 파일 (Attendance.csv)`로 저장합니다.
   - 날짜와 시간을 기준으로 출석 기록을 유지합니다.

---

## 사용된 기술 및 툴

- **프로그래밍 언어**: Python  
- **라이브러리**:  
  - `face_recognition`: 얼굴 감지 및 비교  
  - `opencv-python`: 실시간 영상 처리  
  - `requests`: HTTP 요청 처리 (카카오 API)  
  - `numpy`: 데이터 연산  
- **API**: Kakao API (OAuth2 및 메시지 전송)  
- **파일 형식**: CSV (출석 기록 저장)  

---

## 실행 환경

- Python 3.7 이상  
- 필수 라이브러리 설치:
  ```bash
  pip install face_recognition opencv-python requests numpy
ognition-Attendence-Record

---
---

## 테스트

### 1. 얼굴 이미지 유사성 테스트
- `Face recognition Test.py`를 실행하여 등록된 얼굴 이미지와 테스트 이미지 간의 유사성을 확인합니다:
  ```bash
  python FaceRecognitionTest.py

### 2. 웹캠 테스트
- `test.py`를 실행하여 실시간 얼굴 감지를 테스트합니다:
  ```bash
  python test.py
  
### 3. 출석 기록 테스트
- 웹캠에서 감지된 얼굴 정보를 Attendance.csv 파일에 기록 후 카톡으로 전송 가능합니다 :
  ```bash
    python FaceAttendance.py
    python send_kakao.py

---

## 데모 영상 및 스크린샷

### 데모 영상

1. **웹캠 테스트**  
   [![웹캠 테스트 데모](https://via.placeholder.com/600x400?text=Webcam+Test+Demo)](https://youtu.be/54gbMIA_T5M)

2. **얼굴 인식 데모**  
   [![얼굴 인식 데모](https://via.placeholder.com/600x400?text=Face+Recognition+Demo)](https://youtu.be/mGLfRhTNF9I)

---

### 스크린샷

1. **얼굴 인식 화면**  
   ![TRUE](https://github.com/Hyerim20/Face_Recoginition-Attendance-kakao/blob/main/test_image.png)
   ![FALSE](https://github.com/Hyerim20/Face_Recoginition-Attendance-kakao/blob/main/test_image_false.png)

2**카카오톡 메시지 전송 화면**  
   ![카카오톡 메시지 화면](https://github.com/Hyerim20/Face_Recoginition-Attendance-kakao/blob/main/kakao_send_image.png)

------

## 개선 방안 및 추가 개발 예정 기능

1. **출석 데이터 시각화**
   - 출석 기록을 그래프나 차트로 시각화하여 출석률 분석.
   - `matplotlib` 라이브러리를 사용하여 출석 현황을 시간대별로 파악 가능.

2. **사용자 인터페이스 개선**
   - 웹 기반 인터페이스 추가 개발 (e.g., Flask 또는 Django 활용).
   - 출석 결과 및 관리 페이지 제공.

3. **모바일 지원**
   - 모바일 애플리케이션 연동 (카메라를 통한 얼굴 인식 기능 포함).

4. **안전성 향상**
   - 얼굴 데이터 암호화 및 안전한 저장 방식 구현.
   - 사용자의 개인 정보를 보호하기 위한 데이터 처리 방식 추가.

5. **다중 카메라 지원**
   - 여러 장소에서 동시에 출석체크 가능하도록 다중 카메라 입력 지원.

---
