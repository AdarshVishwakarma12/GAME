import pygame
import os

from env import *
from gameLogic import *
from displayModule import *

WIN = pygame.display.set_mode((650+200+150, 650))
enviornment.reset()
BOARD = pygame.transform.scale(pygame.image.load('images/Chessboard480.svg.png'), (850, 650))

FPS = 5
draw_(WIN, enviornment, BOARD)
run_ = True
clock = pygame.time.Clock()
agent_run_black = False

def s_conv_(): global agent_run_black; agent_run_black = (False if agent_run_black is True else True)

while run_:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); run_ = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                cd_x, cd_y = pygame.mouse.get_pos()
                cd_x, cd_y = normalize_mouse(cd_x, cd_y)
                inst_11 = state_1(cd_x, cd_y, agent_run_black)
                if inst_11 != None:
                    print(cd_x, cd_y, end = ' - ')
                    if agent_run_black is False:
                        friend, enemy = agent_white.valid_moves(inst_11)
                    elif agent_run_black is True:
                        friend, enemy = agent_black.valid_moves(inst_11)
                    cd_x, cd_y = denormalize_mouse(cd_x, cd_y)
                    
                    pygame.draw.rect(WIN, (0, 0, 255), (cd_x, cd_y, PIECE_x, PEICE_y), 3)
                    cool, hot = list(), list()
                    for i in friend:
                        for j in i:
                            if j == []: continue
                            cool.append(j.copy())
                            j[0], j[1] = denormalize_mouse(j[0], j[1])
                            pygame.draw.rect(WIN, (255, 55, 255), (j[0], j[1], PIECE_x, PEICE_y), 3)
                    for i in enemy:
                        if i == []: continue
                        hot.append(i.copy())
                        i[0], i[1] = denormalize_mouse(i[0], i[1])
                        pygame.draw.rect(WIN, (255, 0, 0), (i[0], i[1], PIECE_x, PEICE_y), 3)
                    pygame.display.update()
                    run1_ = True
                    while run1_:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit(); run1_ = False
                            elif event.type == pygame.MOUSEBUTTONUP:
                                if event.button == 1:
                                    cd_x, cd_y = pygame.mouse.get_pos()
                                    cd_x, cd_y = normalize_mouse(cd_x, cd_y)
                                    state_click = state_2(cd_x, cd_y, cool, hot, agent_run_black)
                                    if state_click is None: draw_(WIN, enviornment, BOARD); run1_ = False
                                    else: s_conv_(); inst_11.pos = [cd_x, cd_y]; draw_(WIN, enviornment, BOARD); run1_ = False
                    
                else:
                    draw_(WIN, enviornment, BOARD)