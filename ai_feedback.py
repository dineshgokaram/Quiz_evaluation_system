# ai_feedback.py

def generate_feedback(score, incorrect_questions):
    if score >= 90:
        return "Excellent performance! Keep it up!"
    elif score >= 60:
        return f"Good job! Revise these topics: {', '.join(incorrect_questions)}."
    else:
        return f"Needs improvement. Focus on these concepts: {', '.join(incorrect_questions)}."


def generate_ai_suggestions(incorrect_questions):
    suggestions = {
        "Math": "Practice solving equations and work on algebra basics.",
        "Science": "Focus on understanding physics concepts and experiment analysis.",
        "History": "Review historical events and timelines.",
        "English": "Enhance vocabulary and improve grammar skills."
    }

    return [suggestions.get(topic, "Review the related concepts.") for topic in incorrect_questions]


def analyze_performance(correct, total):
    accuracy = (correct / total) * 100

    if accuracy >= 80:
        feedback = "Excellent performance! 🎯"
    elif accuracy >= 50:
        feedback = "Good job! But you can do better. 💪"
    else:
        feedback = "You need more practice. 📚"

    return {
        "accuracy": accuracy,
        "feedback": feedback
    }
