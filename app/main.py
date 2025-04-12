from app.configs.lifespan import lifespan
from fastapi import FastAPI, HTTPException
from app.utils.custom_error import custom_error
from fastapi.middleware.cors import CORSMiddleware
from app.routers.mcp_router import router as mcp_router

langchain_mcp = FastAPI(
    title="API para consumir los servicios de IA",
    docs_url="/langchain/docs",
    openapi_url="/langchain/openapi.json",
    lifespan=lifespan
)
langchain_mcp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manejador de excepciones personalizada
@langchain_mcp.exception_handler(HTTPException)
def manage_exception(exc):
    return custom_error(exc)


langchain_mcp.include_router(mcp_router)