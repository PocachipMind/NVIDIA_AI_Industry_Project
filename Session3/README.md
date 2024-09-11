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

## 학습 데이터

AI Hub, GitHub 등 인터넷에서 찾아낸 데이터와 직접 촬영한 데이터.

### 1. AI HUB | 인도보행 영상 데이터셋

https://github.com/samuelyu2002/ImVisible?tab=readme-ov-file

### 2. 중국 횡단보도 이미지 | ImVisible 데이터셋

https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=189

### 3. 직접 촬영한 데이터


<br>


위 사이트들을 통해 얻은 이미지의 경우 라벨링이 내가 원하는 방식으로 되어있지 않아 최종 약 3000장 직접 일일이 라벨링.

직접 촬영한 데이터가 학습에 대략 40% 차지.

![image](https://github.com/user-attachments/assets/baf91b30-0623-47ef-af03-e2ee1b09ddab)


