from ultralytics import YOLO

if __name__ == '__main__':

    model = YOLO('yolov8n.yaml')
    result = model.train(data='config.yaml',amp=False,epochs=60,workers=2,batch=16)