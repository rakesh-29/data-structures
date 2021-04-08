from collections import deque

class queue:
    def __init__(self):
        self.buffer = deque()

    def enque(self, value):
        self.buffer.appendleft(value)

    def deque(self):
        return self.buffer.pop()

    def top(self):
        return self.buffer[-1]

    def size(self):
        return len(self.buffer)

    def isempty(self):
        return len(self.buffer) == 0


class binarysearchtree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, value):
        if self.data == value:
            return
        if value < self.data:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = binarysearchtree(value)
        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = binarysearchtree(value)

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left == None and self.right == None:
                return None

            elif self.left == None:
                '''
                temp = self.right
                self = None
                return temp'''
                return self.right

            elif self.right == None:
                '''
                temp = self.right
                self = None
                return temp 
                '''
                return self.left

            else:
                min_value = self.right.find_min()
                self.data = min_value
                self.right = self.right.delete(min_value)

        return self

    def find_max(self):
        temp = self.right
        while temp is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        temp = self.left
        while temp is None:
            return self.data
        return self.left.find_min()

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements = elements + self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements = elements + self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements = elements + self.left.pre_order_traversal()

        if self.right:
            elements = elements + self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements = elements + self.left.pre_order_traversal()

        if self.right:
            elements = elements + self.right.pre_order_traversal()

        elements.append(self.data)

        return elements

    def level_order_traversal(self):
        if self is None:
            return None

        elements = []
        que = queue()
        que.enque(self.data)

        while que.size() > 0:
            node = que.deque()
            elements.append(node)

            if node.left:
                que.enque(node.left)
            if node.right:
                que.enque(node.right)

        return elements


def build_tree(elements):
    root = binarysearchtree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ", numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ", numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ", numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]




