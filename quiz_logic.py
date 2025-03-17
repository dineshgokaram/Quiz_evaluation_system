import json
from ai_feedback import analyze_performance
from database import save_to_db

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


def generate_chart_data(correct, total):
    return {
        "labels": ["Correct", "Incorrect"],
        "values": [correct, total - correct]
    }





async def handle_quiz(websocket, path):
    data = await websocket.recv()
    quiz_data = json.loads(data)

    # AI feedback
    feedback = analyze_performance(quiz_data['correct'], quiz_data['total'])

    # Store in MongoDB
    save_to_db({
        "quiz_data": quiz_data,
        "feedback": feedback
    })

    await websocket.send(json.dumps(feedback))

