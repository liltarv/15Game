import time
import math

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
        self.tile_positions = {}  # Track current positions for animation
        self.animation_duration = 0.2  # seconds (increased for smoother feel)
        self.animated_tiles = {}  # {tile_value: {'start_pos': (x,y), 'end_pos': (x,y), 'start_time': time}}
        self.TILE_SPACING = 8  # pixels between tiles

    def calculate_tile_dimensions(self, globals):
        """Calculate tile width and height accounting for spacing"""
        spacing = self.TILE_SPACING
        tile_width = (globals.DIMX - (spacing * (globals.COLS + 1))) / globals.COLS
        tile_height = (globals.DIMY - (spacing * (globals.ROWS + 1))) / globals.ROWS
        return tile_width, tile_height

    def start_animation(self, tile_value, start_index, end_index, globals):
        """Start animation for a tile moving from start_index to end_index"""
        tile_width, tile_height = self.calculate_tile_dimensions(globals)
        spacing = self.TILE_SPACING
        
        start_x = spacing + (start_index % globals.COLS) * (tile_width + spacing)
        start_y = spacing + (start_index // globals.COLS) * (tile_height + spacing)
        end_x = spacing + (end_index % globals.COLS) * (tile_width + spacing)
        end_y = spacing + (end_index // globals.COLS) * (tile_height + spacing)
        
        self.animated_tiles[tile_value] = {
            'start_pos': (start_x, start_y),
            'end_pos': (end_x, end_y),
            'start_time': time.time()
        }

    def get_animated_position(self, tile_value, default_pos):
        """Get the current animated position of a tile, or default if not animating"""
        if tile_value not in self.animated_tiles:
            return default_pos
        
        anim = self.animated_tiles[tile_value]
        elapsed = time.time() - anim['start_time']
        
        if elapsed >= self.animation_duration:
            del self.animated_tiles[tile_value]
            return default_pos
        
        # Ease-in-out cubic for smoother animation
        progress = elapsed / self.animation_duration
        eased_progress = progress * progress * (3 - 2 * progress)  # Smoothstep
        
        start_x, start_y = anim['start_pos']
        end_x, end_y = anim['end_pos']
        
        current_x = start_x + (end_x - start_x) * eased_progress
        current_y = start_y + (end_y - start_y) * eased_progress
        
        return (int(current_x), int(current_y))

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
                
                # Get animated position if tile is animating
                if value != 0:
                    x, y = self.get_animated_position(value, (x, y))
                
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



