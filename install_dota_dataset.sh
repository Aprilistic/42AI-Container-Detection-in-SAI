#! /bin/bash

mkdir -p pytorch-rotation-decoupled-detector/images/train
mkdir -p pytorch-rotation-decoupled-detector/images/val
mkdir -p pytorch-rotation-decoupled-detector/images/test

mkdir -p pytorch-rotation-decoupled-detector/labelTxt/train
mkdir -p pytorch-rotation-decoupled-detector/labelTxt/val

gdown.pl/gdown.pl https://drive.google.com/file/d/1BlaGYNNEKGmT6OjZjsJ8HoUYrTTmFcO2/view?usp=drive_link pytorch-rotation-decoupled-detector/images/train/part1.zip
gdown.pl/gdown.pl https://drive.google.com/file/d/1JBWCHdyZOd9ULX0ng5C9haAt3FMPXa3v/view?usp=drive_link pytorch-rotation-decoupled-detector/images/train/part2.zip
gdown.pl/gdown.pl https://drive.google.com/file/d/1pEmwJtugIWhiwgBqOtplNUtTG2T454zn/view?usp=drive_link pytorch-rotation-decoupled-detector/images/train/part3.zip
gdown.pl/gdown.pl https://drive.google.com/file/d/1I-faCP-DOxf6mxcjUTc8mYVPqUgSQxx6/view?usp=drive_link pytorch-rotation-decoupled-detector/labelTxt/train/labelv1_0.zip

gdown.pl/gdown.pl https://drive.google.com/file/d/1uCCCFhFQOJLfjBpcL5MC0DHJ9lgOaXWP/view?usp=drive_link pytorch-rotation-decoupled-detector/images/val/part1.zip
gdown.pl/gdown.pl https://drive.google.com/file/d/1uFwxA4B7H8zcI1oD11bj0U8z88qroMlG/view?usp=drive_link pytorch-rotation-decoupled-detector/labelTxt/val/labelv1_0.zip

mkdir pytorch-rotation-decoupled-detector/images/train/images1
mkdir pytorch-rotation-decoupled-detector/images/train/images2
mkdir pytorch-rotation-decoupled-detector/images/train/images3

unzip pytorch-rotation-decoupled-detector/images/train/part1.zip -d pytorch-rotation-decoupled-detector/images/train/images1
unzip pytorch-rotation-decoupled-detector/images/train/part2.zip -d pytorch-rotation-decoupled-detector/images/train/images2
unzip pytorch-rotation-decoupled-detector/images/train/part3.zip -d pytorch-rotation-decoupled-detector/images/train/images3

mv pytorch-rotation-decoupled-detector/images/train/images1/images/* pytorch-rotation-decoupled-detector/images/train/ 
mv pytorch-rotation-decoupled-detector/images/train/images2/images/* pytorch-rotation-decoupled-detector/images/train/
mv pytorch-rotation-decoupled-detector/images/train/images3/images/* pytorch-rotation-decoupled-detector/images/train/

unzip pytorch-rotation-decoupled-detector/images/val/part1.zip -d pytorch-rotation-decoupled-detector/images/val/
mv pytorch-rotation-decoupled-detector/images/val/images/* pytorch-rotation-decoupled-detector/images/

unzip pytorch-rotation-decoupled-detector/labelTxt/train/labelv1_0.zip -d pytorch-rotation-decoupled-detector/labelTxt/train
unzip pytorch-rotation-decoupled-detector/labelTxt/val/labelv1_0.zip -d pytorch-rotation-decoupled-detector/labelTxt/val

rm -rf pytorch-rotation-decoupled-detector/images/train/images1 pytorch-rotation-decoupled-detector/images/train/images2 pytorch-rotation-decoupled-detector/images/train/images3
rm -rf pytorch-rotation-decoupled-detector/images/val/images/
rm -rf pytorch-rotation-decoupled-detector/labelTxt/train/labelv1_0.zip pytorch-rotation-decoupled-detector/labelTxt/val/labelv1_0.zip