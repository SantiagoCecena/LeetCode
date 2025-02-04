class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        missingNumber = 1
        i = 0
        while missingNumber <= n:
            if i<len(nums) and nums[i] <= missingNumber:
                missingNumber += nums[i]
                i += 1
            else:
                patches += 1
                missingNumber += missingNumber
        return patches