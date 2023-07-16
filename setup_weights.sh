#! /bin/bash

mkdir -p pytorch-rotation-decoupled-detector/backbone_weights
mkdir -p pytorch-rotation-decoupled-detector/save/weight

gdown.pl/gdown.pl https://drive.google.com/file/d/1X-2k1KqG8sJpc7I_yY9hBP9LQzpVVMT2/view?usp=drive_link pytorch-rotation-decoupled-detector/backbone_weights/resnet101-5d3b4d8f.pth
gdown.pl/gdown.pl https://drive.google.com/file/d/1iT8R5wQdr4OxnkGykUKogGHEhElFnEp3/view?usp=drive_link pytorch-rotation-decoupled-detector/save/weight/250000.pth