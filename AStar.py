from collections import defaultdict
import heapq
import GameState

class AStar:
    def __init__(self, globals, initial_gridList):
        self.globals = globals
        self.initial_gridList = initial_gridList
        self.parentMap = defaultdict(lambda : -1)
        self.costMap = defaultdict(lambda : -1)
        self.visited = set()
        self.hashDict = defaultdict(lambda : ())

    def heuristic(self, gridList, globals):
        total_distance = 0
        
        for index, value in enumerate(gridList):
            if value != 0:  # Skip the empty space
                target_index = value - 1
                current_row, current_col = index // globals.COLS, index % globals.COLS
                target_row, target_col = target_index // globals.COLS, target_index % globals.COLS
                total_distance += abs(current_row - target_row) + abs(current_col - target_col)
        
        return total_distance

    #gridList is a list representation of the 2d game grid. The empty space is represented by a 0.
    #gridList to integer conversion for hashing and comparison
    #we need to create a unique hash for each possible configuration of the grid
    #however, each hash must map to a unique configuration (no collisions)
    #additionally, the hash must be reversible (we must be able to get the gridList back from the hash)
    #also, it must fit into a standard integer type
    def gridListToHash(self, gridList):
        self.hashDict[hash(tuple(gridList))] = tuple(gridList)
        return hash(tuple(gridList))
    
    def hashToGridList(self, hashNum):
        return list(self.hashDict[hashNum])
    
    def tupleToGridList(self, gridTuple):
        return list(gridTuple)

    #conducts A* from initial_state to goal state (solved configuration)
    def aStarSearch(self):
        pq = []
        heapq.heappush(pq, (self.heuristic(self.initial_gridList, self.globals), -1, self.gridListToHash(self.initial_gridList)))
        self.costMap[self.gridListToHash(self.initial_gridList)] = 0
        goal_gridList = GameState.GameState([]).make_base_gridList(self.globals.ROWS, self.globals.COLS)
        goal_hash = self.gridListToHash(goal_gridList)
        while pq:
            curr_f, curr_p, curr_h = heapq.heappop(pq)
            if curr_h in self.visited:
                continue
            self.visited[curr_h] = True
            if curr_h == goal_hash:
                path = []
                while curr_p != -1:
                    path.append(curr_h)
                    curr_h = curr_p
                    curr_p = self.parentMap[curr_h]
                path.reverse()
                return [self.hashToGridList(h) for h in path]
            curr_gridList = self.hashToGridList(curr_h)
            curr_cost = self.costMap[curr_h]
            curr_state = GameState.GameState(curr_gridList)
            legal_moves = curr_state.get_legal_moves(self.globals)
            for direction in legal_moves:
                #

             