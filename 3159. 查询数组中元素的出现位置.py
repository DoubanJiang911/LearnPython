class Solution:
    def occurrencesOfElement(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        temp_list = []
        for index, num in enumerate(nums):
            if num != x:
                continue
            else:
                temp_list.append(index)
        length = len(temp_list)
        result = []
        for q in queries:
            if q > length:
                result.append(-1)
            else:
                result.append(temp_list[q-1])
        return result
