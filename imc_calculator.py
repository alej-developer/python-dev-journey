#Calculadora de IMC (Índice de Massa Corporal)

def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula el IMC usando la formula estándar OMS

    Args:
        peso (float): Peso en kilogramos
        altura (float): Altura en metros
    Returns:
        El valor del IMC redondeado a 2 decimales
    """

    imc = peso / (altura ** 2)
    return round(imc, 2) 

def clasificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidad"
    
def main():
    print("=" * 40)
    print ("    Calculadora de IMC")
    print("=" * 40)

    peso = float(input("\nIntroduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros (ej; 1.75): "))

    imc = calcular_imc(peso, altura)
    categoria = clasificar_imc(imc)

    print("\n" + "=" * 40)
    print(f"   Tu IMC es: {imc}")
    print(f"   Categoría: {categoria}")
    print("=" * 40)

if __name__ == "__main__":
    main()



