import gradio as gr
import numpy as np
import cv2
import torch
import random

# Load the YOLO model
# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='custom_yolov5n.pt')

def Show(frame):
    # YOLOv5 모델로 추론 수행
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    results = model(frame)

    # 신호등과 횡단보도가 탐지되었는지 확인하기 위한 플래그
    detected_green = False
    detected_red = False
    detected_cross = False
    detected_dcross = False

    # 결과 분석 및 그리기
    for *xyxy, conf, cls in results.xyxy[0].cpu().numpy():
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
            if conf < 0.2:
                continue
            detected_red = True
            color = (255, 0, 0)

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
        
    
    text_x = int(frame.shape[0]/ 2) - 20
    text_y = int(frame.shape[0]/ 2) - 20
    
    # 텍스트 입력
    if current_state:
        cv2.putText(frame, current_state, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)    
    
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    return frame

with gr.Blocks() as demo:
    with gr.Tab("Using Web : video"):
        with gr.Row():
            image_web = gr.Image(source="webcam", streaming=True, label="Web Cam")
        image_output = gr.Image(label="Output IMG")

        image_web.change(Show, inputs=image_web, outputs=image_output)


demo.launch(share=True)