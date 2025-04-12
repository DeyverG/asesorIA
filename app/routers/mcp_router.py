from app.utils.settings import settings
from fastapi import Request, status, APIRouter
from fastapi.responses import StreamingResponse
from app.schemas.chat_schema import ChatRequest
from app.services.generate_answer_agent_service import generate_answer_agent_service


router = APIRouter(prefix=settings.prefix_route)


@router.post(
    "/chat-agent",
    include_in_schema=False,
    tags=["IA"],
    status_code=status.HTTP_200_OK,
    summary="Genera un chat con un Agente IA")
async def generate_answer_agent_router(data_chat: ChatRequest, request: Request):
    """
    ## Genera un chat con un Agente IA

    """

    return StreamingResponse(generate_answer_agent_service(data_chat, request.app.state.agent_ai), media_type="text/event-stream")
