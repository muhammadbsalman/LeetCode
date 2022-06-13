class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=end=max_length=0
        this_set = set()
        while end<len(s):
            if s[end] not in this_set:
                this_set.add(s[end])
                end+=1
            else:
                this_set.remove(s[start])
                start+=1
            max_length=max(max_length,len(this_set))
        return max_length
