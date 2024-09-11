# CrossWalk Detection For ImVisible People

시각 장애인을 위한 횡단보도 감지 프로그램.

#### 시연 영상 [ 소리 존재 ]
https://github.com/user-attachments/assets/5aa59ae5-6378-41ce-a4fd-6294c21793b9


## 개요
시각 장애인들이 횡단보도를 건널 때 도움이 되는 프로그램을 제작.

![image](https://github.com/user-attachments/assets/e4023c74-21d5-45e2-919a-5c607dc806aa)
![image](https://github.com/user-attachments/assets/a0510546-c6af-4d14-a19e-3c5db41270ac)

## Repository 설명
- On_Jetson_Nano :
  
  젯슨 나노 기기에서 TensorRT로 최적화한 모델을 시연.
- On_Local_PC :
  
  윈도우11 환경에서 pt 모델을 시연.
- Submissions :
  
  시연 영상 및 설명 ppt 기재
- Test_Performance

  기본 pt 모델, ONNX 모델, TensorRT로 최적화된 모델. 이 세 모델을 비교하기 위한 코드들
