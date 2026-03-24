class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        counter = collections.Counter(sentence)   
        if len(counter) < 26:
            return False

        return True     