from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memo = defaultdict(int)
        for i in nums:
            memo[i] += 1 # defualtdict를 쓰는 이유 : 존재하지 않는 값에 대해 넘어감
        
        sorted_counts = sorted(memo.items(), key = lambda x:x[1], reverse = True)

        answer = [x[0] for x in sorted_counts[:k]]
        return answer



        
# dict -> sort 
# max() 시간복잡도 
# heapq
# bucket sort