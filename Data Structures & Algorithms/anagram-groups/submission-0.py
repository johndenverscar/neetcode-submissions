class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            mkey = ''.join(sorted(s))
            if mkey in groups:
                groups[mkey].append(s)
            else:
                groups[mkey] = [s]

        return list(groups.values())