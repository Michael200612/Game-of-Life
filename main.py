import os
from time import sleep
from random import choice
import pygame
from sys import exit
from time import sleep

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


def input_cells(board, pixel_size, grid):
    cells = board
    pygame.init()
    screen = pygame.display.set_mode((
        int(grid.split('x')[0]) * pixel_size,
        int(grid.split('x')[1]) * pixel_size
    ))
    clock = pygame.time.Clock()
    running = True
    try:
        while running:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            for j, cell in enumerate(cells):
                for i, row in enumerate(cell):
                    box = pygame.Surface((pixel_size, pixel_size))
                    box_rect = box.get_rect(topleft=(pixel_size * i, pixel_size * j))
                    if row == 'l':
                        box.fill("White")
                    else:
                        box.fill("Black")
                    screen.blit(box, box_rect)
                    mouse_pos = pygame.mouse.get_pos()
                    screen.blit(box, (pixel_size * i, pixel_size * j))
                    if box_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                        cells[int(mouse_pos[1] / pixel_size)][int(mouse_pos[0] / pixel_size)] = ('l', 'd')[cells[int(mouse_pos[1] / pixel_size)][int(mouse_pos[0] / pixel_size)] == 'l']
                        sleep(0.1)
            pygame.display.update()
            clock.tick(60)
    except:
        return cells

def main():
    pixel_size = 5
    grid = '150x150'
    density = 2
    auto = True
    delay = 0
    grid, density, auto, delay, pixel_size = settings(grid, density, auto, delay, pixel_size)
    print(grid, density, auto, delay, pixel_size)
    board = make_board(grid, density)
    board = input_cells(board, pixel_size, grid)
    screen = pygame.display.set_mode((
        int(grid.split('x')[0]) * pixel_size,
        int(grid.split('x')[1]) * pixel_size
                                      ))
    pygame.display.set_caption('Game of Life')
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        cell = pygame.Surface((pixel_size, pixel_size))
        for j, row in enumerate(board):
            for i, status in enumerate(row):
                if status == 'l':
                    cell.fill('White')
                else:
                    cell.fill('Black')
                screen.blit(cell, (i * pixel_size, j * pixel_size))
        pygame.display.update()
        clock.tick(60)
        if not auto:
            input('Press enter to continue\n')
        else:
            sleep(delay)
        change_board(board)

def settings(grid, density, auto, delay, pixel_size):
    while True:
        user_input = input('>> ').lower().strip()
        if user_input.startswith('help'):
            print("""
    setgrid (numberxnumber) -----  change the board size (example: setgrid 15x15)
    setdensity (0-10) ------  set the density of live cells on the board. 0 is 0% live cells ,5 is 50%, 10 is 100% (example: setdensity 4)
    setauto (True/False) -----  choose whether board goes to the next iteration automatically (example: setauto True)                  
    setdelay (0-60) -----  set time in seconds between each iteration when on auto (example: setdelay 0.2)
    setpixel (1-100) ----- set pixel size. 10 is recommended if you plan to manually input cells. (example: setpixel 5)
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
        if user_input.startswith('setpixel'):
            pixel_size = int(user_input.replace('setpixel ', ''))


    return grid, density, auto, delay, pixel_size

main()





