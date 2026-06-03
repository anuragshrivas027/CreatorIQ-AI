conversation_memory = []

MAX_MEMORY_MESSAGES = 20


def add_message(
    role,
    content
):

    conversation_memory.append(
        {
            "role": role,
            "content": content
        }
    )

    if len(
        conversation_memory
    ) > MAX_MEMORY_MESSAGES:

        del conversation_memory[
            :-MAX_MEMORY_MESSAGES
        ]


def get_memory():

    return conversation_memory.copy()


def clear_memory():

    conversation_memory.clear()