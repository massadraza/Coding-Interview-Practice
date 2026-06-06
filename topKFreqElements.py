class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []

        for i in range(len(nums) + 1):
            freq.append([])

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num, count in count.items():
            freq[count].append(num)

        result = []

        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                result.append(n)
                if(len(result) == k):
                    return result

        