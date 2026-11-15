class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        freq = {}

        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1

        left = 0
        count = len(t)
        start = 0
        min_len = float('inf')

        for right in range(len(s)):
            if s[right] in freq:
                if freq[s[right]] > 0:
                    count -= 1
                freq[s[right]] -= 1

            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:
                        count += 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]