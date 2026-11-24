
class Solution:
    def maxLength(self, nums):

        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def get_lcm(a, b):
            return (a // get_gcd(a, b)) * b

        n = len(nums)
        ans = 0

        for i in range(n):
            prod = 1
            g = 0
            l = 1

            for j in range(i, n):
                prod *= nums[j]

                g = get_gcd(g, nums[j])
                l = get_lcm(l, nums[j])

                if prod == g * l:
                    ans = max(ans, j - i + 1)

        return ans
