# =============================================================
# Registro de pacientes con IMC
# Día 3 — Listas, diccionarios y bucles
# =============================================================
# ¿Qué aprenderás hoy?
#   - list: colección ordenada, acceso por índice
#   - dict: colección clave-valor, acceso por nombre
#   - for: recorrer colecciones
#   - Métodos útiles: append(), items(), sorted()
#   - List comprehension: forma pythónica de filtrar listas
# =============================================================


def pedir_numero(mensaje: str, minimo: float = 0.0) -> float:
    """Reutilizamos la función del Día 2 sin cambios."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= minimo:
                print(f"  El valor debe ser mayor que {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Escribe solo números, ej: 70 o 1.75")


def calcular_imc(peso: float, altura: float) -> float:
    """Reutilizamos la función del Día 1 sin cambios."""
    return round(peso / (altura ** 2), 2)


def clasificar_imc(imc: float) -> str:
    """Devuelve solo la categoría como string."""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidad"


def crear_paciente(nombre: str, peso: float, altura: float) -> dict:
    """
    Crea y devuelve un diccionario representando un paciente.

    Un diccionario agrupa datos relacionados bajo un mismo nombre.
    Cada par clave:valor describe una propiedad del paciente.
    Es el equivalente simple a lo que luego será un objeto o una fila en BD.
    """
    imc = calcular_imc(peso, altura)
    return {
        "nombre"   : nombre,
        "peso"     : peso,
        "altura"   : altura,
        "imc"      : imc,
        "categoria": clasificar_imc(imc)
    }


def mostrar_paciente(paciente: dict) -> None:
    """
    Recorre el diccionario con .items() y muestra cada par clave:valor.

    .items() devuelve pares (clave, valor) que desempaquetamos
    directamente en el for — igual que hicimos con la tupla el Día 2.
    """
    print("\n" + "-" * 35)
    for clave, valor in paciente.items():
        print(f"  {clave:<12}: {valor}")
        # {clave:<12} alinea el texto a la izquierda en 12 caracteres
        # Eso hace que los valores queden en columna — más legible


def mostrar_resumen(pacientes: list) -> None:
    """
    Recibe una lista de diccionarios y muestra estadísticas.

    Aquí combinamos lista + diccionario + bucle for.
    Esto es el patrón más común en APIs y bases de datos reales.
    """
    if not pacientes:           # 'not lista' es True cuando la lista está vacía
        print("No hay pacientes registrados.")
        return

    total = len(pacientes)      # len() cuenta elementos de cualquier colección

    # List comprehension: forma compacta de crear una lista a partir de otra
    # Equivale a: for p in pacientes: imcs.append(p["imc"])
    imcs = [p["imc"] for p in pacientes]

    promedio = round(sum(imcs) / total, 2)
    maximo   = max(imcs)
    minimo   = min(imcs)

    # sorted() devuelve una nueva lista ordenada sin modificar la original
    # key= indica por qué campo ordenar; reverse=True = descendente
    ordenados = sorted(pacientes, key=lambda p: p["imc"], reverse=True)

    print("\n" + "=" * 35)
    print("  RESUMEN DE PACIENTES")
    print("=" * 35)
    print(f"  Total registrados : {total}")
    print(f"  IMC promedio      : {promedio}")
    print(f"  IMC más alto      : {maximo}")
    print(f"  IMC más bajo      : {minimo}")
    print("\n  Ranking por IMC:")
    for i, p in enumerate(ordenados, start=1):
        # enumerate() añade un contador automático al bucle
        print(f"  {i}. {p['nombre']:<12} — {p['imc']} ({p['categoria']})")


def main():
    pacientes = []              # Lista vacía: aquí guardaremos los diccionarios

    print("=" * 35)
    print("  Registro de pacientes")
    print("=" * 35)

    while True:
        print("\n¿Qué quieres hacer?")
        print("  1. Añadir paciente")
        print("  2. Ver resumen")
        print("  3. Salir")

        opcion = input("\nElige una opción (1/2/3): ").strip()
        # .strip() elimina espacios en blanco al inicio y al final

        if opcion == "1":
            nombre = input("Nombre del paciente: ").strip()
            peso   = pedir_numero("Peso en kg: ")
            altura = pedir_numero("Altura en metros: ", minimo=0.5)

            paciente = crear_paciente(nombre, peso, altura)
            pacientes.append(paciente)      # append() añade al final de la lista
            mostrar_paciente(paciente)
            print(f"\n  Paciente añadido. Total: {len(pacientes)}")

        elif opcion == "2":
            mostrar_resumen(pacientes)

        elif opcion == "3":
            print("\nHasta luego.")
            break                           # break sale del bucle while

        else:
            print("  Opción no válida. Elige 1, 2 o 3.")


if __name__ == "__main__":
    main()
