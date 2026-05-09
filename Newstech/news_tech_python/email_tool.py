from __future__ import annotations

import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv


# Carrega as variáveis do arquivo .env
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
DESTINATARIOS = os.getenv("DESTINATARIOS", "")


def enviar_email_html(assunto: str, conteudo_html: str) -> str:
    """
    Envia um e-mail em formato HTML.

    Parâmetros:
    - assunto: título do e-mail.
    - conteudo_html: conteúdo HTML gerado pelo Gemini.

    Retorno:
    - mensagem de sucesso ou erro.
    """

    if not EMAIL_ADDRESS:
        return "Erro: EMAIL_ADDRESS não configurado no .env."

    if not EMAIL_PASSWORD:
        return "Erro: EMAIL_PASSWORD não configurado no .env."

    if not DESTINATARIOS:
        return "Erro: DESTINATARIOS não configurado no .env."

    try:
        msg = EmailMessage()
        msg["Subject"] = assunto
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = DESTINATARIOS

        # Conteúdo principal em HTML
        msg.add_alternative(conteudo_html, subtype="html")

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return "E-mail HTML enviado com sucesso."

    except Exception as erro:
        return f"Erro ao enviar e-mail: {erro}"


if __name__ == "__main__":
    html_teste = """
    <html>
      <body style="font-family: Arial, sans-serif;">
        <h1>Teste de e-mail HTML</h1>
        <p>Se você recebeu esta mensagem, o envio em HTML funcionou.</p>
      </body>
    </html>
    """

    resposta = enviar_email_html(
        assunto="Teste de e-mail HTML",
        conteudo_html=html_teste
    )

    print(resposta)
