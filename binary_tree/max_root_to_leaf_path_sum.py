class Node():
    def __init__(self, values):
        self.values = values
        self.left = None
        self.right = None

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1) 
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

        #      5
        #     /  \
        #    11   3
        #   / \    \
        #  4   2    1


# question: find path from to leaf with highest sum

def iteratively(root):
    if not root:
        return None
    left = iteratively(root.left)
    right = iteratively(root.right)
    return root.values + max[left.values,right.values]

print(iteratively(a))