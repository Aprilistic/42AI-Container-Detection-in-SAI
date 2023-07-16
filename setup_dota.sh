#! /bin/bash

apt-get update
apt-get install python3-pip
apt-get install unzip
apt-get install vim

git clone https://github.com/circulosmeos/gdown.pl.git

./install_dota_dataset.sh

./setup_weights.sh

pip install -r pytorch-rotation-decoupled-detector/requirement.txt

python3.8 pytorch-rotation-decoupled-detector/utils/box/ext/rbbox_overlap_gpu/setup.py build_ext --inplace