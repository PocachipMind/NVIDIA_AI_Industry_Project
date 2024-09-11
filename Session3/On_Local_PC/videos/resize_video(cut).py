import cv2

# 동영상 파일 경로
input_video_path = './videos/temp.mp4'
output_video_path = './videos/resized/temp.mp4'

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(input_video_path)

# 원본 동영상의 가로, 세로 크기 가져오기
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 비율 유지하면서 세로 길이를 480으로 조정
new_height = 480
aspect_ratio = original_width / original_height  # 가로/세로 비율
new_width = int(new_height * aspect_ratio)

# 세로 길이 기준으로 가로 길이가 640을 넘는 경우 잘라내기 위한 크기 계산
if new_width > 640:
    crop_start = (new_width - 640) // 2  # 중앙에서 잘라내기 시작
else:
    crop_start = 0

# 동영상 포맷, 프레임 속도 가져오기
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)

# 새로운 비디오 파일 생성 (640x480 고정)
out = cv2.VideoWriter(output_video_path, fourcc, fps, (640, new_height))

# 동영상 프레임 읽기 및 크기 조정
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임 크기 조정 (세로 480, 가로 비율 유지)
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # 가로 중앙 부분을 기준으로 640 너비로 자르기
    cropped_frame = resized_frame[:, crop_start:crop_start + 640]

    # 새로운 동영상 파일에 프레임 쓰기
    out.write(cropped_frame)

# 리소스 해제
cap.release()
out.release()

print(f"동영상 크기 조정 및 잘라내기 완료: {output_video_path}")