class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def node_height(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        if node.left is None:
            return 1 + self.node_height(node.right)
        if self.right is None:
            return 1 + self.node_height(node.left)
        return 1 + max(self.node_height(node.left), self.node_height(node.right))


class AVL:
    def __init__(self):
        self.root = None
        self.height = 0

    def __iter__(self):
        return self.__next__(self.root)

    def __next__(self, node):
        if node is None:
            return
        if node.left:
            for item in self.__next__(node.left):
                yield item
        yield node.key
        if node.right:
            for item in self.__next__(node.right):
                yield item

    def contains(self, val):
        return self._contains(self.root, val)

    def _contains(self, node, val):
        if node is None:
            return False

        if node.key == val:
            return True
        if val > node.key:
            return self._contains(node.right, val)
        else:
            return self._contains(node.left, val)

    def update_height(self):
        self.height = self.root.node_height(self.root)

    def insert(self, key):
        self.root = self._insert(self.root, key)
        self.update_height()

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        elif key <= root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        self.update_height()
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if key <= root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def left_rotate(self, curr):
        new_curr = curr.right
        new_curr_child = new_curr.left
        new_curr.left = curr
        curr.right = new_curr_child
        return new_curr

    def right_rotate(self, curr):
        new_curr = curr.left
        new_curr_child = new_curr.right
        new_curr.right = curr
        curr.left = new_curr_child
        return new_curr

    def get_balance(self, root):
        if root is None:
            return 0
        return root.node_height(root.left) - root.node_height(root.right)
