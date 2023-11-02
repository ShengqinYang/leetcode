# 归并排序：
'''
6. 归并排序
和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(n log n）的时间复杂度。代价是需要额外的内存空间。

归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。归并排序是一种稳定的排序方法。
将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。

6.1 算法描述
把长度为n的输入序列分成两个长度为n/2的子序列；
对这两个子序列分别采用归并排序；
将两个排序好的子序列合并成一个最终的排序序列。

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


def merge_sort_way3(array):
    lenght = len(array)
    if lenght <= 1:
        return array
    m = lenght // 2
    left = merge_sort_way2(array[:m])
    right = merge_sort_way2(array[m:])
    return merge3(left, right)


def merge3(left, right):
    new_list = []
    ll, rr = 0, 0
    while ll < len(left) and rr < len(right):
        if left[ll] < right[rr]:
            new_list.append(left[ll])
            ll += 1
        else:
            new_list.append(right[rr])
            rr += 1
    new_list += left[ll:]
    new_list += right[rr:]
    return new_list


# 方案三递归实现
def merge_sort_third(array):
    if len(array) <= 1:
        return array
    # 将数组拆分成2部分
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    # 递归地对子数组进行排序
    left = merge_sort_third(left_array)
    right = merge_sort_third(right_array)

    # 合并两个有序数组排序
    return merge_third(left, right)


def merge_third(left, right):
    temp = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # 两个有序数组依次对比
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1

    temp.extend(left[i:])
    temp.extend(right[j:])
    return temp


if __name__ == '__main__':
    array = [11, 8, 3, 9, 7, 1, 2, 5, 12]
    r = merge_sort_way3(array)
    print(r)
    # low = 0
    # high = len(array) - 1
    # sorted = merge_sort(array, low, high)
    # print(array)

    print(merge_sort_third(array))
