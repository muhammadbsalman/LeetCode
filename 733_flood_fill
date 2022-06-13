class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image == None or image[sr][sc]==newColor: return image
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image
        
    def dfs(self, image, r, c, initialC, newC):
        if r<0 or r>=len(image) or c<0 or c>=len(image[0]) or image[r][c]!=initialC:return
        
        image[r][c] = newC
        self.dfs(image, r+1, c, initialC, newC) #down
        self.dfs(image, r-1, c, initialC, newC) #up
        self.dfs(image, r, c+1, initialC, newC) #right
        self.dfs(image, r, c-1, initialC, newC) #left
