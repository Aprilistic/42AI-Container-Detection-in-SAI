#!/bin/bash

# Path to your original dataset directory
ORIGINAL_IMAGES_PATH="/root/container_dataset_grained/images_n"
ORIGINAL_LABELS_PATH="/root/container_dataset_grained/labels_n"

# Path to the directories where the split datasets will be saved
TRAIN_IMAGES_PATH="/root/container_dataset_grained/images/train"
TRAIN_LABELS_PATH="/root/container_dataset_grained/labels/train"
VAL_IMAGES_PATH="/root/container_dataset_grained/images/val"
VAL_LABELS_PATH="/root/container_dataset_grained/labels/val"

# Create directories if they don't exist
mkdir -p $TRAIN_IMAGES_PATH
mkdir -p $TRAIN_LABELS_PATH
mkdir -p $VAL_IMAGES_PATH
mkdir -p $VAL_LABELS_PATH

# The ratio of images to be used for validation
VALIDATION_SPLIT=0.1

# Get array of images
IMAGES=($ORIGINAL_IMAGES_PATH/*)

# Calculate number of validation samples
NUM_VAL_IMAGES=$(printf "%.0f" "$(echo "${#IMAGES[@]} * $VALIDATION_SPLIT" | bc)")

# Shuffle images
shuffled_images=($(shuf -e "${IMAGES[@]}"))

# Split images
for i in "${!shuffled_images[@]}"
do
    img_file=${shuffled_images[i]}
    label_file=$(basename "$img_file")
    if [ $i -lt $NUM_VAL_IMAGES ]
    then
        # Copy images for validation
        cp "$img_file" $VAL_IMAGES_PATH

        # Copy corresponding labels for validation
        cp "$ORIGINAL_LABELS_PATH/${label_file%.*}.txt" $VAL_LABELS_PATH
    else
        # Copy images for training
        cp "$img_file" $TRAIN_IMAGES_PATH

        # Copy corresponding labels for training
        cp "$ORIGINAL_LABELS_PATH/${label_file%.*}.txt" $TRAIN_LABELS_PATH
    fi
done