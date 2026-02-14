from fastapi import FastAPI
from pydantic import BaseModel
from .chatbot import LLMChatbot

app = FastAPI(title="LLM Chatbot System")

chatbot = LLMChatbot()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    reply = chatbot.chat(request.message)
    return {"response": reply}
