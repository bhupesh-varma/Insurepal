import os
from langchain.memory.chat_message_histories import PostgresChatMessageHistory

def get_history(session_id):
    return PostgresChatMessageHistory(
        connection_string=os.getenv("POSTGRES_URL"),
        session_id=session_id
    )
