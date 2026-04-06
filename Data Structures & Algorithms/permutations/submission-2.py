class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        
        for val in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, val)
                    new_perms.append(perm_copy)
            perms = new_perms
        
        return perms



        