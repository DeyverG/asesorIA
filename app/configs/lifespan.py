from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.configs.llm import LLM, SYSTEM_PROMPT
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from app.configs.telegram import start_telegram_bot
from app.services.get_tools_service import get_tools_service
from telegram.ext import Application

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan del servidor FastAPI."""
    
    await start_agent_with_mcp(app)
    await start_telegram_bot(app)
    
    yield
    # Notificar que el agente con tools ha terminado
    print("Cerrando los contextos")
    # Cerrar el cliente de tools
    await app.state.client.__aexit__(None, None, None)
    bot: Application = app.state.bot_telegram
    await bot.updater.stop()
    await bot.stop()
    await bot.shutdown()


async def start_agent_with_mcp(app: FastAPI):
    memory = MemorySaver()
    try:
        # Obtenemos El cliente que se conecta con las tools
        client  = get_tools_service()

        # Manualmente entramos al context
        await client.__aenter__()

        # Guardamos el cliente en el state
        app.state.client = client

        # Cargamos el system_prompt al chat
        system_message = ChatPromptTemplate.from_messages(
            [SYSTEM_PROMPT, ("placeholder", "{messages}")])

        # Creamos el agente y sus configuraciones
        agent = create_react_agent(model=LLM, tools=client.get_tools(
        ), checkpointer=memory, prompt=system_message)

        # Guardamos el agente en el state
        app.state.agent = agent

    except Exception as e:
        print("Se ha producido un error:", e, e.args)