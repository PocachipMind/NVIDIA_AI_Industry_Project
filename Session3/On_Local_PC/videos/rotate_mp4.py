import cv2

input_video_path = 'videos/alls/rotate.mp4'
output_video_path = 'output_video_rotated.mp4'

cap = cv2.VideoCapture(input_video_path)

if not cap.isOpened():
    print("Error: Could not open input video.")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Frame size: {frame_width}x{frame_height}, FPS: {fps}")

rotated_frame_width = frame_height
rotated_frame_height = frame_width

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (rotated_frame_width, rotated_frame_height))

if not out.isOpened():
    print("Error: Could not write to output video.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Reached end of video or error occurred.")
        break
    
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    out.write(rotated_frame)

cap.release()
out.release()
cv2.destroyAllWindows()
