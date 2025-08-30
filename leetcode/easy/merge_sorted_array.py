class Solution:
    def solutionOne(self, nums1, m, nums2, n):
        k = m + n - 1 #last position of nums1

        while m > 0 and n > 0: #while there are elements in both arrays
            if nums1[m - 1] > nums2[n - 1]: #compare the last elements of both arrays
                nums1[k] = nums1[m - 1] #place the larger element at position k
                m -= 1
            else:
                nums1[k] = nums2[n - 1] #place the larger element at position k
                n -= 1
            k -= 1
        
        while n > 0:
            nums1[k] = nums2[n - 1] #if there are remaining elements in nums2, place them in nums1
            n -= 1
            k -= 1
        return nums1

    def solutionTwo(self, nums1, m, nums2, n):
        nums1[m:] = nums2[:n] #copy elements of nums2 to the end of nums1
        nums1.sort()
        return nums1

# Url: https://leetcode.com/problems/merge-sorted-array/