class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def insert(self, d):
        if d <= self.data:
            if self.left:
                return self.left.insert(d)
            else:
                self.left = Node(d)
                return Node(d)
        else:
            if self.right:
                return self.right.insert(d)
            else:
                self.right = Node(d)
                return Node(d)

    def find(self, d):
        if self.data == d:
            return d
        elif d <= self.data and self.left:
            return self.left.find(d)
        elif d > self.data and self.right:
            return self.right.find(d)
        return None

    def inorder(self, l):
        if self.left:
            self.left.inorder(l)
        l.append(self.data)
        if self.right:
            self.right.inorder(l)
        return l


class BST(object):
    def __init__(self):
        self.root = None

    # return True if successfully inserted, false if exists
    def insert(self, d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return Node(d)

    # return True if d is found in tree, false otherwise
    def find(self, d):
        if self.root:
            return self.root.find(d)
        else:
            return None

    # return list of inorder elements
    def inorder(self):
        if self.root:
            return self.root.inorder([])
        else:
            return []