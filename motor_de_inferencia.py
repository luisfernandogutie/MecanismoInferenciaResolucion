# motor_de_inferencia.py
from base_de_conocimiento import base_de_conocimiento

def recomendar_planta(condiciones):
    for regla in base_de_conocimiento:
        if all(condiciones.get(condicion, None) == valor for condicion, valor in regla["si"].items()):
            return regla["entonces"]
    return "No se pudo hacer una recomendación"
