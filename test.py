import math
import copy

board = [
    [' ', ' ', ' '],
    [' ', 'X', ' '],
    [' ', ' ', ' '],
]


def getJugada(board):
    jugada = input(
        'Contando horizontalmente indique donde desea poner su ficha: ')
    while jugada.isnumeric() == False or int(jugada) < 1 or int(jugada) > 9:
        print('La jugada ingresada es incorrecta')
        jugada = input(
        'Contando horizontalmente indique donde desea poner su ficha: ')
    fila = math.floor((int(jugada) - 1) / len(board))
    columna = (int(jugada) - 1) % len(board)
    while board[fila][columna] != ' ':
        print('La posicion en la que quiere poner su ficha ya se encuentra ocupada.')
        jugada = input(
        'Contando horizontalmente indique donde desea poner su ficha: ')
        fila = math.floor((int(jugada) - 1) / len(board))
        columna = (int(jugada) - 1) % len(board)

    return (fila, columna)

f, c= getJugada(board)

print(f)
print(c)