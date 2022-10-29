# Input: array of arrays (coordinates)
# Output: cool: true/false

# Algo requirements:
# No duplicate output arrays

# Design:
# for loop over array
# for loop over inner coordinate array
# store initial point: y-x = num
# check if y2-x2 == num
# if not: return false
# outside: return true

# breaks with [0,0]

class Solution(object):
    def checkStraightLine(self, coordinates):

        arr = sorted(coordinates)

        duplicateX = {}
        duplicateY = {}

        for i in range(2):
            for j in range(len(arr[i])-1):
                a = arr[i][j]
                b = arr[i][j+1]
                
                if a & b != 0:
                  check = b-a
                  duplicateX[a]=1
                  duplicateY[b]=1
                  break

        for i in range(1, len(arr)):
            for j in range(len(arr[i])-1):
                x = arr[i][j]
                y = arr[i][j+1]
                if x in duplicateX:
                    return False
                else:
                    duplicateX[x]=1
                if y in duplicateY:
                    return False
                else:
                    duplicateY[y]=1

                diff = y-x
                if diff != check:
                    return False
                
        return True


