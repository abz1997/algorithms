class Node():
    def __init__(self, values):
        self.values = values
        self.left = None
        self.right = None

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1) 
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

        #      3
        #     /  \
        #    11   4
        #   / \    \
        #  4   2    1


# question: sum all values in binary tree

# -------------------------------------------------------------------------------------------------------------------

# using dfs recursively

def sum_dfs(root):
    if not root:
        return 0
        # print(root.values)
    return root.values + sum_dfs(root.left) + sum_dfs(root.right)

aaa = sum_dfs(a)
print(aaa)

def sum_iter(root):
    stack = [root]
    total = 0

    while len(stack) > 0:
        current = stack[-1]
        total += current.values

        stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:                 
            stack.append(current.left)

    return total

print(sum_iter(a))