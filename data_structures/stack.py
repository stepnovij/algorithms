"""
Stack

pop
push
is_empty
"""
# TODO: peek


class Node:
    def __init__(self, data, previous=None):
        self.data = data
        self.previous = previous

    def __repr__(self):
        if self.previous:
            return "{} - {}".format(self.data, self.previous)
        return "{}".format(self.data)


class Stack:
    def __init__(self, node):
        self.last = node

    def push(self, node):
        node.previous = self.last
        self.last = node

    def pop(self):
        node = self.last
        self.last = node.previous
        node.previous = None
        return node

    def is_empty(self):
        return self.last is None

    def __repr__(self):
        node = self.last
        total_string = '{}'.format(self.last.data)
        if node.previous:
            total_string += '->{}'.format(node.__repr__())
        return total_string


if __name__ == "__main__":
    n1 = Node(10)
    s = Stack(n1)

    s.push(Node(15))
    s.push(Node(25))
    s.push(Node(30))
    s.push(Node(21))
    s.push(Node(22))
    s.push(Node(23))
    node = s.pop()
    assert node.data == 23
    node = s.pop()
    assert node.data == 22
    node = s.pop()
    assert node.data == 21
    assert s.is_empty() == False
    node = s.pop()
    node = s.pop()
    node = s.pop()
    node = s.pop()
    assert s.is_empty() == True
