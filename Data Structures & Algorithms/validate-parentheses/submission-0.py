#fifo
class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        pairs = {')': '(', ']':'[', '}':'{'}

        for ch in s:
            if ch in pairs:
                if stck and stck[-1] == pairs[ch]:
                    stck.pop()
                else:
                    return False
            else:
                stck.append(ch)
        return not stck
