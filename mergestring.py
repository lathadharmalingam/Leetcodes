#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#Return the merged string.
class Solution(object):
    def mergeAlternately(self, word1, word2):
        s = len(word1)
        s1 = len(word2)
        result = ""
        if s == s1:
            i=s
            for i in range(len(word1)):
                result=result+(word1[i])
                result=result+(word2[i])
                
            return result
        elif s<s1:
                for i in range(s):
                    result=result+(word1[i])
                    result=result+(word2[i])
                for i in range (s,s1):
                    rem = ''
                    rem = rem + word2[i]
                    result = result + rem
                return result
        else:

                for i in range(s1):
                    result=result+(word1[i])
                    result=result+(word2[i])
                    n=s1-s
                for i in range (s1,s):
                    rem = ''
                    rem = rem + word1[i]
                    result = result + rem

                return result