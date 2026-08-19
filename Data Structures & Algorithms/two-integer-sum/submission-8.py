class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {nums[i]: i for i in range(len(nums))}
        print(nums_map)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums_map and i != nums_map.get(difference):
                print(difference, nums_map.get(difference))
                j = nums_map.get(difference)
                return [i, j]
        return []
        