# FastAPI WebSocket Quiz Evaluation

This project is a FastAPI-based WebSocket server for real-time quiz evaluation with AI feedback generation.

---

## 📁 Project Structure

```
assessment/
│
├── main.py          # FastAPI server with WebSocket endpoint
├── ai_feedback.py  # AI feedback generation logic
├── database.py     # Database interaction logic (optional)
├── test_client.py # WebSocket client for testing
├── requirements.txt # Project dependencies
└── README.md       # Project documentation
```

---

## 🛠️ Setup Instructions

### Step 1: Install Python Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment:

- On Windows:
```bash
.venv\Scripts\activate
```
- On macOS or Linux:
```bash
source .venv/bin/activate
```

---

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Run the FastAPI WebSocket Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🚀 How to Test the WebSocket Client

In a separate terminal, run the test client:

```bash
python test_client.py
```

Expected Output:
```
Response from server: Message received!
Data received: {"correct": 3, "total": 5, "incorrect_questions": ["Math", "Science"]}
```

---

## 🧐 How the Project Works

1️⃣ The **client sends quiz data** (number of correct and total questions) to the server via WebSocket.

2️⃣ The server uses **AI feedback logic (analyze_performance)** to evaluate the quiz and provide performance feedback.

3️⃣ The server sends the **feedback back to the client**.

4️⃣ (Optional) The data can be stored in the database (MongoDB integration is commented out).

---

## ✅ Technologies Used

- FastAPI
- WebSockets
- Python Asyncio

---

## 🎯 Future Enhancements

- MongoDB integration for storing quiz history.
- Deploy to cloud platforms like Heroku or AWS.

---

