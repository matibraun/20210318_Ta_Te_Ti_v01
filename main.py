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

def checkWinner(board):
    if board[0][0] != ' ' and board[0][0] == board[1][0] and board[0][0] == board[2][0] or board[0][1] != ' ' and board[0][1] == board[1][1] and board[0][1] == board[2][1] or board[0][2] != ' ' and board[0][2] == board[1][2] and board[0][2] == board[2][2] or board[0][0] != ' ' and board[0][0] == board[0][1] and board[0][0] == board[0][2] or board[1][0] != ' ' and board[1][0] == board[1][1] and board[1][0] == board[1][2] or board[2][0] != ' ' and board[2][0] == board[2][1] and board[2][0] == board[2][2] or board[0][0] != ' ' and board[0][0] == board[1][1] and board[0][0] == board[2][2] or board[0][2] != ' ' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return True

def checkBoardFull(board):
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        return True    


def render(state):
    if state['stage'] == 'Welcome':
        print(state['welcomeMessage'])

    if state['stage'] == 'LoadingPlayers':
        print(state['players'])

    if state['stage'] == 'Playing':
        print(state['players'])
        print(state['board'])
        print(f"Es el turno de {state['players'][state['turn']]['name']}")
    
    if state['stage'] == 'FinishedWithWinner':
        print(f"El juego ha terminado. El ganador es {state['players'][state['turn']]['name']}")
        print('El tablero final es')
        print(state['board'])
        print('Los jugadores fueron:')
        print(state['players'])
    
    if state['stage'] == 'FinishedWithoutWinner':
        print("El juego ha terminado sin ningun ganador")
        print('El tablero final es')
        print(state['board'])
        print('Los jugadores fueron:')
        print(state['players'])
    
    if state['stage'] == 'AfterGameOptions':
        print(state['board'])            
    
    if state['stage'] == 'CLOSING_APP':
        print('Gracias por usar la app')
        print(state['players'])
        exit()


    


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

    if state['stage'] == 'AfterGameOptions':
        print(
            '1. Ver el historico de la partida\n'
            '2. Jugar la revancha\n'
            '3. Jugar una nueva partida\n'
            '4. Salir de la aplicacion\n'
        )
        option = input('Elija que desea hacer a continuacion: ')

        while option.isnumeric() == False or int(option) < 1 or int(option) > 4:
            print ('La opcion seleccionada es incorrecta') 
            option = input('Elija que desea hacer a continuacion: ')
        
        if option == '1':
            return {
                'type': 'REVIEW_GAME',
            }
        
        if option == '2':
            return {
                'type': 'REMATCH',
            }

        if option == '3':
            return {
                'type': 'NEW_GAME',
            }

        if option == '4':
            return {
                'type': 'EXIT',
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

    if state['stage'] == 'Playing':
        
        if action['type'] == 'LOAD_PLAY':
            new_board = copy.deepcopy(state['board'])
            new_board[action['payload']['lineNumber']][action['payload']['columnNumber']] = state['players'][state['turn']]['symbol']
            new_turn = (state['turn'] + 1) % len(state['players'])

            if checkBoardFull(new_board) == True:
                return {
                    **state,
                    'stage': 'FinishedWithoutWinner',
                    'board': new_board,
                }

            if checkWinner(new_board) == True:
                return {
                    **state,
                    'stage': 'FinishedWithWinner',
                    'board': new_board,
                }

            return {
                **state,
                'board': new_board,
                'turn': new_turn
            }

    
    if state['stage'] == 'FinishedWithoutWinner' or state['stage'] == 'FinishedWithWinner':
        return {
            **state,
            'stage': 'AfterGameOptions'
        }

    if state['stage'] == 'AfterGameOptions':
        if action['type'] == 'REVIEW_GAME':
            return {
                **state,
            }

        if action['type'] == 'REMATCH':
            return {
                **state,
                'stage': 'Playing',
            }

        if action['type'] == 'NEW_GAME':
            return {
                **state,
                'stage': 'LoadingPlayers',
            }

        if action['type'] == 'EXIT':
            return {
                **state,
                'stage': 'ClosingApp',
            }



state = {
    'stage': 'Welcome',
    'welcomeMessage': 'Bienvenidos al Ta Te Ti de Matule',
}

while True:
    render(state)
    action = get_next_action(state)
    state = reducer(state, action)