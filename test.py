import pygame
from sys import exit
from time import sleep

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

cells = [['l','d','d','l'],
         ['l','d','l','l'],
         ['l','l','l','d'],]

def input_cells(board):
    running = True
    try:
        while running:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            for j, cell in enumerate(cells):
                for i, row in enumerate(cell):
                    box = pygame.Surface((10,10))
                    box_rect = box.get_rect(topleft = (10*i,10*j))
                    if row == 'l':
                        box.fill("White")
                    else:
                        box.fill("Black")
                    screen.blit(box, box_rect)
                    mouse_pos = pygame.mouse.get_pos()
                    screen.blit(box, (10*i,10*j))
                    if box_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                            cells[int(mouse_pos[1]/10)][int(mouse_pos[0]/10)] = ('l','d')[cells[int(mouse_pos[1]/10)][int(mouse_pos[0]/10)] == 'l']
                            sleep(0.1)

            pygame.display.update()
            clock.tick(60)
    except:
        return cells

