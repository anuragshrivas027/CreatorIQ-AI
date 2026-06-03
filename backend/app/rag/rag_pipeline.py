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

from rag.vector_store import (
    search_chunks
)

from rag.memory_manager import (
    add_message,
    get_memory
)

from rag.prompt_templates import (
    SYSTEM_PROMPT
)

from utils.video_registry import (
    get_all_videos
)

load_dotenv()


def build_context(question):

    try:

        results = search_chunks(
            question
        )

    except Exception:

        results = {
            "documents": [[]],
            "metadatas": [[]]
        }

    documents = results.get(
        "documents",
        [[]]
    )

    metadatas = results.get(
        "metadatas",
        [[]]
    )

    context = ""

    if documents and documents[0]:

        context = "\n\n".join(
            documents[0]
        )

    videos = get_all_videos()

    video_a = videos.get("A")
    video_b = videos.get("B")

    video_context = ""

    if video_a:

        video_context += f"""

VIDEO A

Title:
{video_a.get('title')}

Creator:
{video_a.get('creator')}

Follower Count:
{video_a.get('follower_count')}

Views:
{video_a.get('views')}

Likes:
{video_a.get('likes')}

Comments:
{video_a.get('comments')}

Engagement Rate:
{video_a.get('engagement_rate')}

Transcript:
{(video_a.get('transcript') or '')[:1500]}
"""

    if video_b:

        video_context += f"""

VIDEO B

Title:
{video_b.get('title')}

Creator:
{video_b.get('creator')}

Follower Count:
{video_b.get('follower_count')}

Views:
{video_b.get('views')}

Likes:
{video_b.get('likes')}

Comments:
{video_b.get('comments')}

Engagement Rate:
{video_b.get('engagement_rate')}

Transcript:
{(video_b.get('transcript') or '')[:1500]}
"""

    memory = get_memory()

    memory_text = "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in memory
        ]
    )

    return (
        context,
        metadatas,
        video_context,
        memory_text
    )


def create_chain():

    prompt = ChatPromptTemplate.from_template(
        """
{system_prompt}

Video Information:
{video_context}

Conversation Memory:
{memory_text}

Retrieved Context:
{context}

Question:
{question}

Instructions:

- Use Video A information when relevant.
- Use Video B information when relevant.
- Compare videos if requested.
- Use transcript context if available.
- Use engagement metrics when available.
- Use conversation memory.
- Give practical creator advice.
- If transcript evidence is used, mention it.
- If follower count is unavailable, say unavailable.
- Never invent information.

Answer:
"""
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv(
            "GEMINI_API_KEY"
        ),
        temperature=0.3
    )

    return (
        prompt
        | llm
        | StrOutputParser()
    )


def ask_rag(question):

    (
        context,
        metadatas,
        video_context,
        memory_text
    ) = build_context(
        question
    )

    try:

        chain = create_chain()

        answer = chain.invoke(
            {
                "system_prompt":
                    SYSTEM_PROMPT,
                "video_context":
                    video_context,
                "memory_text":
                    memory_text,
                "context":
                    context,
                "question":
                    question
            }
        )

    except Exception as e:

        answer = (
            f"LangChain Error: {str(e)}"
        )

    add_message(
        "user",
        question
    )

    add_message(
        "assistant",
        answer
    )

    return {
        "answer": answer,
        "sources": (
            metadatas[0]
            if metadatas
            else []
        )
    }


def stream_rag(question):

    (
        context,
        metadatas,
        video_context,
        memory_text
    ) = build_context(
        question
    )

    chain = create_chain()

    full_answer = ""

    try:

        for chunk in chain.stream(
            {
                "system_prompt":
                    SYSTEM_PROMPT,
                "video_context":
                    video_context,
                "memory_text":
                    memory_text,
                "context":
                    context,
                "question":
                    question
            }
        ):

            full_answer += chunk

            yield chunk

    except Exception as e:

        yield (
            f"\nLangChain Error: {str(e)}"
        )

    add_message(
        "user",
        question
    )

    add_message(
        "assistant",
        full_answer
    )