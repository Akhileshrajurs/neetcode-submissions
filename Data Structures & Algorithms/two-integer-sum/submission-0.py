class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i,num in enumerate(nums):
            ans = target - num

            if ans in hash:
                return [hash[ans],i]

            hash[num] = i
