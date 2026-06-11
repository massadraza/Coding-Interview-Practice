class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix)
        rowOfInterest = None

        while top < bottom:
            m = (bottom + top) // 2

            if matrix[m][0] < target and matrix[m][len(matrix[0]) - 1] < target:
                top = m + 1
            elif matrix[m][0] > target and matrix[m][len(matrix[0]) - 1] > target:
                bottom = m
            else:
                rowOfInterest = m
                break

        if not top < bottom:
            return False

        left = 0
        right = len(matrix[m])

        while left < right: 
            m = int((left + right) / 2)

            if matrix[rowOfInterest][m] < target:
                left = m + 1
            elif matrix[rowOfInterest][m] > target:
                right = m
            else:
                return True

        return False