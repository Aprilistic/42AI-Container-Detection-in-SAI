#! /bin/bash

gdown.pl/gdown.pl https://drive.google.com/file/d/13GKjyxrbc7c26ml4LULW32p9En3uuNfp/view?usp=drive_link container.zip

unzip container.zip

mv rdd_1x/images pytorch-rotation-decoupled-detector/

mv rdd_1x/labelTxt pytorch-rotation-decoupled-detector/

# rm container.zip
# rm -rf rdd_1x
cd pytorch-rotation-decoupled-detector/images