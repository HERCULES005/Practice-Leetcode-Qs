class Solution(object):
    def mergeAlternately(self, word1, word2):
        i,j = 0
        res = []
       #Iterating through each word and alternatively adding the words in thbe result string 
        while(i<len(word1) and j<len(word2)):
           res.append(word1[i])
           res.append(word2[j])
           #also incrementing the value of the variables
           i,j+=1
        #if loops exits which means that one string is shorter than the other one 
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)