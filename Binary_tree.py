class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE
nodeB.right = nodeF 
root.left = nodeG

# print("Data of root.right.left:", root.right.left.value)
# print("Data of root.left.value:", root.left.value)

def preOrder(node): ### Root Left Right
    if node is None:
        return 
    print(node.value,end=",")
    preOrder(node.left)
    preOrder(node.right)

def inOrder(node):  ### Left Root Right
    if node is None:
        return
    inOrder(node.left)
    print(node.value, end=",")
    inOrder(node.right)

def postOrder(node): ### Left Right Root
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.value, end=",")