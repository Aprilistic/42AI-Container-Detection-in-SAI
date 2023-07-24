from ultralytics import YOLO

model = YOLO('/root/runs/segment/train3/weights/best.pt')

# model.predict(source, visualize=True, imgsz=1024, conf=0.1, hide_labels=True, hide_conf=True, boxes=False)

model.predict('/root/vali/valid1', save_txt=True, save_conf=True, conf=0.1, nms=False, iou=0.5, max_det=-1, device=[0,1])
model.predict('/root/vali/valid2', save_txt=True, save_conf=True, conf=0.1, nms=False, iou=0.5, max_det=-1, device=[0,1])
model.predict('/root/vali/valid3', save_txt=True, save_conf=True, conf=0.1, nms=False, iou=0.5, max_det=-1, device=[0,1])

# results = model(source)