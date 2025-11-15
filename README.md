# 🥗 DietWhisper — AI Diet Coach  
A FastAPI + Gemini-powered nutrition assistant

DietWhisper is an AI-powered diet coach built with **FastAPI** and **Gemini 2.0 Flash**, featuring a modern and responsive HTML frontend.  
It provides personalized diet and nutrition recommendations through a clean chat interface.

---

## 🚀 Features

- 🤖 AI diet assistant using Google Gemini  
- ⚡ FastAPI backend with CORS support  
- 🌐 Beautiful, responsive chat UI (`index.html`)  
- 🔐 Secure environment variables via `.env`  
- 🩺 Health-check API endpoint  
- 🎨 Smooth animations, suggestion chips, and structured message formatting  

---

## 📁 Project Structure

project/
│── main.py # FastAPI backend with Gemini integration
│── index.html # Frontend chat interface
│── requirements.txt # Python dependencies
│── .env # Environment variables (Gemini API key)
│── how_to_run.txt # Instructions to run backend
│── main.cpython-310.pyc # Bytecode (not used directly)

yaml
Copy code

---

## 🔧 Backend Overview (`main.py`)

The backend is built with:

- `fastapi`
- `uvicorn`
- `google-generativeai`
- `python-dotenv`

Gemini is initialized via:

GEMINI_API_KEY="use your gemini api key"

pgsql
Copy code
:contentReference[oaicite:0]{index=0}

A `GenerativeModel("gemini-2.0-flash-exp")` is used for generating nutrition advice.

### **API Endpoints**

#### **POST /chat**
Accepts JSON:
```json
{ "message": "Give me a healthy breakfast idea" }
Returns:

json
Copy code
{ "reply": "AI-generated nutrition advice..." }
POST /chat-json
Same functionality but reads raw JSON body.

GET /health
Returns:

json
Copy code
{ "status": "healthy" }
🌐 Frontend Overview (index.html)
The frontend includes:

Modern glassmorphic UI

Animated gradients

Beautiful chat bubble system

Quick suggestion chips for users

Auto-resizing message input

Smooth message animations

AI message formatting (bold, lists, paragraphs)

It sends user messages to:

bash
Copy code
POST http://localhost:8000/chat
and renders AI responses dynamically.

🔑 Environment Variables (.env)
Your .env file should include:

env
Copy code
GEMINI_API_KEY="use your gemini api key"
📦 Installation & Setup
1. Install dependencies
nginx
Copy code
pip install -r requirements.txt

requirements


2. Start the FastAPI backend
nginx
Copy code
uvicorn main:app --reload --host 0.0.0.0 --port 8000
(From how_to_run.txt)

how_to_run


3. Open the frontend
Simply open index.html in any browser.

▶️ How to Use
Run the backend (uvicorn main:app --reload)

Open index.html

Type your nutrition question

Get personalized diet coaching instantly

🧠 How DietWhisper Works
User sends a message from the HTML chat UI

JavaScript sends it to the FastAPI /chat endpoint

Backend constructs a prompt:

"You are a friendly and supportive diet coach named DietWhisper..."

Gemini 2.0 Flash generates a helpful, supportive response

The response is styled and displayed beautifully in the chat UI

📚 Requirements (requirements.txt)
nginx
Copy code
fastapi
uvicorn
python-dotenv
google-genai
❤️ Future Improvements
🔒 Add user authentication

📊 Add calorie tracking & nutrition breakdown

☁️ Deploy backend (Render, Railway, or AWS)

📱 Build mobile app frontend

💾 Add session-based or persistent chat history
