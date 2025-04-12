from app.configs.lifespan import lifespan
from fastapi import FastAPI, HTTPException
from app.utils.custom_error import custom_error
from fastapi.middleware.cors import CORSMiddleware
from app.routers.mcp_router import router as mcp_router

asesor_ia = FastAPI(
    title="API para consumir los servicios de IA",
    docs_url="/asesor_ia/docs",
    openapi_url="/asesor_ia/openapi.json",
    lifespan=lifespan
)
asesor_ia.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manejador de excepciones personalizada
@asesor_ia.exception_handler(HTTPException)
def manage_exception(exc):
    return custom_error(exc)


asesor_ia.include_router(mcp_router)