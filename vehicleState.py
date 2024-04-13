import websockets
import time
import asyncio
import json

class Vehicle:
    def __init__(self) -> None:
        self.speed = 50
        self.left = False
        self.right = False
        self.straight = True

async def main():
    vehicle = Vehicle()
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            state = {
                "speed": vehicle.speed,
                "left" : vehicle.left,
                "right": vehicle.right,
                "straight": vehicle.straight
            }
            objToSend = {
                "name": "Vehicle",
                "message": state
            }
            stateObj = json.dumps(objToSend)
            await websocket.send(stateObj)
            await websocket.recv()

            time.sleep(5)
asyncio.run(main())