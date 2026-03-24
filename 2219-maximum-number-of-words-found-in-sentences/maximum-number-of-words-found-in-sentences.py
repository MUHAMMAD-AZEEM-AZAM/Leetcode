class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        lengths = []
        for sentence in sentences:
            lengths.append(len(sentence.split(' ')))
        return max(lengths)