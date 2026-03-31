class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers)-1

        while first <= last:
            curr = numbers[first] + numbers[last]
            if curr == target:
                return [first+1, last+1]
            elif curr > target:
                last -= 1
            else:
                first += 1
        
        return [first, last]

        