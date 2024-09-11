import torch


model = torch.hub.load('ultralytics/yolov5', 'custom', path='custom_yolov5n.pt')

dummy_input = torch.randn(1, 3, 640, 640)

torch.onnx.export(
    model,                         # 변환할 모델
    dummy_input,                   # 더미 입력
    "custom_yolo_onnx.onnx",           # 저장할 ONNX 파일 이름
    export_params=True,            # 학습된 가중치와 파라미터들을 함께 저장
    opset_version=12,              # ONNX opset 버전 (최신 버전 확인 가능)
    do_constant_folding=True,      # 상수 폴딩 최적화
    input_names=['input'],         # 입력 노드 이름
    output_names=['output'],       # 출력 노드 이름
    dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}  # 동적 배치 크기 지원
)