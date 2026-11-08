class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        n=len(boxGrid)
        m=len(boxGrid[0])
        rote=[]
        i=0
        while i<m:
            row=[""]*n
            rote.append(row)
            i+=1
        left=0
        while left<n:
            right=0
            while right<m:
                rote[right][n-left-1] = boxGrid[left][right]
                right+=1
            left+=1
        col=0
        while col<n:
            new=m-1
            i=m-1
            while i>=0:
                if rote[i][col]=="*":
                    new=i-1
                elif rote[i][col]=="#":
                    rote[i][col]="."
                    rote[new][col]="#"
                    new-=1
                i-=1
            col+=1
        return rote
                