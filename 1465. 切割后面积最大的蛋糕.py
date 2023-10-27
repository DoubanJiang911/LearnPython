class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        mh = horizontalCuts[0]
        mw = verticalCuts[0]
        for hc in range(1, len(horizontalCuts)):
            temp = horizontalCuts[hc] - horizontalCuts[hc-1]
            mh = temp if temp > mh else mh
        temp = h - horizontalCuts[-1]
        mh = temp if temp > mh else mh
        for vc in range(1, len(verticalCuts)):
            temp = verticalCuts[vc] - verticalCuts[vc-1]
            mw = temp if temp > mw else mw
        temp = w - verticalCuts[-1]
        mw = temp if temp > mw else mw
        return (mh*mw) % (10**9+7)
# 从0--horizontalCuts[i]--h之间，找出最大的垂直间距，再同理找出最大的水平间距，从而找出最大的面积，返回取余后数值
