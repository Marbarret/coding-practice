class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter # Import Counter from collections module
        count = Counter(nums) # Count the frequency of each element in nums
        return [item for item, freq in count.most_common(k)] # Return the k most common elements

# Url: https://leetcode.com/problems/top-k-frequent-elements/