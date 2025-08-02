from pydantic import BaseModel, Field
from typing import List, Optional


class Message(BaseModel):
    role: str  # "user", "ai", or "system"
    content: str


class ChatHistoryResponse(BaseModel):
    history: List[Message] = Field(default_factory=list)


class HackRxRunResponse(BaseModel):
    result: str


class AskResponse(BaseModel):
    result: str


class UploadResponse(BaseModel):
    status: str


class HackRxRunRequest(BaseModel):
    query: str = Field(..., description="User question/query")
    session_id: Optional[str] = Field("default_session", description="Session id for chat history")
    # Note: file upload is handled separately as UploadFile, so no File field here.
