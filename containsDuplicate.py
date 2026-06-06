class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()

        for x in nums:
            if x in seenNums:
                return True
            seenNums.add(x)

        return False