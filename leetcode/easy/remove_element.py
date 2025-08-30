class Solution:
    def removeElement(self, nums, val):
        k = 0 #pointer for the next position to place a non-val element
        for i in range(len(nums)): #iterate through the array
            if nums[i] != val:
                nums[k] = nums[i] #place the non-val element at position k
                k += 1 #increment k
        
        return k

# Url: https://leetcode.com/problems/remove-element/