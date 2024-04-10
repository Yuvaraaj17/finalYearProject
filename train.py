from ultralytics import YOLO

model = YOLO('yolov8n.yaml')

model.train(data='config.yaml',epochs=10)