# CrossWalk Detection For ImVisible People On Local PC

## 실행 환경 : Anaconda Environment

저는 ananconda 환경을 활용했습니다.

### 1. 로컬 환경 (OS)에 맞는 Anaconda 실행 파일 다운

링크 : http://www.anaconda.com/

![image](https://github.com/user-attachments/assets/4490edac-3579-495c-a60d-b2e78329026e)

### 2. Anaconda 설치 후 Terminal 실행 ( Windows OS 기준 Powershell Prompt )

![image](https://github.com/user-attachments/assets/e50acb0e-1f3c-43d4-8700-df1366890a45)

### 3. Terminal 실행 후 Python 가상환경 활성화

- 첨부된 nvidia_openCV_pj_env.yaml을 활용
- 
- 하기와 같은 Command를 사용하여 가상환경 설치 진행
```
$ conda env create -f nvidia_openCV_pj_env.yaml
```
- 환경 설치가 완료되면 하기와 같은 Command를 사용하여 가상환경 활성화 진행
```
$ conda activate nvidia_openCV_pj_env
```
## 실행 환경 : Visual Studio (VS) Code

### 1. 로컬 환경 (OS)에 맞는VS Code 실행 파일 다운

링크 : http://code.visualstudio.com/

![image](https://github.com/user-attachments/assets/e6e241c4-765a-4b4b-a886-549211a247c7)

### 2. VS Code 설치 후 Python Extension 설치
좌측이 Extension 아이콘 클릭 후 Python Extension Pack 검색 및 설치
![image](https://github.com/user-attachments/assets/76ebe31a-4b97-4db2-bd17-2eabf1a1c383)

### 3. Windows OS 기준 Control + P 후 Python: Select Interpreter 검색

### 4. 실습에서 사용할 환경 선택

예시 이미지의 경우 이름이 조금 다름. 우리의 경우 nvidia_openCV_pj_env 로 나와야함.

![image](https://github.com/user-attachments/assets/be946505-b5ab-4eb4-ae7f-0309a441d6a1)

### 5. 우측 하단에 3.10.14('nvidia_openCV_pj_env': conda)로 표기 되어있는지 확인

## 실행 방법

이 프로젝트의 최상위 레파지토리를 클론합니다. 
```
$ git clone https://github.com/PocachipMind/NVIDIA_AI_Industry_Project.git
```
그 이후 해당 폴더로 이동합니다.
```
$ cd NVIDIA_AI_Industry_Project
```
```
$ cd Session3
```
```
$ cd On_Local_PC
```

해당 폴더 내의 ```local_video(pygame).py``` 또는 ```web_video(gradio).py``` 을 실행합니다. 

이름에서 알 수 있다 싶이, local은 바로실행, gradio는 웹을 통해 모델을 사용해봅니다.
```
$ python3 local_video(pygame).py
```
```
$ python3 web_video(gradio).py
```

<br>

```local_video(pygame).py``` 코드 내부에서 동영상 파일의 경로를 수정하거나 주석을 해제해서 카메라를 활용해보세요.


