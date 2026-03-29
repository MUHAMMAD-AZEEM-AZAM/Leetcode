class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for i,o in enumerate(operations):
            if o == '+'and len(scores)>=2 :
                scores.append(scores[-1] + scores[-2])
            elif o == 'D' and len(scores)>0:
                scores.append(scores[-1] * 2)
            elif o == 'C' and len(scores)>0:
                scores.pop()
            else:
                scores.append(int(o))
        return sum(scores)
