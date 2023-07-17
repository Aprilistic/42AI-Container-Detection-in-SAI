#! /bin/bash

gdown.pl/gdown.pl https://drive.google.com/file/d/1HtSqZqUSt5tbPtS6dLMfYBhijv8cJ_P_/view?usp=sharing container.zip

unzip container.zip

mv Archive/images pytorch-rotation-decoupled-detector/

mv Archive/labelTxt pytorch-rotation-decoupled-detector/

rm container.zip
rm -rf Archive
cd pytorch-rotation-decoupled-detector/images
mv val/* test/

cd ~
mv 42AI/pytorch-rotation-decoupled-detector ./
rm -rf 42AI