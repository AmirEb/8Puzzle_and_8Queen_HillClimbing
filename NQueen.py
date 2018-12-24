import random
from copy import deepcopy

class NQueen:

    queens = []
    queensNum = 8

    def __init__(self, n):
        self.queens_num = n

    def getState(self):
        return self.queens

    def isGoal(self):
        return self.heuristic() == 0

    def generateRandomBoard(self, hardrate):
        self.queens = []
        for i in range(self.queensNum):
            exists = True
            while exists:
                exists = False

                
                state = (random.randrange(self.queensNum), random.randrange(self.queensNum))

                
                if(len(self.queens) == 0):
                    self.queens.append(state)
                    break

                
                for queen in self.queens:
                    if state == queen:
                        exists = True
                        break

                if not exists:
                    self.queens.append(state)


    def heuristic(self):
        qs = deepcopy(self.queens)

        for (x, y) in self.queens:
            for i in range(self.queensNum):
                if (i, y) in qs and (i, y) != (x, y):
                    qs.remove((i, y))

            for i in range(self.queensNum):
                if (x, i) in qs and (x, i) != (x, y):
                    qs.remove((x, i))

            # simpler version of the code below
            for di in [-1, 1]:
                for dj in [-1, 1]:
                    i, j = x, y
                    condition = self.getCondition(di, dj, i, j)
                    while condition:
                        i += di
                        j += dj
                        if (i, j) in qs and (i, j) != (x, y):
                            qs.remove((i, j))
                        condition = self.getCondition(di, dj, i, j)


        return self.queensNum - len(qs)


