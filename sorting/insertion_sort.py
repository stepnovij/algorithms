import random
import string


size = len(string.ascii_letters) - 1
sorting_array = [string.ascii_letters[random.randint(0, size)] for x in range(10)]


def compare_chars(a: string, b: string) -> int:
    if ord(a) > ord(b):
        return -1
    if ord(a) < ord(b):
        return 1
    return 0


def swap_elements(array: list, from_indx: int, on_indx: int) -> tuple:
    elm = array[on_indx]
    array[on_indx] = array[from_indx]
    array[from_indx] = elm
    return array[from_indx], array[on_indx]


def insertion_sort(array: list) -> list:
    for start_indx in range(len(array)):
        if not start_indx > 0:
            continue
        for index_reverse, element in reversed(list(enumerate(array[start_indx:]))):
            print(start_indx, index_reverse)
            if compare_chars(array[index_reverse], array[index_reverse - 1]) != -1:
                break
            array[index_reverse - 1], array[index_reverse] = array[index_reverse], array[index_reverse - 1]
    return array


if __name__ == '__main__':
    res = insertion_sort(sorting_array)
    print(res)
    print([ord(x) for x in res])