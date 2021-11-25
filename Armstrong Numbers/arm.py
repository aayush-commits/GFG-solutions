class Solution:
    def armstrongNumber (ob, n):
        temp = n
        res = 0
        while n > 0:
            r = n % 10
            res += r ** 3
            n //= 10
        if res == temp:
            return "Yes"
        else:
            return "No"
