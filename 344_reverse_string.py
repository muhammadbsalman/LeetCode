class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for x in range(len(s)//2):
            y=len(s)-1-x
            s[x],s[y]=s[y],s[x]
