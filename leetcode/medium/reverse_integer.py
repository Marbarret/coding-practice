class Solution:
    def reverseInteger(self, x):
        init = -1 if x < 0 else 1 # determine the init of the integer
        x *= init # make x positive for easier manipulation
        reversed_x = 0 # initialize the reversed integer
        while x:
            reversed_x = reversed_x * 10 + x % 10 # append the last digit of x to reversed_x
            x //= 10 # remove the last digit from x
        reversed_x *= init # restore the original init
        if reversed_x < -2**31 or reversed_x > 2**31 - 1: # check for overflow
            return 0
        return reversed_x