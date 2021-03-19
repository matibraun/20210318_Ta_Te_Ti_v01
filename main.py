import math
import copy

def newPlayer():
    name = input('Por favor ingrese el nombre del jugador: ')
    symbol = input('Por favor ingrese una sola letra o numero para el simbolo con el que va a jugar: ')
    while len(symbol) > 1:
        print('El ingreso es incorrecto.')
        symbol = input('Por favor ingrese una sola letra o numero para el simbolo con el que va a jugar: ')
    return {
        'name': name,
        'symbol': symbol,
    }

def getPlay(board):
    play = input(
        'Contando horizontalmente indique donde desea poner su ficha: ')
    while play.isnumeric() == False or int(play) < 1 or int(play) > 9:
        print('La jugada ingresada es incorrecta')
        play = input(
        'Contando horizontalmente indique donde desea poner su ficha: ')
    lineNumber = math.floor((int(play) - 1) / len(board))
    columnNumber = (int(play) - 1) % len(board)
    while board[lineNumber][columnNumber] != ' ':
        print('La posicion en la que quiere poner su ficha ya se encuentra ocupada.')
        play = input(
        'Contando horizontalmente indique donde desea poner su ficha: ')
        lineNumber = math.floor((int(play) - 1) / len(board))
        columnNumber = (int(play) - 1) % len(board)

    return (lineNumber, columnNumber)
    

def render(state):
    if state['stage'] == 'Welcome':
        print(state['welcomeMessage'])

    if state['stage'] == 'LoadingPlayers':
        print(state['players'])

    if state['stage'] == 'Playing':
        print(state['players'])
        print(state['board'])
    


def get_next_action(state):
    if state['stage'] == 'Welcome':
        return {
            'type': 'FINISH_WELCOME_STAGE'
        }
    
    if state['stage'] == 'LoadingPlayers':
        if len(state['players']) < 2:
            player = newPlayer()
            return {
                'type': 'LOAD_PLAYER',
                'payload': player,
            }
        
        else:
            return {
                'type': 'FINISHED_LOADING_PLAYERS'
            }
    

    if state['stage'] == 'Playing':
        lineNumber, columnNumber = getPlay(state['board'])
        return {
            'type': 'LOAD_PLAY',
            'payload': {
                'lineNumber': lineNumber,
                'columnNumber': columnNumber,
            }
            
        }


        



def reducer(state, action):
    if state['stage'] == 'Welcome':
        if action['type'] == 'FINISH_WELCOME_STAGE':
            return {
                'stage': 'LoadingPlayers',
                'players': []
            }
    
    if state['stage'] == 'LoadingPlayers':
        if action['type'] == 'LOAD_PLAYER':
            return {
                **state,
                'players': [*state['players'], action['payload']]
            }

        if action['type'] == 'FINISHED_LOADING_PLAYERS':
            return {
                **state,
                'stage': 'Playing',
                'board': [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
                'turn': 0,
            }
        
        if action['type'] == 'LOAD_PLAY':
            new_board = copy.deepcopy(state['board'])
            new_board[action['payload']['lineNumber']][action['payload']['columnNumber']] = state['players'][state['turn']]['symbol']
            new_turn = state['turn']
            return {
                **state,
                'board': new_board,
                'turn': new_turn
            }


state = {
    'stage': 'Welcome',
    'welcomeMessage': 'Bienvenidos al Ta Te Ti de Matule',
}

while True:
    render(state)
    action = get_next_action(state)
    state = reducer(state, action)