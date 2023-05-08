import numpy as np
import random

tamaño = 10

def crear_tablero(tamaño):
    return np.full((tamaño,tamaño), " ")

def colocar_barco_us(barco, tablero_us):
    for casilla in barco:
        tablero_us[casilla] = "O"
    return tablero_us

def colocar_barco_maq(barco, tablero_maq):
    for casilla in barco:
        tablero_maq[casilla] = "O"
    return tablero_maq

def disparar_us(casilla, tablero_maq,tablero_us_maq):
    if tablero_maq[casilla] == "O":
        tablero_maq[casilla] = "X"
        tablero_us_maq[casilla] = "X"
        print("Tocado")
    else:
        tablero_maq[casilla] = "W"
        tablero_us_maq[casilla] = "W"
        print("Agua")
    return tablero_maq & tablero_us_maq

def disparar_maq(casilla, tablero_us):
    if tablero_us[casilla] == "O":
        tablero_us[casilla] = "X"
        print("Tocado")
    else:
        tablero_us[casilla] = "-"
        print("Agua")
    return tablero_us

def crear_barco_random(eslora, tamaño):
    barco_random = []
    fila_random = random.randint(0,tamaño)
    columna_random = random.randint(0,tamaño)
    barco_random.append((fila_random,columna_random))
    orient = random.choice(["N","S","E","O"])

    while len(barco_random) < eslora:
        if orient == "O":
            columna_random = columna_random - 1 
        elif orient == "E":
            columna_random = columna_random + 1
        elif orient == "N":
            fila_random = fila_random - 1
        elif orient == "S":
            fila_random = fila_random + 1

        if fila_random not in range(tamaño) or columna_random not in range(tamaño):
            fila_random = random.randint(0,tamaño)
            columna_random = random.randint(0,tamaño)
            barco_random = []
            barco_random.append((fila_random,columna_random))
        else:
            barco_random.append((fila_random,columna_random))

        # print(barco_random)
    return barco_random