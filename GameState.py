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
        pass


    #modifies gridList by moving a piece at index in the specified direction
    def move(self, index, direction):
        pass


    #returns an integer heuristic value that is calculates as follows:
    #The sum of the manhattan distances of each piece from its goal position in the 2d grid representation of the game
    def heuristic(self):
        return 0
    

    #returns a boolean indicating whether gridList is in a solved state
    def game_over(self):
        return False
    

    #returns a list of directions in which other pieces can move into the empty space
    #EXAMPLE: A return of [Direction.UP, Direction.LEFT] means that the piece above and to the left of the empty space can move down and right respectively into the empty space
    def get_legal_moves(self):
        return []
    





