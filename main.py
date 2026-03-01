import os
#? pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

## VARIABLES DE ENTORNO
CLAVE = os.getenv("CLAVE")
API_KEY = os.getenv("API_KEY")

## CÓDIGO PRINCIPAL
print("Hola, Academia Ingenio.")
print(CLAVE)
print(API_KEY)

