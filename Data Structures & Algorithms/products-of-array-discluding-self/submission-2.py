class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None] * len(nums)
        runn_keeper = 1
        for i in range(len(nums)):
            output[i] = runn_keeper
            runn_keeper *= nums[i]
        runn_keeper = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= runn_keeper
            runn_keeper *= nums[i]
        return output