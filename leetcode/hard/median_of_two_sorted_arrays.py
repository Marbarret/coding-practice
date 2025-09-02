class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1) # length of nums1
        n = len(nums2)# length of nums2
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m # ensure nums1 is the smaller array
        imin, imax, half_len = 0, m, (m + n + 1) // 2 # binary search range and half length
        while imin <= imax:
            i = (imin + imax) // 2 # partition index for nums1
            j = half_len - i # partition index for nums2
            if i < m and nums2[j-1] > nums1[i]: # i is too small
                imin = i + 1 # move the search range to the right
            elif i > 0 and nums1[i-1] > nums2[j]: # i is too big
                imax = i - 1 # move the search range to the left
            else:
                if i == 0: max_of_left = nums2[j-1] # edge case for i = 0
                elif j == 0: max_of_left = nums1[i-1] # edge case for j = 0
                else: max_of_left = max(nums1[i-1], nums2[j-1]) # max of left partition
                if (m + n) % 2 == 1: # odd length case
                    return max_of_left # return the max of left partition

                if i == m: min_of_right = nums2[j] # edge case for i = m
                elif j == n: min_of_right = nums1[i] # edge case for j = n
                else: min_of_right = min(nums1[i], nums2[j]) # min of right partition

                return (max_of_left + min_of_right) / 2.0 # return the average of max of left and min of right for even length  

    def findMedianSortedArrays_s2(self, nums1, nums2): 
        merged = []
        i = j = 0 
        while i < len(nums1) and j < len(nums2): # merge the two arrays
            if nums1[i] < nums2[j]: # compare elements from both arrays
                merged.append(nums1[i]) # add the smaller element to the merged array
                i += 1
            else:
                merged.append(nums2[j]) # add the smaller element to the merged array
                j += 1
        while i < len(nums1): # add remaining elements from nums1
            merged.append(nums1[i]) # add the remaining elements to the merged array
            i += 1
        while j < len(nums2): # add remaining elements from nums2
            merged.append(nums2[j]) # add the remaining elements to the merged array
            j += 1 # increment j
        total_length = len(merged)
        if total_length % 2 == 1: # odd length case
            return merged[total_length // 2] # return the middle element
        else:
            mid1 = total_length // 2
            mid2 = mid1 - 1
            return (merged[mid1] + merged[mid2]) / 2.0

