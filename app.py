from fastapi import FastAPI
import os
from openai import OpenAI
from dotenv import load_dotenv
from models import NewMessageContext

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)
model = os.environ.get("OPENAI_MODEL")

@app.post("/chat/")
async def chat(context: NewMessageContext):

    completion = client.chat.completions.create(
        model=model,
        messages=context.messages
    )

    return {"response": completion.choices[0].message.content}