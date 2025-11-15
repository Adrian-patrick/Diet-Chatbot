Here is the **fully fixed, clean, properly formatted README.md**, all in **one single Markdown block**, ready to **copy–paste without breaking**:

---

```markdown
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

```

project/
│── main.py                   # FastAPI backend with Gemini integration
│── index.html                # Frontend chat interface
│── requirements.txt          # Python dependencies
│── .env                      # Environment variables (Gemini API key)
│── how_to_run.txt            # Instructions to run backend
│── main.cpython-310.pyc      # Bytecode file (not used directly)

```

---

## 🔧 Backend Overview (`main.py`)

The backend is built with:

- `fastapi`  
- `uvicorn`  
- `google-generativeai`  
- `python-dotenv`

Gemini is configured using a `.env` key:

```

GEMINI_API_KEY="use your gemini api key"

```

The backend uses:

```

GenerativeModel("gemini-2.0-flash-exp")

````

to generate nutrition advice.

---

## 🛠 API Endpoints

### **POST /chat**
Request:
```json
{ "message": "Give me a healthy breakfast idea" }
````

Response:

```json
{ "reply": "AI-generated nutrition advice..." }
```

---

### **POST /chat-json**

Same as `/chat`, but reads raw JSON manually.

---

### **GET /health**

Response:

```json
{ "status": "healthy" }
```

---

## 🌐 Frontend Overview (`index.html`)

The frontend offers:

* Modern glassmorphic UI
* Animated gradients
* Chat bubble messaging
* Quick suggestion chips
* Auto-expanding input textarea
* Smooth animations
* Rich AI message formatting (lists, bold text, paragraphs)

It communicates with the backend via:

```
POST http://localhost:8000/chat
```

---

## 🔑 Environment Variables (`.env`)

Make sure you have:

```env
GEMINI_API_KEY="use your gemini api key"
```

---

## 📦 Installation & Setup

### **1. Install dependencies**

```bash
pip install -r requirements.txt
```

### **2. Start the FastAPI backend**

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### **3. Open the frontend**

Simply open:

```
index.html
```

in your browser.

---

## ▶️ How to Use

1. Start the FastAPI server
2. Open the `index.html` file
3. Type any nutrition-related question
4. Receive personalized diet recommendations instantly

---

## 🧠 How DietWhisper Works

1. User types a question in the web UI
2. A JavaScript `fetch()` call sends it to `/chat`
3. FastAPI constructs a prompt:

   > "You are a friendly and supportive diet coach named DietWhisper..."
4. Gemini 2.0 Flash processes the prompt
5. Response is returned and beautifully formatted in the UI

---

## 📚 Requirements (`requirements.txt`)

```
fastapi
uvicorn
python-dotenv
google-genai
```

---

## ❤️ Future Improvements

* 🔒 Add user login & preferences
* 📊 Include calorie & macronutrient breakdown
* ☁️ Cloud deployment (Render, Railway, AWS)
* 📱 Mobile app interface
* 💾 Save chat history per user

