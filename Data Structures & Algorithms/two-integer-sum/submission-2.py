class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #this is the hash map for numbers that wer have went througgh already
        for i, n in enumerate(nums): #this gets all indicies and vlaues for each num in nums
            needed = target - n
            if needed in seen:
                return [seen[needed], i]
            seen[n] = i
        return

        #redo cold with hash 
               


            
            

