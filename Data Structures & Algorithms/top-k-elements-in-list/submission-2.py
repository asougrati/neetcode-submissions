class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        result = []
        for num in nums:
            freq[num] += 1
        freq_sorted=sorted(freq.items(), key=lambda item: item[1], reverse=True)
        tuples = freq_sorted[:k]
        for t in tuples:
            result.append(t[0])
        return result
        