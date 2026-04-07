class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        buff = []
        digitToChars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i):
            if len(buff) == len(digits):
                res.append("".join(buff))
                return
            
            for ch in digitToChars[digits[i]]:
                buff.append(ch)
                backtrack(i+1)
                buff.pop()
        
        if digits:
            backtrack(0)
        return res


        