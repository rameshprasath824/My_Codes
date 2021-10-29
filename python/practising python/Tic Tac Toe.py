import pygame, sys

# we should intialize pygame by using pygame.init()
pygame.init()

# screen dimensions
WIDTH = 600
HEIGHT = 600

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

drawing_lines()

# main loop
# this loop make the screen open until we press the Exit button
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
