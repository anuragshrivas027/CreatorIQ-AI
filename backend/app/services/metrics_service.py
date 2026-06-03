def calculate_engagement_rate(
    views,
    likes,
    comments
):

    views = views or 0
    likes = likes or 0
    comments = comments or 0

    if views <= 0:
        return 0.0

    engagement_rate = (
        (
            likes + comments
        ) / views
    ) * 100

    return round(
        engagement_rate,
        2
    )