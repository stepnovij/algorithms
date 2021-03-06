import random


nodes = list(range(0, 10**7))
connection = list(range(0, 10**7))
weights = [1 for n in range(0, 10**7)]
arr_number_of_checks = []


def is_connected(a, b):
    return get_root(a) == get_root(b)


def connect(a, b):
    if is_connected(a, b):
        return
    wighted_union(a, b)


def get_root(element):
    number_of_checks = 1
    while connection[element] != element:
        number_of_checks += 1
        element = connection[element]
    arr_number_of_checks.append(number_of_checks)
    return element


def wighted_union(a, b):
    root_of_a = get_root(a)
    root_of_b = get_root(b)
    if weights[root_of_a] > weights[root_of_b]:
        weights[root_of_a] += weights[root_of_b]
        connection[b] = root_of_a
    else:
        connection[a] = root_of_b
        weights[root_of_b] += weights[root_of_a]
    connection[a] = root_of_b


if __name__ == '__main__':
    number_of_accesses = 0
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
    res = [
        connect(random.randint(0, 10**7-1), random.randint(0, 10**7-1)) for r in range(10**6)
    ]
    print(float(sum(arr_number_of_checks))/10**6)