import cv2

# 동영상 파일 경로
input_video_path = './videos/1.mp4'
output_video_path = './videos/for_pj_resize/1.mp4'

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(input_video_path)

# 원본 동영상의 가로, 세로 크기 가져오기
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 비율 유지하면서 가로 길이를 640으로 조정
new_width = 640
aspect_ratio = original_height / original_width
new_height = int(new_width * aspect_ratio)

# 동영상 포맷, 프레임 속도 가져오기
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)

# 새로운 비디오 파일 생성
out = cv2.VideoWriter(output_video_path, fourcc, fps, (new_width, new_height))

# 동영상 프레임 읽기 및 크기 조정
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임 크기 조정
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # 새로운 동영상 파일에 프레임 쓰기
    out.write(resized_frame)

# 리소스 해제
cap.release()
out.release()

print(f"동영상 크기 조정 완료: {output_video_path}")
