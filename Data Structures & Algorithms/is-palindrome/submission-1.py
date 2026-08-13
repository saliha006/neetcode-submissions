class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [] #cleaned string

        for ch in s:
            if ch.isalnum():
                clean.append(ch.lower())
        l = 0
        r = len(clean) -1
        
        while l < r:
            if clean[l] == clean[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        