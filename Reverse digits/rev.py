class Solution:
	def reverse_digit(self, n):
		temp = n
		rev = 0
		while n > 0:
		    digit = n % 10
		    rev = 10 * rev + digit
		    n //= 10
	    return int(rev)
