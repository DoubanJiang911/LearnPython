class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        a = 0
        b = len(nums) - 1
        sums = 0
        while a < b:
            ta = str(nums[a])
            tb = str(nums[b])
            strtype = ta + tb
            inttype = int(strtype)
            sums += inttype
            a += 1
            b -= 1
        if a == b:
            sums += nums[(len(nums)-1)//2]
        return sums
