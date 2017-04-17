import random
import string


size = len(string.ascii_letters) - 1
sorting_array = [string.ascii_letters[random.randint(0, size)] for x in range(1000)]


# TODO: plot graph with number of access
def count_array_accesses():
    pass


def compare_chars(a: string, b: string) -> int:
    if ord(a) > ord(b):
        return -1
    if ord(a) < ord(b):
        return 1
    return 0


def selection_sort(array: list) -> list:
    for start_indx in range(len(array)):
        min_indx = 0
        for indx, el in enumerate(array[start_indx:]):
            sub_index = min_indx + start_indx
            if compare_chars(array[sub_index], el) == -1:
                min_indx = indx
            if start_indx + indx == len(array) - 1:
                array[sub_index], array[start_indx] = array[start_indx], array[sub_index]
    return array


if __name__ == '__main__':
    res = selection_sort(sorting_array)
    print(res)
    print([ord(x) for x in res])