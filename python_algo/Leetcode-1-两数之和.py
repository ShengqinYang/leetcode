'''
两数之和
题目：
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
    并返回他们的数组下标.你可以假设每种输入只会对应一个答案。
    但是，你不能重复利用这个数组中同样的元素
示例：
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] f+ nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
考点：哈希
'''





class Myclass():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    @property
    def sum_of_two_nums_01(self):
        '''时间复杂度n^2'''
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]

    @property
    def sum_of_two_nums_02(self):
        '''时间复杂度n'''
        # 产生散列表
        hash_ = dict(zip(nums, range(len(nums))))
        print(hash_)
        # 反向寻找
        for i in range(len(self.nums)):
            ta = self.target - self.nums[i]
            print(ta)
            if hash_.get(ta) and i != hash_.get(ta):
                return [i, hash_.get(ta)]

    def test(self):
        hash_ = dict(zip(nums, range(len(nums))))
        print(hash_)
        for i in range(len(self.nums)):
            ta = self.target - hash_.get(nums[i])
            if hash_.get(ta) and i != hash_.get(ta):
                return [i,hash_.get(ta)]


if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    # target = 9
    nums = [3, 3, 3]
    target = 6
    # my = Myclass(nums, target)
    # # print(my.sum_of_two_nums_01)
    # print(my.sum_of_two_nums_02)
