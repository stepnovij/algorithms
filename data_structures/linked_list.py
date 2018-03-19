"""
linked list with insert, append, find, delete, length, and print methods

insert/deleting at beginning O(1)
insert/deleting when last element is not known O(n)

finding element: O(n)
get length: O(n)
"""


class NoElmInLinkedList(Exception):
    pass


class Node:
    def __init__(self, data, next=None):
        self.id = data
        self.next = next

    def __repr__(self):
        if self.next:
            return "{} - {}".format(self.id, self.next)
        return "{}".format(self.id)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_node(self, node):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def find(self, elm):
        node = self.head
        while node.next:
            if elm == node.id:
                return node
            else:
                node = node.next
        else:
            raise NoElmInLinkedList

    def insert(self, after, data):
        node = self.find(after)
        previous_next = node.next
        node.next = Node(data, previous_next)

    def delete(self, elm):
        node = self.head
        while node.next:
            if node.next.id == elm:
                node.next = node.next.next
                return
            else:
                node = node.next
        else:
            raise NoElmInLinkedList

    def __len__(self):
        count = 1
        node = self.head
        #
        while node:
            node = node.next
            count += 1
        return count

    def __repr__(self):
        total_string = ''
        node = self.head
        total_string += '({id})'.format(id=node.id)
        if node.next:
            total_string += '->{}'.format(node.__repr__())
        return total_string


def create_linked_list():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    n10 = Node(10)
    #
    l = LinkedList(n1)
    l.add_node(n2)
    l.add_node(n3)
    l.add_node(n4)
    l.add_node(n5)
    l.add_node(n6)
    l.add_node(n7)
    l.add_node(n8)
    l.add_node(n9)
    l.add_node(n10)
    return l


if __name__ == '__main__':
    linked_list = create_linked_list()
    print(linked_list)
    #
    node = linked_list.find(2)
    print(node.id)
    node = linked_list.find(1)
    print(node.id)
    #
    print("Length of linked list {}".format(str(len(linked_list))))
    #
    linked_list.insert(after=5, data=100)
    print(linked_list)
    #
    print("Length of linked list {}".format(str(len(linked_list))))
    linked_list.delete(8)
    print(linked_list)
    print("Length of linked list {}".format(str(len(linked_list))))