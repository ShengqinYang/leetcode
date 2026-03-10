"""
leetcode198:打家劫舍:你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例 1:
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1)，然后偷窃 3 号房屋 (金额 = 3)。偷窃到的最高金额 = 1 + 3 = 4。
示例 2:
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2)，偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。偷窃到的最高金额 = 2 + 9 + 1 = 12。

方程：
设 dp[i] 为偷到第 i 间房时能获得的最大金额。
你站在第i个房子，偷或不偷
偷：dp[i] = dp[i-2] + nums[i] (因为不能偷相邻的，所以只能在i-2的基础上偷当前的房子)
不偷：dp[i] = dp[i-1]（不抢第 i 间： 那么你的收益就等于偷完前一间房的收益，即 dp[i-1]）
dp[i] = max(dp[i-1], dp[i-2] + nums[i])


"""


def rob(nums):
    pre, cur = 0, 0
    for num in nums:
        pre, cur = cur, max(cur, pre + num)
    return cur
    
    
def rob1(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev_prev = 0
    prev = 0
    for i in nums:
        cur_max = max(prev_prev+i, prev)
        prev_prev = prev
        prev = cur_max
    return prev


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))
    print(rob([2, 7, 9, 3, 1]))
    print(rob([1, 5, 2, 9, 7]))
    print(rob([1]))



