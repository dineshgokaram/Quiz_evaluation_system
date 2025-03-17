import asyncio
import websockets
import json


async def test_websocket():
    uri = "ws://localhost:8000/ws/quiz"
    async with websockets.connect(uri) as websocket:
        quiz_data = {
            "correct": 3,
            "total": 5,
            "incorrect_questions": ["Math", "Science"]
        }
        await websocket.send(json.dumps(quiz_data))
        response = await websocket.recv()
        print("Response from server:", response)


if __name__ == "__main__":
    asyncio.run(test_websocket())