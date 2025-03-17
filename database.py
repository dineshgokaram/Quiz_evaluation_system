# database.py

from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://mongo_db:27017/")
db = client.quiz_database
collection = db.quiz_results

def fetch_cached_result(quiz_data):
    return collection.find_one({
        "correct": quiz_data.get("correct"),
        "total": quiz_data.get("total"),
        "incorrect_questions": quiz_data.get("incorrect_questions")
    })

def store_quiz_result(result):
    collection.insert_one(result)


client = MongoClient("mongodb://localhost:27017/")
db = client['quiz_db']
collection = db['quiz_results']

def save_to_db(data):
    collection.insert_one(data)
    print("Data saved to MongoDB ✅")

