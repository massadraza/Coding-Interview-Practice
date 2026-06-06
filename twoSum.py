class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index, num in enumerate(nums):
            if target - num in prevMap:
                return [index, prevMap[target-num]]
            prevMap[num] = index
        

        return None
                 