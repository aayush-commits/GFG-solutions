class Solution:
    def isDigitSumPalindrome(self,N):
        res = sum(int(digit) for digit in str(N))
        # print(res)
        temp = res
        s2 = 0
        while res > 0:
            d = res % 10
            s2 = s2*10 +d
            res //= 10
        # print(s2)
        if s2 == temp:
            return 1
        else:
            return 0
