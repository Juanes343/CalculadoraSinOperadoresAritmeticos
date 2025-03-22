def obtener_entero(mensaje):
    """
    Solicita al usuario un número entero y valida la entrada.
    """
    while True:
        entrada = input(mensaje)
        if entrada.lower() == "salir":
            print("Calculadora finalizada.")
            exit()
        if entrada.lstrip('-').isdigit():
            return int(entrada)
        else:
            print("Error: Solo se permiten números enteros.")