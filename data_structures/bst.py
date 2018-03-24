"""
search O(log n)
insert O(log n)

depends on tree, if not balanced then worst case is O(n)

Binary Search Tree
"""

# TODO: add remove
# TODO: add __repr__
# TODO: add rebuild tree


class Node:
    def __init__(self, data, *args, **kwargs):
        self.data = data
        self.left = kwargs.get('left')
        self.right = kwargs.get('right')


class Bst:
    def __init__(self, head):
        self.head = head

    def insert_node(self, node):
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

    def _print_one_level_data(self):
        pass

    def _get_node(self, node, seen_nodes):
        if node.left or node.right:
            if node.left and node.left not in seen_nodes:
                return node.left
            elif node.right and node.right not in seen_nodes:
                return node.right
            else:
                return None

    @property
    def height(self):
        node = self.head

        height = 0
        path = []
        seen_nodes = []

        path.append(node)
        seen_nodes.append(node)

        while True:
            node = self._get_node(node, seen_nodes)
            if node:
                path.append(node)
                seen_nodes.append(node)
            else:
                if len(path) < 1:
                    break
                node = path[-2]
                if node == self.head:
                    if self._get_node(node, seen_nodes) is None:
                        break
                path_height = len(path)
                if path_height > height:
                    height = path_height
                path = path[:-1]

        return height

    def get_nodes_levels(self, level):
        #
        current_nodes = dict()
        current_level = 1
        current_nodes[current_level] = [self.head]
        #
        while current_level != level:
            next_level_nodes = []
            for node in current_nodes[current_level]:

                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)

            current_level += 1
            if len(next_level_nodes) == 0:
                break
            current_nodes[current_level] = next_level_nodes

        return current_nodes


if __name__ == "__main__":
    head = Node(10)

    bst = Bst(head)
    bst.insert_node(Node(20))
    bst.insert_node(Node(30))
    bst.insert_node(Node(5))
    bst.insert_node(Node(25))
    bst.insert_node(Node(40))

    x = bst.height
    print("Height of the tree is: ", x)

    res = bst.get_nodes_levels(5)
    print(res)
    print(bst)
