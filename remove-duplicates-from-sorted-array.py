# Input: array of integers, sorted, in non-decreasing order
# Output: k (count of remaining integers in array), and array of integers (altered)

# Algo requirements:
# Delete in place, remove duplicates
# return array with ints in the front, deletions at the end

# Design:
# edge case: given empty array, return 0, []
# set k = 0
# for loop through array (start at second element, end at length)
#   if arr[i] == arr[i-1]
#       array.remove(arr[i])
#   else
#       k += 1
# return arr

# # My out of the box solution that failed:
# k=2
# for i in range(1, len(nums)-1):
#     if nums[i] == nums[i-1]:
#         print(nums[i])
#         print(k)
#         del nums[i]
#     else:
#         k+=1
# print(nums)


class Solution(object):
    def removeDuplicates(self, nums):
        temp = nums[0]
        count = 1

        for i in range(len(nums)):
            if nums[i] > temp:
                temp = nums[i]
                nums[count] = temp
                count += 1

        return count
