import torch
import cv2

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='custom_yolov5n.pt')

# 이미지를 로드하고 추론 실행
image_path = 'test_img.jpg'  # 입력 이미지 경로
frame = cv2.imread(image_path)  # 이미지 로드


results = model(frame)  # 이미지에 대한 모델 추론

print()
print(f"[ Base ] Inference Time: {results.t[1]:.4f} microseconds") # t[0]은 전처리 t[1]은 추론 t[2]는 후처리

