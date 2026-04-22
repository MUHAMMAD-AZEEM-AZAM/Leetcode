class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answers = []
        def difference(str1: str, str2: str):
            if str1 == str2:
                return 0
            return sum(c1 != c2 for c1, c2 in zip(str1, str2))
        for s1 in queries:
            for s2 in dictionary:
                if difference(s1,s2) <= 2:
                    answers.append(s1)
                    break
        return answers        
