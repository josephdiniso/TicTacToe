#!/usr/src/env python3

import pygame
from pygame.locals import *
import numpy as np

BLACK = (0,0,0)
WHITE = (255,255,255)

# Board variable to specify where xs and os are
board = np.zeros((3,3))
coords = np.array([[10,10],[176, 10], [343, 10], [10, 176], [176, 176], [343, 176], [10, 343], [176, 343], [343, 343]])
# Pygame initializations
pygame.init()
pygame.mixer.init(22050, -8, 16, 65536 )
pygame.display.set_caption("Tic Tac Toe")
size = (500, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Image loading
x_img = pygame.image.load("./x.png")
x_img = pygame.transform.scale(x_img, (150,150))
o_img = pygame.image.load("./o.png")
o_img = pygame.transform.scale(o_img, (150,150))

def draw_screen():
    for index, val in enumerate(board.flat):
        if val == 1:
            screen.blit(x_img, (coords[index][0], coords[index][1]))
        elif val == 2:
            screen.blit(o_img, (coords[index][0], coords[index][1]))
        

def check_win():
    if (np.all(board[:,0] == board[0,0]) and board[0,0]) or (np.all(board[:,1] == board[0,1]) and board[0,1]) or (np.all(board[:,2] == board[0,2]) and board[0,2]) or (np.all(board[0,:] == board[0,0]) and board[0,0]) or (np.all(board[1,:] == board[1,0]) and board[1,0]) or (np.all(board[2,:] == board[2,0]) and board[2,0]):
        return 1
    elif (board[0,0] == board[1,1] and board[0,0] == board[2,2] and board[0,0]) or (board[0,2] == board[1,1] and board[0,2] == board[2,0] and board[1,1]):
        return 1
    elif np.all(board) != 0:
        return 2
    return 0

def main():
    global board
    done = False
    box_tup = None
    side = 1
    while not done:
        pos = pygame.mouse.get_pos()
        if pos[0] > 0 and pos[0] < 166 and pos[1] > 0 and pos[1] < 166:
            box_tup = (0,0)
        elif pos[0] > 166 and pos[0] < 333 and pos[1] > 0 and pos[1] < 166:
            box_tup = (1,0)
        elif pos[0] > 333 and pos[0] < 500 and pos[1] > 0 and pos[1] < 166:
            box_tup = (2,0)
        elif pos[0] > 0 and pos[0] < 166 and pos[1] > 166 and pos[1] < 333:
            box_tup = (0,1)
        elif pos[0] > 166 and pos[0] < 333 and pos[1] > 166 and pos[1] < 333:
            box_tup = (1,1)
        elif pos[0] > 333 and pos[0] < 500 and pos[1] > 166 and pos[1] < 333:
            box_tup = (2,1)
        elif pos[0] > 0 and pos[0] < 166 and pos[1] > 333 and pos[1] < 500:
            box_tup = (0,2)
        elif pos[0] > 166 and pos[0] < 333 and pos[1] > 333 and pos[1] < 500:
            box_tup = (1,2)
        elif pos[0] > 333 and pos[0] < 500 and pos[1] > 333 and pos[1] < 500:
            box_tup = (2,2)
        else:
            box_tup = (None, None)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP and box_tup[0] != None:
                if not board[box_tup[1], box_tup[0]]:
                    board[box_tup[1], box_tup[0]] = side
                    side = 2 if side == 1 else 1
        clock.tick(30)
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, [size[0]//3, 0, 2, size[1]])
        pygame.draw.rect(screen, BLACK, [size[0]//3*2, 0, 2, size[1]])
        pygame.draw.rect(screen, BLACK, [0, size[1]//3, size[0], 2])
        pygame.draw.rect(screen, BLACK, [0, size[1]//3*2, size[0], 2])
        draw_screen()
        val = check_win()
        if val == 1:
            if side == 1:
                print("O wins")
            else:
                print("X wins")

            board = np.zeros((3,3))
            side = 1
        elif val == 2:
            board = np.zeros((3,3))
            side = 1
            print("Draw")
        pygame.display.flip()
    
if __name__=="__main__":
    main()