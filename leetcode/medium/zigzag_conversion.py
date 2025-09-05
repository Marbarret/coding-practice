class Solution:
    def zigzagConversion(self, s, numRows):
        if numRows == 1 or numRows >= len(s): # edge case
            return s 
        rows = [''] * numRows # create a list of empty strings for each row
        current_row = 0 
        going_down = False # direction flag
        for char in s: # iterate through each character in the string
            rows[current_row] += char # append the character to the current row
            if current_row == 0 or current_row == numRows - 1: # change direction at the first and last row
                going_down = not going_down # toggle direction
            current_row += 1 if going_down else -1 # move to the next row
        return ''.join(rows) # join all rows to get the final string

# Url: https://leetcode.com/problems/zigzag-conversion/