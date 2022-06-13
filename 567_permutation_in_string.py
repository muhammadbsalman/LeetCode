class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = collections.Counter(s1)
        
        for x in range(len(s2)-len(s1)+1):
            s2_dict = collections.Counter(s2[x:x+len(s1)])
            if s1_dict==s2_dict: return True
        return False
