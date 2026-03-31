class Solution:
    def generateTupleKey(self, strs: str) -> Tuple[int]:
        counts = [0]*26

        for char in strs:
            counts[ord(char)-ord('a')] += 1
        
        return tuple(counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sol = defaultdict(list)

        for i, val in enumerate(strs):
            key = self.generateTupleKey(val)
            sol[key].append(val)

        return list(sol.values())