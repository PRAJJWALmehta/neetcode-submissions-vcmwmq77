class Solution:
    def generateTupleKey(self, strs: str) -> Tuple[int]:
        counts = [0]*26

        for i in strs:
            counts[ord(i)-ord('a')] += 1
        
        return tuple(counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert string to unique key and return tuple in a function
        # make a set with  the returned tuple and append the value to the unique key

        sol = {}

        for i, val in enumerate(strs):
            key = self.generateTupleKey(val)
            if key not in sol:
                sol[key] = []

            sol[key].append(val)
            

        return list(sol.values())