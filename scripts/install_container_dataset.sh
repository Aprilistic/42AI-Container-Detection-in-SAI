#! /bin/bash

gdown.pl/gdown.pl https://drive.google.com/file/d/1HtSqZqUSt5tbPtS6dLMfYBhijv8cJ_P_/view?usp=sharing container.zip

unzip container.zip

mv container/images pytorch-rotation-decoupled-detector/

mv container/labelTxt pytorch-rotation-decoupled-detector/

rm -rf container
cd pytorch-rotation-decoupled-detector/images

mv val/* test/