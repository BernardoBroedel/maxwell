from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Qualquer API compatível com OpenAI: Groq, OpenRouter, Ollama...
    llm_base_url: str = "https://api.groq.com/openai/v1"
    llm_api_key: str = ""
    llm_model: str = "qwen/qwen3.8-27b"
    llm_temperature: float = 0.3

    # Material do RAG: Markdown do livro e das notas. Sem a pasta, o tutor roda sem RAG.
    material_dir: str = "data/processed"


@lru_cache
def get_settings() -> Settings:
    return Settings()
