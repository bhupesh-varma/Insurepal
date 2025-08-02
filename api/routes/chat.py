from fastapi import APIRouter, Form, HTTPException
from core.vectorstore import get_vectorstore
from core.qa_chain import build_qa_chain
from core.db import get_history
from api.schemas import AskResponse

router = APIRouter()

@router.post("/ask", response_model=AskResponse)
async def ask_query(
    query: str = Form(...),
    session_id: str = Form("default_session")
):
    try:
        vectorstore = get_vectorstore()
        qa_chain = build_qa_chain(vectorstore)
        answer = qa_chain.run(query)

        history = get_history(session_id)
        history.add_user_message(query)
        history.add_ai_message(answer)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query processing error: {e}")

    return AskResponse(result=answer)
