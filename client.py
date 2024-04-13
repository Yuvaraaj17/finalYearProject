import asyncio
import websockets
from ultralytics import YOLO

async def sending():
    async with websockets.connect("ws://localhost:8765") as websocket:
        model = YOLO('best.pt')
        result = model.predict(0,stream=True) #stream=True for Result generation
        for r in result:
            classnameTensor = r.boxes.cls #tensor type
            res =''
            if len(classnameTensor) != 0:
                    i = classnameTensor[0]
                    classNumber = int(i.item())
                    className = r.names[classNumber]
                    res=res + f' {className}'
                    await websocket.send(res)
                    await websocket.recv()
async def main():
    await sending()
asyncio.run(main())

# print("hello")

