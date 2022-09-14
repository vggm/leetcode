from typing import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        n = 0
        for i in range(len(str(highLimit))):
            n += 1

        mem = [0] * (n*10)

        for i in range(lowLimit,highLimit+1):
            x = sum(int(j) for j in str(i))
            mem[x] += 1

        return max(mem)


print(Solution().countBalls(19,28))