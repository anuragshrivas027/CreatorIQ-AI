from fastapi import APIRouter
from fastapi import HTTPException

from models.video_model import (
    VideoRequest
)

from services.video_processing_service import (
    process_youtube_video
)

from services.instagram_service import (
    get_instagram_data
)

router = APIRouter()


@router.post("/youtube")
async def youtube_video(
    request: VideoRequest
):

    try:

        return process_youtube_video(
            request.url
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.post("/instagram")
async def instagram_video(
    request: VideoRequest
):

    try:

        return get_instagram_data(
            request.url
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )