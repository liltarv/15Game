class Draw:
    def __init__(self, globals):
        self.screen = self.initScreen(globals)

    #draws the current game grid on the screen
    def drawGrid(self, gameState, globals):
        import pygame
        # Fill background with black
        self.screen.fill((0, 0, 0))
        
        # Calculate tile dimensions
        tile_width = globals.DIMX // globals.COLS
        tile_height = globals.DIMY // globals.ROWS
        
        # Draw grid tiles
        for i in range(globals.ROWS):
            for j in range(globals.COLS):
                x = j * tile_width
                y = i * tile_height
                
                # Get the value at this position
                index = i * globals.COLS + j
                value = gameState.gridList[index] if index < len(gameState.gridList) else 0
                
                # Draw tile background
                if value == 0:
                    # Empty tile - draw with darker color
                    pygame.draw.rect(self.screen, (50, 50, 50), (x, y, tile_width, tile_height))
                else:
                    # Number tile - draw with light color
                    pygame.draw.rect(self.screen, (200, 200, 200), (x, y, tile_width, tile_height))
                
                # Draw tile border
                pygame.draw.rect(self.screen, (255, 255, 255), (x, y, tile_width, tile_height), 2)
                
                # Draw number if not empty
                if value != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(value), True, (0, 0, 0))
                    text_rect = text.get_rect(center=(x + tile_width // 2, y + tile_height // 2))
                    self.screen.blit(text, text_rect)

    #initializes the pygame screen
    def initScreen(self, globals):
        import pygame
        screen = pygame.display.set_mode((globals.DIMX, globals.DIMY))
        pygame.display.set_caption("15 Puzzle Game")
        return screen



    