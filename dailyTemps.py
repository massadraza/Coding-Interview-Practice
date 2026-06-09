class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = (index - stackInd)
            stack.append([temperature, index])

        return result
        


