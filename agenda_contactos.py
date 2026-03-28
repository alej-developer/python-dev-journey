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
    print(f"     Tel      : {contacto['telefono'}}")
    if contacto["email"]:                 # Solo muestra si no está vacío
        print(f"     Email   :  {contacto['email']}")
    print(f"     Grupo  : {contacto['grupo']}")



def main():
    print("=" * 40)
    print("     Agenda de contactos v1")
    print("=" * 40)
    print("   [Fase 1 completada - estructura base]")


if __name__ == "__main__":
    main()

    