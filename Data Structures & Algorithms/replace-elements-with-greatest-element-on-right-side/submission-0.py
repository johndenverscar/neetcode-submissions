class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i, n in enumerate(arr):
            if len(arr[i+1:]):
                arr[i] = max(arr[i+1:])
            else:
                arr[i] = -1

        return arr