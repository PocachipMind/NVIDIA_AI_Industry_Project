import torch
import cv2
import random

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='custom_yolov5n.pt')

# 이미지를 로드하고 추론 실행
image_path = 'test_img.jpg'  # 입력 이미지 경로
frame = cv2.imread(image_path)  # 이미지 로드
results = model(frame)  # 이미지에 대한 모델 추론

# 바운딩 박스를 그리기
for *xyxy, conf, cls in results.xyxy[0].cpu().numpy():
    if conf < 0.5:
        continue  # 신뢰도 임계값보다 낮은 경우 건너뛰기

    x1, y1, x2, y2 = map(int, xyxy)
    class_id = int(cls)

    # 신호등과 횡단보도 탐지 확인
    if class_id == 0:  # Green 클래스 - 녹색
        detected_green = True
        color = (0, 255, 0)
    elif class_id == 1:  # Cross 클래스 - 임의의 색
        detected_cross = True
        color = [random.randint(0, 255) for _ in range(3)]
    elif class_id == 2:  # D_Cross 클래스 - 검정색
        detected_dcross = True
        color = (0, 0, 0)
    elif class_id == 3:  # Red 클래스 - 빨간색
        detected_red = True
        color = (0, 0, 255)

    # 바운딩 박스 그리기
    label = f"{model.names[class_id]} {conf:.2f}"
    tl = round(0.002 * (frame.shape[0] + frame.shape[1]) / 2) + 1  # line/font thickness
    c1, c2 = (x1, y1), (x2, y2)
    cv2.rectangle(frame, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    tf = max(tl - 1, 1)  # font thickness
    t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
    c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
    cv2.rectangle(frame, c1, c2, color, -1, cv2.LINE_AA)  # filled
    cv2.putText(frame, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

# 결과 이미지 저장
output_image_path = 'result_base.jpg'  # 저장할 이미지 경로
cv2.imwrite(output_image_path, frame)

print(f"결과 이미지가 {output_image_path}에 저장되었습니다.")


