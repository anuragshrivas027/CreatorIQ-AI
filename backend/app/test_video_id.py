from services.youtube_service import (
    extract_video_id
)

urls = [
    "https://www.youtube.com/watch?v=jNQXAC9IVRw",
    "https://youtu.be/jNQXAC9IVRw",
    "https://youtu.be/jNQXAC9IVRw?si=test"
]

for url in urls:

    print(url)

    print(
        extract_video_id(url)
    )

    print("-" * 40)