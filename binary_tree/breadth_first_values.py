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

def breadth_first_values(root):
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current.values)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

breadth_first_values(a)

# n = no of nodes
# time : O(n) we only visit each node once 
# space : O(n) we aren't storing more than n items in queue  


# there is no recursive method for this as recursive methods under the hood use stacks and we are using a queue.

    