## Comandos para levantar el Proyecto

#### Instalar uv (si no esta instalado)
Seguir los pasos de la documentacion **[uv](https://docs.astral.sh/uv/getting-started/installation/)** y guardar las variables de entorno en el sistema, 
###### **pdta: crear archivo .env y ajustar variables de entorno**

#### Sincronizamos el repositorio para que se cree el entorno y se instalen las dependencias
- [`uv sync`](#code)

#### 

#### Activamos el Entorno
- [`source .venv/bin/activate`](#code)

#### Levantar servidor de FastAPI
- [`uvicorn app.main:langchain_mcp --port 9001 --reload`](#code)

#### desactivar Entorno
- [`source .venv/bin/deactivate`](#code)
