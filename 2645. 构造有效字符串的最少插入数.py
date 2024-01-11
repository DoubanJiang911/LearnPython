class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        cnt = 1
        # cnt定义字符串word最终需要构造abc的组数,因为1 <= word.length <= 50,说明至少需要构造一组abc
        for i in range(1, n):
            if word[i] <= word[i-1]:
                # 一组完整的abc字符必须严格按照s[0]<s[1]<s[2]的趋势，否则就只能各自构造成不同组的abc
                cnt += 1
        return cnt * 3 - n
