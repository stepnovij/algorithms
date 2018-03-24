"""
Queue with methods like enqueue and dequeue methods

enqueue = O(1)
dequeue = O(1)
"""


class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __repr__(self):
        if self.next:
            return "{} - {}".format(self.data, self.next)
        return "{}".format(self.data)


class Queue:
    def __init__(self, node):
        self.top = node
        self.last = node

    def enqueue(self, node):
        self.last.next = node
        self.last = node

    def dequeue(self):
        if self.top:
            node = self.top
            self.top = self.top.next
            if node == self.last:
                self.last = None
            return node

    def __repr__(self):
        node = self.top
        total_string = '{}'.format(self.top.data)
        if node.previous:
            total_string += '->{}'.format(node.__repr__())
        return total_string


if __name__ == "__main__":
    n1 = Node(10)
    q = Queue(n1)

    q.enqueue(Node(15))
    q.enqueue(Node(25))
    q.enqueue(Node(21))
    r = q.dequeue()
    assert r.data == 10
    r = q.dequeue()
    assert r.data == 15
    r = q.dequeue()
    assert r.data == 25
    r = q.dequeue()
    assert r.data == 21
    r = q.dequeue()
    assert q.last is None
    assert q.top is None