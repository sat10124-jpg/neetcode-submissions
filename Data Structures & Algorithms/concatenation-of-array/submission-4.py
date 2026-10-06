class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[i]
        ans += ans
        return ans

        