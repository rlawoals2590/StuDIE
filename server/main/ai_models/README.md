# Studying recognition with mediapipe

> mediapipe의 Hand landmark detection & Face detection & Face landmark detection을 사용해 사용자가 학습중인지를 판별하는 프로젝트이다.

> mediapipe가 제공하는 Hand landmark detection, Face detection. Face landmark을 사용한다.

> mediapipe Solutions sites
* https://developers.google.com/mediapipe/solutions/vision/hand_landmarker
* https://developers.google.com/mediapipe/solutions/vision/face_detector
* https://developers.google.com/mediapipe/solutions/vision/face_landmarker

# 모델 사용 방법

> repository에 첨부한 ' checkout_studying.py '에 CHECKOUT_STUDYING 클래스를 사용한다.

### librarys
```
mediapipe version : 0.10.2
```

### function
```python
detection = CHECKOUT_STUDYING()
score = detection.start_detection("--your image path")
```
