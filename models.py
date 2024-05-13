from enum import Enum
from pydantic import BaseModel

class RoleEnum(str, Enum):
    user = "user"
    system = "system"
    assistant = "assistant"

class Message(BaseModel):
    role: RoleEnum 
    content: str

class NewMessageContext(BaseModel):
    conversation_id: int
    messages: list[Message]
    latest_message: Message