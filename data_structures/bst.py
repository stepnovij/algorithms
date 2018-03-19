"""
Binary Search Tree
"""


class Node:
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.left = kwargs.get('left')
        self.right = kwargs.get('right')


class Bst:
    def __init__(self, head):
        self.head = head

    def add_node(self, node):
        next_node = self.head
        while True:
            if next_node.data > node.data:
                if next_node.left:
                    next_node = next_node.left
                else:
                    next_node.left = node
                    return
            else:
                if next_node.right:
                    next_node = next_node.right
                else:
                    next_node.right = node
                    return

    def __repr__(self):
        node = self.head
        height = 0
        print_string = height*" " + "({})\n".format(node.data)
        if node.right:
            print_string += height*" " + "\\\n"
            height += 1
            print_string += height * " " + "{}"
        if node.left:
            print_string += "/\n" + height*" "
            height += 1
            print_string += height * " " + "{}"



if __name__ == "__main__":
    head = Node(10)
    bst = Bst(head)
    bst.add_node(Node(20))
    bst.add_node(Node(30))