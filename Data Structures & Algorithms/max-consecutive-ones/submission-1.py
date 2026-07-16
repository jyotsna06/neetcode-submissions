class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        n = len(nums)

        for i in range(n):
            while i < n:
                if nums[i] == 1:
                    count +=1
                    i+=1
                else:
                    max_count = max(max_count, count)
                    count = 0
                    i+=1
                    
                max_count = max(max_count, count)
            return max_count

        