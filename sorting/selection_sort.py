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


def swap_elements(array: list, from_indx: int, on_indx: int) -> list:
    print(on_indx, from_indx)
    elm = array[on_indx]
    array[on_indx] = array[from_indx]
    array[from_indx] = elm
    return array


def selection_sort(array: list) -> list:
    for start_indx in range(len(array)):

        min_indx = start_indx
        array_to_find_min = array[start_indx:]

        for indx, el in enumerate(array_to_find_min[1:]):

            print(array[min_indx], el, compare_chars(array[min_indx], el))

            if compare_chars(array_to_find_min[min_indx], el) == -1:
                min_indx = indx

            if indx == len(array_to_find_min) + 1:
                print('Here')
                array[start_indx:] = swap_elements(array_to_find_min[start_indx:], min_indx, start_indx)
                print(array[start_indx:], array[min_indx])

    return array


if __name__ == '__main__':
    print(selection_sort(sorting_array))