class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        i,j = 0, len(s)-1
        vowelSet = set('aeiouAEIOU')
        while(i<j):
            if(s[i] not in vowelSet):
                i+=1
            elif(s[j] not in vowelSet):
                j-=1
            else:
                s[i],s[j] = s[j] , s[i]
                i+=1
                j-=1

        return "".join(s)