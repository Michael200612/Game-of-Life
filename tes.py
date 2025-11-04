import pygame
from sys import exit
from time import sleep

from_value = '0,0=10,0,255'
to_value = '5,5=255,80,10'

from_pos, from_rgb = from_value.split('=')
from_r, from_g, from_b = [int(y) for y in from_rgb.split(',')]
from_x, from_y = [int(y) for y in from_pos.split(',')]

to_pos, to_rgb = to_value.split('=')
to_r, to_g, to_b = [int(y) for y in to_rgb.split(',')]
to_x, to_y = [int(y) for y in to_pos.split(',')]

x1 = to_x
x2 = from_x

y1 = to_y
y2 = from_y

d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
# d = abs(int(((x2 - x1) + (y2 - y1))))
m = (y2 - y1) / (x2 - x1)

print("Slope: ",m)
print("Distance: ",d)

n = int(d)
colours = []
for colour in [(from_r, to_r), (from_g, to_g), (from_b, to_b)]:
    colour_changes = []
    print(colour)
    r1 = colour[0]
    r2 = colour[1]
    b = (r2 - r1) /(n-1)
    colour_changes.append(r2)
    for i in range(n-2):
        r2 -= b
        colour_changes.append(int(r2))
    colour_changes.append(r1)
    colours.append(colour_changes)

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
x = 0
y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    for i, colour in enumerate(colours[0]):
        print(f'{colours[0][i]}, {colours[1][i]}, {colours[2][i]}')
        # screen.fill((0, 0, 0))
        pixel = pygame.Surface((50,50))
        pixel.fill((colours[0][i], colours[1][i], colours[2][i]))
        screen.blit(pixel, (x,y))
        x += 50
        y += m + (50,0)[m == -0.0]
        pygame.display.update()
        sleep(0.05)
    clock.tick(60)