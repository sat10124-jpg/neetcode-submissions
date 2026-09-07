class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()  # Create an empty set to keep track of numbers
        
        for num in nums:
            if num in seen:
                return True  # Found a duplicate!
            seen.add(num)    # Otherwise, add it to the set and keep looking
            
        return False  # Looped through everything and found no duplicates
