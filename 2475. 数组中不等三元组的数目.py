from collections import Counter


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        n = len(nums)
        t = 0
        for v in count.values():
            res += t * v * (n - t - v)
            t += v
        return res
# 使用Counter函数，按照nums各个元素出现次数形成哈希表
# 以v作为指针，记录三元组的中间数对应的出现次数，t记录v指针当前左边全部元素对应的出现次数，n-t-v记录v指针当前右边全部元素对应的出现次数
