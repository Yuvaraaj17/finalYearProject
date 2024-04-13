from ultralytics import YOLO
import cv2

model = YOLO('best.pt')
results = model.predict(source=0,stream=True)

for r in results:
    classTensor = r.boxes.cls
    if len(classTensor) != 0:
        print(classTensor[0])

