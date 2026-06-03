from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.video_routes import (
    router as video_router
)

from routes.chat_routes import (
    router as chat_router
)

from routes.compare_routes import (
    router as compare_router
)

app = FastAPI(
    title="CreatorIQ AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    video_router,
    prefix="/api/videos",
    tags=["Videos"]
)

app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["Chat"]
)

app.include_router(
    compare_router,
    prefix="/api/compare",
    tags=["Compare"]
)


@app.get("/")
async def root():

    return {
        "message": "CreatorIQ AI Backend Running",
        "status": "healthy",
        "version": "1.0.0"
    }