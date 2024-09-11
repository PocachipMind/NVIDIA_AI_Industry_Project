import sys
import cv2
import imutils
from yolov5Det import YoloV5TRT

model = YoloTRT(library="yolov5/build/libmyplugins.so", engine="yolov5/build/custom_yolov5n.engine", conf=0.2, yolo_ver="v5")

# 이미지를 로드하고 추론 실행
image_path = 'test_img.jpg'  # 입력 이미지 경로
frame = cv2.imread(image_path)  # 이미지 로드

detections = model.Inference(frame)

# 결과 이미지 저장
output_image_path = 'result_RT.jpg'  # 저장할 이미지 경로
cv2.imwrite(output_image_path, frame)

print(f"결과 이미지가 {output_image_path}에 저장되었습니다.")