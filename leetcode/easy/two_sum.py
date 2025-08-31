class Solution:
    def twoSum(self, nums, target):
        num_map = {} #create a dictionary to store numbers and their indices
        for i, num in enumerate(nums): #iterate through the list with index
            complement = target - num #calculate the complement
            if complement in num_map: #check if the complement exists in the dictionary
                return [num_map[complement], i] #return the indices if found
            num_map[num] = i #store the number and its index in the dictionary
        return []