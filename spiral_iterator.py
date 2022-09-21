# 给定二维数组实现螺形输出
# arrays = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# 输出：[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def myfunc(arrays):
    rows = len(arrays)
    if rows == 0:
        return []
    elif rows == 1:
        return arrays[0]
    else:
        cols = len(arrays[0])
        if cols == 0:
            return []
        if cols == 1:
            for i in arrays:
                return i[0]
        else:
            l = []
            r = []
            new_arrays =[]
            for i in range(1, rows - 1):
                l.append(arrays[i][0])
                r.append(arrays[i][-1])
                new_arrays.append(arrays[i][1:-1])
            return arrays[0] + r + arrays[-1][::-1] + l[::-1] + myfunc(arrays=new_arrays)


if __name__ == '__main__':
    arrays = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    # arrays = [
    #     [1],
    #     [5],
    #     [9]
    # ]
    # arrays = [[1, 2, 3, 4]]
    m = myfunc(arrays)
    print(m)
