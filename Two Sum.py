class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}

        for i, num in enumerate(nums):
            x = target - num
            
            if x in num_indices:
                return [num_indices[x], i]
            
            num_indices[num] = i
        
        return []
