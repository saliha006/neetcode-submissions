from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counting = {} #key:val Lcount:words

        for word in strs:
            lcount = Counter(word)
            lcounted = frozenset(lcount.items())

            if lcounted in counting:
                counting[lcounted].append(word)
            else:
                counting[lcounted] = [word]
        return list(counting.values())
            