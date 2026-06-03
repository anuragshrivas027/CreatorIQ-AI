from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from models.chat_model import (
    ChatRequest
)

from rag.rag_pipeline import (
    ask_rag,
    stream_rag
)

router = APIRouter()


@router.post("/ask")
async def ask_question(
    request: ChatRequest
):

    try:

        return ask_rag(
            request.question
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/stream")
async def stream_question(
    request: ChatRequest
):

    try:

        return StreamingResponse(
            stream_rag(
                request.question
            ),
            media_type="text/plain"
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )