class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in numbers:
                j = numbers.get(difference)
                return [j, i]
            else:
                numbers[num] = i
            
