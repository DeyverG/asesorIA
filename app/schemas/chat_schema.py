from pydantic import BaseModel

class ChatRequest(BaseModel):
    id_chat: str
    user_message: str