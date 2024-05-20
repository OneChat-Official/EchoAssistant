from fastapi import FastAPI
from models import NewMessageContext

app = FastAPI()

@app.post("/chat/")
async def chat(context: NewMessageContext):
    return {"response": context.latest_message.content}