class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=[]
        if s=='' or len(s)==1:
            return s
        
        for i in range(len(s)):
            s1 = ''
            for j in range(i, len(s)):
                s1 += s[j]
                if s1 == s1[::-1]:
                    l.append(s1)
        return max(l,key=len)