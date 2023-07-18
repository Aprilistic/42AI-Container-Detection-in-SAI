#! /bin/bash

sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install zip
sudo apt-get install unzip
sudo apt-get install vim
sudo apt-get install libgl1-mesa-glx

git clone https://github.com/circulosmeos/gdown.pl.git

./install_container_dataset.sh

./setup_weights.sh

pip install -r pytorch-rotation-decoupled-detector/requirement.txt

cd pytorch-rotation-decoupled-detector/utils/box/ext/rbbox_overlap_gpu
python setup.py build_ext --inplace