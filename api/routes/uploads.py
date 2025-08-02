import os
import tempfile
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from core.document import load_and_chunk
from core.vectorstore import get_vectorstore
from core.qa_chain import build_qa_chain
from core.db import get_history
from api.schemas import UploadResponse, HackRxRunResponse

router = APIRouter()

@router.post("/document", response_model=UploadResponse)
async def upload_document(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp_path = tmp.name

        chunks = load_and_chunk(tmp_path)
        vectorstore = get_vectorstore()
        vectorstore.add_documents(chunks)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Document upload error: {e}")

    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return UploadResponse(status="Indexed")

@router.post("/run", response_model=HackRxRunResponse)
async def hackrx_run(
    query: str = Form(...),
    file: UploadFile = File(...),
    session_id: str = Form("default_session"),
):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp_path = tmp.name

        chunks = load_and_chunk(tmp_path)
        vectorstore = get_vectorstore()
        vectorstore.add_documents(chunks)

        qa_chain = build_qa_chain(vectorstore)
        answer = qa_chain.run(query)

        history = get_history(session_id)
        history.add_user_message(query)
        history.add_ai_message(answer)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {e}")

    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    return HackRxRunResponse(result=answer)
