import websockets
import asyncio

async def listen():
    url = "ws://127.0.0.1:7890"
    async with websockets.connect(url) as ws:
        await ws.send("Hello friend, I'm Geha window!")
        message = input("send a message 2 server: ")
            await websocket.send(message)
            print(f"Sent message to server: {message}")

            msg = await websocket.recv()
            print(f"Received message from server: {msg}")

asyncio.get_event_loop().run_until_complete(listen())
