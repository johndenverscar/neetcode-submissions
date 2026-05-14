class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join([str(x) for x in digits])) + 1
        
        return list(str(n))