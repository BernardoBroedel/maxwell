import re
from importlib.resources import files

from langchain_openai import ChatOpenAI

from maxwell.config import Settings


def build_llm(settings: Settings) -> ChatOpenAI:
    if not settings.llm_api_key:
        raise RuntimeError(
            "LLM_API_KEY não definida no .env. Use a chave da API do plano B "
            "ou 'ollama' para o Qwen local (veja .env.example)."
        )
    return ChatOpenAI(
        base_url=settings.llm_base_url,
        api_key=settings.llm_api_key,
        model=settings.llm_model,
        temperature=settings.llm_temperature,
        streaming=True,
    )


def segundos_para_tentar_de_novo(erro: Exception, maximo: float = 60) -> float | None:
    """Quanto esperar depois de um erro de limite por minuto (HTTP 429); None se não for o caso.

    O Groq diz o tempo na mensagem ("Please try again in 34.5s"); sem isso, espera 20 s.
    """
    if getattr(erro, "status_code", None) != 429:
        return None
    tempo = re.search(r"try again in (?:(\d+)m)?([\d.]+)s", str(erro))
    segundos = 60 * int(tempo.group(1) or 0) + float(tempo.group(2)) if tempo else 20
    return min(segundos + 1, maximo)


def load_prompt(arquivo: str) -> str:
    """Regras comuns (base.md) seguidas das instruções do modo."""
    prompts = files("maxwell.prompts")
    base = prompts.joinpath("base.md").read_text(encoding="utf-8")
    return base + "\n" + prompts.joinpath(arquivo).read_text(encoding="utf-8")
