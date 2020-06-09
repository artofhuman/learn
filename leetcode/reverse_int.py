class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        res_mult = 1
        max = 2 ** 31
        min = -max - 1

        if x < 0:
            x = x * -1
            res_mult = -1

        while x >= 1:
            pop = int(x) % 10
            x /= 10
            rev = rev * 10 + pop
            if not min < rev < max:
                rev = 0
                break
        return rev * res_mult

print(Solution().reverse(-123))
print(Solution().reverse(1))
print(Solution().reverse(1534236469))
