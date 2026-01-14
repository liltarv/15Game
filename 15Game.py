import pygame
import GameState
import Globals
from pygame import draw, display

globals = Globals.Globals(400, 400, 4, 4)
model = GameState.GameState([])
model.make_base_gridList(globals.ROWS, globals.COLS)

#to be run when a key is pressed
#when the arrow keys are pressed, the piece adjacent to the empty space in the opposite direction should move into the empty space
def key_handler(event):
    pass


#update display
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # ✅ handles close button
            running = False

pygame.quit()