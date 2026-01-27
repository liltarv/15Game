class Draw:
    def __init__(self, globals):
        self.screen = self.initScreen(globals)
        # Define color constants
        self.BG_COLOR = (30, 30, 50)
        self.EMPTY_TILE_COLOR = (50, 50, 70)
        self.CORRECT_TILE_COLOR = (76, 175, 80)
        self.INCORRECT_TILE_COLOR = (100, 150, 200)
        self.BORDER_COLOR = (200, 200, 220)
        self.TEXT_COLOR = (255, 255, 255)
        self.TILE_SPACING = 8  # pixels between tiles

    def calculate_tile_dimensions(self, globals):
        """Calculate tile width and height accounting for spacing"""
        spacing = self.TILE_SPACING
        tile_width = (globals.DIMX - (spacing * (globals.COLS + 1))) / globals.COLS
        tile_height = (globals.DIMY - (spacing * (globals.ROWS + 1))) / globals.ROWS
        return tile_width, tile_height

    #draws the current game grid on the screen
    def drawGrid(self, gameState, globals):
        import pygame
        # Fill background with a pleasant dark blue
        self.screen.fill(self.BG_COLOR)
        
        # Calculate tile dimensions with proper spacing
        tile_width, tile_height = self.calculate_tile_dimensions(globals)
        spacing = self.TILE_SPACING
        border_radius = 15  # Increased from 10 for smoother corners
        
        # Draw grid tiles
        for i in range(globals.ROWS):
            for j in range(globals.COLS):
                x = spacing + j * (tile_width + spacing)
                y = spacing + i * (tile_height + spacing)
                
                # Get the value at this position
                index = i * globals.COLS + j
                value = gameState.gridList[index] if index < len(gameState.gridList) else 0
                
                # Check if tile is in correct position
                if gameState.is_tile_correct(value, index, globals.ROWS, globals.COLS):
                    tile_color = self.CORRECT_TILE_COLOR
                else:
                    tile_color = self.INCORRECT_TILE_COLOR
                
                # Draw tile background with rounded corners
                if value == 0:
                    # Empty tile - match background color
                    self.draw_rounded_rect(self.screen, self.BG_COLOR, (int(x), int(y), int(tile_width), int(tile_height)), border_radius)
                else:
                    tile_color = self.CORRECT_TILE_COLOR if gameState.is_tile_correct(value, index, globals.ROWS, globals.COLS) else self.INCORRECT_TILE_COLOR
                    self.draw_rounded_rect(self.screen, tile_color, (int(x), int(y), int(tile_width), int(tile_height)), border_radius)
                
                # Border removed for cleaner look
                
                # Draw number if not empty
                if value != 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(value), True, self.TEXT_COLOR)
                    text_rect = text.get_rect(center=(int(x + tile_width // 2), int(y + tile_height // 2)))
                    self.screen.blit(text, text_rect)

    def draw_rounded_rect(self, surface, color, rect, radius):
        import pygame
        pygame.draw.rect(surface, color, rect, border_radius=radius)

    #initializes the pygame screen
    def initScreen(self, globals):
        import pygame
        screen = pygame.display.set_mode((globals.DIMX, globals.DIMY))
        pygame.display.set_caption("15 Puzzle Game")
        return screen



