class Solution(object):
    def sortColors(self, nums):
        l,r = 0,len(nums)-1
        i=0
        def swap(i,r):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[r] = tmp

        while(i<=r):
            if(nums[i] == 0):
                swap(l,i)
                l+=1

            elif(nums[j] == 2):
                swap(i,r)
                r-=1
                i-=1
            i+=1