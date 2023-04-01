class Node():
    def __init__(self, values):
        self.values = values
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f') 
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

        #      a
        #     /  \
        #    b    c
        #   / \    \
        #  d   e    f


# question: check if 'e' in binary tree. Can use bfs or dfs

# -------------------------------------------------------------------------------------------------------------------

# using bfs iteratively:
def bfs(root, check_node):
    queue = [root]
    check_list = []

    while len(queue) > 0:
        current = queue.pop(0)
        check_list.append(current.values)
        print(check_list)
        if current.values == check_node:
            return True

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

bfs(root=a, check_node='e')

# -----------------------------------------------------------------------------------------------------------------

# using dfs recursively:
def dfs(root, check_node):
    if root == None:
        return False

    if root.values == check_node:
        return True

    return dfs(root.left, check_node) or dfs(root.right, check_node)

print(dfs(root=a, check_node='e'))
