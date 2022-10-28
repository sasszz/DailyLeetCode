# Input: array of integers, 
# Output: array of array(s) of ints that add up to 3

# Algo requirements:
# No duplicate output arrays

# Design:
# output = []
# for loop over array, i keeps track of position
# inner for loop has a sum

nums = [-1,0,1,2,-1,-4]

class Solution(object):
    def threeSum(self, nums):
        output = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                innerArray = []
                if (nums[i] + nums[j] + nums[j+1]) == 0:
                    innerArray.append(nums[i])
                    innerArray.append(nums[j])
                    innerArray.append(nums[j+1])
                    innerArray = sorted(innerArray)
                    if innerArray not in output:
                            output.append(innerArray)
        return output

# doesn't work - breaks at [-2,0,1,1,2]