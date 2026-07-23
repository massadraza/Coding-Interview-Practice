class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # need to create a hashmap for this
        adjList = {c : [] for c in range(n)}

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit = set()
        def dfs(i):
            for n in adjList[i]:
                if n not in visit:
                    visit.add(n)
                    dfs(n)

        count = 0

        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                count += 1

        return count