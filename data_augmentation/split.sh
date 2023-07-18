#!/bin/bash

# Source and target directories
src_image_dir="train_images"
src_label_dir="train_labels"
dest_dir_images="images"
dest_dir_labels="labelTxt"

# Create destination directories
mkdir -p "${dest_dir_images}"/{train,val,test}
mkdir -p "${dest_dir_labels}"/{train,val,test}

# Get list of files
image_files=(${src_image_dir}/*.png)
label_files=(${src_label_dir}/*.txt)

# Get the number of image and label files
num_image_files=${#image_files[@]}
num_label_files=${#label_files[@]}

# Verify that the number of image and label files are the same
if [ $num_image_files -ne $num_label_files ]; then
    echo "The number of image and label files do not match"
    exit 1
fi

# Shuffle files
shuffled_indices=( $(seq 0 $((num_image_files-1)) | awk 'BEGIN{srand();} {print rand() "\t" $0}' | sort -k1,1n | cut -f2-) )

# Split indices into train, val, test
num_train=$((8 * num_image_files / 10))
num_val=$((num_image_files / 10))
train_indices=(${shuffled_indices[@]:0:$num_train})
val_indices=(${shuffled_indices[@]:$num_train:$num_val})
test_indices=(${shuffled_indices[@]:$((num_train + num_val))})

# Function to move files
move_files() {
    dest_dir=$1
    shift
    indices=("$@")
    for i in "${indices[@]}"; do
        base_name=$(basename "${image_files[$i]}" .png)
        mv "${src_image_dir}/${base_name}.png" "${dest_dir_images}/${dest_dir}"
        mv "${src_label_dir}/${base_name}.txt" "${dest_dir_labels}/${dest_dir}"
    done
}

# Move files
move_files train "${train_indices[@]}"
move_files val "${val_indices[@]}"
move_files test "${test_indices[@]}"

