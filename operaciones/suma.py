def sumar(a, b):
    """
    Realiza la suma de dos números sin utilizar el operador '+'.
    """
    while b != 0:
        a += 1
        b -= 1
    return a