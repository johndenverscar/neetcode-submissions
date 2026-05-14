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
        #    a. if there's nothing in the stack, return false
        #    b. if the last element in the stack is it's match, pop it
        #    c. if the last element in the stack isn't it's match, return false

        for c in s:
            
            # if it's an open value, add to the stack
            if c in pairs.values():
                stack.append(c)
            # else, it's a close value
            else:
                # if there's nothing in the stack, there's nothing to match
                # the open with, return false
                if len(stack) == 0:
                    return False
                # if the last element in the stack is it's match, pop it from
                # the stack
                elif stack[-1] == pairs[c]:
                    stack.pop()
                # else, the last item in the stack isn't a match which means
                # that this is not a valid "parens" set, return false
                else:
                    return False
        
        # the return is going to be to check that the length is zero
        # if it's not, then we haven't fully cleared out stack
        return len(stack) == 0