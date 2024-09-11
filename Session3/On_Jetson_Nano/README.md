# CrossWalk Detection For ImVisible People On Jetson Nano

## 실행 환경 : Hardware
Jetson Nano 2GB


![image](https://github.com/user-attachments/assets/3cc3aa59-6ec2-4d2c-bcf3-dc55cc9a4b83)

## 실행 환경 : Software
#### Install libraries
sudo apt-get update

sudo apt-get install -y liblapack-dev libblas-dev gfortran libfreetype6-dev libopenblas-base libopenmpi-dev libjpeg-dev zlib1g-dev

sudo apt-get install -y python3-pip

#### Update Pip
python3 -m pip install --upgrade pip

#### Install below necessary packages <Br> For numpy, first uninstall the version already installed, and then install numpy==1.19.0
numpy==1.19.0

pandas==0.22.0

Pillow==8.4.0

PyYAML==3.12

scipy==1.5.4

psutil

tqdm==4.64.1

imutils

#### Install Pycuda
export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}

export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH

python3 -m pip install pycuda --user

#### Install Seaborn
sudo apt install python3-seaborn

#### Install torch & torchvision
wget https://nvidia.box.com/shared/static/fjtbno0vpo676a25cgvuqc1wty0fkkg6.whl -O torch-1.10.0-cp36-cp36m-linux_aarch64.whl

pip3 install torch-1.10.0-cp36-cp36m-linux_aarch64.whl

git clone --branch v0.11.1 https://github.com/pytorch/vision torchvision

cd torchvision

sudo python3 setup.py install 

#### Not required but good library
jetson-stats==3.1.4

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
$ cd On_Jetson_Nano
```

마지막으로 ```JetsonNano_video(TensorRT).py```을 실행합니다. 
```
$ python3 JetsonNano_video(TensorRT).py
```

<br>

```JetsonNano_video(TensorRT).py``` 코드 내부에서 동영상 파일의 경로를 수정하거나 주석을 해제해서 카메라를 활용해보세요.


![image](https://github.com/user-attachments/assets/0b92a0a9-8286-43d5-8e67-4952a65e8bd2)

