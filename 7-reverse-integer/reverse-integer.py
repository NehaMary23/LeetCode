class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        rev=s[::-1] if s[0]!="-" else ""
        if rev=="":
            s=s[1:]
            rev='-'+s[::-1]
        if int(rev) not in range(-2**31,2**31 -1):
            return 0
        return int(rev)