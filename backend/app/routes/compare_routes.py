from fastapi import APIRouter
from fastapi import HTTPException

from services.comparison_service import (
    compare_videos
)

router = APIRouter()


@router.get("/")
async def compare():

    try:

        return compare_videos()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )