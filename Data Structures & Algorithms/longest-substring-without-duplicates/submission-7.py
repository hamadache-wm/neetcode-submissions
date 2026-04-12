class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        s_dup = []

        for i, e in enumerate(s):
            if e in s_dup:
                longest_substring = len(s_dup) if len(s_dup) > longest_substring else longest_substring
                s_dup = s_dup[s_dup.index(e)+1:]
                s_dup.append(e)
            else:
                s_dup.append(e)

        return longest_substring if longest_substring > len(s_dup) else len(s_dup)