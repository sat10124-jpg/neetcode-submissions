class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        reviser = set()
        for i in nums:
            if i not in reviser:
                reviser.add(i)
            else:
                return True
        return False
