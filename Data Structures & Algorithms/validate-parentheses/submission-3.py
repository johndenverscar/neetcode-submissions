class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        # Checks
        # 1. if it's an open value, append to the stack
        # 2. if it's a close value
        # 

        for c in s:

            if c in pairs.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0