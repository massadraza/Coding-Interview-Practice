class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target: # hit a dead end in the tree
                return

            # if yes, we include
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # if no, we don't include
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res