class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        output = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums)-1, 0, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i+1] * nums[i]
        # print(prefix)
        # print(suffix)
        for i in range(len(nums)):
            # print(i)
            if i == 0:
                output[i] = suffix[i+1]
            elif i == len(nums) - 1:
                output[i] = prefix[i - 1]
            else:
                output[i] = prefix[i-1] * suffix[i+1]
            # print(output)
        return output
        