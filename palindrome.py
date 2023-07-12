'''check palindrome or not'''
class Solution(object):
    def isPalindrome(self, x):
       temp = str(x)
       rev = temp[::-1]
       if rev == temp:
           return True
       else: 
            return False
