class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ref[tuple(count)].append(s)
        return list(ref.values())