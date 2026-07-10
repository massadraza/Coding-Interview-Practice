class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}

        for t in tasks:
            freq[t] = 1 + freq.get(t, 0)
             
        maxHeap = list(freq.values())
        heapq.heapify_max(maxHeap)
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt != 0:
                    queue.append([cnt, time + n]) # [count, time it will be available again]

            if queue and queue[0][1] == time:
                heapq.heappush_max(maxHeap, queue.popleft()[0])
            
        return time