class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        # ！！重要：使用set转为哈希表，优化遍历words的时间
        mark = []
        # 通过[[student_id],[evaluate]]的形式记录每个id对应的评价结果，写入mark数组
        for i, v in enumerate(report):
            evaluate = 0
            words = v.split(' ')
            # print(words)
            # 使用split函数将report[x]按照空格分列，记录分离出的单词写入words
            for j in words:
                if j in positive_feedback:
                    evaluate += 3
                elif j in negative_feedback:
                    evaluate -= 1
                else:
                    continue
            mark.append([student_id[i], evaluate])
        # print(mark)
        # 排序，通过evaluate降序排列，假如evaluate相同则按照student_id升序排列
        sortedMark = sorted(mark, key=lambda x: (-x[1], x[0]))
        # 仅返回前k个student_id
        return [y[0] for y in sortedMark[:k]]

