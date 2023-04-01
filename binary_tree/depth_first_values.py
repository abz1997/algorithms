class Node():
    '''binary tree class'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# build the binary tree
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

# depth first values algorithm which traverses the binary tree from left to right starting from root. When we get
# to a node that has no children we go back up then right.
def depth_first_values(root):
    stack = [root] # the stack means we get lifo
    # print(root.value)

    while len(stack) > 0:
        current = stack.pop() # remove last value
        print(current.value)

        if current.right:
            stack.append(current.right) # we add right node to the list first

        if current.left:
            stack.append(current.left) # we add left node to end of list. This is then removed first and printed.

'''So what is happening here? We add node 'a' to stack. We remove 'a'. We check if 'a' had anything
on right then add that to stack so now stack = [c]. Then we check if 'a' had anything on left and append that to
stack so now stack = [c,b]. We remove 'b' then check right and left of 'b' and append those to stack 
so stack = [c,e,d]. We remove 'd' and as that has no children, we then remove 'e' which also has no children. 
We then remove 'c' from stack and check what is right which is 'f' so stack = [f]. There is nothing left of 'c'.
We then remove 'f' and then stop because now len(stack) < 0. '''

# n = no of nodes
# time : O(n) we only visit each node once 
# space : O(n) we aren't storing more than n items in stack  

# depth_first_values(a)

# recursive method
# under the hood recursive methods use stacks
def depth_first_values_recursive(root):
    if root == None:
        return []
    print(f'root {root.value}')
    left_values = depth_first_values_recursive(root.left) # from a we get [b, d, e] from this function
    # print(f'left value = {left_values}')
    right_values = depth_first_values_recursive(root.right) # from a we get [c, f] from this function
    # print(f'right value = {right_values}')
    return [root.value, *left_values, *right_values] # unpacking operator '*' allows us to add to list without square brackets

print(depth_first_values_recursive(a))

        #      a
        #     /  \
        #    b    c
        #   / \    \
        #  d   e    f


