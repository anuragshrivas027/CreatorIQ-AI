video_store = {}


def save_video(video_data):

    if "A" not in video_store:

        video_store["A"] = video_data

        return "A"

    if "B" not in video_store:

        video_store["B"] = video_data

        return "B"

    video_store["B"] = video_data

    return "B"


def get_video(label):

    return video_store.get(
        label
    )


def get_all_videos():

    return video_store.copy()


def clear_videos():

    video_store.clear()