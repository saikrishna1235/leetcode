class Solution:
    def frequencySort(self, nums):
        freq = {}

        # Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort using frequency, then number in descending order
        nums.sort(key=lambda x: (freq[x], -x))

        return nums