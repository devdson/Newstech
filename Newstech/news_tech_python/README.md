# Agente Editorial com Gemini

Projeto didático para aula prática de Engenharia de Prompt.

A ideia principal da aula é mostrar que, em um agente de IA, o prompt deixa de ser apenas uma pergunta e passa a funcionar como uma instrução operacional.

O projeto foi simplificado para deixar o foco no prompt:

- o código principal quase não muda;
- o modelo continua o mesmo;
- a diferença aparece quando trocamos o prompt ativo em `prompt.py`.

## O que o projeto faz

O projeto gera um boletim profissional sobre IA e tecnologia usando Gemini.

Ele permite testar três níveis de prompt:

1. **Prompt fraco** — pedido genérico, sem contexto nem formato.
2. **Prompt intermediário** — já define papel, tarefa, público, formato e restrições.
3. **Prompt profissional** — funciona como especificação de trabalho e pede saída em HTML para e-mail.

A proposta de sala é rodar o mesmo código com prompts diferentes e comparar os resultados.

## Estrutura dos arquivos

```text
projeto-agente-editorial/
├── 01_agente.py
├── 02_email_tool.py
├── 03_boletim_ia.py
├── prompt.py
├── requirements.txt
├── .env.example
├── README.md
└── saidas/
```

### `prompt.py`

Arquivo mais importante para a aula.

Ele contém:

- `prompt_fraco`
- `prompt_intermediario`
- `prompt_pro_agente`
- `prompt_ativo`

Para trocar o comportamento do agente, basta comentar e descomentar a linha desejada:

```python
# prompt_ativo = prompt_fraco
# prompt_ativo = prompt_intermediario
prompt_ativo = prompt_pro_agente
```

Deixe apenas uma linha ativa por vez.

### `01_agente.py`

Primeiro teste simples com Gemini.

Use para mostrar:

- como carregar a chave da API;
- como chamar o Gemini;
- como importar o prompt ativo;
- como o resultado muda quando o prompt muda.

### `02_email_tool.py`

Ferramenta de envio de e-mail HTML.

Esse arquivo mostra a ideia de ferramenta externa: o modelo gera o conteúdo, mas o envio é feito por uma função separada.

O envio é opcional na aula.

### `03_boletim_ia.py`

Projeto final.

Ele:

1. importa o `prompt_ativo`;
2. monta a mensagem final com data, tema, público e insumos didáticos;
3. chama o Gemini;
4. salva o resultado como HTML na pasta `saidas/`;
5. pergunta se o usuário deseja enviar por e-mail.

## Pré-requisitos

- Python 3.10 ou superior.
- Uma chave da API do Gemini.
- Opcional: conta Gmail com senha de app para envio de e-mail.

## Passo a passo de instalação

### 1. Criar a pasta do projeto

```bash
mkdir projeto-agente-editorial
cd projeto-agente-editorial
```

Coloque os arquivos do projeto dentro dessa pasta.

### 2. Criar ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Criar arquivo `.env`

Copie o arquivo `.env.example` e renomeie para `.env`.

No Windows:

```bash
copy .env.example .env
```

No macOS/Linux:

```bash
cp .env.example .env
```

Depois, edite o `.env`:

```env
GEMINI_API_KEY=sua_chave_do_gemini_aqui
GEMINI_MODEL=gemini-2.0-flash
```

Para testar e-mail, preencha também:

```env
EMAIL_ADDRESS=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
DESTINATARIOS=email_destino@exemplo.com
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
```

> Nunca envie o arquivo `.env` para o GitHub.

## Como usar em aula

### Parte 1 — Rodar com prompt fraco

Abra o arquivo `prompt.py` e deixe assim:

```python
prompt_ativo = prompt_fraco
# prompt_ativo = prompt_intermediario
# prompt_ativo = prompt_pro_agente
```

Rode:

```bash
python 01_agente.py
```

Observe com a turma:

- O resultado ficou genérico?
- O formato foi respeitado?
- O texto parece pronto para envio?
- Faltou público-alvo?
- Faltou restrição?

### Parte 2 — Rodar com prompt intermediário

Altere o `prompt.py`:

```python
# prompt_ativo = prompt_fraco
prompt_ativo = prompt_intermediario
# prompt_ativo = prompt_pro_agente
```

Rode novamente:

```bash
python 01_agente.py
```

Compare:

- Melhorou o formato?
- O texto ficou mais didático?
- As restrições foram respeitadas?
- Ainda faltou algo para virar produto?

### Parte 3 — Rodar com prompt profissional

Altere o `prompt.py`:

```python
# prompt_ativo = prompt_fraco
# prompt_ativo = prompt_intermediario
prompt_ativo = prompt_pro_agente
```

Rode o projeto final:

```bash
python 03_boletim_ia.py
```

O resultado será salvo em:

```text
saidas/boletim_ia_DD-MM-AAAA.html
```

Esse arquivo pode ser aberto no navegador para visualizar o e-mail.

## Como testar envio de e-mail

Primeiro, configure no `.env`:

```env
EMAIL_ADDRESS=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app
DESTINATARIOS=email_destino@exemplo.com
```

Depois rode:

```bash
python 02_email_tool.py
```

Se o teste funcionar, rode:

```bash
python 03_boletim_ia.py
```

Quando aparecer a pergunta:

```text
Deseja enviar este boletim por e-mail? [s/N]:
```

Digite:

```text
s
```

## O que comentar com os alunos

### Mensagem principal

Mesmo código. Mesmo modelo. Mesma tarefa. O que mudou foi o prompt.

### Perguntas para discussão

- O que o prompt fraco deixou em aberto?
- Que parte do prompt intermediário melhorou o resultado?
- O prompt profissional ficou maior ou ficou mais organizado?
- O que está no código?
- O que está no prompt?
- Qual parte seria mais fácil de adaptar para outro tema?

### Erros comuns

- Achar que prompt grande é automaticamente melhor.
- Misturar regras sem hierarquia.
- Pedir fontes, mas permitir que o modelo invente.
- Não definir público-alvo.
- Não especificar formato de saída.
- Não dizer o que fazer quando a informação não estiver disponível.
- Colocar chave de API direto no código.

## Adaptações possíveis

Você pode trocar o tema do boletim em `03_boletim_ia.py`:

```python
tema = "Automação com N8N para pequenos negócios"
```

Também pode trocar o público:

```python
publico = "Pequenos empreendedores que querem começar a usar IA"
```

Depois rode novamente e compare o resultado.

## Extensão para N8N

O pacote também inclui um fluxo N8N simplificado.

A lógica do N8N é a mesma:

```text
Chat Trigger → Organizar Variáveis → Chamar Gemini → Preparar Saída → Google Sheets → Resposta Final
```

A ideia é mostrar que Python e N8N são formas diferentes de orquestrar a solução, mas o prompt continua sendo o centro da inteligência operacional.
