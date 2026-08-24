import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field

class Config(BaseModel):
    gemini_api_key: str = Field(..., min_length=1)

def load_config(dotenv_path: str | None = ".env") -> Config:
    if dotenv_path and os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key.strip() == "" or api_key.strip() == "sua_chave_aqui":
        raise ValueError("GEMINI_API_KEY não foi encontrada ou não foi configurada corretamente no ambiente.")
    return Config(gemini_api_key=api_key.strip())
