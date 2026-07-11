class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_sum = 0
        n = len(heights)
        left = 0
        right = n-1
    
        while left < right:
           ans = min(heights[left], heights[right]) * ( right-left)
           max_sum = max(max_sum,ans)
   
           if heights[left] <= heights[right]:
            left+=1
           else:
                right-=1
        return max_sum




        