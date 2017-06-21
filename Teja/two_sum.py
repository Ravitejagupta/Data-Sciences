class Solution:
    def twoSum(self, nums, target):
        if len(nums)<=1:
            return False
        a = {}
        for i in range(len(nums)):
            if nums[i] in a:
                return [a[nums[i]],i]
            else:
                a[target-nums[i]] = i
                
            
        
