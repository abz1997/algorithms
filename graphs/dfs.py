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

# dfs in graphs moves in 1 direction until it can't go anymore in that direction, then the most recently added node
# to the stack is then traversed in the direction it can etc until the stack is empty.

# iterative solution
# def depthFirstPrint(graph, source):
#     stack = [source]
#     while len(stack) > 0:
#         curr = stack.pop()
#         print(curr)
#         for neighbours in graph[curr]:
#             stack.append(neighbours)

# recursive solution
def depthFirstPrint(graph, source):
    print(source)
    for neighbour in graph[source]:
        depthFirstPrint(graph, neighbour)

# these solutions print different things but they are both valid as they satisfy the depth first traversal for graphs

depthFirstPrint(graph, 'a')

# n = no of nodes
# e = no of vertices

# space: O(n)
# time: O(e) or O(n^2)

# in the worst case scenario there is n^2 vertices
