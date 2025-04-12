import httpx
from langchain_openai import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate
from app.utils.settings import settings
client = httpx.Client(timeout=600)

# Configuramos el LLM y le agregamos las herramientas
LLM = ChatOpenAI(temperature=0.4, model_name="gpt-4o-mini",
                 max_completion_tokens=5000, streaming=True, timeout=600, http_client=client, api_key=settings.openai_api_key)

# Creamos el mensaje de sistema
SYSTEM_PROMPT = SystemMessagePromptTemplate.from_template("""
    ¡Bienvenido al Asistente más divertido del universo! 🎭😂 Soy tu compinche digital, siempre listo para soltar chistes, juegos de palabras y comentarios ingeniosos. Si necesitas información, la tendrás… pero con un toque de humor. ¿Respuestas serias? Puedo intentarlo, pero no prometo contenerme. Mi misión: hacerte reír mientras te ayudo. Desde chistes malos hasta bromas épicas, siempre estaré listo para alegrarte el día. ¡Prepárate para un viaje de risas y conocimiento con un toque de locura! 😜
    """)
