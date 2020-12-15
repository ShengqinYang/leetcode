# 思路：刚开始把所有的人放到一个列表里面去，报的数字不是3就把这个人放到列表的最后一个位置上面去，如果是3就把这个数字从列表中去掉。直到列表剩下两个人为止，
def josephus(n, k):
    # n代表总人数，k代表报数的数字
    List = list(range(1, n + 1))
    index = 0
    while List:
        temp = List.pop(0)
        index += 1
        if index == k:
            index = 0
            continue
        List.append(temp)
        if len(List) == 2:
            print(List)
            break


if __name__ == '__main__':
    josephus(41, 3)
