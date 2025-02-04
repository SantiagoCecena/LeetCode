class Solution:
    def shortestPalindrome(self, s: str) -> str:
        wordLength = len(s)
        reversedString = s[::-1]
        newWord = s + "#" + reversedString
        lps = [0]*len(newWord)
        i=0
        j=1
        while j < len(newWord):
            if(newWord[i] == newWord[j]):
                lps[j]=i+1
                i+=1
                j+=1
            else:
                if(i!=0):
                    i=lps[i-1]
                else:
                    lps[j]=0
                    j+=1

        diff = wordLength - lps[wordLength*2]
        return (reversedString[:diff]+s)