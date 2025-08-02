from fastapi import APIRouter, HTTPException, Query
from core.db import get_history
from api.schemas import ChatHistoryResponse

router = APIRouter()

@router.get("/", response_model=ChatHistoryResponse)
async def get_chat_history(session_id: str = Query(...)):
    try:
        history = get_history(session_id)
        messages = [{"role": msg.type, "content": msg.content} for msg in history.messages]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"History retrieval error: {e}")

    return ChatHistoryResponse(history=messages)
