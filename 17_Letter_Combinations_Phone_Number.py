class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ""
        
        n = len(digits)
        pool = {}
        pool['2'] = ["a","b","c"]
        pool['3'] = ["d","e","f"]
        pool['4'] = ["g","h","i"]
        pool['5'] = ["j","k","l"]
        pool['6'] = ["m","n","o"]
        pool['7'] = ["p","q","r","s"]
        pool['8'] = ["t","u","v"]
        pool['9'] = ["w","x","y","z"]
        
        def backtrack(curr,next_digits):
            if len(next_digits)==0:
                out.append(curr)
            else:
                for letter in pool[next_digits[0]]:
                    backtrack(curr+letter,next_digits[1:])
        
        out = []
        if digits:
            backtrack("",digits)
        
        return out
            
            