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


if __name__ == '__main__':
    unsorted = [21, 2, 12, 3, 54, 78, 2, 6, 10, 12]
    print(select_sort(unsorted))
