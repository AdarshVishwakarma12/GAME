import pygame

INITIAL_x, INITIAL_y = (75, 1)
PIECE_x, PEICE_y = (106, 81)

def draw_(WIN, enviornment, BOARD, draw = False):
    WIN.fill((100, 255, 100)); WIN.blit(BOARD, (150//2, 0))
    for i in enviornment.instance:
        if i.pos[0] != None: WIN.blit(i.image, denormalize_mouse(i.pos[0], i.pos[1]))
    pygame.display.update()
def normalize_mouse(x:int, y:int): return ((x-INITIAL_x)//PIECE_x, (y-INITIAL_y)//PEICE_y)
def denormalize_mouse(x:int, y:int): return (INITIAL_x + (PIECE_x * x) + x//2, INITIAL_y + (PEICE_y * y) + y//3)