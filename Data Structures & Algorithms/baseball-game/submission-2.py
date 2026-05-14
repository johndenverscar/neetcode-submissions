class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []

        for op in operations:
            delta = 0
            if op == "C":
                delta = -1 * stack.pop()
            elif op == "D":
                delta = stack[-1] * 2
                stack.append(delta)
            elif op == "+":
                delta = stack[-1] + stack[-2]
                stack.append(delta)
            else:
                delta = int(op)
                stack.append(delta)
            total += delta
            
        return total 