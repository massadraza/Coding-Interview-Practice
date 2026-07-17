class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for x in wordDict:
                if (i + len(x)) <= len(s) and s[i : i + len(x)] == x:
                    dp[i] = dp[i + len(x)]
                if dp[i]: # If already TRUE then we can just skip it we already found valid word
                    break

        return dp[0]