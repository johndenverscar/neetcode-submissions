class MinStack:

    def __init__(self):
        self._mins = []
        self._vals = []

    def push(self, val: int) -> None:
        self._vals.append(val)
        cur_min = val if not self._mins else self._mins[-1]
        self._mins.append(min(cur_min, val))
        

    def pop(self) -> None:
        self._vals.pop()
        self._mins.pop()
        

    def top(self) -> int:
        return self._vals[-1]

    def getMin(self) -> int:
        return self._mins[-1]
