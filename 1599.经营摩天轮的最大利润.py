class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        min_cnt = -1
        cnt = wait = onboard = 0
        for i in range(len(customers)):
            cnt += 1
            arrived = customers[i]
            if arrived + wait <= 4:
                temp = arrived + wait
                wait = 0
            else:
                temp = 4
                wait += arrived - 4
            onboard += temp
            current_profit = onboard * boardingCost - cnt * runningCost
            # print(f'{arrived}位游客抵达,{temp}位登舱,{wait}位等待.摩天轮第{cnt}次轮转,当前利润:{current_profit}')
            if current_profit > max_profit:
                max_profit = current_profit
                min_cnt = cnt
        while wait > 0:
            cnt += 1
            if wait > 4:
                temp = 4
                wait -= 4
            else:
                temp = wait
                wait = 0
            onboard += temp
            current_profit = onboard * boardingCost - cnt * runningCost
            # print(f'已不再有游客抵达,{temp}位登舱,{wait}位等待.摩天轮第{cnt}次轮转,当前利润:{current_profit}')
            if current_profit > max_profit:
                max_profit = current_profit
                min_cnt = cnt
        return min_cnt
