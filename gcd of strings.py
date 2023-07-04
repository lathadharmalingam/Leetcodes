'''For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.'''

 class Solution(object):
    def gcdOfStrings(self, str1, str2):
        n=len(str1)
        n1=len(str2)
        if str1+str2 == str2+str1: 
            print str1+str2
            print str2+str1
            if n<n1:
                small = n 
            else:
                small= n1
                print small
                for i in range(1,small+1):
                     if(n%i == 0) and (n1 %i==0):
                        gcd = i
                return str1[0:gcd]
        else:
            return ""