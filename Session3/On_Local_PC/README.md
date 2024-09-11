# CrossWalk Detection For ImVisible People On Local PC

## 실행 환경

저는 ananconda 환경을 활용했습니다.

첨부된 nvidia_openCV_pj_env.yaml을 참고하세요.

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


