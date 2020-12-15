# 16进制转10进制

# 例：2AF5换算成10进制:
# 用竖式计算：
# 第0位： 5 * 16^0 =
# 第1位： F * 16^1 = 240
# 第2位： A * 16^2= 2560
# 第3位： 2 * 16^3 = 8192
# 5 * 16 ^ 0 + F * 16 ^ 1 + A * 16 ^ 2 + 2 * 16 ^ 3 = 10997
import math


def jinzhi(key):
    keyl = list(key)
    reto = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    mlt = 0
    for i, v in enumerate(keyl):
        if reto.get(v):
            mlt += reto.get(v) * math.pow(16, len(keyl) - i - 1)
        else:
            mlt += int(v) * math.pow(16, len(keyl) - i - 1)
    return mlt


if __name__ == '__main__':
    key = '2AF5'
    # key = '1A'
    result = jinzhi(key)
    print(result)
    # mlis = ['sd', 'sdf', 'tew', 'df4rs']
    # for i, v in enumerate(mlis):
    #     print('zhengxu', i, 'daoxu', len(mlis) - i - 1)
