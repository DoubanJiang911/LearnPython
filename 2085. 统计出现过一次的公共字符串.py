from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt = 0
        freq1 = Counter(words1)
        print(freq1)
        freq2 = Counter(words2)
        print(freq2)
        for w in freq1:
            print(f"查询字符串：{w},words1中出现{freq1[w]}次,words2中出现{freq2[w]}次")
            if freq1[w] == 1 and freq2[w] == 1:
                cnt += 1
                print(f"字符串{w}符合条件，cnt更新:{cnt}")
        return cnt
