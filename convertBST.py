class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, value):
        self.root = TreeNode(value)

    def is_leaf(self, node):
        return node.left == None and node.right == None

    def add_node(self, root, value):
        if self.is_leaf(root):
            if value < root.value:
                root.left = TreeNode(value)
            elif value > root.value:
                root.right = TreeNode(value)
                
        elif value < root.value:
            self.add_node(root.left, value)
        elif value > root.value:
            self.add_node(root.right, value)
        else:
            print('Node already exists')

    