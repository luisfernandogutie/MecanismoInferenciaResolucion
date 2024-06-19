# main.py
from interfaz_usuario import obtener_condiciones, mostrar_recomendacion
from motor_de_inferencia import recomendar_planta

def main():
    condiciones = obtener_condiciones()
    recomendacion = recomendar_planta(condiciones)
    mostrar_recomendacion(recomendacion)

if __name__ == "__main__":
    main()
