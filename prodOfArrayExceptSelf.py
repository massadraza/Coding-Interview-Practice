class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resultArr = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            resultArr[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for j in range(len(nums) - 1, -1, -1):
            resultArr[j] *= postfix
            postfix *= nums[j]

        return resultArr