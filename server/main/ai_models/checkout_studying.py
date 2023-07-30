import cv2
import numpy as np
import mediapipe as mp
import time
import math

class CHECKOUT_STUDYING :
    def __init__(self, time) :
        # hand detection
        self.mp_hands = mp.solutions.hands
        self.middle_finger_mcp_list = []
        self.no_detection_time = None
        self.not_moved_time = None
        self.previous_dot_distance = None
        
        # face detection
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_face_mesh = mp.solutions.face_mesh
        self.eye_closed_time = None
      
        self.user_score = 100
        
        # set time
        self.time = time
        
    def pythagorean_theorem_dot_dist(selft, coordinate_list):
        dot_distance = math.sqrt((coordinate_list[0].x - coordinate_list[1].x)**2 + (coordinate_list[0].y - coordinate_list[1].y)**2 + (coordinate_list[0].z - coordinate_list[1].z)**2)
        return dot_distance
    
    def hand_checkout(self, image) :
        with self.mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands: 
            not_studying = False
            
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                self.middle_finger_mcp_list.append(results.multi_hand_landmarks[0].landmark[9])
                
                # 손이 움직이지 않는지 판별하는 코드
                if len(self.middle_finger_mcp_list) > self.time :
                    dot_distance = self.pythagorean_theorem_dot_dist(self.middle_finger_mcp_list)
                    if self.previous_dot_distance is not None:
                        distance_change = abs(dot_distance - self.previous_dot_distance)
                        if distance_change <= 0.03:
                            if self.not_moved_time is None :
                                self.not_moved_time = time.time()
                            elif time.time() - self.not_moved_time > 3 :
                                not_studying = True
                                self.not_moved_time = None
                        else : 
                            self.not_moved_time = None
                            
                    self.previous_dot_distance = dot_distance
                    self.middle_finger_mcp_list.pop(1)
                
                self.no_detection_time = None  # 손이 감지되면 감지되지 않는 시간을 초기화
            else:
                if self.no_detection_time is None:
                    self.no_detection_time = time.time()  # 손이 감지되지 않는 시간을 기록 시작
                elif time.time() - self.no_detection_time > self.time :  # 손이 감지되지 않는 시간이 5초 이상 지나면
                    not_studying = True
                    self.no_detection_time = None
        return not_studying
    
    def face_checkout(self, image) :
        with self.mp_face_detection.FaceDetection(
            model_selection=1, 
            min_detection_confidence=0.5) as face_detection :
            not_studying = False
            
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections :
                for detection in results.detections:
                    if detection.location_data:
                        box = detection.location_data.relative_bounding_box
                        ih, iw, _ = image.shape
                        x, y, w, h = int(box.xmin * iw), int(box.ymin * ih), int(box.width * iw), int(box.height * ih)
                        # Crop the face with margins
                        face_image = image[y:y+h, x:x+w]
                        face_image = cv2.resize(face_image, dsize=(500, 500), interpolation=cv2.INTER_AREA)
                        
                        with self.mp_face_mesh.FaceMesh(
                            max_num_faces=1,
                            refine_landmarks=True) as face_mesh :

                            face_image.flags.writeable = False
                            face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
                            results = face_mesh.process(face_image)
    
                            face_image.flags.writeable = True
                            face_image = cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR)
                            if results.multi_face_landmarks :
                                LEFT_TOP_EYELID = 159
                                LEFT_BOTTOM_EYELID = 145
                            
                                RIGHT_TOP_EYELID = 386
                                RIGHT_BOTTOM_EYELID = 374
                                
                                for face_landmarks in results.multi_face_landmarks:
                                    left_top_eyelid_coordinate = face_landmarks.landmark[LEFT_TOP_EYELID]
                                    left_bottom_eyelid_coordinate = face_landmarks.landmark[LEFT_BOTTOM_EYELID]
                                    
                                    right_top_eyelid_coordinate = face_landmarks.landmark[RIGHT_TOP_EYELID]
                                    right_bottom_eyelid_coordinate = face_landmarks.landmark[RIGHT_BOTTOM_EYELID]
                                    
                                    left_distance = self.pythagorean_theorem_dot_dist([left_top_eyelid_coordinate, left_bottom_eyelid_coordinate])
                                    right_distance = self.pythagorean_theorem_dot_dist([right_top_eyelid_coordinate, right_bottom_eyelid_coordinate])
                                    
                                    if left_distance <= 0.04 and right_distance <= 0.045 :
                                        if self.eye_closed_time is None :
                                            not_studying = True
                                        elif time.time() - self.eye_closed_time > self.time :
                                            not_studying = True
                                            self.eye_closed_time = None
                            else :
                                not_studying = True
            else :
                not_studying = True
    
        return not_studying                                    
    def start_detection(self, image_path : str) :
        image = cv2.imread(image_path)
        if self.face_checkout(image) and self.hand_checkout(image) :
            if self.user_score > 0 :
                self.user_score -= 2
            
        return self.user_score