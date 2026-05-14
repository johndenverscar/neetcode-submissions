class Solution:
    def calPoints(self, operations: List[str]) -> int:
        cur = 0
        ans = [0] * len(operations)

        for op in operations:
            if op == "+":
                ans[cur] = ans[cur - 1] + ans[cur - 2]
                cur += 1
            elif op == "C":
                cur -= 1
                ans[cur] = 0
            elif op == "D":
                ans[cur] = ans[cur - 1] * 2
                cur += 1
            else:
                ans[cur] = int(op)
                cur += 1

        return sum(ans)