import asyncio
import websockets
from ultralytics import YOLO

async def sending():
    async with websockets.connect("ws://localhost:8765") as websocket:
        model = YOLO('yolov8n.pt')
        result = model.predict(0,stream=True) #stream=True for Result generation
        for r in result:
            classnameTensor = r.boxes.cls #tensor type
            res =''
            for i in classnameTensor:
                classNumber = int(i.item())
                className = r.names[classNumber]
                res=res + f' {className}'
            await websocket.send(res)
            await websocket.recv()
async def main():
    await sending()
asyncio.run(main())
