class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev_list = []
        s = ""
        space = " "
        for a in words:
            a=list(a)
            for x in range(len(a)//2):
                y = len(a)-1-x
                a[x],a[y]=a[y],a[x]
            a=s.join(a)
            rev_list.append(a)
        
        return " ".join(rev_list)
