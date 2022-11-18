# 26. 删除有序数组中的重复项-双指针思路
class Solution:
    def removeDuplicates(self, nums):
        length = len(nums)
        p, q = 0, 1
        while q < length:
            if nums[p] != nums[q]:
                if q - p > 1:
                    nums[p + 1] = nums[q]
                p += 1
            q += 1
        return p + 1, nums[:p + 1]


if __name__ == '__main__':
    nums = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 6, 6, 7, 9]
    sol = Solution()
    index, result = sol.removeDuplicates(nums)
    print(index, result)
