import os

from dotenv import load_dotenv

from langchain_core.prompts import (
    ChatPromptTemplate
)

from langchain_core.output_parsers import (
    StrOutputParser
)

from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from utils.video_registry import (
    get_all_videos
)

load_dotenv()


def compare_videos():

    videos = get_all_videos()

    video_a = videos.get("A")
    video_b = videos.get("B")

    if not video_a or not video_b:

        return {
            "winner": "Unknown",
            "comparison":
                "Please upload both Video A and Video B."
        }

    transcript_a = (
        video_a.get("transcript")
        or ""
    )[:2000]

    transcript_b = (
        video_b.get("transcript")
        or ""
    )[:2000]

    prompt = ChatPromptTemplate.from_template(
        """
You are a senior social media growth strategist.

Analyze the following two videos.

VIDEO A

Title:
{title_a}

Creator:
{creator_a}

Follower Count:
{followers_a}

Views:
{views_a}

Likes:
{likes_a}

Comments:
{comments_a}

Engagement Rate:
{engagement_a}

Transcript:
{transcript_a}


VIDEO B

Title:
{title_b}

Creator:
{creator_b}

Follower Count:
{followers_b}

Views:
{views_b}

Likes:
{likes_b}

Comments:
{comments_b}

Engagement Rate:
{engagement_b}

Transcript:
{transcript_b}


Return the answer EXACTLY in this format:

WINNER:
<Video A or Video B>

ENGAGEMENT ANALYSIS:
<analysis>

HOOK ANALYSIS:
<analysis>

CREATOR ANALYSIS:
<analysis>

RECOMMENDATIONS:
<analysis>

ACTION PLAN:
<analysis>

FINAL VERDICT:
<analysis>
"""
    )

    try:

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv(
                "GEMINI_API_KEY"
            ),
            temperature=0.3
        )

        chain = (
            prompt
            | llm
            | StrOutputParser()
        )

        report = chain.invoke(
            {
                "title_a":
                    video_a.get("title"),

                "creator_a":
                    video_a.get("creator"),

                "followers_a":
                    video_a.get(
                        "follower_count"
                    ),

                "views_a":
                    video_a.get("views"),

                "likes_a":
                    video_a.get("likes"),

                "comments_a":
                    video_a.get("comments"),

                "engagement_a":
                    video_a.get(
                        "engagement_rate"
                    ),

                "transcript_a":
                    transcript_a,

                "title_b":
                    video_b.get("title"),

                "creator_b":
                    video_b.get("creator"),

                "followers_b":
                    video_b.get(
                        "follower_count"
                    ),

                "views_b":
                    video_b.get("views"),

                "likes_b":
                    video_b.get("likes"),

                "comments_b":
                    video_b.get("comments"),

                "engagement_b":
                    video_b.get(
                        "engagement_rate"
                    ),

                "transcript_b":
                    transcript_b,
            }
        )

    except Exception as e:

        error_text = str(e)

        if "RESOURCE_EXHAUSTED" in error_text:

            return {
                "winner": "Unknown",
                "comparison":
                    (
                        "Gemini API quota exceeded. "
                        "Please wait a few minutes "
                        "or use a new API key."
                    )
            }

        return {
            "winner": "Unknown",
            "comparison":
                f"LangChain Error: {error_text}"
        }

    winner = "Unknown"

    try:

        if "WINNER:" in report:

            winner_section = (
                report.split(
                    "WINNER:"
                )[1][:100]
            )

            if "Video A" in winner_section:

                winner = "Video A"

            elif "Video B" in winner_section:

                winner = "Video B"

    except Exception:

        winner = "Unknown"

    return {
        "winner": winner,
        "comparison": report
    }