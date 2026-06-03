import re

import yt_dlp

from youtube_transcript_api import (
    YouTubeTranscriptApi
)

from services.metrics_service import (
    calculate_engagement_rate
)


def extract_video_id(url):

    pattern = (
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    )

    match = re.search(
        pattern,
        url
    )

    if match:
        return match.group(1)

    return None


def get_youtube_data(url):

    ydl_opts = {
        "quiet": True,
        "noplaylist": True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        info = ydl.extract_info(
            url,
            download=False
        )

    video_id = extract_video_id(
        url
    )

    transcript_text = ""

    if video_id:

        try:

            transcript = (
                YouTubeTranscriptApi()
                .fetch(video_id)
            )

            transcript_text = " ".join(
                item.text
                for item in transcript
            )

        except Exception as e:

            transcript_text = (
                f"Transcript unavailable: {str(e)}"
            )

    else:

        transcript_text = (
            "Transcript unavailable: "
            "Invalid YouTube URL"
        )

    description = (
        info.get("description")
        or ""
    )

    hashtags = re.findall(
        r"#\w+",
        description
    )

    return {
        "platform": "youtube",
        "video_id": video_id,
        "title": info.get(
            "title"
        ),
        "creator": info.get(
            "uploader"
        ),
        "follower_count": (
            info.get(
                "channel_follower_count"
            )
            or "Unavailable"
        ),
        "views": info.get(
            "view_count"
        ) or 0,
        "likes": info.get(
            "like_count"
        ) or 0,
        "comments": info.get(
            "comment_count"
        ) or 0,
        "duration": info.get(
            "duration"
        ),
        "upload_date": info.get(
            "upload_date"
        ),
        "hashtags": hashtags,
        "description": description,
        "engagement_rate": (
            calculate_engagement_rate(
                info.get(
                    "view_count"
                ),
                info.get(
                    "like_count"
                ),
                info.get(
                    "comment_count"
                )
            )
        ),
        "transcript": transcript_text
    }