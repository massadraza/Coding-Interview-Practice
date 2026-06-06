class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for x in strs:
            count = [0] * 26

            for e in x: 
                count[ord(e) - ord("a")] += 1

            result[tuple(count)].append(x)
        

        return list(result.values())
