# this undirected graph can allow nodes between vertices to travel to one another

# i - j
# |
# k  - l
# |
# m

# o - n

'''Write a function undirectedPath, that takes in an array of edges for an undirected graph and two nodes
The function should return a boolean indicating whether or not there exists a path between nodeA and nodeB.'''

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


# convert edge list into adjacency list
def buildGraph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

# iterative queue
# def hasPath(graph, nodeA, nodeB):
#     queue = [nodeA]
#     visited_nodes = set()
#     while len(queue) > 0:
#         curr = queue.pop(0)
#         for neighbour in graph[curr]:
#             if neighbour == nodeB:
#                 return True
#             if neighbour not in visited_nodes:
#                 queue.append(neighbour)
#             visited_nodes.add(neighbour)
#     return False


# recursive
def hasPath(graph, nodeA, nodeB, visited_node=set()):
    curr = nodeA
    if curr not in visited_node:
        visited_node.add(curr)
        for neighbour in graph[curr]:
            if neighbour == nodeB:
                return True
            return hasPath(graph, neighbour, nodeB, visited_node)
    return False


def undirectedPath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB)


print(undirectedPath(edges, 'l', 'm'))
