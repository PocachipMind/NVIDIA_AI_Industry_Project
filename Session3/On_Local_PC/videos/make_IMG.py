import cv2
import os


video_directory = "./videos/test"

for video_file in os.listdir(video_directory):
    if video_file.endswith(('.mp4', '.avi', '.mov')):
        video_path = os.path.join(video_directory, video_file)
        cap = cv2.VideoCapture(video_path)
        frame_number = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # 프레임에 텍스트 추가 및 저장
            output_image_file = os.path.join("videos\make_img_from_mp4", f"{os.path.splitext(video_file)[0]}_frame{frame_number:04d}.jpg")

            cv2.imwrite(output_image_file, frame)  # 결과 이미지를 저장

            frame_number += 1

        cap.release()
