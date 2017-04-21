import random
import string

from insertion_sort import insertion_sort

size = len(string.ascii_letters) - 1
sorting_array = [string.ascii_letters[random.randint(0, size)] for x in range(1000)]


def compare_chars(a: string, b: string) -> int:
    if ord(a) > ord(b):
        return -1
    if ord(a) < ord(b):
        return 1
    return 0


def shell_sort(array: list) -> list:
    h = len(array)
    while True:
        h //= 2
        print(h)
        start_from = 0
        while (len(array) - 1 - start_from) // h > 0:
            indx_range = list(range(start_from, len(array), h))
            for indx, step in enumerate(indx_range):
                if indx == 0:
                    continue
                previous_indx = indx_range[indx - 1]
                if h > 1:
                    if compare_chars(array[previous_indx], array[step]) == -1:
                        array[previous_indx], array[step] = array[step], array[previous_indx]
                elif h == 1:
                    insertion_sort(array)
            if h == 1:
                return array
            start_from += 1


if __name__ == '__main__':
    res = shell_sort(sorting_array)
    print(res)
    print([ord(x) for x in res])