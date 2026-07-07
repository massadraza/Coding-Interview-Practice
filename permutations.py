class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        
        def dfs():
            if len(cur) == n:
                res.append(cur.copy())
                return

            for x in nums:
                if x not in cur:
                    cur.append(x)
                    dfs()
                    cur.pop()

        dfs()
        return res