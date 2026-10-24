class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2 :
            return 1
        # memo = [0] * (n+1) # 경우의 수 저장

        # memo[1] = 1
        # memo[2] = 2

        # for i in range(3, n+1):
        #     memo[i] = memo[i-1] + memo[i-2]

        # return memo[n]


        memo = [0] * (n+1)


        def help(a: int) -> int :
            if a <= 2 :
                return a

            if memo[a] != 0 :
                return memo[a]

            memo[a] = help(a-1) + help(a-2)
            return memo[a]

        return help(n)