import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_stones = [-stone for stone in stones]

        heapq.heapify(max_stones) 

        while len(max_stones) >= 2:
            x = heapq.heappop(max_stones)
            y = heapq.heappop(max_stones)

            if x != y:
                heapq.heappush(max_stones, x-y)

        if len(max_stones) == 0 :
            return 0
        else :
            return -max_stones[0]

