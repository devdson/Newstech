from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from prompt import prompt_ativo
from email_tool import enviar_email_html


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


def gerar_boletim() -> str:
    """
    Envia o prompt ativo para o Gemini e retorna o conteúdo gerado.

    Repare que o código não muda.
    Quem muda o comportamento do agente é o prompt escolhido em prompt.py.
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


def salvar_boletim(conteudo: str) -> Path:
    """
    Salva o boletim gerado na pasta saidas/.

    Se o prompt profissional estiver ativo, o conteúdo será HTML.
    Se outro prompt estiver ativo, pode ser texto simples.
    """

    pasta_saida = Path("saidas")
    pasta_saida.mkdir(exist_ok=True)

    data_arquivo = datetime.now().strftime("%Y-%m-%d_%H-%M")
    caminho_arquivo = pasta_saida / f"boletim_ia_{data_arquivo}.html"

    caminho_arquivo.write_text(conteudo, encoding="utf-8")

    return caminho_arquivo


def perguntar_envio_email() -> bool:
    """Pergunta se o usuário deseja enviar o boletim por e-mail."""

    resposta = input("\nDeseja enviar este boletim por e-mail? [s/N]: ")
    return resposta.strip().lower() == "s"


def main() -> None:
    """Executa o fluxo principal do projeto."""

    print("\nGerando boletim com Gemini...")
    print("Dica: altere o prompt ativo no arquivo prompt.py para comparar os resultados.\n")

    conteudo = gerar_boletim()

    print("=" * 80)
    print("BOLETIM GERADO")
    print("=" * 80)
    print(conteudo)
    print("=" * 80)

    caminho = salvar_boletim(conteudo)
    print(f"\nArquivo salvo em: {caminho}")

    if perguntar_envio_email():
        data_atual = datetime.now().strftime("%d/%m/%Y")
        assunto = f"Boletim IA & Tecnologia - {data_atual}"

        resultado = enviar_email_html(
            assunto=assunto,
            conteudo_html=conteudo,
        )

        print(resultado)
    else:
        print("Envio cancelado. O boletim foi apenas salvo localmente.")


if __name__ == "__main__":
    main()
