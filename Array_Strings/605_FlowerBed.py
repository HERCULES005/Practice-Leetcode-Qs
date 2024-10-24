class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        f =[0] + flowerbed +[0]
        for i in range(1, len(f) - 1): #i increment on its own in range function#!len(f) not flowerbed

            if( f[i-1] == 0 and f[i] == 0 and f[i+1] == 0 ):
                f[i]=1 #Value at position in changed to 1 and now i is incremented to next position
                n-=1
        return n<=0 #this means return iff n is less than or equal to zero