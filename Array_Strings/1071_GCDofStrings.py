class Solution(object):
    def gcdOfStrings(self, str1, str2):
        res = []

        for i in range(str1):
            for j in range(str2):
                if(str1[i]==str2[j]):
                    res.append(str1[i])
                elif(str1[i] != str2[j]):
                    res.append("")
                i+=1
                j+=1

        return "".join(res)