class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
  
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            m = (left + right) // 2
            hr = 0

            for p in piles:
                hr += math.ceil(p / m)

            if hr <= h:
                res = min(res, m)
                right = m - 1
            else:
                left = m + 1

        
        return res
