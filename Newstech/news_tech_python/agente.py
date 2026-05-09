"""
01_agente.py
============

Objetivo da aula:
Mostrar que o comportamento do agente muda conforme o prompt escolhido.

Como testar:
1. Abra o arquivo prompt.py.
2. Escolha o prompt ativo comentando/descomentando a variável `prompt_ativo`.
3. Rode no terminal:

   python 01_agente.py

Nesta versão, o código é propositalmente simples.
O foco da aula é o prompt, não a arquitetura Python.
"""

from __future__ import annotations

import os
from datetime import datetime

from dotenv import load_dotenv
from google import genai

from prompt import prompt_ativo


# Carrega as variáveis do arquivo .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")


if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY não encontrada. "
        "Crie um arquivo .env com: GEMINI_API_KEY=sua_chave_aqui"
    )


# Cria o cliente do Gemini
client = genai.Client(api_key=GEMINI_API_KEY)


def gerar_resposta() -> str:
    """
    Envia o prompt ativo para o Gemini.

    A única informação adicional enviada aqui é a data,
    para que o boletim consiga preencher a edição corretamente.

    O restante da inteligência está no prompt.py.
    """
    data_atual = datetime.now().strftime("%d/%m/%Y")

    prompt_final = f"""
DATA DA EDIÇÃO: {data_atual}

{prompt_ativo}
""".strip()

    resposta = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt_final,
    )

    return resposta.text or ""


if __name__ == "__main__":
    resposta = gerar_resposta()

    print("\n" + "=" * 80)
    print("RESPOSTA DO GEMINI")
    print("=" * 80 + "\n")
    print(resposta)