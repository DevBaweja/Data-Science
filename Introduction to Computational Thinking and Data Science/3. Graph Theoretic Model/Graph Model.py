class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + ' -> ' + self.dest.getName()
    
class Digraph(object):
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        self.edges[node] = []
    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges or dest in self.edges):
            raise ValueError('Node is absent')
        self.edges[src].append(dest)
    
    def childrens(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for node in self.edges:
            if node.getName() == name:
                return node
        raise NameError(name + 'doesn\'t exists')
    
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result += src.getName() + ' -> ' + dest.getName() + '\n'
        return result

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

def buildGraph(graphType):
    graph = graphType()
    nodes = ['Boston', 'Providence', 'New York', 'Chicago',
                'Denver', 'Phoenix', 'Los Angeles']
    for node in nodes:
        graph.addNode(Node(node))

    graphTemp = [['Providence', 'New York'], ['Boston', 'New York'], ['Chicago'], ['Denver', 'Phoenix'], ['Phoenix', 'New York'], ['Boston']]
    
    for index,nodeList in enumerate(graphTemp):
        for node in nodeList:
            edge = Edge(graph.getNode(nodes[index]), graph.getNode(node))
            graph.addEdge(edge)
    return graph

def printPath(path):
    if not path:
        return
    cur,*remain = path
    if len(path) == 1:
        print(cur)
        return
    print(cur, '->', end=" ")
    printPath(remain)

def DFS(graph, start, end, path, shortest):
    path = path + [start]
    print('Current Path:', end=" ")
    printPath(path)
    if start == end:
        return path
    
    for node in graph.childrens(start):
        if node not in path: 
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest)
                if newPath != None:
                    shortest = newPath
        else:
            print("Visited:", node)
    
    return shortest

def BFS(graph, start, end):
    initPath = [start]
    pathQueue = [initPath]

    while len(pathQueue) != 0:
        print('Queue:', len(pathQueue))
        for path in pathQueue:
            printPath(path)

        tempPath = pathQueue.pop(0)
        print('Current Path:')
        printPath(tempPath)
    
        lastNode = tempPath[-1]
        if lastNode == end:
            return tempPath

        for nextNode in graph.childrens(lastNode):
            if nextNode not in tempPath:
                newPath = tempPath + [nextNode]
                pathQueue.append(newPath)

    return None

def shortestPath(graph, start, end, algorithm):
    if algorithm == DFS:
        return algorithm(graph, start, end, [], None)
    if algorithm == BFS:
        return algorithm(graph, start, end)

def testShortestPath(source, destination, algorithm):
    graph = buildGraph(Digraph)
    path = shortestPath(graph, graph.getNode(source), graph.getNode(destination), algorithm)
    if path:
        print('Path from ', source, ' to ', destination, ' is ')
        printPath(path)
    else:
        print('There is no path from ', source, ' to ', destination)

testShortestPath('Chicago', 'Boston', DFS)
testShortestPath('Boston', 'Phoenix', BFS)
