# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0

        while n > 0:
            num = n % 10
            n //= 10

            s += num
            p *= num

        return p - s

solution = Solution()

assert (solution.subtractProductAndSum(234) == 15)
assert (solution.subtractProductAndSum(4421) == 21)

