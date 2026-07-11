class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # rob1 represents two houses ago nums[i - 2]
        # rob2 represents 1 house ago nums[i - 1]

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2