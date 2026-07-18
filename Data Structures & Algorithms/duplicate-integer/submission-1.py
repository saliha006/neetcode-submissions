class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #sorts the number
        for i in range(len(nums)-1): #checks for each number in array
            if nums[i] == nums[i+1]: 
                return True
        return False 