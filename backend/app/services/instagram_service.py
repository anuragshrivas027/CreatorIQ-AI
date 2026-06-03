import re

import yt_dlp

from services.metrics_service import (
    calculate_engagement_rate
)

from utils.video_registry import (
    save_video
)


def get_instagram_data(url):

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

    description = (
        info.get(
            "description"
        ) or ""
    )

    hashtags = re.findall(
        r"#\w+",
        description
    )

    video_data = {
        "platform": "instagram",
        "video_id": info.get(
            "id"
        ),
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
        "transcript": description
    }

    label = save_video(
        video_data
    )

    video_data[
        "video_label"
    ] = label

    return video_data