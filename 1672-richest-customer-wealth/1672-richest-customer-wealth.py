class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        n=len(accounts)
        m=len(accounts[0])
        ans=0
        for i in range(n):
            total=0
            for j in range(m):
                total+=accounts[i][j]
            ans=max(ans,total)
        return ans        


        