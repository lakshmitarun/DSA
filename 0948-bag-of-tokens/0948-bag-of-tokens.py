class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        left=0
        right=len(tokens)-1
        maxm=0
        score=0
        while left<=right:
            if power>=tokens[left]:
                power-=tokens[left]
                score+=1
                maxm=max(maxm,score)
                left+=1
            elif score>0:
                power+=tokens[right]
                score-=1
                right-=1
            else:
                break
        return maxm
        