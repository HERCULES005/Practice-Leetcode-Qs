class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        res=[]
        max_candies = max(candies)
        for maxi in candies:
            if(maxi + extraCandies >= max_candies):
                res.append(True)

            else:
                res.append(False)
        return res