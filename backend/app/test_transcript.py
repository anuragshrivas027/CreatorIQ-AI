from youtube_transcript_api import (
    YouTubeTranscriptApi
)

video_id = "jNQXAC9IVRw"

transcript = (
    YouTubeTranscriptApi()
    .fetch(video_id)
)

print(
    len(transcript)
)

print(
    transcript[0].text
)