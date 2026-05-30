class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left)
    print(node.value, end=",")
    inOrderTraversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)


root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18



# inOrderTraversal(root)


### Searching in Binary Search Tree

def search(node, target):
    if node is None:
        return False
    elif node.value == target:
        return node
    elif target < node.value:
        return search(node.left, target)
    else:
        return search(node.right, target)
    
result = search(root, 13)

if result:
    print(f"\nFound node with value: {result.value}")
else:    
    print("\nNode not found.")


## Insert in Binary Search Tree

def insert(node, value):
    if node is None:
        return TreeNode(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

root = insert(root, 10)
inOrderTraversal(root)


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
# print("\nMinimum value in the tree:", minValueNode(root).value)



def deleteNode(node, key):
    if not node:
        return node 
    if key < node.value:
        node.left = deleteNode(node.left, key)
    elif key > node.value:
        node.right = deleteNode(node.right, key)
    else:
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp
        node.value = minValueNode(node.right).value
        node.right = deleteNode(node.right, node.value)
    return node


deleteNode(root, 15)
print("\nIn-order traversal after deletion:")
inOrderTraversal(root)  
    