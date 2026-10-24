from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = defaultdict(int)

        for idx, val in enumerate(nums):
            need = target-val

            if need in hash :
                return [hash[need], idx]

            hash[val] = idx
        