class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxArea = 0
        area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1

            if area > maxArea:
                maxArea = area

        return maxArea

