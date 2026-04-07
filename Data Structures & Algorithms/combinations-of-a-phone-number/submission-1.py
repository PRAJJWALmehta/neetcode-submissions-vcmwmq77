class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
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

        for d in digits:
            curr = []
            charset = digitToChars[d]
            for ch in charset:
                for cmb in res:
                    curr.append(cmb+ch)
            res = curr


        return res


        