from ultralytics import YOLO

# Load a model
model = YOLO('yolov8m-seg.yaml')

# Train the model
model.train(data='/root/aug/ctn.yaml', epochs=1000, patience=50, imgsz=1024, pretrained=False, batch=16, seed=42, device=[0, 1], optimizer='auto')