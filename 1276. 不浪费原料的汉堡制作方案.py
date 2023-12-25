class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        temp = tomatoSlices - 2 * cheeseSlices
        if temp < 0 or temp % 2 != 0:
            return []
        x = temp // 2
        y = tomatoSlices - cheeseSlices - 3 * x
        if y < 0:
            return []
        else:
            return [x, y]
    # 4x + 2y == tomatoSlices, x + y == cheeseSlices
