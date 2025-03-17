import unittest
from main import process_quiz, generate_feedback


class TestQuizProcessing(unittest.TestCase):

    def test_process_quiz(self):
        quiz_data = {"correct": 3, "total": 5, "incorrect_questions": ["Math", "Science"]}
        result = process_quiz(quiz_data)
        self.assertEqual(result["score"], 60.0)
        self.assertEqual(result["feedback"], "Good job! Revise these topics: Math, Science.")

    def test_generate_feedback(self):
        self.assertEqual(generate_feedback(90, []), "Excellent performance! Keep it up!")
        self.assertEqual(generate_feedback(75, ["Math"]), "Good job! Revise these topics: Math.")
        self.assertEqual(generate_feedback(50, ["Science", "History"]), "Needs improvement. Focus on these concepts: Science, History.")


if __name__ == "__main__":
    unittest.main()