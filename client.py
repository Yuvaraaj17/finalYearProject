import asyncio
import websockets
from ultralytics import YOLO

async def sending():
    async with websockets.connect("ws://localhost:8765") as websocket:
        model = YOLO('yolov8n.pt')
        result = model.predict(0,stream=True) #stream=True for Result generation
        for r in result:
            classnameTensor = r.boxes.cls #tensor type
            classNumber = int(classnameTensor.item())
            className = r.names[classNumber]
            print("Result is:",className)
            await websocket.send(className)
            await websocket.recv()
async def main():
    await sending()
asyncio.run(main())
