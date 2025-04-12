from qdrant_client import QdrantClient
from app.utils.settings import settings
from langchain_qdrant import QdrantVectorStore
from langchain_openai import OpenAIEmbeddings
# Creamos una sola instancia de la base de datos


class DB:
    _instance = None
    _vector_store = None

    def __init__(self):
        # Primero creamos la instancia de la base de datos
        if self._instance is None:
            try:
                self._instance = QdrantClient(
                    url="http://localhost:6333", timeout=30)
            except Exception as e:
                print("Error al crear la instancia de la base de datos:", e)

        # Luego de crear la instancia, creamos el vector store
        if self._vector_store is None:
            try:
                embeddings = OpenAIEmbeddings()
                self._vector_store = QdrantVectorStore(
                    client=self._instance,
                    collection_name=settings.collection_name,
                    embedding=embeddings,
                    content_payload_key="fragment",
                )
            except Exception as e:
                print("Error al crear el vector store:", e)

    def search_documents(self, query):
        retriever = self._vector_store.as_retriever(search_kwargs={"k": 3})

        context = retriever.invoke(query)

        return context
