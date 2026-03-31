class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = {}

        for i in nums:
            if i in frequency:
                return True
            else:
                frequency[i] = 1;


        return False