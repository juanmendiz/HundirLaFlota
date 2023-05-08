from functions import *

print("Bienvenido al hundir la flota!")
# opcion = input("Quieres una demo? (S/N)")
# if opcion = "S":
#     jugar demo...
# else:
#     juego completo


tablero_us = crear_tablero(tamaño)
tablero_maq = crear_tablero(tamaño)
tablero_us_maq = crear_tablero(tamaño)


barco_1 = crear_barco_random(2, tamaño)
barco_2 = crear_barco_random(4, tamaño)

lista_barcos = [barco_1, barco_2]

for barco in lista_barcos:
    tablero_maq = colocar_barco_maq(barco, tablero_maq)
    
# vidas = suma de las casillas del barco
# while vidas >0:
# while "O" in tablero...

print(tablero_us)

while vidas > 0:

    fila_disparo = int(input("Qué fila disparas (0-9)?"))
    columna_disparo = int(input("Qué columna disparas (0-9)?"))
    tablero_maq = disparar_us((fila_disparo, columna_disparo), tablero_maq)
    vidas = vidas -1

print(tablero_us_maq)