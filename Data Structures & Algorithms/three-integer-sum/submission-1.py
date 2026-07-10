class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        n = len(nums)
        nums.sort()
        
        for i in range(n-2):
            left = i+1
            right = n-1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:
                ans = nums[i]+nums[left]+nums[right]
                if ans == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                         left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1

                elif ans < 0:
                    left+=1
                else:
                    right-=1
            
        return result
                

            

                

            

