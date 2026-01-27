from enum import Enum, auto

class GameState:

    class Direction(Enum):
        UP = auto()
        DOWN = auto()
        LEFT = auto()
        RIGHT = auto()

        def opposite(self):
            opposites = {
                self.UP: self.DOWN,
                self.DOWN: self.UP,
                self.LEFT: self.RIGHT,
                self.RIGHT: self.LEFT,
            }
            return opposites[self]
        

    #gridList is a list representation of the 2d game grid. The empty space is represented by a 0.
    def __init__(self, gridList):
        self.gridList = gridList

    #edit gridList to be the base (solved) configuration for a grid of size rows x cols
    def make_base_gridList(self, rows, cols):
        self.gridList = list(range(1, rows * cols)) + [0]


    #swaps two pieces in the grid
    def swapPieces(self, index1, index2):
        self.gridList[index1], self.gridList[index2] = self.gridList[index2], self.gridList[index1]

    
    #returns the index, row, and column of the empty space (0)
    def getEmptyPosition(self, globals):
        empty_index = self.gridList.index(0)
        empty_row = empty_index // globals.COLS
        empty_col = empty_index % globals.COLS
        return empty_index, empty_row, empty_col


    #modifies gridList by moving a piece in the specified direction
    #the piece should NOT be 0
    def move(self, piece_index, direction, globals):
        empty_index, _, _ = self.getEmptyPosition(globals)
        self.swapPieces(empty_index, piece_index)


    #returns an integer heuristic value that is calculates as follows:
    #The sum of the manhattan distances of each piece from its goal position in the 2d grid representation of the game
    def heuristic(self):
        return 0
    

    #returns a boolean indicating whether gridList is in a solved state
    def game_over(self):
        for i in range(len(self.gridList) - 1):
            if self.gridList[i] != i + 1:
                return False
        return self.gridList[-1] == 0
    

    #returns a list of directions in which other pieces can move into the empty space
    #EXAMPLE: A return of [Direction.UP, Direction.LEFT] means that the piece above and to the left of the empty space can move down and right respectively into the empty space
    def get_legal_moves(self, globals):
        empty_index, empty_row, empty_col = self.getEmptyPosition(globals)
        legal_moves = []
        
        # Check if there's a piece above (it can move DOWN)
        if empty_row > 0:
            legal_moves.append(self.Direction.DOWN)
        # Check if there's a piece below (it can move UP)
        if empty_row < globals.ROWS - 1:
            legal_moves.append(self.Direction.UP)
        # Check if there's a piece to the left (it can move RIGHT)
        if empty_col > 0:
            legal_moves.append(self.Direction.RIGHT)
        # Check if there's a piece to the right (it can move LEFT)
        if empty_col < globals.COLS - 1:
            legal_moves.append(self.Direction.LEFT)
        
        return legal_moves

    def is_tile_correct(self, tile_value, tile_index, rows, cols):
        """Check if a tile is in its correct position"""
        if tile_value == 0:
            return tile_index == rows * cols - 1
        return tile_value == tile_index + 1

    #turn gridList into a random, but solvable, configuration
    #use parity to make sure its solveble
    def randomizeBoard(self, globals):
        """Randomize the board to a solvable configuration using parity to ensure solvability"""
        import random
        
        # Create a random permutation of all tiles
        tiles = list(range(1, globals.ROWS * globals.COLS)) + [0]
        random.shuffle(tiles)
        
        # Count inversions (excluding the empty tile)
        def count_inversions(arr):
            count = 0
            for i in range(len(arr)):
                if arr[i] == 0:
                    continue
                for j in range(i + 1, len(arr)):
                    if arr[j] != 0 and arr[i] > arr[j]:
                        count += 1
            return count
        
        # For solvability, we need even number of inversions
        inversions = count_inversions(tiles)
        
        # If odd number of inversions, swap two non-zero tiles to make it even
        if inversions % 2 == 1:
            # Find and swap two different non-zero tiles
            non_zero_indices = [i for i in range(len(tiles)) if tiles[i] != 0]
            if len(non_zero_indices) >= 2:
                i, j = non_zero_indices[0], non_zero_indices[1]
                tiles[i], tiles[j] = tiles[j], tiles[i]
        
        self.gridList = tiles






