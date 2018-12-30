class PriorityQueue:

    def  __init__(self):
         print(" ")

def raiseNotDefined():
    print(" ")

class SearchProblem:
    print(" ")

def hillClimbing(problem):

    (current, c_cost, c_path) = (problem.getStartState(), 0, [])

    if current.isGoal():
        return c_path

    def getNeighbor(node, cost, path):
        bestH=0
        for child_node, child_action, child_cost in problem.getSuccessors(node):
            if child_node.heuristic() > bestH:
                new_cost = cost + child_cost
                new_path = path + [child_action]
                bestNode = (child_node, new_cost, new_path)
                bestH = child_node.heuristic()
        return bestNode

    while True:
        (neighbor, n_cost, n_path) = getNeighbor(current, c_cost, c_path);
        if neighbor.heuristic() <= current.heuristic():
            return c_path
        (current, c_cost, c_path) = (neighbor, n_cost, n_path)
        
