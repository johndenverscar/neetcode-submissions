class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            a = max(stones)
            stones.remove(a)
            b = max(stones)
            stones.remove(b)
            
            diff = abs(a - b)

            if diff != 0:
                stones.append(diff)
        
        return stones[0] if len(stones) > 0 else 0