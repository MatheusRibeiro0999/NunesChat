from groq import Groq
from config import *
import handlers.suporte as suporte
import handlers.comercial as comercial
import handlers.financeiro as financeiro

client = Groq(api_key=GROQ_API_KEY)

def main():
    print("Bem Vindo(a) a Acertsoft Sistemas de gestão, ")
    print("Digite o canal desejado: ")
    print("1 - Suporte Técnico")
    print("2 - Comercial")
    print("3 - Financeiro")
    
    while True:
        
        escolha = input("Por favor, escolha uma opção (1-3): ")
        
        if escolha == "1":
            suporte.iniciar_atendimento(client)
        elif escolha == "2":
            comercial.atender()
        elif escolha == "3":
            financeiro.atender()
        else:
            print("Opção inválida. Por favor, escolha novamente.")
            print("1 - Suporte Técnico")
            print("2 - Comercial")
            print("3 - Financeiro")
            

if __name__ == "__main__":
    main()