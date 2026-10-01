class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        current_streak = 0
        max_length = 0

        for num in n:
            if not num - 1 in n:
                current_streak = 1
                i = 1
                while True:
                    if num + i in n:
                        i += 1
                        current_streak += 1
                    else:
                        max_length = max(current_streak, max_length)
                        break;
        return max_length
                

        