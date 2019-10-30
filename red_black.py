class Node:
    def __init__(self, key, color='red'):
        self.parent = None
        self.left = None
        self.right = None
        self.key = key
        self.color = color


class RBTree:
    def __init__(self):
        self.root = None

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

    def insert(self, key):
        if self.root is None:
            self.root = Node(key, 'black')
            return
        new_node = Node(key)
        curr = self.root
        new_parent = None
        while curr is not None:
            new_parent = curr
            if new_node.key <= curr.key:
                curr = curr.left
            else:
                curr = curr.right
        new_node.parent = new_parent
        if new_node.key <= new_parent.key:
            new_node.parent.left = new_node
        else:
            new_node.parent.right = new_node
        self.rebalance(new_node)

    def left_rotate(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            self.replace_child(node.parent, node, node.right)
        else:
            self.root = node.right
            self.root.parent = None
        self.set_child(node.right, 'left', node)
        self.set_child(node, 'right', right_left_child)

    def right_rotate(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            self.replace_child(node.parent, node, node.left)
        else:
            self.root = node.left
            self.root.parent = None
        self.set_child(node.left, 'right', node)
        self.set_child(node, 'left', left_right_child)

    def rebalance(self, node):
        # If node is the tree root, set to black
        if node.parent is None:
            node.color = 'black'
            return
        if node.parent.color is 'black':
            return
        parent = node.parent
        grandparent = self.get_grandparent(node)
        uncle = self.get_uncle(node)
        if uncle is not None and uncle.color is 'red':
            parent.color = uncle.color = 'black'
            grandparent.color = 'red'
            self.rebalance(grandparent)
            return
        if grandparent.left is not None and parent is not None and parent.right is not None:
            if node.key is parent.right.key and parent.key is grandparent.left.key:
                self.left_rotate(parent)
                node = parent
                parent = node.parent
            elif node.key is parent.left.key and parent.key is grandparent.right.key:
                self.right_rotate(parent)
                node = parent
                parent = node.parent
            parent.color = 'black'
            grandparent.color = 'red'
            if node.key is parent.left.key:
                self.right_rotate(grandparent)
            else:
                self.left_rotate(grandparent)

    def get_grandparent(self, node):
        if node.parent is None:
            return None
        return node.parent.parent

    def get_uncle(self, node):
        grandparent = None
        if node.parent is not None:
            grandparent = node.parent.parent
        if grandparent is None:
            return None
        if grandparent.left is None:
            return None
        if grandparent.left.key is node.parent.key:
            return grandparent.right
        else:
            return grandparent.left

    def set_child(self, parent, which_child, child):
        if which_child is not 'left' and which_child is not 'right':
            return False
        if which_child is 'left':
            parent.left = child
        else:
            parent.right = child
        if child is not None:
            child.parent = parent
        return True

    def replace_child(self, parent, curr_child, new_child):
        if parent.left is not None or curr_child is not None or parent.right is not None:
            if parent.left.key is curr_child.key:
                return self.set_child(parent, 'left', new_child)
            elif parent.right.key is curr_child.key:
                return self.set_child(parent, 'right', new_child)
        return False
