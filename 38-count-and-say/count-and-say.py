class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return str(1)
        s=self.countAndSay(n-1)
        c=1
        ns=""
        
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                c+=1
            else:
                ns += str(c)+s[i-1]
                c=1
        ns += str(c)+s[-1]
        return ns
        