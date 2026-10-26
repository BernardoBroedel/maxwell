"""Aplica a identidade e as configurações do Maxwell no Open WebUI pela API.

O Open WebUI guarda a configuração no banco após a primeira inicialização, então
variáveis de ambiente deixam de valer. Este script é idempotente: pode rodar de
novo depois de qualquer mudança aqui.

Uso (com o stack no ar):
    docker compose --profile setup run --rm configurar

Requer WEBUI_ADMIN_EMAIL e WEBUI_ADMIN_PASSWORD no .env (credenciais do admin).
Os modos (um cartão de modelo para cada) vêm de maxwell.modos; o resto só usa
a biblioteca padrão.
"""

import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from maxwell.modos import MODOS, PADRAO, Modo

URL = os.environ.get("OPENWEBUI_URL", "http://open-webui:8080").rstrip("/")
AVATAR = Path(__file__).resolve().parent.parent / "branding" / "maxwell-avatar-256.png"

CREDITOS = "Eletromagnetismo II (UFES)."


def sugestoes(modo: Modo) -> list[dict]:
    return [{"title": [linha1, linha2], "content": mensagem} for linha1, linha2, mensagem in modo.sugestoes]

BANNERS = [
    {
        "id": "maxwell-fase-de-testes",
        "type": "info",
        "title": "",
        "content": "O Maxwell está em fase de testes. Avalie as respostas com 👍/👎: isso ajuda a melhorar o tutor.",
        "dismissible": True,
        "timestamp": int(time.time()),
    }
]


def request(method: str, path: str, token: str | None = None, body: dict | None = None, *, none_if_404=False):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(URL + path, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            payload = response.read()
            return json.loads(payload) if payload else None
    except urllib.error.HTTPError as error:
        if none_if_404 and error.code == 404:
            return None
        raise SystemExit(f"Erro {error.code} em {method} {path}: {error.read().decode()[:300]}") from None


def passo(descricao: str):
    print(f"• {descricao}")


def main():
    email = os.environ.get("WEBUI_ADMIN_EMAIL")
    senha = os.environ.get("WEBUI_ADMIN_PASSWORD")
    if not email or not senha:
        sys.exit("Defina WEBUI_ADMIN_EMAIL e WEBUI_ADMIN_PASSWORD no .env (credenciais do admin).")

    token = request("POST", "/api/v1/auths/signin", body={"email": email, "password": senha})["token"]

    passo("Cadastros: abertos, com aprovação do admin")
    admin = request("GET", "/api/v1/auths/admin/config", token)
    admin.update(
        ENABLE_SIGNUP=True,
        DEFAULT_USER_ROLE="pending",
        ENABLE_MESSAGE_RATING=True,
        PENDING_USER_OVERLAY_TITLE="Cadastro recebido!",
        PENDING_USER_OVERLAY_CONTENT=(
            "Seu acesso ao Maxwell será liberado pela equipe em breve. "
            "Depois da aprovação, entre com o mesmo e-mail e senha."
        ),
    )
    request("POST", "/api/v1/auths/admin/config", token, admin)

    passo("Permissões dos alunos: sem envio de arquivos e sem prompt de sistema")
    permissoes = request("GET", "/api/v1/users/default/permissions", token)
    permissoes["chat"].update(file_upload=False, system_prompt=False)
    request("POST", "/api/v1/users/default/permissions", token, permissoes)

    passo("Idioma padrão: português (Brasil)")
    request("POST", "/api/v1/configs/import", token, {"config": {"ui.default_locale": "pt-BR"}})

    passo("Tarefas de fundo: só o título do chat (tags e sugestões gastariam o limite por minuto da API)")
    tarefas = request("GET", "/api/v1/tasks/config", token)
    tarefas.update(
        ENABLE_TITLE_GENERATION=True,
        ENABLE_FOLLOW_UP_GENERATION=False,
        ENABLE_TAGS_GENERATION=False,
        ENABLE_AUTOCOMPLETE_GENERATION=False,
        ENABLE_SEARCH_QUERY_GENERATION=False,
        ENABLE_RETRIEVAL_QUERY_GENERATION=False,
    )
    request("POST", "/api/v1/tasks/config/update", token, tarefas)

    passo(f"Modelo padrão: {PADRAO}")
    modelos = request("GET", "/api/v1/configs/models", token)
    modelos["DEFAULT_MODELS"] = PADRAO
    request("POST", "/api/v1/configs/models", token, modelos)

    passo("Sugestões da tela inicial")
    padrao = next(modo for modo in MODOS if modo.id == PADRAO)
    request("POST", "/api/v1/configs/suggestions", token, {"suggestions": sugestoes(padrao)})

    passo("Banner de fase de testes")
    request("POST", "/api/v1/configs/banners", token, {"banners": BANNERS})

    avatar = "data:image/png;base64," + base64.b64encode(AVATAR.read_bytes()).decode()
    for modo in MODOS:
        passo(f"Cartão do {modo.nome}: nome, avatar, descrição, visível para todos")
        modelo = {
            "id": modo.id,
            "base_model_id": None,
            "name": modo.nome,
            "meta": {
                "profile_image_url": avatar,
                "description": f"{modo.descricao} {CREDITOS}",
                "suggestion_prompts": sugestoes(modo),
            },
            "params": {},
            "access_grants": [{"principal_type": "user", "principal_id": "*", "permission": "read"}],
            "is_active": True,
        }
        existente = request("GET", f"/api/v1/models/model?id={modo.id}", token, none_if_404=True)
        request("POST", "/api/v1/models/model/update" if existente else "/api/v1/models/create", token, modelo)

    print("Pronto. Recarregue o Open WebUI no navegador.")


if __name__ == "__main__":
    main()
