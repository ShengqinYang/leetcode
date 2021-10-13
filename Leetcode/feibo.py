'''
斐波那契数列：0、1、1、2、3、5、8、13、21、34...
设数列长度为n
斐波那契数列指的是每一项都等于前两项之和的数列，定义为F[1]=1，F[2]=1, F[n]=F[n-1]+F[n-2]（n>=3）。

递归使用条件：1.大问题可以拆解成小问题。2.每个小问题都可以用同一方法实现。3.有终止条件
斐波那契：每个值都等于前两项之和
'''


def feibo_dg(n):
    '''
    递归实现
    :param n:
    :return:
    '''
    if n <= 0:
        return 1
    else:
        return (feibo_dg(n - 1) + feibo_dg(n - 2))


def feibo(capacity):
    n1 = 0
    n2 = 1
    count = 0
    if capacity <= 0:
        return n1
    elif capacity == 1 or capacity == 2:
        return n2
    else:
        while count < capacity:
            n1, n2 = n2, n2 + n1
            count += 1
            print(n2, end=' ')


if __name__ == '__main__':
    # result = feibo(capacity=10)
    # print(result, end=' ')

    for i in range(11):
        result = feibo_dg(i)
        print(result, end=' ')
