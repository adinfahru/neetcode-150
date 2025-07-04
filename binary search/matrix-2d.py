from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)  
        n = len(matrix[0])

        total_elements = m * n
        print(f"m: {m}, n: {n}, total_elements: {total_elements}")

        left = 0
        right = total_elements - 1


        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            guess = matrix[row][col]

            print(f"left: {left}, right: {right}, mid: {mid}, row: {row}, col: {col}, guess: {guess}")

            if guess == target:
                return True
            elif guess > target:
                right =  mid - 1
            else:
                left = mid + 1
        return False


print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True