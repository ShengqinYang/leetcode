'''
1、冒泡排序（Bubble Sort）
冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

1.1 算法描述：核心-找最大的，最大的往后移动
比较相邻的元素。如果第一个比第二个大，就交换它们两个；
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
针对所有的元素重复以上的步骤，除了最后一个；
重复步骤1~3，直到排序完成。

冒泡排序的时间复杂度也是O(n^2)。
'''


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
