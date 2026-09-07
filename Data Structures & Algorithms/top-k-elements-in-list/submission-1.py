class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for i in nums:
            frequencies[i] = frequencies.get(i,0) + 1
        tuple_of_frequencies = sorted(frequencies.items(),key = lambda value:value[1], reverse = True)[:k] # this would be like (3,3)
        new_list = [i[0] for i in tuple_of_frequencies]
        return new_list

