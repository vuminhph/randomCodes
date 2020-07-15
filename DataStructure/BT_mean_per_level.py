class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def mean_of_levels(root):
    leaves = [root]
    avgs = [root.val]

    while True:
        nodes = leaves 
        leaves = []
        for node in nodes:
            if node.left is not None:
                leaves.append(node.left)
            if node.right is not None:
                leaves.append(node.right)
        
        if len(leaves) == 0:
            break
        
        sum = 0
        count = 0

        for leaf in leaves:
            sum += leaf.val
            count += 1
        
        avgs.append(int(sum / count))

    return avgs

root = Node(2)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(4)
root.left.right = Node(8)
root.right.right = Node(9)

print(mean_of_levels(root))