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
        
def main():
    print("=" * 40)
    print("   Agenda de contactos")
    print("=" * 40)

    while True:
        print("\n¿Qué quieres hacer?")
        print("  1. Añadir contacto")
        print("  2. Ver todos")
        print("  3. Buscar")
        print("  4. Salir")

        opcion = input("\nOpción (1-4): ").strip()

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
            print("\nHasta luego.")
            break

        else:
            print("  Opción no válida.")


if __name__ == "__main__":
    main()