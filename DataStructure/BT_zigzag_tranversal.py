class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigZagTraversal(root):
    leaves = [root]
    leaves_values = [root.val]
    order = 0

    result = []

    while True:
        if len(leaves) == 0:
            break
        
        result.append(leaves_values)
        leaves_values = []
        nodes = leaves
        leaves = []

        for i in range(len(nodes) - 1, -1, -1):
            if order % 2 == 0:
                if nodes[i].right is not None:
                    leaves.append(nodes[i].right)
                if nodes[i].left is not None:
                    leaves.append(nodes[i].left)
            else:
                if nodes[i].left is not None:
                    leaves.append(nodes[i].left)
                if nodes[i].right is not None:
                    leaves.append(nodes[i].right)

        order += 1
        
        for leaf in leaves:
            leaves_values.append(leaf.val)

    return result

tree5 = Node(8)
tree5.left = Node(6)
tree5.right = Node(9)
tree5.left.left = Node(5)
tree5.left.right = Node(7)
tree5.right.right = Node(10)

print(zigZagTraversal(tree5))