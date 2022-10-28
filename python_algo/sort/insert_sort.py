
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


if __name__ == '__main__':
    unsorted = [21, 2, 12, 3, 54, 78, 2, 6, 10, 12]
    print(insert_sort(unsorted))
