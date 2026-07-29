class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=("".join(c for c in s if c.isalnum())).lower()
        return True if p[::-1]==p else False