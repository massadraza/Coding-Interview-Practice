class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            large1 = heapq.heappop_max(stones)
            large2 = heapq.heappop_max(stones)

            if large1 == large2:
                continue
            elif large1 < large2:
                newW = large2 - large1
                heapq.heappush_max(stones, newW)
            else:
                # large1 > large2
                newW = large1 - large2
                heapq.heappush_max(stones, newW)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
            