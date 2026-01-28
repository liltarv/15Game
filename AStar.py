from collections import defaultdict


class AStar:
    def __init__(self, globals, initial_state):
        self.globals = globals
        self.initial_state = initial_state
        self.parentMap = defaultdict(lambda : -1)
        self.costMap = defaultdict(lambda : -1)
        self.visited = set()

    #gridList is a list representation of the 2d game grid. The empty space is represented by a 0.
    #gridList to integer conversion for hashing and comparison
    #we need to create a unique hash for each possible configuration of the grid
    #however, each hash must map to a unique configuration (no collisions)
    #additionally, the hash must be reversible (we must be able to get the gridList back from the hash)
    #also, it must fit into a standard integer type
    def gridListToHash(self, gridList):
        return hash(tuple(gridList))
    
    def hashToGridList(self, hashNum, num_pieces):
        pass
    
    #conducts A* from initial_state to goal state (solved configuration)
    def aStarSearch(self):
        pass