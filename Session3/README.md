# CrossWalk Detection For ImVisible People

시각 장애인을 위한 횡단보도 감지 프로그램.

#### 시연 영상 [ 소리 존재 ]
https://github.com/user-attachments/assets/5aa59ae5-6378-41ce-a4fd-6294c21793b9

- 횡단 보도를 발견하면 :
  Crosswalk Detected 라고 소리가 나서 착용자에게 횡단보도가 있음을 인식시킵니다.

- 횡단 보도가 현재 빨간불이거나 자동차가 있어서 건널 수 없다면 :
  You can not cross. Please wait a moment. 소리를 통해 착용자가 기다리도록 이야기합니다.

- 횡단 보도가 초록불이며 건널 수 있다면 :
  You can cross over. Please cross with care. 소리를 통해 현재 건널 수 있음을 알려줍니다.

## 개요
시각 장애인들이 횡단보도를 건널 때 도움이 되는 프로그램을 제작.

![image](https://github.com/user-attachments/assets/6ea7403f-2d09-4367-ad90-65da1d45d94a)

![image](https://github.com/user-attachments/assets/57c39be4-4e74-46d2-ae23-3a1c84bd77cb)


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

#### 1. AI HUB | 인도보행 영상 데이터셋

https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=189

<img src="https://github.com/user-attachments/assets/a9a9fd26-bc6d-46c8-9845-41162e8435ba" width="70%" height="70%"/>

- 이미지 예시
  <img src="https://github.com/user-attachments/assets/a21ef189-8664-4fbc-b30c-3af90b039b13" width="50%" height="50%"/>


#### 2. 중국 횡단보도 이미지 | ImVisible 데이터셋

https://github.com/samuelyu2002/ImVisible?tab=readme-ov-file

<img src="https://github.com/user-attachments/assets/66aeb372-7773-4596-9527-79f6a9b89d1a" width="50%" height="50%"/>


#### 3. 직접 촬영한 데이터

<img src="https://github.com/user-attachments/assets/9826325a-dd59-434a-b1dc-6d57d56c0673" width="50%" height="50%"/>


<br>


위 사이트들을 통해 얻은 이미지의 경우 라벨링이 내가 원하는 방식으로 되어있지 않아 직접 일일이 라벨링.

직접 촬영한 데이터가 학습에 대략 30% 차지.

![image](https://github.com/user-attachments/assets/a74999f8-81df-4036-9020-2526265a6e37)



## 학습 모델

최종적으로 Nano Jetson에 적용할 것이므로 Fast RCNN 보다 6배 빠른 YOLO 채택

Yolov5, Yolov7 두 모델 모두 TensorRT 가능BUT Yolov5의  정밀도와 mAP가 yolov7보다 높아실시간성 목적에는 yolov5가 적합. 

![image](https://github.com/user-attachments/assets/759ce6f1-122f-4eb1-92d3-72ee00a5377b)

- 자세한 내용은 첨부된 A Comparative Study of YOLOv5 and YOLOv7.pdf 논문 참조


또한 최종적으로 나노 젯슨에 적용할 것이기에 임베디드 기기에 적합한 가장 작은 모델 사용.

![image](https://github.com/user-attachments/assets/03e57880-ee0a-43af-bfc9-3500363157ba)


## 작동 기전

![image](https://github.com/user-attachments/assets/a8733347-a911-41d7-867f-f17827ea4ea4)
![image](https://github.com/user-attachments/assets/c8a2244c-5f53-47a6-82c8-88b76bb350bb)
![image](https://github.com/user-attachments/assets/3514b99d-03e7-48c8-a3d6-c0d598fa2fac)
![image](https://github.com/user-attachments/assets/0afa3312-cfba-4a0f-b2bb-41cf0e999b04)
![image](https://github.com/user-attachments/assets/455c3300-9355-4929-9d7e-09ee6c594ef5)


## 시연 영상
![image](https://github.com/user-attachments/assets/82ec6eaf-ad8a-4a9e-8de4-ddb73d6d0d2e)

### 1. 로컬(컴퓨터)
