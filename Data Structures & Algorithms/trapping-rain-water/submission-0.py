class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = 0
        right_max = 0
        left = 0
        right = n-1
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
                left +=1
            elif height[left] >= height[right]:
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                right -=1

        return total_water



  




        