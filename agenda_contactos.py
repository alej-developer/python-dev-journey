# =============================================================
# Agenda de contactos
# Día 4 — Funciones avanzadas, commits progresivos
# =============================================================
# ¿Qué aprenderás hoy?
#   - Funciones con *args y **kwargs
#   - Parámetros opcionales con valores por defecto
#   - Buscar y filtrar diccionarios
#   - Ordenar con múltiples criterios
#   - Guardar datos en un archivo .txt simple
# =============================================================

# Base de datos en memoria: lista de diccionarios
# Mañana aprenderemos a persistirla en un archivo real

import email


contactos: list = []


def crear_contacto(nombre: str, telefono: str,
                   email: str = "", grupo: str = "General") -> dict:
    """
    Crea un contacto con campos obligarotiro y opcionales.
    
    emial y grupo tienen valores por defecto - son opcionales.
    Esto se llama 'parametro con valor por defecto' y es muy 
    útil para hacer funciones flexibles sin romper el código existente.
    """
    return {
        "nombre" : nombre.strip().title(),  # .title() -> "alejandro garcia" 
        "telefono" : telefono.strip(),      # capitaliza cada palabra
        "email" : email.strip().lower(),    # .lower() normaliza emails
        "grupo" : grupo.strip().title()
    }

def mostrar_contacto(contacto: dict, indice: int = None) -> None:
    """
    Muestra un contacto formateado.
    indice es opcional - si se pasa, se muestra el número.
    """
    prefijo = f"{indice}. " if indice is not None else "   "
    print(f"\n{prefijo}{contacto['nombre']}")
    print(f"     Tel      : {contacto['telefono']}")
    if contacto["email"]:                 # Solo muestra si no está vacío
        print(f"     Email   :  {contacto['email']}")
    print(f"     Grupo  : {contacto['grupo']}")

def agregar_contacto() -> None:
    """Pide datos al usuario y añade el contenido a la list global."""
    print("\n--- Nuevo Contacto ---")
    nombre = input("Nombre (obligatorio):  ").strip()
    if not nombre:                           # 'not string' es True si está vacío
        print("   El nombre no puede estar vacío.")
        return
    
    telefono = input("Teléfono (obligatorio): ").strip()
    if not telefono: 
        print
        ("   El teléfono no puede estar vacío.")
        return

    email = input("Email (opcional, Enter para saltar): ")
    grupo = input("Grupo (opcional; Enter = General):").strip()
    if not grupo:
        grupo = "General"

    contacto = crear_contacto(nombre, telefono, email, grupo)
    contactos.append(contacto)
    print(f"\n  Contacto '{contacto['nombre']}' añadido.")

def listar_contactos() -> None:
    """Muestra todos los contactos ordenados alfabéticamente."""
    if not contactos:
        print("\n  No hay contactos en la agenda.")
        return
    
    #Ordenamos por nombre antes de mostrar
    ordenados = sorted(contactos, key=lambda c: c["nombre"])

    print(f"\n--- Agenda ({len(contactos)} contactos) ---")
    for i, contacto in enumerate(ordenados, start=1):
        mostrar_contacto(contacto, indice=i)

def buscar_contacto(termino: str) -> list:
    """
    Busca contactos cuyo nombre o email contenga el término.
    
    Usamos list comprenhesion con condición - patrón muy común
    para filtar datos sin necesidad de bucles explícitos.
    
    'termino.lower() in c["nombre"].lower()' hace la búsqueda
    sin importar mayúsculas o minúsculas. 
    """
    termino = termino.lower()
    return [
        c for c in contactos
        if termino in c["nombre"].lower()
        or termino in c["email"].lower()
    ]

def eliminar_contacto() -> None:
    """
    Elimina un contacto por su posición en la lista.

    del lista[indice] elimina el elemento en esa posición.
    Restamos 1 al índice porque el usuario ve números desde 1
    pero Python indexa desde 0.
    """
    listar_contactos()
    if not contactos:
        return

    try:
        numero = int(input("\nNúmero del contacto a eliminar (0 para cancelar): "))
        if numero == 0:
            return
        if 1 <= numero <= len(contactos):
            # Ordenamos igual que en listar para que el índice coincida
            ordenados = sorted(contactos, key=lambda c: c["nombre"])
            eliminado = ordenados[numero - 1]
            contactos.remove(eliminado)     # .remove() busca y elimina el objeto
            print(f"\n  '{eliminado['nombre']}' eliminado.")
        else:
            print("  Número fuera de rango.")
    except ValueError:
        print("  Escribe un número válido.")


def mostrar_por_grupos() -> None:
    """
    Agrupa los contactos por su campo 'grupo' usando un diccionario.

    Construimos un dict donde cada clave es un grupo y su valor
    es una lista de contactos — dict de listas, patrón muy común.
    """
    if not contactos:
        print("\n  No hay contactos.")
        return

    grupos: dict = {}
    for contacto in contactos:
        grupo = contacto["grupo"]
        if grupo not in grupos:
            grupos[grupo] = []          # Creamos la lista si no existe
        grupos[grupo].append(contacto)

    print("\n--- Contactos por grupo ---")
    for grupo, miembros in sorted(grupos.items()):
        print(f"\n  [{grupo}] — {len(miembros)} contacto(s)")
        for c in miembros:
            print(f"    - {c['nombre']} · {c['telefono']}")
        
def main():
    print("=" * 40)
    print("   Agenda de contactos")
    print("=" * 40)

    while True:
        print("\n¿Qué quieres hacer?")
        print("  1. Añadir contacto")
        print("  2. Ver todos")
        print("  3. Buscar")
        print("  4. Ver por grupos")    # ← nueva
        print("  5. Eliminar")          # ← nueva
        print("  6. Salir")             # ← era 4
        opcion = input("\nOpción (1-6): ").strip()

        if opcion == "1":
            agregar_contacto()

        elif opcion == "2":
            listar_contactos()

        elif opcion == "3":
            termino = input("Buscar por nombre o email: ").strip()
            if termino:
                resultados = buscar_contacto(termino)
                if resultados:
                    print(f"\n  {len(resultados)} resultado(s):")
                    for c in resultados:
                        mostrar_contacto(c)
                else:
                    print("  No se encontraron contactos.")

        elif opcion == "4":
            mostrar_por_grupos()

        elif opcion == "5":
            eliminar_contacto()

        elif opcion == "6":
            print("\nHasta luego.")
            break

        else:
            print("  Opción no válida.")


if __name__ == "__main__":
    main()