import asyncio
import websockets
from ultralytics import YOLO
import cv2
import json

model = YOLO('best.pt')
video = cv2.VideoCapture(0)
async def sending():
    async with websockets.connect("ws://localhost:8765") as websocket:
        
        while True:
             ret, frame = video.read()
             result = model.predict(frame) #stream=True for Result generation

             for r in result:
                classnameTensor = r.boxes.cls #tensor type
                if len(classnameTensor) != 0:
                    i = classnameTensor[0]
                    classNumber = int(i.item())
                    className = r.names[classNumber]
                    xyxy = r.boxes.xyxy[0]
                    cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]),int(xyxy[3])),(0,0,255),2)
                    cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[0])+(12*len(className)),int(xyxy[1])+20),(0,0,255),-1)
                    cv2.putText(frame, className, (int(xyxy[0]+5), int(xyxy[1])+15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
                    
                    
                    data_to_send = {"name":"Model","message":{"result": className}}
                    await websocket.send(json.dumps(data_to_send))
                    await websocket.recv()
                cv2.imshow("Feed",frame)
             if cv2.waitKey(5) & 0xFF == 27:
                break
            
        
        video.release()
        cv2.destroyAllWindows()
async def main():
    
    await sending()
asyncio.run(main())

# print("hello")

