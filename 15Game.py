import pygame
import GameState
import Globals
import Draw
from pygame import draw, display

# Initialize pygame
pygame.init()

globals = Globals.Globals(400, 400, 4, 4)
model = GameState.GameState([])
model.make_base_gridList(globals.ROWS, globals.COLS)

# Initialize the screen
drawer = Draw.Draw(globals)

# Game clock for FPS control
clock = pygame.time.Clock()
FPS = 60

#to be run when a key is pressed
#when the arrow keys are pressed, the piece adjacent to the empty space in the opposite direction should move into the empty space
def key_handler(event):
    global model
    
    # Map pygame keys to directions and their piece offsets
    key_to_direction_offset = {
        pygame.K_UP: (GameState.GameState.Direction.UP, -globals.COLS),
        pygame.K_DOWN: (GameState.GameState.Direction.DOWN, globals.COLS),
        pygame.K_LEFT: (GameState.GameState.Direction.LEFT, -1),
        pygame.K_RIGHT: (GameState.GameState.Direction.RIGHT, 1),
    }
    
    if event.key in key_to_direction_offset:
        direction, offset = key_to_direction_offset[event.key]
        legal_moves = model.get_legal_moves(globals)
        
        if direction in legal_moves:
            empty_index = model.gridList.index(0)
            piece_index = empty_index + offset
            model.move(piece_index, direction, globals)


#update display
running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # ✅ handles close button
            running = False
        elif event.type == pygame.KEYDOWN:
            key_handler(event)
    
    # Draw the grid
    drawer.drawGrid(model, globals)
    display.flip()
    
    # Check if game is won
    if model.game_over():
        print("You won!")
        running = False

pygame.quit()