class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # Creating an adjacency list
        adjList = {c: [] for c in range(n)}

        for n1, n2 in edges:
            # undirected graphs, goes both ways
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)

            for j in adjList[i]:
                if j == prev:
                    continue 
                if not dfs(j, i):
                    return False
                
            return True
        
        return dfs(0, -1) and len(visit) == n