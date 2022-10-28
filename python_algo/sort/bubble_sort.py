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


if __name__ == '__main__':
    unsorted = [21, 2, 12, 3, 54, 78, 2, 6, 10, 12]
    print(bubble_sort(unsorted))
