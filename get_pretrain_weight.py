import sys

sys.path.append('.')

import os
import tqdm
import torch

from torch import optim
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from data.aug.compose import Compose
from data.aug import ops
from data.dataset import DOTA

from model.rdd import RDD
from model.backbone import resnet
from model.backbone.resnet import resnet101

from utils.adjust_lr import adjust_lr_multi_step
from utils.parallel import convert_model, CustomDetDataParallel

# dataset = DOTA(dir_dataset, ['train', 'val'], aug)
#     loader = DataLoader(dataset, batch_size, shuffle=True, num_workers=num_workers, pin_memory=True, drop_last=True,
#                         collate_fn=dataset.collate)
dataset_name = ['baseball-diamond', 'basketball-court', 'bridge', 'ground-track-field', 'harbor', 'helicopter',
                     'large-vehicle', 'plane', 'roundabout', 'ship', 'small-vehicle', 'soccer-ball-field',
                     'storage-tank', 'swimming-pool', 'tennis-court']


# reference is train.py

num_classes = len(dataset_name) # len(dataset.names)

prior_box = {
    'strides': [8, 16, 32, 64, 128],
    'sizes': [3] * 5,
    'aspects': [[1, 2, 4, 8]] * 5,
    'scales': [[2 ** 0, 2 ** (1 / 3), 2 ** (2 / 3)]] * 5,
}

cfg = {
    'prior_box': prior_box,
    'num_classes': num_classes,
    'extra': 2,
}

torch.manual_seed(0)
torch.backends.cudnn.benchmark = True

device_ids = [0, 1]
torch.cuda.set_device(device_ids[0])
backbone = resnet.resnet101
image_size = 768
lr = 1e-3
batch_size = 12
num_workers = 4

# Specify the path to the .pth file
root = '/root'
path = root + "pytorch-rotation-decoupled-detector/save/weights/120000.pth"

# define model
model = RDD(backbone(fetch_feature=True), cfg)
model.build_pipe(shape=[2, 3, image_size, image_size])
model.init()
# if len(device_ids) > 1:
#     model = convert_model(model)
#     model = CustomDetDataParallel(model, device_ids)
model.cuda()
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=0.9, weight_decay=5e-4)
print(model.num_levels)
# Use the loaded weights for your model
model.restore(path)

# Access the model's state dictionary
state_dict = model.state_dict()

# Create a dictionary to store the weights
weights_dict = {}

# Iterate through the model's named parameters
for name, param in model.named_parameters():
  if 'backbone' in name:
    weights_dict[name] = param.data

torch.save(weights_dict, 'pretrain_weights.pth')