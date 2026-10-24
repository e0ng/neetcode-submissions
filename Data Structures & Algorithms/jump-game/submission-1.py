class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0

        for i, val in enumerate(nums):
            if max_jump < i :
                return False

            max_jump = max(max_jump, i + val)

        return True

        