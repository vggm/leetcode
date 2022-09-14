class Solution:
    def totalMoney(self, n: int) -> int:
        loops = n//7
        res = 0

        def moneyPerDay(day: int, loop):
            if day < 1:
                return 0
            if day == 1:
                return loop + 1
            return moneyPerDay(day - 1, loop) + day + loop

        i = 0
        while i <= loops:
            res += moneyPerDay(7 if n > 7 else n,i)
            n -= 7
            i += 1

        return res

print(Solution().totalMoney(175))