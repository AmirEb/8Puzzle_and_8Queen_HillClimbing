import NQueen

class search:

    def __init__(self,agentsCount):
        self.agentCount = agentsCount
        self.agents = [ None for j in range(agentsCount) ]
        self.isDone=0
        for i in range(agentsCount):
            p=NQueen.queen8()
            self.agents[i] = NQueen.agent(p)
    def allAgentsGoToNext(self):
        if self.isDone:
            return 0
        doneCount=0
        for a in self.agents:
            doneCount = doneCount + (a.goToNext() == 0)
        s="stoped agents: " + str(doneCount)
        print (s)
        self.isDone = ( doneCount == self.agentCount)
        if self.isDone:
            return 0
        return 1
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
        s="total agents: "+ str(self.agentCount)
        print (s)
        s="successful agents: "+ str(count)
        print (s)
        s="success rate: "+ str((count+0.0)*100/self.agentCount) +"%"
        print (s)



AI = searcher(12)

AI.solve()
