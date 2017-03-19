nodes = list(range(0, 10**7))
connection = list(range(0, 10**7))


def is_connected(a, b):
    return get_root(a) == get_root(b)


def connect(a, b):
    if is_connected(a, b):
        return
    union_effective(a, b)


def get_root(element):
    while connection[element] != element:
        element = connection[element]
    return element


def union_not_effective(a, b):
    root_of_a = get_root(a)
    root_of_b = get_root(b)
    for indx, val in enumerate(connection):
        if connection[indx] == root_of_a:
            connection[indx] = root_of_b


def union_effective(a, b):
    root_of_a = get_root(a)
    root_of_b = get_root(b)
    connection[a] = root_of_b


if __name__ == '__main__':
    print(is_connected(0, 1))
    print(is_connected(0, 10))
    connect(3, 4)
    connect(0, 1)
    connect(10, 3)
    connect(4, 3)
    connect(88891, 3)
    connect(8889, 8890)
    print(is_connected(4, 3))
    print(is_connected(10, 3))
    print(is_connected(0, 1))
    print(is_connected(8889, 8890))
    print(is_connected(88891, 3))