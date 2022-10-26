class Solution(object):
    def arrayRankTransform(self, arr):
        # create new dictionary of key:value, value:none(to be assigned a ranking) 
        rankDictionary={}

        # sort the list
        sortedList = sorted(arr)

        # assign rankings to each item w/ for loop
            # if item is = in value, assign same ranking
        
        # push ranking to dictionary where value == key

        # create array with values from object

        # return array


class Solution(object):
    def arrayRankTransform(self, arr):
        sortedArr=sorted(arr)
        rank=1
        outputArr=[]
        rankDictionary={}
        rankDictionary[sortedArr[0]]=1
        for index in range(1,len(sortedArr)):
            if sortedArr[index]>sortedArr[index-1]:
                rank=rank+1
                rankDictionary[sortedArr[index]]=rank

        for index in range(len(arr)):
            thisElement=arr[index]
            outputArr.append(rankDictionary[thisElement])
            print(arr)
            print(sortedArr)
            print(rankDictionary)
            print(outputArr)

        return(outputArr)
