# Nunes - ACERTSOFT SISTEMAS

Chatbot de suporte técnico desenvolvido para atendimento automatizado, utilizando Llama3 da Groq.

## Funcionalidades

- Triagem inicial (Suporte, Comercial ou Financeiro)
- Respostas baseadas em base de conhecimento
- Encaminhamento para setores específicos quando necessário
- Controle de escopo para evitar desvios do propósito

## Configuração
1. Crie um ambiente virtual:
    python -m venv venv

2. instale as dependências:
    pip install -r requirements.txt

3. adicione a base de conhecimento:
    edite o arquivo base_suporte.txt com perguntas e respostas no formato
    p. pergunta aqui?
    r. resposta aqui.

4. inicie o bot:
    python app.py