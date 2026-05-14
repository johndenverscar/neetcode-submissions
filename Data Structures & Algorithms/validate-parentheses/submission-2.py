class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack[-1] == pairs[c]:
                    stack.pop()
            else:
                return False
        
        return len(stack) == 0