from .resta import restar
from .suma import sumar

def dividir(a, b):
    """
    Realiza la división sin utilizar el operador '/'.
    """
    if b == 0:
        return "Error: división por cero"
    
    negativo = (a < 0) != (b < 0)
    
    cociente = 0
    while a >= b:
        a = restar(a, b)
        cociente = sumar(cociente, 1)

    return cociente if not negativo else restar(0, cociente)