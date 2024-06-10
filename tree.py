class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    @staticmethod
    def insert(root, key):
        if root is None:
            return Node(key)
        elif key < root.key:
            root.left = Node.insert(root.left, key)
        else:
            root.right = Node.insert(root.right, key)
        return root

    @staticmethod
    def search(root, key):
        if root is None:
            return False
        elif key < root.key:
            return Node.search(root.left, key)
        elif key > root.key:
            return Node.search(root.right, key)
        else:
            return True

    @staticmethod
    def preorder_traversal(root):
        if root is not None:
            print(root.key)
            Node.preorder_traversal(root.left)
            Node.preorder_traversal(root.right)

    @staticmethod
    def inorder_traversal(root):
        if root is not None:
            Node.inorder_traversal(root.left)
            print(root.key)
            Node.inorder_traversal(root.right)

    @staticmethod
    def postorder_traversal(root):
        if root is not None:
            Node.postorder_traversal(root.left)
            Node.postorder_traversal(root.right)
            print(root.key)

# Create the tree and perform operations
root = None
root = Node.insert(root, 1)
root = Node.insert(root, 2)
root = Node.insert(root, 3)
root = Node.insert(root, 4)
root = Node.insert(root, 5)
root = Node.insert(root, 6)

if Node.search(root, 3):
    print("Nilai 3 ditemukan dalam pohon")
else:
    print("Nilai 3 tidak ditemukan dalam pohon")

print("Preorder traversal:")
Node.preorder_traversal(root)

print("Inorder traversal:")
Node.inorder_traversal(root)

print("Postorder traversal:")
Node.postorder_traversal(root)