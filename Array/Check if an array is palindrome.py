def ispalindrome (arr, start = 0, end = None): # creating function by creating array, first array element, last array element
    if end is None: # if the end is not the last element
        end = len(arr) - 1 #providing value to end
        
    if start >= end: #comapring start and end
        return True 
    return arr[start] == arr[end] and ispalindrome(arr, start + 1, end - 1) # palindrome check

num = int(input())    #size of array
arr = [] #array
for i in range(num): 
    element = int(input()) # user defined elements 
    arr.append(element)
    
if ispalindrome(arr):
    print("True")
else:
    print("False")
    
    