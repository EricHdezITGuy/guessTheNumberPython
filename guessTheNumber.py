# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random


def adivina_el_numero(x):

    print("=============================")
    print(" Bienvenido(a) al juego!")
    print("=============================")
    print("Tu meta es adivinar el numero generado por la computadora")

    numero_aleatorio = random.randint(1, x) #Numero aleatorio entre 1 y X.

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) #Estoy usando un F-string

        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este numero es muy pequeno")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este numero es muy grande")

    print(f"Felicitaciones! Adivinaste el numero {numero_aleatorio} correctamente") #Estoy usando un F-string


adivina_el_numero(10)