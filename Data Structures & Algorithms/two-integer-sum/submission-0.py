class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for idx, num in enumerate(nums):
            ans = target - num 
            if ans in my_dict:
                return [my_dict[ans] , idx]
            my_dict[num] = idx
            
        
        
        