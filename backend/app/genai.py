from langchain_core.language_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI


def gemini_llm() -> BaseChatModel:
    client = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
    )
    return client
