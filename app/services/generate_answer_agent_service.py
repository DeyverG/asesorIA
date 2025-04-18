from app.configs.db import DB
from langchain.schema import HumanMessage
from app.schemas.chat_schema import ChatRequest
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt.chat_agent_executor import AgentState
from langgraph.prebuilt.chat_agent_executor import CompiledGraph

# client_db = DB()
memory = MemorySaver()

class ChatAgentState(AgentState):
    context: str


async def generate_answer_agent_service(data_chat: ChatRequest, agent_ai: CompiledGraph):

    try:
        # Configuramos el agente para que se ejecute en un thread y mantener el contexto de la conversación
        config = {"configurable": {"thread_id": data_chat.id_chat}}

        # Creamos el mensaje de usuario
        user_message = HumanMessage(data_chat.user_message)

        # Realizamos la consulta a la base de datos
        # context = client_db.search_documents(data_chat.user_message)

        # Ejecutamos el agente
        response = await agent_ai.ainvoke({"messages": user_message}, stream_mode="values", config=config)
        print(response['messages'][-1].content)
        return response['messages'][-1].content
    
    except Exception as e:
        print("Se ha producido un error:", e, e.args)
    
