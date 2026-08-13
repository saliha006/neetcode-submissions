from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counting = {} #key:val
        
        for word in strs:
            counted = Counter(word)
            counted_key = frozenset(counted.items())

            if counted_key in counting:
                counting[counted_key].append(word)
            else:
                counting[counted_key] = [word]
                
        return list(counting.values())
