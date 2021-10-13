# 作者：路路通关
# 链接：https://www.nowcoder.com/discuss/246780?type=1&order=0&pos=5&page=1&channel=1009&source_id=discuss_tag
# 来源：牛客网

# class Solution(object):
#
#
#     def lenLongestFibSubseq(self, A):
#     """
#     :type A: List[int]
#     :rtype: int
#     """
#     s = set(A)
#     n = len(A)
#     res = 0
#     for i in range(n - 1):
#         for j in range(i 1, n):
#         a, b = A[i], A[j]
#     count = 2
#     while a b in s:
#         a, b = b, a
#     b
#     count = 1
#     res = max(res, count)
#     return res if res > 2 else 0

# 1,1,2,3,5,8,13,21,34

# 斐波那契
import collections


def feibo():
    sl = []
    for i in range(20):
        if i == 0 or i == 1:
            sl.append(1)
        else:
            sl.append(sl[i - 2] + sl[i - 1])
    return sl


# 最长的斐波那契子序列的长度
def feibo_zi(mylist):
    """
    :type mylist: List[int]
    :rtype: int
    """
    dp = collections.defaultdict(int)
    myset = set(mylist)
    for j in range(len(mylist)):
        for i in range(j):
            if mylist[j] - mylist[i] < mylist[i] and mylist[j] - mylist[i] in myset:
                dp[mylist[i], mylist[j]] = dp.get((mylist[j] - mylist[i], mylist[i]), 2) + 1
    print(dp)
    return max(dp.values() or [0])


if __name__ == '__main__':
    feibo()
    mylist = [1, 3, 7, 11, 12, 14, 18]
    lenfeibo = feibo_zi(mylist)
    print(lenfeibo)
