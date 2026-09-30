class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(len(nums)):
            residual = target - nums[i]

            if residual in n.keys():            
                return [n[residual], i]
            n[nums[i]] = i 

            
