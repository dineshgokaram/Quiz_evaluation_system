from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json
from pymongo import MongoClient
import asyncio
import websockets

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://mongo_db:27017/")
db = client.quiz_database
collection = db.quiz_results

# Store active connections
connections = []

from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws/quiz")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_text()
    print("Data received:", data)
    await websocket.send_text("Message received!")
    await websocket.close()



def fetch_cached_result(quiz_data):
    return collection.find_one({
        "correct": quiz_data.get("correct"),
        "total": quiz_data.get("total"),
        "incorrect_questions": quiz_data.get("incorrect_questions")
    })


def process_quiz(quiz_data):
    correct_answers = quiz_data.get("correct", 0)
    total_questions = quiz_data.get("total", 5)

    score_percentage = (correct_answers / total_questions) * 100
    feedback = generate_feedback(score_percentage, quiz_data.get("incorrect_questions", []))
    chart_data = generate_chart_data(correct_answers, total_questions)
    ai_suggestions = generate_ai_suggestions(quiz_data.get("incorrect_questions", []))

    return {
        "correct": correct_answers,
        "total": total_questions,
        "score": score_percentage,
        "feedback": feedback,
        "chart_data": chart_data,
        "ai_suggestions": ai_suggestions
    }


def generate_feedback(score, incorrect_questions):
    if score >= 90:
        return "Excellent performance! Keep it up!"
    elif score >= 60:
        return f"Good job! Revise these topics: {', '.join(incorrect_questions)}."
    else:
        return f"Needs improvement. Focus on these concepts: {', '.join(incorrect_questions)}."


def generate_chart_data(correct, total):
    return {
        "labels": ["Correct", "Incorrect"],
        "values": [correct, total - correct]
    }


def generate_ai_suggestions(incorrect_questions):
    suggestions = {
        "Math": "Practice solving equations and work on algebra basics.",
        "Science": "Focus on understanding physics concepts and experiment analysis.",
        "History": "Review historical events and timelines.",
        "English": "Enhance vocabulary and improve grammar skills."
    }

    return [suggestions.get(topic, "Review the related concepts.") for topic in incorrect_questions]


async def broadcast(message):
    for connection in connections:
        await connection.send_json(message)