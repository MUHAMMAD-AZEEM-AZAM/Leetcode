class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answers = []
        for s1 in queries:
            for s2 in dictionary:
                if s1 == s2 or sum(c1 != c2 for c1, c2 in zip(s1, s2)) <= 2:
                    answers.append(s1)
                    break
        return answers        
