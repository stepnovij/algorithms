import random
import string


size = len(string.ascii_letters) - 1
sorting_array = [string.ascii_letters[random.randint(0, size)] for x in range(1000)]


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


def insertion_sort(array: list):
    for start_indx in range(len(array)+1):
        for index_reverse, element in reversed(list(enumerate(array[:start_indx]))):
            if index_reverse == 0:
                continue
            if compare_chars(array[index_reverse - 1], array[index_reverse]) != -1:
                break
            array[index_reverse - 1], array[index_reverse] = array[index_reverse], array[index_reverse - 1]


if __name__ == '__main__':
    #print(sorting_array)
    insertion_sort(sorting_array)
    print(sorting_array)
    print([ord(x) for x in sorting_array])