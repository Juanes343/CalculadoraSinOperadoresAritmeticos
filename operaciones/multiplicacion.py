from .suma import sumar
from .resta import restar

def multiplicar(a, b):
    """
    Realiza la multiplicación sin utilizar el operador '*'.
    """
    if a == 0 or b == 0:
        return 0
    
    negativo = (a < 0) != (b < 0)

    resultado = 0
    while b > 0:
        resultado = sumar(resultado, a)
        b = restar(b, 1)
    
    return resultado if not negativo else restar(0, resultado)