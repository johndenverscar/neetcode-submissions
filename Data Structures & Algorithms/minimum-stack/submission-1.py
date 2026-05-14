class MinStack:

    def __init__(self):
        self._mins = []
        self._vals = []

    def push(self, val: int) -> None:
        self._vals.append(val)
        self._mins.append(min(val, self._mins[-1] if self._mins else val))
        

    def pop(self) -> None:
        self._vals.pop()
        self._mins.pop()
        

    def top(self) -> int:
        return self._vals[-1]

    def getMin(self) -> int:
        return self._mins[-1]
