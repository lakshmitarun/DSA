class Solution:
    def reverseVowels(self, s: str) -> str:
        n=list(s)
        vowels="AEIOUaeiou"
        left=0
        right=len(n)-1
        while left<right:
            if n[left] in vowels and n[right] in vowels:
                n[left],n[right]=n[right],n[left]
                left+=1
                right-=1
            elif n[left] not in vowels:
                left+=1
            elif n[right] not in vowels:
                right-=1
        return "".join(n)
