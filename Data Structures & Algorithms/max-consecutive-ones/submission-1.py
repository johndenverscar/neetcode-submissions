class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        cur_count = 0
        print(nums)

        for n in nums:
            if n == 0:
                max_count = max(max_count, cur_count)
                cur_count = 0
            else:
                cur_count += 1
        
        return max(cur_count, max_count)