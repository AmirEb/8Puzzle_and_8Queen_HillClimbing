import NQueen

class solver:

    def __init__(self,agentsCount):
        self.agentCount = agentsCount
        self.agents = [ None for j in range(agentsCount) ]
        self.isDone=0
        for i in range(agentsCount):
            p=search.queen8()  # a random 8 queen puzzle with a wrong preset of queens is stored in p
            self.agents[i] = search.agent(p)     # the agent will later use hillclimbing algorithm to fix the wrong preset of queens stored in p (its exclusive problem)
    def allAgentsGoToNext(self):
        if self.isDone:
            return 0    # all agents are done....
        doneCount=0
        for a in self.agents:
            doneCount = doneCount + (a.goToNext() == 0)
        s="stoped agents: " + str(doneCount)
        print (s)
        self.isDone = ( doneCount == self.agentCount)
        if self.isDone:
            return 0    # all agents are done....
        return 1    # at least one agent is moving....
    def solve(self):
        while not self.isDone:
            self.allAgentsGoToNext()
        count=0
        i=-1
        for a in self.agents:
            i=i+1
            if (a.problem.isSolved()):
                count = count + 1
                s= "answer number " + str(count) + " from agent number " + str(i)
                print (s)
                a.problem.showG()
                print (" ")

        s="successful agents: "+ str(count)
        print (s)



# just to test class methods

AI = solver(12)       # creates a hillclimb based solver with 1000 agents for 8 queen problem

AI.solve() # solves the 8 queen problem and show the successful agents result (may contain duplicated answers)
