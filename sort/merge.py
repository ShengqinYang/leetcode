def bubble_sort(unsorted):
    lenght = len(unsorted)
    is_ex = False
    for i in range(0, lenght):
        for j in range(0, lenght - i - 1):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                is_ex = True
        if not is_ex: break
    return unsorted


def insert_sort(unsorted):
    lenght = len(unsorted)
    for i in range(1, lenght):
        temp = unsorted[i]
        j = i - 1
        while j >= 0 and unsorted[j] > temp:
            unsorted[j + 1] = unsorted[j]
            j -= 1
        unsorted[j + 1] = temp
    return unsorted


def select_sort(unsorted):
    for i in range(len(unsorted)):
        min_v = i
        for j in range(i + 1, len(unsorted)):
            if unsorted[j] < unsorted[min_v]:
                min_v = j
        unsorted[i], unsorted[min_v] = unsorted[min_v], unsorted[i]
    return unsorted


if __name__ == '__main__':
    unsorted = [21, -2, 12, 3, 54, 78, 2, 6, 10, 12]
    # r = bubble_sort(unsorted)
    # r = insert_sort(unsorted)
    r = select_sort(unsorted)
    print(r)
