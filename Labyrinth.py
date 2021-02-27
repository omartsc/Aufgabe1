import numpy as np
import sys

class Labyrinth():

    def __init__(self, levels):
        self.minimal_time = np.inf
        self.start_i = 0
        self.start_j = 0
        self.start_k = 0

        L = len(levels)
        R = len(levels[0])
        C = len(levels[0][0])

        self.lab = np.ones((L+2, R+2, C+2), np.int8)
        
        # create labyrinth with numeric values and find start position
        for i in range(L):
            rows = levels[i]
            for j in range(R):
                row = rows[j]
                for k in range(C):
                    if row[k] == 'S':
                        self.lab[i+1][j+1][k+1] = -1
                        self.start_i = i+1
                        self.start_j = j+1
                        self.start_k = k+1
                    elif row[k] == 'E':
                        self.lab[i+1][j+1][k+1] = -2
                    elif row[k] == '.':
                        self.lab[i+1][j+1][k+1] = 0

    def search_path(self, i, j, k, time):

        # search Upwards
        if self.lab[i+1][j][k] == 0:
            self.lab[i+1][j][k] = 1
            self.search_path(i+1, j, k, time + 1)
        elif self.lab[i+1][j][k] == -2:
            time += 1
            if  time < self.minimal_time:
                self.minimal_time = time
            
        # search Downwards
        if self.lab[i-1][j][k] == 0:
            self.lab[i-1][j][k] = 1
            self.search_path(i-1, j, k, time + 1)
        elif self.lab[i-1][j][k] == -2:
            time += 1
            if time < self.minimal_time:
                self.minimal_time = time
            
        # search southwards
        if self.lab[i][j+1][k] == 0:
            self.lab[i][j+1][k] = 1
            self.search_path(i, j+1, k, time + 1)
        elif self.lab[i][j+1][k] == -2:
            time += 1
            if time < self.minimal_time:
                self.minimal_time = time

        # search northwards
        if self.lab[i][j-1][k] == 0:
            self.lab[i][j-1][k] = 1
            self.search_path(i, j-1, k, time + 1)
        elif self.lab[i][j-1][k] == -2:
            time += 1
            if time < self.minimal_time:
                self.minimal_time = time
        
        # search eastwards
        if self.lab[i][j][k+1] == 0:
            self.lab[i][j][k+1] = 1
            self.search_path(i, j, k+1, time + 1)
        elif self.lab[i][j][k+1] == -2:
            time += 1
            if time < self.minimal_time:
                self.minimal_time = time
        
        # search westwards
        if self.lab[i][j][k-1] == 0:
            self.lab[i][j][k-1] = 1
            self.search_path(i, j, k-1, time + 1)
        elif self.lab[i][j][k-1] == -2:
            time += 1
            if time < self.minimal_time:
                self.minimal_time = time
        

if __name__ == "__main__":

    filepath = sys.argv[1]

    with open(filepath) as input:
        
        line = input.readline()
        while line:
            levels = []
            L = 0
            R = 0
            C = 0
            if line == "0 0 0":
                sys.exit(0)
            else:
                L = int(line[0])
                R = int(line[2])
                C = int(line[4])
                
                for i in range(L):
                    level = []
                    for j in range(R):
                        row = input.readline().rstrip()
                        level.append(row)
                    levels.append(level)
                    empty_line = input.readline()

            labyrinth = Labyrinth(levels)
            labyrinth.search_path(labyrinth.start_i, labyrinth.start_j, labyrinth.start_k, 0)

            if(labyrinth.minimal_time < np.inf):
                print("Entkommen in " + str(labyrinth.minimal_time) + " Minute(n)!")
            else:
                print("Gefangen :(")

            line = input.readline()