
numero1 : float
numero2 : float
resultado : float

def sumar(numero1: float, numero2: float) -> float:
    
    resultado = numero1 + numero2
    return resultado

def restar(numero1: float, numero2: float) -> float:
    resultado = numero1 - numero2
    return resultado

def multiplicar(numero1: float, numero2: float) -> float:
    resultado = numero1 * numero2
    return resultado

def dividir(numero1: float, numero2: float) -> float:
    if numero2 == 0:
        raise ValueError("No se puede dividir entre cero")
    resultado = numero1 / numero2
    return resultado