
## Librerías.
    #@ Para cargar variables de entorno.
import os
from dotenv import load_dotenv

    #@ Carga del entorno virtual.
load_dotenv()

## Configuración de hardware.
    #@ Velocidad máxima en RPM.
MAX_SPEED_RPM = os.getenv('MAX_SPEED_RPM')
    #@ Rango máximo de giro.
MAX_TURN_RANGE = os.getenv('MAX_TURN_RANGE')

## Muestra de configuración
print(MAX_SPEED_RPM)
print(MAX_TURN_RANGE)

