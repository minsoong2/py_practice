import sys

class Node:
    def __init__(self, data, l, r):
        self.data = data
        self.l = l
        self.r = r

def pre_order(node):
    print(node.data, end=' ')
    if node.l != None:
        pre_order(tree[node.l])
    if node.r != None:
        pre_order(tree[node.r])

def in_order(node):
    if node.l != None:
        in_order(tree[node.l])
    print(node.data, end=' ')
    if node.r != None:
        in_order(tree[node.r])

def post_order(node):
    if node.l != None:
        post_order(tree[node.l])
    if node.r != None:
        post_order(tree[node.r])
    print(node.data, end=' ')

n = int(sys.stdin.readline())
tree = {}

for i in range(n):
    data, l, r = sys.stdin.readline().split()
    if l == 'None':
        l = None
    if r == 'None':
        r = None
    tree[data] = Node(data, l, r)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])