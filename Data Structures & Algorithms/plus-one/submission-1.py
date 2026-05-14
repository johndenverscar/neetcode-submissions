class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Convert the list into an int and add one
        n = int("".join([str(x) for x in digits])) + 1
        
        # convert that number back to a string and split it
        # back into a list
        return list(str(n))