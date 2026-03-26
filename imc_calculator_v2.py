# =============================================================
# Calculadora de IMC v2 — Con manejo de errores
# Día 2 - Nuevo concepto: try / except / else / finally
# =============================================================
# ¿Qué mejora hoy?
#   - try/except: captura errores sin que el programa explote
#   - ValueError: el error específico cuando float() recibe texto
#   - Bucle while: repite la pregunta hasta obtener un dato válido
#   - Función reutilizable: pedir_numero() — patrón muy usado en apps reales
# =============================================================

def pedir_numero(mensaje: str, minimo: float = 0.0) -> float: 
    """
    Pide un número al usuario y repite hasta que sea válido.

    Este patrón — bucle + try/except — es uno de los más usados
    en cualquier aplicación real que reciba input del usuario.

    Args:
        mensaje: texto que se muestra al usuario
        minimo:  valor mínimo aceptado (por defecto 0)
    Returns:
        Un float válido y mayor que el mínimo
    """
    while True:                #Bucle infinito: sale solo con 'return'
        try: 
            valor = float(input(mensaje)) # Puede lanzar ValueError 
            if valor <= minimo: 
                print(f"   El valor debe ser mayor que {minimo}. Intenta de nuevo.")
                continue        # 'continue' salta al inicio del while
            return valor        # Si llegamos aquí, el dato es valido
        
        except ValueError:      
            # ValueError ocurre cuando float() recibe algo que no es número
            # Ej: float("hola") → ValueError: could not convert string to float
            print("  Eso no parece un número. Escribe solo dígitos, ej: 70 o 1.75")


def calcular_imc(peso: float, altura: float) -> float:
    """Misma función del Día 1 — no la tocamos, sigue funcionando igual."""
    return round(peso / (altura ** 2), 2)

1
def clasificar_imc(imc: float) -> tuple[str, str]:
    """
    Ahora devuelve una tupla: (categoría, consejo).

    Una tupla es una colección ordenada e inmutable.
    Perfecta para devolver dos valores relacionados desde una función.
    """

    if imc < 18.5: 
        return "Bajo peso", "Considera consultar con un nutricionista."
    elif imc < 25.0:
        return "Peso normal", "¡Sigue así, estás en un rango saludable!"
    elif imc < 30.0: 
        return "Sobrepeso", "Una dieta equilibrada y ejercicio pueden ayudar"
    else: 
        return "Obesidad", "Te recomendamos consultar con un médico."


def main():
    print("=" * 45)
    print("   Calculadora de IMC v2")
    print("=" * 45)

    try:
        # Ahora usamos nuestra función segura en vez de input() directo
        peso   = pedir_numero("\nIntroduce tu peso en kg: ")
        altura = pedir_numero("Introduce tu altura en metros (ej: 1.75): ", minimo=0.5)

        imc = calcular_imc(peso, altura)
        categoria, consejo = clasificar_imc(imc)   # Desempaquetamos la tupla

    except KeyboardInterrupt:
        # Esto captura cuando el usuario pulsa Ctrl+C para salir
        print("\n\nPrograma interrumpido. ¡Hasta luego!")
        return
    
    else:
        # Este bloque SOLO se ejecuta si no hubo ninguna excepción en el try
        print("\n" + "=" * 45)
        print(f"  Tu IMC es    : {imc}")
        print(f"  Categoría    : {categoria}")
        print(f"  Consejo      : {consejo}")
        print("=" * 45)

    finally:
        # Este bloque se ejecuta SIEMPRE, con error o sin él
        # Útil para cerrar ficheros, conexiones a base de datos, etc.
        print("\nGracias por usar la calculadora.")


if __name__ == "__main__":
    main()
