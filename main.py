from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)
model = os.environ.get("OPENAI_MODEL")

class Message(BaseModel):
    text: str

@app.post("/chat/")
async def chat(message: Message):

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": message.text}
        ]
    )

    print(completion.choices[0].message)

    return {"response": completion.choices[0].message.content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)