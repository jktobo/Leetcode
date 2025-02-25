class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for k in range(len(nums)):
            if (nums[k]):
                nums[i], nums[k] = nums[k], nums[i]
                i += 1 