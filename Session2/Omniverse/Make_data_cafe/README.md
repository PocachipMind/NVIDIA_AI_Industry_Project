# NVIDIA Omniverse
실행 환경은 제 윈도우 로컬 환경입니다.

usd 경로를 수정해 준다면 DLI 내부에서도 실행 가능합니다.

DLI 주소 : https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-OV-03+V1

### 학습 데이터 제작

카페 내부의 환경에서 학습 데이터를 제작하는 코드입니다.

1. 해당 usd 파일들을 바탕화면에 저장한 이후 ( Window 기준 ) 

2. Test의 코드를 Nvidia Omniverse에 올리고 실행하여 데이터를 제작합니다.

-> 해당 데이터에대한 바운딩박스 등 학습 데이터가 같이 추출됩니다. 


### 학습

해당 데이터를 활용하여 Faster R-CNN모델을 통해 학습을 진행합니다.

자세한 학습 코드는 Make_data_fruit폴더에 있습니다.

[ https://github.com/PocachipMind/NVIDIA_AI_Industry_Project/tree/main/Session2/Omniverse/Make_data_fruit ]

![rgb_0002](https://github.com/user-attachments/assets/6e962d4f-62ca-479a-9057-d452e50e5ff0)
