#! /bin/bash

gdown.pl/gdown.pl https://drive.google.com/file/d/1oV27G0rGWymw8mkSuLyh_FTgEAQwNlde/view?usp=sharing container.zip

unzip container.zip

mv rdd_1x/images pytorch-rotation-decoupled-detector/

mv rdd_1x/labelTxt pytorch-rotation-decoupled-detector/

# rm container.zip
# rm -rf rdd_1x
cd pytorch-rotation-decoupled-detector/images