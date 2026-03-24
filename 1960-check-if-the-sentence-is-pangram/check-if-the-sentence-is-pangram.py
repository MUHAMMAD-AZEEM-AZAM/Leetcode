class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = collections.Counter(sentence)   
        if len(counter) < 26:
            return False

        return True     