class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        if s=='':
            return 0
        for i in range(len(s)):
            s1='' 
            for j in range(i,len(s)):
                if s[j] not in s1:
                    s1+=s[j]
                else:
                    break
            l.append(s1)
        m=max(l,key=len)
        return len(m)