class Solution:
    def kthDigit(self, A, B, K):
        N = A ** B
        for i in range(K):
            digit = N % 10
            N //= 10
        return digit
