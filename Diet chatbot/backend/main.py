from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai
import os
from pydantic import BaseModel

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model - correct way for Gemini 2.0 Flash
model = genai.GenerativeModel("gemini-2.0-flash-exp")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Optional: Define request model for better validation
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    try:
        user_message = chat_request.message
        
        if not user_message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        prompt = (
            "You are a friendly and supportive diet coach named DietWhisper. "
            "Help the user with healthy food suggestions based on their input. "
            "Always be kind, helpful, and never judgmental.\n\n"
            f"User: {user_message}"
        )

        # Correct way to generate content with Gemini
        response = model.generate_content(prompt)
        
        # Check if response was generated successfully
        if not response or not response.text:
            raise HTTPException(status_code=500, detail="Failed to generate response")

        return {"reply": response.text}
    
    except Exception as e:
        # Handle API errors gracefully
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Alternative endpoint that accepts JSON directly (your original approach)
@app.post("/chat-json")
async def chat_json(request: Request):
    try:
        data = await request.json()
        user_message = data.get("message", "")
        
        if not user_message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")

        prompt = (
            "You are a friendly and supportive diet coach named DietWhisper. "
            "Help the user with healthy food suggestions based on their input. "
            "Always be kind, helpful, and never judgmental.\n\n"
            f"User: {user_message}"
        )

        # Correct way to generate content with Gemini
        response = model.generate_content(prompt)
        
        if not response or not response.text:
            raise HTTPException(status_code=500, detail="Failed to generate response")

        return {"reply": response.text}
    
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)