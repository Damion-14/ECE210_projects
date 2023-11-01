import asyncio
import websockets

async def subscriber():
    uri = "ws://6.tcp.ngrok.io:11193"  # Replace with your WebSocket server URL

    async with websockets.connect(uri) as websocket:
        while True:
            response = await websocket.recv()
            print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(subscriber())
