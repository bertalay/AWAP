"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
aylu
jafish
"""
from awap2019 import Tile, Direction, State

class Team(object):
    
    def __init__(self, initial_board, team_size, company_info):
        """
        The initializer is for you to precompute anything from the
        initial board and the company information! Feel free to create any
        new instance variables to help you out.

        Specific information about initial_board and company_info are
        on the wiki. team_size, although passed to you as a parameter, will
        always be 4.
        """
        self.team_size = team_size
        self.company_info = company_info
        self.board = initial_board
        self.visited = []
        self.dimensions = [len(initial_board), len(initial_board[0])]
        self.remembered_board = [[0 for i in range(len(initial_board[0]))] for j in range(len(initial_board))]
        self.phase = ["spreading" for i in range(self.team_size)]
        self.turnCount = 0
        
        

        self.team_name = "this is fine"

    def step(self, visible_board, states, score):
        returnList = [Direction.UP, Direction.UP, Direction.UP, Direction.UP]
        print(self.turnCount)
        self.turnCount += 1
        for i in range(self.team_size):
            if self.phase == "spreading":
                i = i + 1 - 1
                #implmement
            
            #same sort of structure for each of these phases
        return returnList
