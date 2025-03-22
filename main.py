from operaciones.suma import sumar
from operaciones.resta import restar
from operaciones.multiplicacion import multiplicar
from operaciones.division import dividir
from validaciones.entrada import obtener_entero

def obtener_operacion():
    """
    Solicita al usuario una operación válida y la devuelve.
    """
    operaciones_validas = {"1", "2", "3", "4", "5"}
    
    while True:
        operacion = input("Seleccione la operación (1.suma, 2.resta, 3.multiplicacion, 4.division o 5 para finalizar): ").lower()
        if operacion in operaciones_validas:
            if operacion == "5":
                print("Calculadora finalizada.")
                exit()
            return operacion
        else:
            print("Error: Operación no válida.")

def iniciar_calculadora():
    """
    Inicia la calculadora interactiva.
    """
    while True:
        print("\nBienvenido a la Calculadora sin Operadores")

        operacion = obtener_operacion()
        num1 = obtener_entero("Ingrese el primer número: ")
        num2 = obtener_entero("Ingrese el segundo número: ")

        if operacion == "1":
            resultado = sumar(num1, num2)
        elif operacion == "2":
            resultado = restar(num1, num2)
        elif operacion == "3":
            resultado = multiplicar(num1, num2)
        elif operacion == "4":
            resultado = dividir(num1, num2)

        print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    iniciar_calculadora()