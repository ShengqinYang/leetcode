# 归并排序：
'''
归并排序的核心思想还是蛮简单的。如果要排序一个数组，我们先把数组从中间分成前后两部分，然后对前后两部分分别排序，再将排好序的两部分合并在一起，
这样整个数组就都有序了。
            11 8 3 9 7 1 2 5
分      11 8 3 9          7 1 2 5
解    11 8     3 9     7 1     2 5

合    8 11     3 9     1 7     2 5
并      3 8 9 11         1 2 5 7
            1 2 3 5 7 8 9 11

'''

# 两种写法：
# 第一种：
from typing import List


def merge_sort(a: List[int], low: int, high: int):
    # The indices are inclusive for both low and high.
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high)
        _merge(a, low, mid, high)


def _merge(a: List[int], low: int, mid: int, high: int):
    # a[low:mid], a[mid+1, high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp


# 第二种：
def merge(left, right):
    ll, rr = 0, 0
    new_list = []
    while ll < len(left) and rr < len(right):
        if left[ll] > right[rr]:
            new_list.append(right[rr])
            rr += 1
        else:
            new_list.append(left[ll])
            ll += 1
    new_list += left[ll:]
    new_list += right[rr:]
    return new_list


def merge_sort_way2(array: list):
    lenght = len(array)

    if lenght <= 1:
        return array

    m = lenght // 2
    left = merge_sort_way2(array[:m])
    right = merge_sort_way2(array[m:])
    return merge(left, right)


if __name__ == '__main__':
    array = [11, 8, 3, 9, 7, 1, 2, 5, 12]
    # r = merge_sort_way2(array)
    # print(r)
    low = 0
    high = len(array) - 1
    sorted = merge_sort(array, low, high)
    print(array)
