class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        cur=[]
        col=image[sr][sc]
        res=[[sr,sc]]
        while res:
            p=res.pop()
            image[p[0]][p[1]]=newColor
            cur.append(p)
            if p[0]>0 and [p[0]-1,p[1]] not in cur and image[p[0]-1][p[1]]==col:
                res.append([p[0]-1,p[1]])
            if p[0]<len(image)-1 and [p[0]+1,p[1]] not in cur and image[p[0]+1][p[1]]==col:
                res.append([p[0]+1,p[1]])
            if p[1]>0 and [p[0],p[1]-1] not in cur and image[p[0]][p[1]-1]==col:
                res.append([p[0],p[1]-1])
            if p[1]<len(image[0])-1 and [p[0],p[1]+1] not in cur and image[p[0]][p[1]+1]==col:
                res.append([p[0],p[1]+1])
        return image