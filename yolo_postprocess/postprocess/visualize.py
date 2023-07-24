from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('/root/runs/segment/train10-m-731-new/weights/best.pt')

# Define path to the image file
source = '/root/vali/valid2/OBJ05724_PS3_K3A_NIA0363.png'

# Run inference on the source
results = model.predict(source, imgsz=1024, conf=0.1, iou=0.5, max_det=-1, save=True)  # list of Results objects
