'''
二分查找
使用条件：
    1.必须是顺序表【即：数组】做数据的存贮，因为需要通过下标来便捷访问
    2.必须是有序的数组
    3.数据量太小不推荐二分法，直接遍历就行。例外：如果数据之间比较很耗时的情况下无论数组大小，都推荐二分查找
    4.数据量太大不推荐二分法，因为数组是一个连续存储的空间，对内存要求比较苛刻，假如1G数据，那么则需要1G连续的内存空间

时间复杂度：n、n/2、n/4、n/8....n/2^k , n/2^k=1 --> k =log2n

注意点: 1.循环退出条件：是 high >= low，而不是 high > low

       2.mid 的取值：(low+high)/2，为了防止数字太大而导致溢出，优化中间取值：low+(high-low)/2
          【注解：low+(high-low)/2 = (low*2)/2+(high-low)/2 = (low*2+high-low)/2 = (high+low)/2】

       3.low和high的值更新：low=mid+1，high=mid-1。注意这里的 +1 和 -1，如果直接写成 low=mid 或者 high=mid，就可能会发生死循环。
            比如，当 high=3，low=3 时，如果 a[3]不等于 value，就会导致一直循环不退出。

应用场景：假设我们有 1000 万个整数数据，每个数据占 8 个字节，如何设计数据结构和算法，快速判断某个整数是否出现在这 1000 万数据中？
        我们希望这个功能不要占用太多的内存空间，最多不要超过 100MB。

变形二分查找：
    数组中有多个重复的值的时候：
    1.查找第一个值等于给定值的元素
    2.查找最后一个值等于给定值的元素
    3.查找第一个大于等于给定值的元素
    4.查找最后一个小于等于给定值的元素
'''


def array_search(param, aim):
    '''非递归实现
    :param param: 有序数组
    :param aim: 目标值
    :return: True or False
    '''
    low = 0
    high = len(param) - 1
    while high >= low:
        mid = (low + high) // 2
        if param[mid] == aim:
            return True
        elif aim > param[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return False


def recursion_search(param, low, high, aim):
    '''
    递归实现
    :param param: 有序数组
    :param low: 低位索引
    :param high: 高位索引
    :param aim: 目标值
    :return: True or False
    '''
    if low > high:
        return False
    mid = (high + low) // 2
    if param[mid] == aim:
        return True
    elif param[mid] < aim:
        return recursion_search(param, mid + 1, high, aim)
    else:
        return recursion_search(param, low, mid - 1, aim)


def shift_first(param, aim):
    '''
    1.查找第一个值等于给定值的元素
    例如：3，5，6，7，7，8，9，10 第一个值等于 7 的元素下标就是 3
    :param param:
    :param aim:
    :return:下标 or False
    '''
    low = 0
    high = len(param) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if param[mid] > aim:
            high = mid - 1
        elif param[mid] < aim:
            low = mid + 1
        else:
            if mid == 0 or param[mid - 1] != aim:
                return mid
            else:
                high = mid - 1
    return False


def shift_second(param, aim):
    '''
    2.查找最后一个值等于给定值的元素
    例如：3，5，6，7，7，7，8，9，10 最后一个值等于 7 的元素下标就是 5
    :param param:
    :param aim:
    :return:下标 or False
    '''
    low = 0
    high = len(param) - 1
    while high >= low:
        mid = low + (high - low) // 2
        if param[mid] > aim:
            high = mid - 1
        elif param[mid] < aim:
            low = mid + 1
        else:
            if mid == 0 or param[mid + 1] != aim:
                return mid
            else:
                low = mid + 1
    return False


def shift_third(param, aim):
    '''
    3.查找第一个大于等于给定值的元素
    例如：3，5，6，7，7，7，8，9，10 第一个大于等于 7 的元素就是下标为3的元素 7
    :param param:
    :param aim:
    :return:
    '''
    low = 0
    high = len(param) - 1
    while high >= low:
        mid = low + (high - low) // 2
        if param[mid] >= aim:
            if mid == 0 or param[mid - 1] < aim:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return False


def shift_fourth(param, aim):
    '''
    4.查找最后一个小于等于给定值的元素
    例如：3，5，6，8，9，10 最后一个小于等于 7 的元素就是 6
    :param param:
    :param aim:
    :return:
    '''
    low = 0
    high = len(param) - 1
    while high >= low:
        mid = low + (high - low) // 2
        if param[mid] <= aim:
            if mid == 0 or param[mid + 1] > aim:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1


if __name__ == '__main__':
    aim = 20
    param = [1, 4, 5, 8, 11, 14, 17, 20, 23, 25, 25, 27, 29, 35, 64, 65, 78, 78, 79, 82, 90, 94, 96, 98, 99, 101]
    # result = array_search(param, aim)
    # print(result)

    # result = recursion_search(param, 0, len(param) - 1, aim)
    # print(result)

    # result = shift_first(param, aim=25)
    # print(result)
    #
    # result = shift_second(param, aim=25)
    # print(result)
    #
    # result = shift_third(param, aim=25)
    # print(result)
    #
    # result = shift_fourth(param, aim=25)
    # print(result)
