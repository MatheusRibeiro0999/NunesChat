from dotenv import load_dotenv
import os

load_dotenv()  #carrega do dotenv

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama3-70b-8192"


CONTATO_COMERCIAL = os.getenv("CONTATO_COMERCIAL")
CONTATO_FINANCEIRO = os.getenv("CONTATO_FINANCEIRO")
CONTATO_SUPORTE = os.getenv("CONTATO_SUPORTE")