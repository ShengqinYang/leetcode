'''
7. 快速排序
快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

7.1 算法描述
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

从数列中挑出一个元素，称为 “基准”（pivot）；
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

'''


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
