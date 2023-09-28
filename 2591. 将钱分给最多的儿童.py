class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        cnt = min(money//7, children)
        money -= cnt * 7
        children -= cnt
        if children == 0 and money > 0:
            cnt -= 1
        # 若剩余 0 个人，并且 money>0，那么将所有的美元分配给一个已经分到 8 美元的人，令 cnt 减去 1
        elif children == 1 and money == 3:
            cnt -= 1
        # 若剩余 1 个人，并且 money=3，为了避免分到 4 美元，并注意到题目输入中的 children>=2，因此将这 3 美元拆成两部分，将其中的一部分分配给已经分到 8 美元的人，令 cnt 减去 1。
        else:
            pass
        # 对于其他情况，若 money>0，可以将所有美元分配给一个人，cnt 不变。
        return cnt
