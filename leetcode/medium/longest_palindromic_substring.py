class Solution:
    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        max_len = 1
        max_str = s[0]
        for i in range(len(s) - 1): # iterate through the string
            l, r = i, i # initialize left and right pointers
            while l >= 0 and r < len(s) and s[l] == s[r]: # expand around the center
                current_len = r - l + 1 # calculate the current length of the palindrome
                if current_len > max_len: # update max_len and max_str if a longer palindrome is found
                    max_len = current_len # update max_len
                    max_str = s[l:r+1] # update max_str
                l -= 1
                r += 1
            l, r = i, i + 1 # check for even length palindromes
            while l >= 0 and r < len(s) and s[l] == s[r]: # expand around the center
                current_len = r - l + 1 # calculate the current length of the palindrome
                if current_len > max_len: # update max_len and max_str if a longer palindrome is found
                    max_len = current_len # update max_len
                    max_str = s[l:r+1] # update max_str
                l -= 1 # move left pointer to the left
                r += 1 # move right pointer to the right
        return max_str # return the longest palindromic substring

# Url: https://leetcode.com/problems/longest-palindromic-substring/