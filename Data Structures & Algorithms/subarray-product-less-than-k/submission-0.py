class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        count = 0
        prod = 1

        if k <= 1:
            return 0

        for right in range(n):
            prod *= nums[right]

            while prod >= k:
                prod /= nums[left]
                left +=1

            count += right - left + 1
        
        return count
        

        