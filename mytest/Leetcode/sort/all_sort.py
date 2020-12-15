'''
极客时间 第11节：为什么插入排序比冒泡排序更受欢迎？
第一组：冒泡排序、插入排序、选择排序
    1.衡量一个排序算法的标准：时间复杂度、空间复杂度、稳定性【即排序完成后，值相等的的数不发生位置变化，则稳定行高】
    概念：原地排序（Sorted in place）。原地排序算法，就是特指空间复杂度是 O(1) 的排序算法
    时间复杂度：O(n^2)，比较适合小规模数据排序

排序动图：https://www.cnblogs.com/onepixel/articles/7674659.html
'''
import urllib
from typing import List


def bubble_sort(unsorted):
    '''
    冒泡排序，是原地排序，是稳定排序
    外环从头到尾遍历
    内环遍历到lenght-i-1
    两两比较大小，交换位置
    优化：如果某一轮的冒泡没有可以交换的值，说明已经达到有序
    '''
    lenght = len(unsorted)
    if_ex = False  # 提前退出循环标志
    for i in range(lenght):
        for j in range(lenght - i - 1):  # 两两交换的结果是最大的值已经放队尾
            if unsorted[j] > unsorted[j + 1]:  # 注意排序的稳定性，相等的时候不交换
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                if_ex = True  # 有交换
        if not if_ex:  # 表示该轮冒泡无可交换值，退出循环
            break
    return unsorted


def insert_sort(unsorted):
    '''
    插入排序，原地排序，稳定排序
    分两步：左边为有序部分，右边为无序部分
    它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    有序--无序 向前比较，找到最小的然后交换
    '''
    lenght = len(unsorted)
    for i in range(1, lenght):  # 从第一位开始，左侧是有序集合，右侧是无序集合
        temp = unsorted[i]  # 取出待插入的值
        j = i - 1  # 待插入的值的前一个位置开始倒叙查找
        while j >= 0 and unsorted[j] > temp:  # 如果待插入的值 小于右侧的比较值 则比较值右移【后移】一位
            unsorted[j + 1] = unsorted[j]  # 后移一位会替换之前的值，不用担心替换的是temp的位置
            j -= 1  # 下一个比较值位置
        unsorted[j + 1] = temp  # 插入值大于比较值时，插入比较值右侧【后面】
    return unsorted


def select_sort(unsorted):
    '''
    选择排序：也没分已经排序和未排序部分
    有序--无序 向后比较，找到最小的然后交换

    :param unsorted:
    :return:
    '''
    lenght = len(unsorted)
    for i in range(lenght):
        minindex = i
        for j in range(i + 1, lenght):
            if unsorted[j] < unsorted[minindex]:
                minindex = j
        unsorted[minindex], unsorted[i] = unsorted[i], unsorted[minindex]
    return unsorted


'''
极客时间：12 | 排序（下）：如何用快排思想在O(n)内查找第K大元素？
第二组：归并排序和快速排序
时间复杂度：O(nlogn)，比较适合大规模数据排序
归并排序：分解--合并，分治思想，适合用递归
'''


def merge_sort(unsorted, low, high):
    '''
    拆分
    :param unsorted:
    :param low:
    :param high:
    :return:
    '''
    if high > low:  # 停止拆分的条件
        mid = (low + high) // 2
        merge_sort(unsorted, low, mid)  # left数组
        merge_sort(unsorted, mid + 1, high)  # right数组
        return _merge_sort_between(unsorted, low, mid, high)  # 合并


def _merge_sort_between(unsorted, low, mid, high):
    '''
    有序合并
    :return:
    '''
    i, j = low, mid + 1
    temp = []
    while i <= mid and j <= high:
        if unsorted[i] < unsorted[j]:
            temp.append(i)
            i += 1
        else:
            temp.append(j)
            j += 1
    # 判断那个数组还有剩余
    if i <= mid:
        start = i
        end = mid
    else:
        start = j
        end = high
    # 剩余部分加到temp尾
    temp.extend(unsorted[start:end + 1])
    # 将tmp中的数组拷贝回A[p...r]
    unsorted[low:high + 1] = temp


def quick_sort(unsorted):
    pass


if __name__ == '__main__':
    unsorted = [21, 2, 12, 3, 54, 78, 2, 6, 10, 12]
    # sorted = bubble_sort(unsorted)
    # print(sorted)
    # sorted = insert_sort(unsorted)
    # print(sorted)
    # sorted = select_sort(unsorted)
    # print(sorted)
    low = 0
    high = len(unsorted) - 1
    sorted = merge_sort(unsorted, low, high)
    print(unsorted)
