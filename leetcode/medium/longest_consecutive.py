class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums) #create a set of numbers for O(1) lookups
        longest_streak = 0 #initialize the longest streak to 0

        for num in num_set: #iterate through each number in the set
            if num - 1 not in num_set: #check if it's the start of a sequence
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set: #count the length of the sequence
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak) #update the longest streak if needed
        return longest_streak

# Url: https://leetcode.com/problems/longest-consecutive-sequence/