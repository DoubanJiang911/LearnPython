class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        restaurants = sorted(restaurants, key=lambda x: (-x[1], -x[0]))  # 按照rating和ID降序排序
        restaurants = [r for r in restaurants if not(veganFriendly and not r[2]) and r[3] <= maxPrice and r[4] <= maxDistance]  # 过滤餐厅
        return [r[0] for r in restaurants]  # 返回餐厅ID列表
