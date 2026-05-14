class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3, 2, 2, 2, 3, 3, 4]
        count = 0

        for n in nums:
            if n != val:
                nums[count] = n
                count += 1
        
        return count