class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        occurrences = set(freq.values())
        return len(occurrences) == len(freq)