import sys
import cv2
import imutils
from yoloDet import YoloTRT

model = YoloTRT(library="yolov5/build/libmyplugins.so", engine="yolov5/build/custom_yolov5n.engine", conf=0.2, yolo_ver="v5")

# 이미지를 로드하고 추론 실행
image_path = 'test_img.jpg'  # 입력 이미지 경로
frame = cv2.imread(image_path)  # 이미지 로드

detections, t = model.Inference(frame)

print(f"[ tensorRT ] Inference Time: {1000*t:.4f} microseconds")