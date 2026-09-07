class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs: 
            key_s = "".join(sorted(s))
            if key_s not in groups:
                groups[key_s] = []
            groups[key_s].append(s)
        values_for_groups = list(groups.values())
        return values_for_groups

