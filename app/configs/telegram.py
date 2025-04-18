from telegram import Update
from fastapi import FastAPI
from ..utils.settings import settings
from app.schemas.chat_schema import ChatRequest
from app.utils.escape_markdown_v2 import escape_markdown_v2
from telegram.ext import filters, ContextTypes, MessageHandler, ApplicationBuilder
from app.services.generate_answer_agent_service import generate_answer_agent_service


async def start_telegram_bot(app: FastAPI):
    """Bot de telegram"""
    try:
        # Creamos el bot de telegram
        bot = ApplicationBuilder().token(settings.telegram_bot_token).build()

        # Registramos el handler de mensajes
        bot.add_handler(MessageHandler(filters.TEXT & (~filters.UpdateType.EDITED_MESSAGE), handle_message))

        # Guardamos el bot en el state
        app.state.bot_telegram = bot

        # Iniciamos el bot
        await bot.initialize()
        await bot.start()
        await bot.updater.start_polling()

    except Exception as e:
        print("Se ha producido un error en el bot de telegram:", e)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler de mensajes"""
    print("id del chat:", update.effective_chat.id)
    # enviamos una señal de typing
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    # Importamos el state para obtener el agente
    from app.main import asesor_ia

    # json que recibe la función del agente
    json_data = {
        "id_chat": str(update.effective_chat.id),
        "user_message": update.effective_message.text,
    }

    # llamamos a la función del agente
    response = await generate_answer_agent_service(ChatRequest(**json_data), asesor_ia.state.agent)

    # enviamos el mensaje
    await context.bot.send_message(chat_id=update.effective_chat.id, text=escape_markdown_v2(response), parse_mode="MarkdownV2")
