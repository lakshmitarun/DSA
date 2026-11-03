class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        res=""
        for word in dictionary:
            left=0
            right=0
            while left<len(s) and right<len(word):
                if s[left]==word[right]:
                    left+=1
                    right+=1
                else:
                    left+=1
            if right==len(word):
                if len(word)>len(res):
                    res=word
                elif len(word)==len(res) and word<res:
                    res=word
        return res