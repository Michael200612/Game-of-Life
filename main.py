import os
from time import sleep
from random import choice

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def colour_board(board):
    ENDC = '\033[m'
    for row in board:
        list1 = []
        for cell in row:
            if cell == 'd':
                colour =  f'\033[100m'
            elif cell == 'l':
                    colour =  f'\033[107m'
            list1.extend((colour + f" ", ENDC))
        print(*list1)

def get_valid_cells(board, y_axis, x_axis):
    valid_cells = []
    positions = [(0,1), (0,-1), (1,0), (1,1), (1,-1), (-1,-1), (-1,1), (-1,0)]
    for i in positions:
            try:
                _ = board[(IndexError,y_axis + i[0])[y_axis + i[0] > 0]][(IndexError, x_axis + i[1])[x_axis + i[1] > 0]]
                valid_cells.append((y_axis + i[0],x_axis + i[1]))
            except (TypeError, IndexError):
                pass
    return valid_cells

def evaluate(board, cell, y_axis, x_axis):
    live = 0
    dead = 0
    valid_cells = get_valid_cells(board, y_axis, x_axis)
    for cells in valid_cells:
        neighbor = board[cells[0]][cells[1]]
        if neighbor == 'l':
            live += 1
        elif neighbor == 'd':
            dead += 1
    # print(f'Cell: {cell}\nPosition: {y_axis, x_axis}\nLive: {live}\nDead: {dead}\n')
    match cell:
        case 'd':
            if live == 3:
                return (y_axis, x_axis)
        case 'l':
            if live not in [2,3]:
                return (y_axis, x_axis)
    return False

def change_board(board):
    listo = []
    for y_axis, row in enumerate(board):
        for x_axis, cell in enumerate(row):
            result = evaluate(board, cell, y_axis, x_axis)
            if result:
                listo.append((result[0], result[1]))
    for pos in listo:
        match board[pos[0]][pos[1]]:
            case 'd':
                board[pos[0]][pos[1]] = 'l'
            case 'l':
                board[pos[0]][pos[1]] = 'd'
    return board

def make_board(grid, density):
    board = []
    chances = []
    y_axis, x_axis = grid.split('x')
    for i in range(int(y_axis)):
        board.append(['d' for i in range(int(x_axis))])
    for i in range(density):
        chances.append('l')
    for i in range(10-density):
        chances.append('d')
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            board[j][i] = choice(chances)
    return board


def main():
    grid = '150x150'
    density = 2
    auto = True
    delay = 0.1
    grid, density, auto, delay = settings(grid, density, auto, delay)
    print(grid, density, auto, delay)
    board = make_board(grid, density)
    while True:
        clear()
        colour_board(board)
        if not auto:
            input('Press enter to continue\n')
        else:
            sleep(delay)
        change_board(board)

def settings(grid, density, auto, delay):
    while True:
        user_input = input('>> ').lower().strip()
        if user_input.startswith('help'):
            print("""
    setgrid (numberxnumber) -----  change the board size (example: setgrid 15x15)
    setdensity (0-10) ------  set the density of live cells on the board. 0 is 0% live cells ,5 is 50%, 10 is 100% (example: setdensity 4)
    setauto (True/False) -----  choose whether board goes to the next iteration automatically (example: setauto True)                  
    setdelay (0-60) -----  set time in seconds between each iteration when on auto (example: setdelay 0.2)
    return ----- exit settings                       
    """)
        if user_input.startswith('setgrid '):
            grid = user_input.replace('setgrid ', '')
        if user_input.startswith('setdensity'):
            density = int(user_input.replace('setdensity ', ''))
        if user_input.startswith('setauto '):
            auto = (False, True)[user_input.replace('setauto ','') == 'true']
        if user_input.startswith('setdelay '):
            delay = float(user_input.replace('setdelay ', ''))
        if user_input.startswith('return'):
            break

    return grid, density, auto, delay

main()





