def partition(a, low, high):
    '''
    pivot是分区点，他的左边的数要比他小，他右边的数要比他大
    '''
    pivot = a[low]
    j = low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            print(a[j], a[i])
            a[j], a[i] = a[i], a[j]
    a[low], a[j] = a[j], a[low]
    return j


def _quick_sort_between(a, low, high):
    if high > low:
        q = partition(a, low, high)
        _quick_sort_between(a, low, q - 1)
        _quick_sort_between(a, q + 1, high)


if __name__ == "__main__":
    a = [21, 2, 12, 3, 54, 78, 2, 6, 10, 12]
    # a = [21, 2, 12]
    _quick_sort_between(a, 0, len(a) - 1)
    print(a)
