class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None, visited=0):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.visited = visited
# Creating a more complex binary tree
# root = BinaryTree(20)
# root.left = BinaryTree(10, parent=root)
# root.right = BinaryTree(30, parent=root)
#
# root.left.left = BinaryTree(5, parent=root.left)
# root.left.right = BinaryTree(15, parent=root.left)
#
# root.right.left = BinaryTree(25, parent=root.right)
# root.right.right = BinaryTree(35, parent=root.right)
#
# root.left.left.left = BinaryTree(3, parent=root.left.left)
# root.left.left.right = BinaryTree(6, parent=root.left.left)
#
# root.left.right.left = BinaryTree(12, parent=root.left.right)
# root.left.right.right = BinaryTree(17, parent=root.left.right)




def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if not hasattr(find_successor, 'searched_node'):
        find_successor.searched_node = node.value

    searched_node = find_successor.searched_node

    if node.left is not None and node.left.visited != 1:
        find_successor(tree, node.left)
    elif node.right is not None and node.right.visited != 1:
        find_successor(tree, node.right)
    else:
        parent_node = node.parent
        if parent_node:
            parent_node.visited = 1
            parent_node.left.visited = 1
            parent_node.right.visited = 1
            if parent_node.left and parent_node.left.value > searched_node:
                return parent_node.value
            elif parent_node.value > searched_node:
                return parent_node.value
            elif parent_node.right and parent_node.right.value > searched_node:
                return parent_node.right.value
            return find_successor(tree, parent_node)
    return None


print(find_successor(root, root.left.right.left))
