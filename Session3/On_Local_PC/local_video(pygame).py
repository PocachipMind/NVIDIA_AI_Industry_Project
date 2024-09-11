'''
0 : Green
1 : Cross

2 : D_Cross
3 : Red
'''

import threading
import pygame
import cv2
import torch
import random


# 동영상 파일 열기
video_path = './videos/resized/1.mp4'  # 동영상 파일 경로 설정
cap = cv2.VideoCapture(video_path)

# 웹캠으로 하고싶다면.
# cap = cv2.VideoCapture(0)

# 소리 재생을 위한 pygame 초기화
pygame.mixer.init()

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='custom_yolov5n.pt')

# 소리 파일 경로 설정
crosswalk_sound = pygame.mixer.Sound('crosswalk_sound.mp3')  # 횡단보도가 있다는 소리
can_cross_sound = pygame.mixer.Sound('can_cross_sound.mp3')  # Can Cross 상태일 때 재생할 소리
dont_cross_sound = pygame.mixer.Sound('dont_cross_sound.mp3')  # Don't Cross 상태일 때 재생할 소리

# 소리 재생 상태 플래그
can_cross_playing = False
dont_cross_playing = False
detect_cross_playing = False

# 비동기 재생 함수
def play_sound_async(sound):
    threading.Thread(target=sound.play, daemon=True).start()

# Can Cross 소리 재생 가능
def reset_can_cross():
    global can_cross_playing
    can_cross_playing = False

# Don't Cross 소리 재생 가능
def reset_dont_cross():
    global dont_cross_playing
    dont_cross_playing = False

# detect Cross 소리 재생 가능
def reset_detect_cross():
    global detect_cross_playing
    detect_cross_playing = False



able_cross_frame_counter = 0

pass_counter = 0

d_able_cross_frame_counter = 0

d_pass_counter = 0

detect_cross_frame_counter = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOv5 모델로 추론 수행
    results = model(frame)

    # 신호등과 횡단보도가 탐지되었는지 확인하기 위한 플래그
    detected_green = False
    detected_red = False
    detected_cross = False
    detected_dcross = False

    # 결과 분석 및 그리기
    for *xyxy, conf, cls in results.xyxy[0].cpu().numpy():
        # if conf < 0.5:
        #     continue  # 신뢰도 임계값보다 낮은 경우 건너뛰기
        
        x1, y1, x2, y2 = map(int, xyxy)
        class_id = int(cls)

        # 신호등과 횡단보도 탐지 확인
        if class_id == 0:  # Green 클래스 - 녹색
            if conf < 0.5:
                continue 
            detected_green = True
            color = (0, 255, 0)
        elif class_id == 1:  # Cross 클래스 - 이쁜색
            if conf < 0.5:
                continue 
            detected_cross = True
            color = [random.randint(0, 255) for _ in range(3)]
        elif class_id == 2:  # D_Cross 클래스 - 검정색
            if conf < 0.5:
                continue 
            detected_dcross = True
            color = (0, 0, 0)
        elif class_id == 3:  # Red 클래스 - 빨간색
            if conf < 0.2: # 유독 RED만 검출을 못하므로. ( 선생님과 상의해본 결과 데이터 이슈였음. )
                continue 
            detected_red = True
            color = (0, 0, 255)
            

        # 바운딩 박스 그리기( TensorRT 를 통해 생성된 박스 그리기 코드 채용 )
        label = f"{model.names[class_id]} {conf:.2f}"
        tl = round(0.002 * (frame.shape[0] + frame.shape[1]) / 2) + 1  # line/font thickness
        c1, c2 = (x1, y1), (x2, y2)
        cv2.rectangle(frame, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(frame, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(frame, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

    # 현재 상태를 판단하여 텍스트 표시
    if detected_red or detected_dcross:
        current_state = "Don't Cross"
    elif detected_green and detected_cross:
        current_state = "Can Cross"
    else:
        current_state = "None"  # 탐지가 안된 경우

    # 텍스트 입력
    if current_state:
        cv2.putText(frame, current_state, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 0), 3)

    if detected_cross or detected_dcross:
        cv2.putText(frame, "Detect", (frame.shape[1]-120, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

    
    # 소리 출력 부분 Can_Cross ( 프레임(sound_points)을 넘어가면 소리 낸다, Timer시간동안 소리재생은 안한다.  )
    if current_state == "Can Cross":
        if able_cross_frame_counter >= 30 and not can_cross_playing:
            can_cross_playing = True
            play_sound_async(can_cross_sound)
            threading.Timer(60, reset_can_cross).start()
            detect_cross_frame_counter = 0
        able_cross_frame_counter += 1
    else:
        pass_counter += 1
        if pass_counter >= 40:
            able_cross_frame_counter = 0
            pass_counter = 0
    
    if current_state == "Don't Cross":
        if d_able_cross_frame_counter <= -50 and not dont_cross_playing:
            dont_cross_playing = True
            play_sound_async(dont_cross_sound)
            threading.Timer(60, reset_dont_cross).start()
            detect_cross_frame_counter = 0
        d_able_cross_frame_counter -= 1
    else:
        d_pass_counter += 1
        if d_pass_counter >= 40:
            d_able_cross_frame_counter = 0
            d_pass_counter = 0

    # print(able_cross_frame_counter)


    # Detect 부분
    if detected_cross or detected_dcross:
        if detect_cross_frame_counter >= 20 and not detect_cross_playing:
            detect_cross_playing = True
            play_sound_async(crosswalk_sound)
            threading.Timer(60, reset_detect_cross).start()
        detect_cross_frame_counter += 1
    else:
        detect_cross_frame_counter = 0

    # 결과 프레임 출력
    cv2.imshow('YOLOv5', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()