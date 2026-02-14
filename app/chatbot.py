import os
from openai import OpenAI
from dotenv import load_dotenv
from .memory import ConversationMemory

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
memory = ConversationMemory()

class LLMChatbot:
    def chat(self, user_message: str):
        memory.add_message("user", user_message)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=memory.get_history()
        )

        assistant_reply = response.choices[0].message.content
        memory.add_message("assistant", assistant_reply)

        return assistant_reply
