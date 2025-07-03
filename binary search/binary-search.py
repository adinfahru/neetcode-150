from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1
        return - 1
                
print(Solution().search([-1,0,2,4,6,8], 4)) 