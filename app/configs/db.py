from app.utils.settings import settings
from langchain_openai import OpenAIEmbeddings


class DB:
    _instance = None
    _vector_store = None

    def __init__(self):
        pass