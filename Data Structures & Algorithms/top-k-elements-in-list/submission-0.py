class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count)
        freq = [[] for i in range(len(nums) + 1)]
        for c, v in count.items():
            freq[v].append(c)
        print(freq)
        res = []
        for i in range(len(nums), 0, -1):
            if len(freq[i]) > 0:
                for num in freq[i]:
                    res.append(num)
            if len(res) >= k:
                return res
        
        

        