from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    openai_api_key: str = ""
    prefix_route: str = ""
    collection_name: str = ""
    telegram_bot_token: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()