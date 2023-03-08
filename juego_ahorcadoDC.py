# #Pasos
# 1.funcion para extraer la data y elegir una palabra aleatoria
# 2.funcion para mostrar la longitud de la palabra elegida, y mostrar el numero de lineas de acuerdo al numero de letras de la palabra aleatoria
# 3.funcion para pedir la letra y compararla con cada letra de la palabra aleatoria, 
# 4. funcion actualizar_tablero: si la letra esta en la palabra aleatoria reemplazar la letra en el tablero y pedir otra letra, si la letra no esta en el tablero mostrar un mensaje de "la letra no esta en el tablero"
# 5.si la palabra aleatoria es igual al tablero mostrar un mensaje de "ganaste la partida"

import random
import os


def palabra_aleatoria():
    palabras = []
  
    with open("archivos/data.txt", "r",encoding = "utf-8") as f:
    # with open("venv/archivos/data.txt", "r",encoding = "utf-8") as f:
        palabras = [c for c in f]
    global aleatoria   # Esta global me permite usar la variable en cualquier parte
    aleatoria = random.choice(palabras)
    aleatoria = aleatoria.rstrip('\n,')
    # aleatoria = "sol"
    longitud_aleatoria = len(aleatoria)
    # print(longitud_aleatoria)
    global tablero
    tablero = longitud_aleatoria*["-"]
    print("tablero es:",tablero)
    global letras_incorrectas
    letras_incorrectas = []
    global intentos
    try:
        intentos = int(input("Escriba el numero de intentos para jugar: "))
    except ValueError:  
        print("Debes ingresar un numero")
        intentos = int(input("Escriba el numero de intentos para jugar: "))
    return aleatoria, tablero, intentos, []

def pedir_letra():
    global letra
    palabra_completa = " ".join(tablero)

    while palabra_completa != aleatoria:
        print("palabra completa: ", palabra_completa)
        
        letra = input("Ingrese una letra:")
        if letra.isalpha() == False:
            print("Debes ingresar una letra, no otro caracter")
            letra = str(input("Ingrese una letra:"))
        else:
            os.system ("clear")
        procesar_letra(letra,aleatoria)
        actualizar_tablero(aleatoria, tablero, letra,letras_incorrectas)
        print("Tu Palabra", tablero)
        print("Tus letras falladas \n", letras_incorrectas)
        palabra_completa = "".join(tablero)
        
    fin_juego()
    return letra

def procesar_letra(letra,aleatoria):
    if letra in aleatoria:
        print("la letra existe")
        print("Te quedan, ", intentos, "intentos")
        actualizar_tablero(aleatoria, tablero, letra, letras_incorrectas)
    else:
        print('¡Oh! Has fallado.')
        numero_intentos()
        actualizar_tablero(aleatoria, tablero,letra, letras_incorrectas)
        letras_incorrectas.append(letra)
        


def actualizar_tablero(aleatoria, tablero, letra,letras_incorrectas): 
        for indice, letra_palabra in enumerate(aleatoria):
            if letra == letra_palabra:
                tablero[indice] = letra
        # indice = 0
        # tablero[indice] = [indice for letra_palabra in enumerate(aleatoria) if letra == letra_palabra]
                
def numero_intentos():
    global intentos
    intentos = intentos - 1
    if intentos == 0:
        print("PERDISTE, EL JUEGO HA TERMINADO")
        print(tablero)
        print("La palabra era:", aleatoria )
        exit()
    else:
        print("Te quedan, ", intentos, "intentos")
        
def fin_juego():
    print("FELICIDADES GANASTE EL JUEGO")
    print("La palabra era:", aleatoria )
    exit()


def run():
    palabra_aleatoria()
    pedir_letra()


if __name__ == '__main__':
    run()