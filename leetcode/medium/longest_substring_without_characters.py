class Solution:
    def lengthOfLongestSubstring(self, s):
        index_map = {} # Dictionary to store the last index of each character
        left = 0 # Left pointer of the sliding window
        maxLength = 0 # Variable to store the maximum length found
        for right in range(len(s)): # Right pointer of the sliding window
            if s[right] in index_map and index_map[s[right]] >= left: # If the character is already in the map and within the current window
                left = index_map[s[right]] + 1 # Move the left pointer to the right of the last occurrence
            index_map[s[right]] = right # Update the last index of the character
            maxLength = max(maxLength, right - left + 1) # Update the maximum length
        return maxLength
