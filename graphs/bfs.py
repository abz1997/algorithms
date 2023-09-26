# a -* c
# |    |
# *    *
# b    e
# |
# *
# d -* f

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

# bfs in graphs moves to all neighbours  and then from those neighbours moves to all their neighbours etc

# iterative solution
def breadthFirstPrint(graph, source):
    queue = [source]
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr)
        for neighbours in graph[curr]:
            queue.append(neighbours)

breadthFirstPrint(graph, 'a')

# n = no of nodes
# e = no of vertices

# space: O(n)
# time: O(e) or O(n^2)

# in the worst case scenario there is n^2 vertices
