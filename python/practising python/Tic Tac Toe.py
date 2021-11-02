import pygame, sys
import numpy as np

# we should intialize pygame by using pygame.init()
pygame.init()

### CONSTANT VALUES ####

# screen dimensions
WIDTH = 600
HEIGHT = 600
BOARD_ROWS = 3
BOARD_COLUMNS = 3

# colors will be in (r , g , b) format
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
LINE_WIDTH = 15

# below statement to display the screen with given WIDTH and HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#displaying window title
pygame.display.set_caption('Tic Tac Toe')

screen.fill(BG_COLOR)

# below np.zeros() function will create new array of given shape. here we kept 3 X 3
board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))
print(board)

# drawing the lines
def drawing_lines():
   # drawing first horizontal line
   pygame.draw.line( screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
   # drawing second horizontal line
   pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
   # drawing first vertical line
   pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
   # drawing second vertical line
   pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

# this function will mark the square in the array
def mark_square(row, col, player):
    board[row][col] = player

# this function checks square is available or not
def availabe_square(row, col):
    #return board[row][col] == 0 this line and below if and else statement will do same operation
    if board[row][col] == 0:
        return True
    else:
        return False

# this function checks if the board is full or not
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0:
                return False
    return True

drawing_lines()

# main loop
# this loop make the screen open until we press the Exit button
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
