# CrossWalk Detection For ImVisible People

시각 장애인을 위한 횡단보도 감지 프로그램.

#### 시연 영상 [ 소리 존재. 음소거 해제 요망 ]
https://github.com/user-attachments/assets/5aa59ae5-6378-41ce-a4fd-6294c21793b9

- 횡단 보도를 발견하면 :

  Crosswalk Detected 라고 소리가 나서 시각 장애인에게 횡단보도가 있음을 인식시킵니다.

- 횡단 보도가 현재 빨간불이거나 자동차가 있어서 건널 수 없다면 :

  You can not cross. Please wait a moment. 소리를 통해 시각 장애인이 기다리도록 이야기합니다.

- 횡단 보도가 초록불이며 건널 수 있다면 :

  You can cross over. Please cross with care. 소리를 통해 시각 장애인에게 현재 건널 수 있음을 알려줍니다.

## 개요
시각 장애인들이 횡단보도를 건널 때 도움이 되는 프로그램을 제작.

![image](https://github.com/user-attachments/assets/6ea7403f-2d09-4367-ad90-65da1d45d94a)

![image](https://github.com/user-attachments/assets/57c39be4-4e74-46d2-ae23-3a1c84bd77cb)

이번 OpenCV 프로젝트는 NVIDIA AI Inderstry 에 걸맞게 NVIDIA NANO JETSON을 활용한 프로젝트를 진행하고 싶었습니다.

나노 젯슨의 특징인 "소형", "GPU 존재"에 아이디어를 얻어 해당 프로젝트를 생각하게 되었습니다.

최종적으로 학습한 모델을 TensorRT를 통해 nano jetson 기기에 최적화 시키고 성능을 비교보았습니다.

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


위 사이트들을 통해 얻은 이미지의 경우 라벨링이 내가 원하는 방식으로 되어있지 않아 직접 일일이 라벨링하였습니다.

학습에 쓰인 데이터 40%정도가 직접 촬영한 데이터입니다.

![image](https://github.com/user-attachments/assets/a74999f8-81df-4036-9020-2526265a6e37)



## 학습 모델

최종적으로 Nano Jetson에 적용할 것이므로 Fast RCNN 보다 6배 빠른 YOLO를 채택했습니다.

Yolov5, Yolov7 두 모델 모두 TensorRT 가능했지만, Yolov5의 정밀도와 mAP가 yolov7보다 높아 실시간성 목적에는 yolov5가 적합하다고 판단하여 Yolov5를 사용하였습니다. 

![image](https://github.com/user-attachments/assets/759ce6f1-122f-4eb1-92d3-72ee00a5377b)

- 자세한 내용은 첨부된 A Comparative Study of YOLOv5 and YOLOv7.pdf 논문 참조


또한 최종적으로 나노 젯슨에 적용할 것이기에 임베디드 기기에 적합한 가장 작은 Yolov5 nano 모델을 사용하였습니다.

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

맨 윗부분 시연 영상과 동일합니다.

https://github.com/user-attachments/assets/8b75aa29-b906-4569-9293-0dc36d12f719

![image](https://github.com/user-attachments/assets/287ad09e-c159-4d2b-8975-13141b02f7fa)


#### 한계점
저는 프로그램을 실제로 시연해 보고 싶었습니다. 그러나 로컬에 구현된 프로그램의 경우 노트북을 들고 횡단보도를 가기 불가했습니다.

![image](https://github.com/user-attachments/assets/f535519f-cd1e-4c95-b316-3960b70c1d59)


### 2. 웹(인터넷)

이에, 서버를 개설해서 핸드폰으로 직접 젯슨 나노 처럼 실험 시도했습니다.

[ Gradio 프레임 워크 사용 ]

![2 웹-14Page](https://github.com/user-attachments/assets/7ae30423-b79f-4872-8df2-38857d05fbc2)

#### 한계점

서버간의 접속, 전송 시간 등 오버헤드로 인해 실시간성 매우 저하, 소리 재생 불가 한계점이 존재했습니다.

### 3. 나노 젯슨

동영상의 경우 ( 30초부터 프로그램 실행 ) :


https://github.com/user-attachments/assets/7e5211ec-014f-46e1-9fae-1f11952cdadc


카메라의 경우 :

https://github.com/user-attachments/assets/b1fcc4cb-8772-4316-bcaf-448ee6f6695f


![image](https://github.com/user-attachments/assets/86b1f062-6f20-4932-ad36-4a0c734af7bf)

#### 한계점

모두 잘 동작하는것을 확인 할 수 있었지만, 머리에 부착할 수 있는 소형 카메라와 나노젯슨과 연결할 이어폰을 구하지못하여 실제 상황처럼 길거리에서 시연해보지는 못했습니다.

## 모델 성능 비교

모델을 각각 pt, onnx, tensorRT변환 이렇게 3종류로 변환하고 성능을 비교해봅니다.

![image](https://github.com/user-attachments/assets/f2077fc1-c961-47aa-9871-8b4c6126ee2e)

다음과 같은 코드로 추론시간만 측정하도록 노력했습니다

<img src="https://github.com/user-attachments/assets/aea14aba-a42c-482c-bc7e-efa9be838c6c" width="80%" height="80%"/>

### 성능 비교
![image](https://github.com/user-attachments/assets/cb5e948c-a7f1-43b4-b116-cb79cb3796e9)

보라색 화면의 경우 nano jetson, 하얀 배경의 경우 제 로컬 PC입니다.

pt파일의 경우 나노 젯슨에서 실행해보지 못했습니다.

이에, 제 로컬에서 비교한 내용을 기재합니다.

기본 모델 < 오닉스 < TensorRT 순으로 성능이 좋다고 이론적으로 알고 있었는데,

실제 성능 시간 비교를 보았을 때, 결과가 이론대로 나왔다고 판단합니다.

#### 기본 모델 : 학습과 디버깅에 유리하지만 속도가 느림 ( 최적화 X )
#### 오닉스 모델 : 다양한 플랫폼에서 호환 가능하며, 기본 모델보다 속도 향상 가능 ( 일정 수준 최적화 )
#### TensorRT 모델 : 배포 및 실시간 추론에 최적, GPU에서 성능 극대화 ( 최적화 극대화 )

## 구현 이슈

![image](https://github.com/user-attachments/assets/aca1720a-ca45-42da-89c5-6285a5aec5aa)
![image](https://github.com/user-attachments/assets/afb73d82-d7af-405a-a0a0-b716fd2c0a87)


