from winreg import REG_RESOURCE_REQUIREMENTS_LIST


# Planning - read the question, understand the constraints
# Requirements - return true or false
# Design - mod10, arraylist
# Code
# Test

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return(False)
        if abs(x)<10:
            return(True)
        originalX = x
        flippedNumber=[]
        while(x>=1):
            lastDigit=x%10
            flippedNumber.append(str(lastDigit))
            lastDigit=int(x/10)
            flippedNumberString=int("".join(flippedNumber))
            return(originalX==flippedNumberString)


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return(False)
        if abs(x)<10:
            return(True)
        flippedString=""
        stringX=str(x)
        for letter in stringX:
            flippedString=letter+flippedString
        flippedNumber=int(flippedString)
        return(flippedNumber==x)

