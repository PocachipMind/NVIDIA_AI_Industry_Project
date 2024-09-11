# CrossWalk Detection For ImVisible People

시각 장애인을 위한 횡단보도 감지 프로그램.

#### 시연 영상 [ 소리 존재 ]
https://github.com/user-attachments/assets/5aa59ae5-6378-41ce-a4fd-6294c21793b9



# 실행 환경

## - On_Jetson_Nano 폴더 :
### Hardware
Jetson Nano
### SoftWare
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
