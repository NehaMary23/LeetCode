class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=0
        if x<0:
            return False
        num=x
        while x!=0:
            n=x%10
            x=x//10
            s=s*10 + n
        if num==s:
            return True
        else:
            return False