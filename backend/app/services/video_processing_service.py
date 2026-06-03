from services.youtube_service import (
    get_youtube_data
)

from rag.process_video import (
    process_transcript
)

from utils.video_registry import (
    save_video
)


def process_youtube_video(url):

    print(
        f"Processing URL: {url}"
    )

    video_data = get_youtube_data(
        url
    )

    print(
        "YouTube data fetched successfully"
    )

    label = save_video(
        video_data
    )

    print(
        f"Video label assigned: {label}"
    )

    transcript = (
        video_data.get(
            "transcript"
        ) or ""
    )

    metadata = {
        "video_id": label,
        "title": video_data.get(
            "title"
        ),
        "creator": video_data.get(
            "creator"
        ),
        "views": video_data.get(
            "views"
        ),
        "likes": video_data.get(
            "likes"
        ),
        "comments": video_data.get(
            "comments"
        ),
        "engagement_rate": video_data.get(
            "engagement_rate"
        )
    }

    chunks_created = 0

    if (
        transcript
        and not transcript.startswith(
            "Transcript unavailable"
        )
    ):

        print(
            "Starting transcript processing"
        )

        try:

            chunks_created = (
                process_transcript(
                    transcript,
                    metadata
                )
            )

            print(
                f"Chunks created: {chunks_created}"
            )

        except Exception as e:

            print(
                f"RAG Processing Error: {e}"
            )

            chunks_created = 0

    else:

        print(
            "Transcript unavailable. Skipping RAG processing."
        )

    print(
        "Returning API response"
    )

    return {
        "video_label": label,
        "video": video_data,
        "chunks_created": chunks_created
    }