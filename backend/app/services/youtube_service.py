import re

import yt_dlp

from youtube_transcript_api import (
    YouTubeTranscriptApi
)

from services.metrics_service import (
    calculate_engagement_rate
)


def extract_video_id(url):

    patterns = [
        r"(?:v=)([0-9A-Za-z_-]{11})",
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
        r"shorts\/([0-9A-Za-z_-]{11})"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            url
        )

        if match:

            return match.group(1)

    return None


def get_youtube_data(url):

    print(
        f"Processing URL: {url}"
    )

    video_id = extract_video_id(
        url
    )

    print(
        f"Video ID: {video_id}"
    )

    transcript_text = ""

    if video_id:

        try:

            print(
                f"Fetching transcript for: {video_id}"
            )

            transcript = (
                YouTubeTranscriptApi()
                .fetch(video_id)
            )

            transcript_text = " ".join(
                item.text
                for item in transcript
            )

            print(
                f"Transcript fetched successfully. Length: {len(transcript_text)}"
            )

        except Exception as e:

            print(
                f"Transcript Error: {e}"
            )

            transcript_text = (
                f"Transcript unavailable: {str(e)}"
            )

    else:

        transcript_text = (
            "Transcript unavailable: Invalid YouTube URL"
        )

    try:

        ydl_opts = {
            "quiet": False,
            "noplaylist": True,
            "extract_flat": False
        }

        with yt_dlp.YoutubeDL(
            ydl_opts
        ) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )

        print(
            "YouTube metadata fetched successfully"
        )

    except Exception as e:

        print(
            f"YouTube Metadata Error: {e}"
        )

        raise Exception(
            f"YouTube Metadata Error: {e}"
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