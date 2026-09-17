class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n=len(mat)
        m=len(mat[0])
        low=0
        high=m-1
        while low<=high:
            mid=(low+high)//2
            one=max(range(n),key=lambda i:mat[i][mid])
            left=mat[one][mid-1] if mid-1>=0 else -1
            right=mat[one][mid+1] if mid+1< m else-1
            if mat[one][mid]> left and mat[one][mid]>right:
                return [one,mid]
            elif mat[one][mid]<left:
                high=mid-1
            else:
                low=mid+1