class Solution(object):
    def increasingTriplet(self, nums):

        for i in range(1,len(nums)-1):
            if(nums[i-1] < nums[i] and nums[i] < nums[i+1]):
                return True

#!Check again question might be wrong