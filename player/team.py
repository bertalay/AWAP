"""
The team.py file is where you should write all your code!

Write the __init__ and the step functions. Further explanations
about these functions are detailed in the wiki.

List your Andrew ID's up here!
aylu
jafish
"""
from awap2019 import Tile, Direction, State
import queue

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
        self.board = initial_board
        self.visited = []
        self.remembered_board = [[0 for i in range(len(initial_board[0]))] for j in range(len(initial_board))]
        self.goals = [None, None, None, None]
        
        self.team_size = team_size
        self.company_info = company_info

        self.team_name = "this is fine"
        print(self.team_name)
        for s in self.board:
            acc = ""
            for k in s:
                acc += str(k.get_booth()) + " "
            print(acc)
         
        print(self.board[1][2].get_booth())
        print(self.company_info)

	#return Tile of the company end of line
	#@ensures new goal has not been visited yet, and also no overlap in goals
    def goal_finder(self, state):
        lim = 100
        h = []
        #acc = [] #tuples that represent the tentative distance
        q = queue.Queue()
        q.put((state.y, state.x))
        while(not q.empty()):
            
            p = q.get()
            while(p in h):
                p = q.get()
			
            if(self.board[p[1]][p[0]].get_line() != None and not self.board[p[1]][p[0]] in self.goals and self.board[p[1]][p[0]] in self.visited):
				# also check if in visited or goals
                self.goals[state.id] = self.board[p[1]][p[0]] #sets it here but good enough
                return self.board[p[1]][p[0]]
			
            if(p[0] + 1 < len(initial_board[0]) and self.board[p[1]][p[0]+1].get_booth() == None):
                q.put((p[0]+1, p[1]))
            if(p[0] - 1 >= 0 and self.board[p[1]][p[0]-1].get_booth() == None):
                q.put((p[0]-1, p[1]))
            if(p[1] + 1 < len(initial_board) and self.board[p[1]+1][p[0]].get_booth() == None):
                q.put((p[0], p[1]+1))
            if(p[1] - 1 >= 0 and self.board[p[1]-1][p[0]].get_booth() == None):
                q.put((p[0], p[1]-1))
				
            h.append(p)
			
        return self.board[state.y][state.x]


    def step(self, visible_board, states, score):


		#add company to self.visited

        return [Direction.UP, Direction.LEFT, Direction.DOWN, Direction.RIGHT]
