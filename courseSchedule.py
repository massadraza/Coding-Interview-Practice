class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}

        # Engineer a hashmap mapping courses to their prereqs
        for crs, pre in prerequisites: 
            preMap[crs].append(pre)
        
        visitSet = set()

        def dfs(curr):
            if curr in visitSet:
                return False
            if preMap[curr] == []:
                return True

            visitSet.add(curr)
            # looping through all available prereqs mapped to this course
            for pre in preMap[curr]:
                if not dfs(pre): return False
            visitSet.remove(curr) # Remember we need to explore multiple paths
            # Once done seeing this path we need to remove from set
            preMap[curr] = []

            return True

        for curr in range(numCourses):
            if not dfs(curr): return False

        return True