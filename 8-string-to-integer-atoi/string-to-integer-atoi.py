class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        
        sign='+'
        if s[0]=='-' or s[0]=='+':
            sign=s[0]
            s=s[1:]
            
        sti=""
        for ch in s:
            if ch.isdigit():
                sti+=ch
            else:
                break

        if not sti:
            return 0
        s=('-'+sti) if sign=='-' else sti
        
        if int(s)<-2**31:
            return -2**31
        elif int(s)> 2**31-1:
            return 2**31-1
        else:
            return int(s)