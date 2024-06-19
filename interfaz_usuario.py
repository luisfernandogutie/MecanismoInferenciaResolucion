# interfaz_usuario.py
def obtener_condiciones():
    condiciones = {}
    condiciones["luz_solar"] = input("¿Cuánta luz solar recibe el área? (alta/media/baja): ").strip().lower()
    condiciones["espacio"] = input("¿Qué tan grande es el espacio disponible? (grande/pequeño): ").strip().lower()
    condiciones["mantenimiento"] = input("¿Cuánto mantenimiento estás dispuesto a dar? (alto/medio/bajo): ").strip().lower()
    return condiciones

def mostrar_recomendacion(recomendacion):
    print(f"Recomendación de planta: {recomendacion}")
