import os
#? pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

## VARIABLES DE ENTORNO
CLAVE = os.getenv("CLAVE")
API_KEY = os.getenv("API_KEY")

## CÓDIGO PRINCIPAL
print("Hola, mundo.")
print("Hasta luego.")
print(CLAVE)
print(API_KEY)

