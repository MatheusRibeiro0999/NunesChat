from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME, CONTATO_SUPORTE
from utils.logger import logger
import os
from typing import Optional, Tuple


class SuporteHandler:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.base_conhecimento = self._carregar_base_conhecimento()
        self.comandos_saida = ['sair', 'encerrar', 'exit', 'fim', 'voltar']
        self.respostas_saida = [
            "Obrigado por utilizar nosso suporte! Volte sempre.",
            "Atendimento encerrado. Se precisar, estaremos aqui!",
            "Foi um prazer ajudar! Até a próxima."
        ]

    def _carregar_base_conhecimento(self) -> str:#carrega base_suporte
        try:
            with open("base_suporte.txt", "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            logger.log_error(Exception("Arquivo base_suporte.txt não encontrado"))
            return ""

    def _gerar_prompt(self, pergunta: str) -> list:
        return [
            {
                "role": "system",
                "content": f"""
                Você é o Nunes, assistente virtual de suporte técnico.
                Base de conhecimento:
                {self.base_conhecimento}

                Regras:
                1. Responda apenas sobre suporte técnico
                2. Seja conciso (máximo 2 parágrafos)
                3. Para perguntas fora do escopo: "{self._mensagem_generica()}"
                """
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]

    def _mensagem_generica(self) -> str:#msg padrão para perguntas fora do escopo
        return f"Desculpe, não posso ajudar com isso. Entre em contato com nosso suporte: {CONTATO_SUPORTE}"

    def _processar_resposta(self, resposta_api: dict) -> str:#processa a resposta da API
        try:
            return resposta_api.choices[0].message.content
        except (AttributeError, KeyError, IndexError) as e:
            logger.log_error(e)
            return self._mensagem_generica()

    def _verificar_saida(self, input_usuario: str) -> bool:
        return input_usuario.lower() in self.comandos_saida

    def _confirmar_saida(self) -> bool:
        from random import choice
        confirmacao = input(f"\n{choice(['Tem certeza?', 'Deseja mesmo encerrar?', 'Confirmar saída?'])} (s/n): ").strip().lower()
        return confirmacao in ['s', 'sim', 'y', 'yes']

    def gerar_resposta(self, pergunta: str) -> str:
        """
        Gera resposta técnica baseada na base de conhecimento
        
        Args:
            pergunta: Texto da pergunta do usuário
            
        Returns:
            Resposta gerada ou mensagem padrão
        """
        if not pergunta.strip():
            return "Por favor, digite sua dúvida."

        try:
            resposta = self.client.chat.completions.create(
                messages=self._gerar_prompt(pergunta),
                model=MODEL_NAME,
                temperature=0.3
            )
            return self._processar_resposta(resposta)
        except Exception as e:
            logger.log_error(e)
            return self._mensagem_generica()

    def iniciar_atendimento(self):#loop de atendimento 
        logger.logger.info("Início do atendimento de suporte")
        print("\n🔧 Suporte Técnico Nunes (digite 'sair' a qualquer momento)")

        while True:
            try:
                pergunta = input("\n👤 Você: ").strip()
                
                if self._verificar_saida(pergunta):
                    if self._confirmar_saida():
                        from random import choice
                        print(f"\n🤖 Nunes: {choice(self.respostas_saida)}")
                        logger.logger.info("Atendimento encerrado pelo usuário")
                        break
                    print("Continuando atendimento...")
                    continue
                
                resposta = self.gerar_resposta(pergunta)
                logger.log_interaction(pergunta, resposta)
                print(f"\n🤖 Nunes: {resposta}")
                
            except KeyboardInterrupt:
                print("\nAtendimento interrompido.")
                logger.logger.warning("Atendimento interrompido pelo usuário (Ctrl+C)")
                break
            except Exception as e:
                logger.log_error(e)
                print("\n⚠️ Ocorreu um erro. Reiniciando atendimento...")
                continue


# Interface pública do módulo
def iniciar_atendimento(client=None):  
    handler = SuporteHandler()
    handler.iniciar_atendimento()