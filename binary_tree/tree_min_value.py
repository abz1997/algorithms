class Node():
    def __init__(self, values):
        self.values = values
        self.left = None
        self.right = None

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(15)
f = Node(12) 
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

        #      5
        #     /  \
        #    11   3
        #   / \    \
        #  4   15   12


# question: find min value in binary tree